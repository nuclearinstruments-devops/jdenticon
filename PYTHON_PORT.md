# Jdenticon Python Port

This directory contains a Python port of the Jdenticon library.

## What is Jdenticon?

Jdenticon is a JavaScript library for generating highly recognizable identicons using HTML5 canvas or SVG. This Python port provides the same functionality for Python applications.

## Quick Start

### Installation

```bash
cd python
pip install .
```

For PNG support (optional):
```bash
pip install .[png]
```

### Basic Usage

```python
import jdenticon

# Generate SVG
svg_string = jdenticon.to_svg("user@example.com", 200)

# Generate PNG (requires Pillow)
png_bytes = jdenticon.to_png("user@example.com", 200)
```

### Command Line

```bash
# Generate SVG
jdenticon "user@example.com" -s 200 -o icon.svg

# Generate PNG
jdenticon "user@example.com" -s 200 -o icon.png
```

## Features

- ✅ SVG generation (no dependencies)
- ✅ PNG generation (with Pillow)
- ✅ Command-line interface
- ✅ Configurable colors, padding, and more
- ✅ Compatible with original Jdenticon hash format
- ✅ Pure Python implementation

## Directory Structure

```
python/
├── jdenticon/           # Main library package
│   ├── __init__.py
│   ├── generator.py     # Main API (to_svg, to_png)
│   ├── icon_generator.py
│   ├── hash_utils.py
│   ├── color.py
│   ├── config.py
│   ├── shapes.py
│   ├── graphics.py
│   ├── transform.py
│   ├── renderer.py
│   ├── svg_renderer.py
│   └── cli.py           # Command-line interface
├── examples/            # Usage examples
│   ├── basic_usage.py
│   ├── custom_config.py
│   ├── batch_generation.py
│   └── cli_examples.sh
├── tests/               # Tests
│   └── test_basic.py
├── setup.py            # Setup script
├── pyproject.toml      # Modern Python package config
├── README.md           # Full documentation
└── INSTALL.md          # Installation guide
```

## Documentation

- See `python/README.md` for full documentation
- See `python/INSTALL.md` for installation instructions
- See `python/examples/` for usage examples

## API Compatibility

This Python port aims to be compatible with the original JavaScript library:
- Same hash input produces the same identicon
- Same configuration options
- Same visual output

## Examples

Generate identicons for users:
```python
import jdenticon

users = ['alice@example.com', 'bob@example.com', 'charlie@example.com']

for user in users:
    svg = jdenticon.to_svg(user, 128)
    with open(f'{user.split("@")[0]}.svg', 'w') as f:
        f.write(svg)
```

Custom configuration:
```python
import jdenticon

config = {
    'hue': [200, 220],  # Blue hues
    'colorSaturation': 0.7,
    'padding': 0.1,
    'backColor': '#f0f0f0'
}

svg = jdenticon.to_svg('user@example.com', 200, config)
```

## Testing

```bash
cd python/tests
python3 test_basic.py
```

## Requirements

- Python 3.6+
- Pillow (optional, for PNG generation)

## License

MIT License - Same as the original Jdenticon JavaScript library

## Credits

- Original Jdenticon JavaScript library by [Daniel Mester Pirttijärvi](https://github.com/dmester/jdenticon)
- Python port by GitHub Copilot

## Links

- [Original Jdenticon](https://github.com/dmester/jdenticon)
- [Jdenticon Website](https://jdenticon.com)
