"""Check wheel and sdist contents produced by the package smoke job."""

from __future__ import annotations

import configparser
import json
import re
import sys
import tarfile
import zipfile
from email import policy
from email.parser import BytesParser
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ENTRY_POINTS = {
    "swarm-consensus": "tools.consensus_swarm:main",
    "swarm-benchmark": "tools.benchmark:main",
    "swarm-translate": "tools.translate_swarm:main",
    "swarm-summarize": "tools.summarize_chunks:main",
    "swarm-stigmergy-init": "tools.stigmergy_init:main",
}


def _project_identity() -> tuple[str, str]:
    metadata = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    name_match = re.search(r'^name\s*=\s*"([^"]+)"\s*$', metadata, re.MULTILINE)
    version_match = re.search(r'^version\s*=\s*"([^"]+)"\s*$', metadata, re.MULTILINE)
    if name_match is None or version_match is None:
        raise AssertionError("project name/version are missing from pyproject.toml")
    return name_match.group(1), version_match.group(1)


def _check_no_marketing_log(paths: list[str]) -> None:
    if any(PurePosixPath(path).name.casefold() == "marketing-log.txt" for path in paths):
        raise AssertionError("private MARKETING-LOG.txt was included in a public artifact")


def _check_json_payloads(paths: list[str], read_bytes) -> None:
    json_paths = [
        path
        for path in paths
        if len(PurePosixPath(path).parts) == 2
        and PurePosixPath(path).parts[0] == "tools"
        and PurePosixPath(path).suffix.casefold() == ".json"
    ]
    required = {"tools/swarm_haiku_3.json", "tools/swarm_haiku_research.json"}
    missing = required - set(json_paths)
    if missing:
        raise AssertionError(f"packaged JSON configuration is missing: {sorted(missing)}")
    for path in json_paths:
        json.loads(read_bytes(path).decode("utf-8"))


def _check_identity(metadata_bytes: bytes, expected_name: str, expected_version: str) -> None:
    metadata = BytesParser(policy=policy.default).parsebytes(metadata_bytes)
    metadata_version = metadata.get("Metadata-Version")
    if metadata_version is None:
        raise AssertionError("distribution metadata is missing Metadata-Version")
    try:
        metadata_version_parts = tuple(int(part) for part in metadata_version.split("."))
    except ValueError as error:
        raise AssertionError(f"invalid Metadata-Version: {metadata_version}") from error
    if metadata_version_parts < (2, 4):
        raise AssertionError(f"Metadata-Version 2.4 or newer is required, got {metadata_version}")

    actual_name = metadata.get("Name")
    actual_version = metadata.get("Version")
    if actual_name is None or actual_version is None:
        raise AssertionError("distribution metadata is missing Name or Version")
    if actual_name.strip().casefold() != expected_name.casefold():
        raise AssertionError(f"unexpected distribution name: {actual_name}")
    if actual_version.strip() != expected_version:
        raise AssertionError(f"unexpected distribution version: {actual_version}")

    if metadata.get("License-Expression", "").strip() != "MIT":
        raise AssertionError("distribution metadata must declare License-Expression: MIT")
    if metadata.get_all("License-File", []) != ["LICENSE"]:
        raise AssertionError("distribution metadata must declare exactly License-File: LICENSE")


def check_wheel(path: Path, expected_name: str, expected_version: str, license_bytes: bytes) -> None:
    with zipfile.ZipFile(path) as archive:
        paths = archive.namelist()
        _check_no_marketing_log(paths)
        _check_json_payloads(paths, archive.read)

        license_paths = [
            item
            for item in paths
            if item.casefold().endswith(".dist-info/licenses/license")
        ]
        if len(license_paths) != 1 or archive.read(license_paths[0]) != license_bytes:
            raise AssertionError("wheel must contain a byte-identical MIT LICENSE file")

        metadata_paths = [item for item in paths if item.endswith(".dist-info/METADATA")]
        if len(metadata_paths) != 1:
            raise AssertionError("wheel must contain exactly one dist-info/METADATA file")
        _check_identity(archive.read(metadata_paths[0]), expected_name, expected_version)

        entry_point_paths = [item for item in paths if item.endswith(".dist-info/entry_points.txt")]
        if len(entry_point_paths) != 1:
            raise AssertionError("wheel must declare its CLI console entry points")
        parser = configparser.ConfigParser()
        parser.read_string(archive.read(entry_point_paths[0]).decode("utf-8"))
        actual_entry_points = dict(parser.items("console_scripts"))
        for command, target in EXPECTED_ENTRY_POINTS.items():
            if actual_entry_points.get(command) != target:
                raise AssertionError(f"wheel entry point {command!r} is missing or incorrect")


def check_sdist(path: Path, expected_name: str, expected_version: str, license_bytes: bytes) -> None:
    with tarfile.open(path, "r:gz") as archive:
        members = [item for item in archive.getmembers() if item.isfile()]
        paths = [item.name for item in members]
        _check_no_marketing_log(paths)
        json_paths = [
            item.name
            for item in members
            if PurePosixPath(item.name).parts[-2:] in (
                ("tools", "swarm_haiku_3.json"),
                ("tools", "swarm_haiku_research.json"),
            )
        ]
        if len(json_paths) != 2:
            raise AssertionError("sdist must include both packaged JSON configurations")
        for item in json_paths:
            payload = archive.extractfile(item)
            if payload is None:
                raise AssertionError(f"cannot read packaged JSON configuration: {item}")
            json.loads(payload.read().decode("utf-8"))

        license_members = [item for item in members if PurePosixPath(item.name).name == "LICENSE"]
        if len(license_members) != 1:
            raise AssertionError("sdist must contain exactly one LICENSE file")
        license_payload = archive.extractfile(license_members[0])
        if license_payload is None or license_payload.read() != license_bytes:
            raise AssertionError("sdist LICENSE must be byte-identical to repository LICENSE")

        metadata_members = [
            item
            for item in members
            if PurePosixPath(item.name).name == "PKG-INFO"
            and len(PurePosixPath(item.name).parts) == 2
        ]
        if len(metadata_members) != 1:
            raise AssertionError("sdist must contain exactly one PKG-INFO file")
        metadata_payload = archive.extractfile(metadata_members[0])
        if metadata_payload is None:
            raise AssertionError("cannot read sdist PKG-INFO")
        _check_identity(metadata_payload.read(), expected_name, expected_version)


def main() -> int:
    dist_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    wheels = sorted(dist_dir.glob("*.whl"))
    source_archives = sorted(dist_dir.glob("*.tar.gz"))
    if len(wheels) != 1 or len(source_archives) != 1:
        raise AssertionError("expected exactly one wheel and one .tar.gz source distribution")

    name, version = _project_identity()
    license_bytes = (ROOT / "LICENSE").read_bytes()
    check_wheel(wheels[0], name, version, license_bytes)
    check_sdist(source_archives[0], name, version, license_bytes)
    print(f"Validated {wheels[0].name} and {source_archives[0].name}")
    print("Verified distribution metadata, CLI entry points, packaged JSON, MIT LICENSE bytes, and log exclusion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
