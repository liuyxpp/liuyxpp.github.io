#!/usr/bin/env python3
"""Build the complete Polyorder Lab logo suite from canonical SVG sources."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source"
SVG_DIR = ROOT / "dist" / "svg"
PNG_DIR = ROOT / "dist" / "png"
PREVIEW_DIR = ROOT / "preview"
MANIFEST_PATH = ROOT / "dist" / "manifest.json"

EXPECTED_SVGS = {
    "polyorder-lab-compact-on-dark.svg",
    "polyorder-lab-compact.svg",
    "polyorder-lab-mark-monochrome-dark.svg",
    "polyorder-lab-mark-monochrome-white.svg",
    "polyorder-lab-mark.svg",
    "polyorder-lab-monochrome-dark.svg",
    "polyorder-lab-monochrome-white.svg",
    "polyorder-lab-navbar-on-dark.svg",
    "polyorder-lab-navbar.svg",
    "polyorder-lab-primary-on-dark.svg",
    "polyorder-lab-primary.svg",
    "polyorder-lab-stacked-on-dark.svg",
    "polyorder-lab-stacked.svg",
    "polyorder-lab-wordmark-on-dark.svg",
    "polyorder-lab-wordmark.svg",
}

SOURCE_COLORS = {
    "rgb(71.763611%, 18.431091%, 27.842712%)": "#B72F47",
    "rgb(19.999695%, 30.195618%, 36.077881%)": "#334D5C",
    "rgb(27.058411%, 69.802856%, 61.567688%)": "#45B29D",
    "rgb(35.68573%, 43.920898%, 51.371765%)": "#5B7083",
}


def qname(name: str) -> str:
    return f"{{{SVG_NS}}}{name}"


def load_spec() -> dict:
    return json.loads((SOURCE_DIR / "logo-spec.json").read_text(encoding="utf-8"))


def source_paths(path: Path, expected_count: int) -> list[ET.Element]:
    root = ET.parse(path).getroot()
    paths = list(root.findall(qname("path")))
    if len(paths) != expected_count:
        raise RuntimeError(
            f"{path.name}: expected {expected_count} paths, found {len(paths)}"
        )
    return paths


def normalize_colors(element: ET.Element) -> None:
    for node in element.iter():
        for attribute in ("fill", "stroke"):
            value = node.get(attribute)
            if value in SOURCE_COLORS:
                node.set(attribute, SOURCE_COLORS[value])


def recolor(element: ET.Element, color: str) -> None:
    for node in element.iter():
        if node.get("fill") and node.get("fill") != "none":
            node.set("fill", color)
        if node.get("stroke") and node.get("stroke") != "none":
            node.set("stroke", color)


def make_root(view_box: str, title: str, description: str) -> ET.Element:
    root = ET.Element(
        qname("svg"),
        {
            "viewBox": view_box,
            "role": "img",
            "aria-labelledby": "title description",
            "preserveAspectRatio": "xMidYMid meet",
        },
    )
    ET.SubElement(root, qname("title"), {"id": "title"}).text = title
    ET.SubElement(root, qname("desc"), {"id": "description"}).text = description
    return root


def add_group(
    root: ET.Element,
    group_id: str,
    paths: list[ET.Element],
    transform: str | None = None,
    policy: str = "brand",
) -> ET.Element:
    attrs = {"id": group_id}
    if transform:
        attrs["transform"] = transform
    group = ET.SubElement(root, qname("g"), attrs)
    for source in paths:
        element = copy.deepcopy(source)
        normalize_colors(element)
        if policy == "mono-dark":
            recolor(element, "#223746")
        elif policy == "mono-white":
            recolor(element, "#FFFFFF")
        elif policy == "wordmark-on-dark":
            current = element.get("fill")
            element.set("fill", "#F05A70" if current == "#B72F47" else "#FFFFFF")
        elif policy == "descriptor-on-dark":
            recolor(element, "#DCE6EC")
        group.append(element)
    return group


def write_svg(root: ET.Element, path: Path) -> None:
    ET.indent(root, space="  ")
    path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def build_primary_variants(primary: list[ET.Element], groups: dict) -> None:
    mark = primary[slice(*groups["mark"])]
    wordmark = primary[slice(*groups["wordmark"])]
    descriptor = primary[slice(*groups["descriptor"])]
    concept = (
        "Nested P-shaped contours represent polymer domains, composition fields, "
        "and ordered morphologies."
    )

    variants = [
        (
            "polyorder-lab-primary.svg",
            "0 0 1710 540",
            [("mark", mark, None, "brand"), ("wordmark", wordmark, None, "brand"), ("descriptor", descriptor, None, "brand")],
            "Polyorder Lab primary logo",
        ),
        (
            "polyorder-lab-primary-on-dark.svg",
            "0 0 1710 540",
            [("mark", mark, None, "brand"), ("wordmark", wordmark, None, "wordmark-on-dark"), ("descriptor", descriptor, None, "descriptor-on-dark")],
            "Polyorder Lab primary logo for dark backgrounds",
        ),
        (
            "polyorder-lab-compact.svg",
            "90 80 1500 385",
            [("mark", mark, None, "brand"), ("wordmark", wordmark, None, "brand")],
            "Polyorder Lab compact logo",
        ),
        (
            "polyorder-lab-compact-on-dark.svg",
            "90 80 1500 385",
            [("mark", mark, None, "brand"), ("wordmark", wordmark, None, "wordmark-on-dark")],
            "Polyorder Lab compact logo for dark backgrounds",
        ),
        (
            "polyorder-lab-wordmark.svg",
            "560 130 1035 230",
            [("wordmark", wordmark, None, "brand")],
            "Polyorder wordmark",
        ),
        (
            "polyorder-lab-wordmark-on-dark.svg",
            "560 130 1035 230",
            [("wordmark", wordmark, None, "wordmark-on-dark")],
            "Polyorder wordmark for dark backgrounds",
        ),
        (
            "polyorder-lab-monochrome-dark.svg",
            "0 0 1710 540",
            [("mark", mark, None, "mono-dark"), ("wordmark", wordmark, None, "mono-dark"), ("descriptor", descriptor, None, "mono-dark")],
            "Polyorder Lab monochrome dark logo",
        ),
        (
            "polyorder-lab-monochrome-white.svg",
            "0 0 1710 540",
            [("mark", mark, None, "mono-white"), ("wordmark", wordmark, None, "mono-white"), ("descriptor", descriptor, None, "mono-white")],
            "Polyorder Lab monochrome white logo",
        ),
    ]

    for filename, view_box, elements, title in variants:
        root = make_root(view_box, title, concept)
        for group_id, paths, transform, policy in elements:
            add_group(root, group_id, paths, transform, policy)
        write_svg(root, SVG_DIR / filename)

    navbar_transforms = {
        "mark": "matrix(0.38 0 0 0.38 -31 -15)",
        "wordmark": "matrix(0.60 0 0 0.60 -157 -54)",
    }
    for dark in (False, True):
        suffix = "-on-dark" if dark else ""
        root = make_root(
            "0 0 820 180",
            f"Polyorder Lab navigation logo{' for dark backgrounds' if dark else ''}",
            concept,
        )
        add_group(root, "mark", mark, navbar_transforms["mark"], "brand")
        add_group(
            root,
            "wordmark",
            wordmark,
            navbar_transforms["wordmark"],
            "wordmark-on-dark" if dark else "brand",
        )
        write_svg(root, SVG_DIR / f"polyorder-lab-navbar{suffix}.svg")

    for dark in (False, True):
        suffix = "-on-dark" if dark else ""
        root = make_root(
            "0 0 900 630",
            f"Polyorder Lab stacked logo{' for dark backgrounds' if dark else ''}",
            concept,
        )
        add_group(root, "mark", mark, "matrix(0.60 0 0 0.60 267 -25)", "brand")
        add_group(
            root,
            "wordmark",
            wordmark,
            "matrix(0.72 0 0 0.72 -327 233)",
            "wordmark-on-dark" if dark else "brand",
        )
        add_group(
            root,
            "descriptor",
            descriptor,
            "matrix(0.72 0 0 0.72 -253 274)",
            "descriptor-on-dark" if dark else "brand",
        )
        write_svg(root, SVG_DIR / f"polyorder-lab-stacked{suffix}.svg")


def build_mark_variants(mark_paths: list[ET.Element]) -> None:
    concept = "Three nested P-shaped contours representing polymer ordering."
    for filename, policy, title in (
        ("polyorder-lab-mark.svg", "brand", "Polyorder Lab mark"),
        ("polyorder-lab-mark-monochrome-dark.svg", "mono-dark", "Polyorder Lab dark monochrome mark"),
        ("polyorder-lab-mark-monochrome-white.svg", "mono-white", "Polyorder Lab white monochrome mark"),
    ):
        root = make_root("0 0 168 168", title, concept)
        add_group(root, "mark", mark_paths, None, policy)
        write_svg(root, SVG_DIR / filename)


def render_png(magick: str, source: Path, output: Path, width: int) -> None:
    subprocess.run(
        [magick, "-background", "none", str(source), "-resize", f"{width}x", str(output)],
        check=True,
    )


def build_rasters(magick: str) -> None:
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    jobs = {
        "polyorder-lab-primary.svg": (600, 1200, 2400),
        "polyorder-lab-primary-on-dark.svg": (600, 1200),
        "polyorder-lab-compact.svg": (600, 1200),
        "polyorder-lab-compact-on-dark.svg": (600, 1200),
        "polyorder-lab-navbar-on-dark.svg": (240, 480),
        "polyorder-lab-stacked.svg": (512, 1024),
        "polyorder-lab-stacked-on-dark.svg": (512, 1024),
        "polyorder-lab-mark.svg": (16, 32, 48, 180, 512, 1024),
        "polyorder-lab-mark-monochrome-dark.svg": (512,),
        "polyorder-lab-mark-monochrome-white.svg": (512,),
    }
    for source_name, widths in jobs.items():
        source = SVG_DIR / source_name
        stem = source.stem
        for width in widths:
            render_png(magick, source, PNG_DIR / f"{stem}-{width}.png", width)

    subprocess.run(
        [
            magick,
            str(PNG_DIR / "polyorder-lab-mark-16.png"),
            str(PNG_DIR / "polyorder-lab-mark-32.png"),
            str(PNG_DIR / "polyorder-lab-mark-48.png"),
            str(PNG_DIR / "polyorder-lab-favicon.ico"),
        ],
        check=True,
    )


def build_preview(primary: list[ET.Element], groups: dict, magick: str | None) -> None:
    mark = primary[slice(*groups["mark"])]
    wordmark = primary[slice(*groups["wordmark"])]
    descriptor = primary[slice(*groups["descriptor"])]
    root = make_root(
        "0 0 1600 1400",
        "Polyorder Lab logo suite preview",
        "Preview board showing primary, dark-background, compact, stacked, and mark variants.",
    )
    ET.SubElement(root, qname("rect"), {"width": "1600", "height": "1400", "fill": "#F3F6F8"})
    ET.SubElement(root, qname("text"), {"x": "80", "y": "75", "font-family": "Arial, sans-serif", "font-size": "34", "font-weight": "700", "fill": "#172A54"}).text = "Polyorder Lab identity suite"
    ET.SubElement(root, qname("text"), {"x": "80", "y": "112", "font-family": "Arial, sans-serif", "font-size": "20", "fill": "#5B7083"}).text = "Nested contours connect architecture, fields, and ordered morphologies."

    ET.SubElement(root, qname("rect"), {"x": "65", "y": "150", "width": "1470", "height": "410", "rx": "26", "fill": "#FFFFFF"})
    add_group(root, "preview-primary-mark", mark, "matrix(0.74 0 0 0.74 45 145)", "brand")
    add_group(root, "preview-primary-wordmark", wordmark, "matrix(0.74 0 0 0.74 45 145)", "brand")
    add_group(root, "preview-primary-descriptor", descriptor, "matrix(0.74 0 0 0.74 45 145)", "brand")

    ET.SubElement(root, qname("rect"), {"x": "65", "y": "595", "width": "1470", "height": "360", "rx": "26", "fill": "#172A54"})
    add_group(root, "preview-dark-mark", mark, "matrix(0.70 0 0 0.70 75 575)", "brand")
    add_group(root, "preview-dark-wordmark", wordmark, "matrix(0.70 0 0 0.70 75 575)", "wordmark-on-dark")
    add_group(root, "preview-dark-descriptor", descriptor, "matrix(0.70 0 0 0.70 75 575)", "descriptor-on-dark")

    ET.SubElement(root, qname("rect"), {"x": "65", "y": "990", "width": "420", "height": "335", "rx": "26", "fill": "#FFFFFF"})
    add_group(root, "preview-mark", mark, "matrix(0.55 0 0 0.55 106 990)", "brand")
    ET.SubElement(root, qname("text"), {"x": "185", "y": "1290", "font-family": "Arial, sans-serif", "font-size": "20", "font-weight": "700", "fill": "#334D5C", "text-anchor": "middle"}).text = "Contour P mark"

    ET.SubElement(root, qname("rect"), {"x": "520", "y": "990", "width": "1015", "height": "335", "rx": "26", "fill": "#FFFFFF"})
    add_group(root, "preview-navbar-mark", mark, "matrix(0.38 0 0 0.38 520 1008)", "brand")
    add_group(root, "preview-navbar-wordmark", wordmark, "matrix(0.60 0 0 0.60 394 969)", "brand")
    ET.SubElement(root, qname("text"), {"x": "1025", "y": "1290", "font-family": "Arial, sans-serif", "font-size": "20", "font-weight": "700", "fill": "#334D5C", "text-anchor": "middle"}).text = "Compact navigation lockup"

    preview_svg = PREVIEW_DIR / "polyorder-lab-logo-suite-preview.svg"
    write_svg(root, preview_svg)
    if magick:
        render_png(magick, preview_svg, PREVIEW_DIR / "polyorder-lab-logo-suite-preview.png", 1600)


def write_web_manifest() -> None:
    manifest = {
        "name": "Polyorder Lab",
        "short_name": "Polyorder",
        "icons": [
            {"src": "polyorder-lab-mark-180.png", "sizes": "180x180", "type": "image/png"},
            {"src": "polyorder-lab-mark-512.png", "sizes": "512x512", "type": "image/png"},
        ],
        "theme_color": "#172A54",
        "background_color": "#FFFFFF",
        "display": "standalone",
    }
    (PNG_DIR / "site.webmanifest").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_manifest() -> None:
    files = []
    for directory in (SVG_DIR, PNG_DIR, PREVIEW_DIR):
        for path in sorted(p for p in directory.rglob("*") if p.is_file()):
            files.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    MANIFEST_PATH.write_text(
        json.dumps({"suite": "Polyorder Lab", "files": files}, indent=2) + "\n",
        encoding="utf-8",
    )


def validate_generated(magick: str | None) -> None:
    actual_svgs = {path.name for path in SVG_DIR.glob("*.svg")}
    if actual_svgs != EXPECTED_SVGS:
        missing = sorted(EXPECTED_SVGS - actual_svgs)
        extra = sorted(actual_svgs - EXPECTED_SVGS)
        raise RuntimeError(f"Unexpected SVG set; missing={missing}, extra={extra}")
    for path in SVG_DIR.glob("*.svg"):
        ET.parse(path)
    ET.parse(PREVIEW_DIR / "polyorder-lab-logo-suite-preview.svg")
    if magick:
        pngs = sorted(PNG_DIR.glob("*.png")) + [
            PREVIEW_DIR / "polyorder-lab-logo-suite-preview.png"
        ]
        subprocess.run([magick, "identify", *map(str, pngs)], check=True, stdout=subprocess.DEVNULL)


def check_manifest(magick: str | None = None) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    failures = []
    for item in manifest["files"]:
        path = ROOT / item["path"]
        if not path.exists():
            failures.append(f"missing: {item['path']}")
        elif path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
            failures.append(f"changed: {item['path']}")
    if failures:
        raise RuntimeError("Logo suite verification failed:\n" + "\n".join(failures))
    validate_generated(magick)
    print(f"Verified {len(manifest['files'])} generated logo artifacts.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--svg-only", action="store_true", help="Skip PNG, ICO, and raster preview generation")
    parser.add_argument("--check", action="store_true", help="Verify generated files against dist/manifest.json")
    args = parser.parse_args()

    magick = shutil.which("magick")
    if args.check:
        check_manifest(magick)
        return

    for generated_dir in (SVG_DIR, PNG_DIR, PREVIEW_DIR):
        if generated_dir.exists():
            shutil.rmtree(generated_dir)

    spec = load_spec()
    primary_path = SOURCE_DIR / spec["source_files"]["primary"]
    mark_path = SOURCE_DIR / spec["source_files"]["mark"]
    primary = source_paths(primary_path, spec["primary_path_groups"]["descriptor"][1])
    mark = source_paths(mark_path, 3)

    SVG_DIR.mkdir(parents=True, exist_ok=True)
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    build_primary_variants(primary, spec["primary_path_groups"])
    build_mark_variants(mark)

    if not args.svg_only:
        if not magick:
            raise RuntimeError("ImageMagick 7 is required for PNG and ICO output. Run with --svg-only to build vectors only.")
        build_rasters(magick)
        write_web_manifest()
    build_preview(primary, spec["primary_path_groups"], magick if not args.svg_only else None)
    write_manifest()
    check_manifest(magick if not args.svg_only else None)


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
