# Jdenticon Python

Python library for generating highly recognizable identicons.

![Sample identicons](https://jdenticon.com/hosted/github-samples.png)

This is a Python port of the original [Jdenticon](https://jdenticon.com) JavaScript library.

## Features

- Generate SVG identicons (no dependencies required)
- Generate PNG identicons (requires Pillow)
- Command-line tool for generating icons
- Configurable colors, padding, and more
- Compatible with the original Jdenticon hash format

## Installation

### Basic installation (SVG support only)

```bash
pip install jdenticon
```

### Installation with PNG support

```bash
pip install jdenticon[png]
```

Or install Pillow separately:

```bash
pip install jdenticon Pillow
```

## Quick Start

### Generate SVG

```python
import jdenticon

# Generate SVG string
svg_string = jdenticon.to_svg("user@example.com", 200)

# Save to file
with open("icon.svg", "w") as f:
    f.write(svg_string)
```

### Generate PNG (requires Pillow)

```python
import jdenticon

# Generate PNG bytes
png_bytes = jdenticon.to_png("user@example.com", 200)

# Save to file
with open("icon.png", "wb") as f:
    f.write(png_bytes)
```

### Command Line

```bash
# Generate SVG to stdout
jdenticon "user@example.com" -s 200 -f svg

# Generate PNG to file
jdenticon "user@example.com" -s 200 -o icon.png

# With custom background and padding
jdenticon "test" -s 200 -o icon.svg -f svg -b "#ff0000" -p 0.1
```

### Configuration

```python
import jdenticon

# Configure globally
jdenticon.configure({
    'hue': [100, 200],  # List of allowed hues (in degrees)
    'colorSaturation': 0.5,  # Color saturation (0.0 - 1.0)
    'grayscaleSaturation': 0.0,  # Grayscale saturation (0.0 - 1.0)
    'colorLightness': [0.4, 0.8],  # Lightness range for colors
    'grayscaleLightness': [0.3, 0.9],  # Lightness range for grayscale
    'backColor': '#ffffff',  # Background color
    'padding': 0.08  # Padding (0.0 - 0.5)
})

# Generate with configuration
svg = jdenticon.to_svg("user@example.com", 200)
```

You can also pass configuration directly to the generation functions:

```python
# Per-icon configuration
config = {'padding': 0.1, 'backColor': '#ff0000'}
svg = jdenticon.to_svg("user@example.com", 200, config)
```

## API Reference

### `to_svg(hash_or_value, size, config=None)`

Generates an identicon as an SVG string.

**Parameters:**
- `hash_or_value`: A hexadecimal hash string or any value that will be hashed
- `size`: Icon size in pixels
- `config`: Optional configuration (dict or number for padding)

**Returns:** SVG string

### `to_png(hash_or_value, size, config=None)`

Generates an identicon as PNG.

**Parameters:**
- `hash_or_value`: A hexadecimal hash string or any value that will be hashed
- `size`: Icon size in pixels
- `config`: Optional configuration (dict or number for padding)

**Returns:** PNG data as bytes

**Note:** Requires Pillow to be installed.

### `configure(config_dict)`

Configures the global Jdenticon settings.

**Parameters:**
- `config_dict`: Dictionary with configuration options (see Configuration section above)

## Examples

See the `examples/` directory for more usage examples:

- `basic_usage.py` - Basic SVG and PNG generation
- `custom_config.py` - Using custom configurations
- `batch_generation.py` - Generating multiple icons
- `cli_examples.sh` - Command-line usage examples

## Compatibility

This Python port aims to be compatible with the original Jdenticon JavaScript library,
meaning that the same hash value will produce the same identicon across both implementations.

## License

Jdenticon Python is available under the [MIT license](https://github.com/dmester/jdenticon/blob/master/LICENSE).

## Credits

- Original Jdenticon JavaScript library by [Daniel Mester Pirttijärvi](https://github.com/dmester)
- Python port by GitHub Copilot

## Links

- [Original Jdenticon (JavaScript)](https://github.com/dmester/jdenticon)
- [Jdenticon Website](https://jdenticon.com)
- [Jdenticon API Documentation](https://jdenticon.com/js-api/)
