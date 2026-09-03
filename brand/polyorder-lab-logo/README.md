# Polyorder Lab logo suite

This folder is the reproducible source of truth for the Polyorder Lab identity. The nested contour **P** connects three ideas central to the lab: polymer architecture, composition fields, and ordered morphologies.

## Build

Requirements:

- Python 3.9 or later for all SVG variants
- ImageMagick 7 (`magick`) for PNG, ICO, and the raster preview

Run:

```bash
make
make check
```

For vector-only output:

```bash
make svg
```

The build script reads the two canonical outlined SVGs in `source/`, creates every variant under `dist/`, generates the preview board, and records file sizes and SHA-256 checksums in `dist/manifest.json`. The outlined wordmark has no runtime font dependency.

## Which file to use

| Context | Recommended asset |
| --- | --- |
| Reports, posters, slides on white | `dist/svg/polyorder-lab-primary.svg` |
| Dark presentation or banner | `dist/svg/polyorder-lab-primary-on-dark.svg` |
| Small horizontal placement | `dist/svg/polyorder-lab-compact.svg` |
| Website dark navigation bar | `dist/svg/polyorder-lab-navbar-on-dark.svg` |
| Square avatar or social profile | `dist/svg/polyorder-lab-mark.svg` |
| Centered or narrow composition | `dist/svg/polyorder-lab-stacked.svg` |
| One-color print | `dist/svg/polyorder-lab-monochrome-dark.svg` |
| Reversed one-color print | `dist/svg/polyorder-lab-monochrome-white.svg` |
| Browser and app icons | `dist/png/polyorder-lab-favicon.ico` and mark PNGs |

SVG is preferred whenever the destination supports it. PNG exports are supplied at several practical sizes for Office, web, and social use.

## Identity rules

### Palette

| Name | Hex | Meaning |
| --- | --- | --- |
| Polymer red | `#B72F47` | Molecular architecture and the outer domain |
| Field slate | `#334D5C` | Field theory and computation |
| Order mint | `#45B29D` | Emergent order and resolved structure |
| Descriptor slate | `#5B7083` | Supporting text |
| Deep navy | `#172A54` | Dark institutional backgrounds |

### Clear space and minimum size

- Keep clear space around the logo equal to at least one inner-stroke width of the contour mark.
- Do not place the primary logo smaller than 220 px wide on screen or 40 mm wide in print.
- Use the compact lockup below 220 px and the mark alone below 120 px.
- Use the dedicated 16, 32, and 48 px exports for browser icons.

### Do not

- Stretch, rotate, outline, or rearrange the elements.
- Change individual colors or add gradients, badges, bevels, or drop shadows.
- Place the dark wordmark on a dark background; use an `on-dark` variant.
- Typeset the wordmark manually; use the outlined artwork.

## Folder map

```text
source/      Canonical outlined SVG artwork and machine-readable specification
scripts/     Reproducible asset generator and validator
dist/svg/    Vector logo variants
dist/png/    Raster sizes, favicon, and web manifest
preview/     Visual suite board
```

Copyright © Polyorder Lab. All rights reserved.
