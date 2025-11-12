# Jdenticon Python - Quick Start Guide

Get started with Jdenticon Python in 5 minutes!

## Installation

```bash
# Navigate to the python directory
cd python

# Install the package (SVG only)
pip install .

# OR install with PNG support
pip install .[png]
```

## Your First Identicon

### Python Script

Create a file called `my_first_icon.py`:

```python
import jdenticon

# Generate an SVG identicon
svg = jdenticon.to_svg("user@example.com", 200)

# Save to file
with open("my_icon.svg", "w") as f:
    f.write(svg)

print("Icon created: my_icon.svg")
```

Run it:
```bash
python3 my_first_icon.py
```

### Command Line

```bash
# Generate SVG
jdenticon "user@example.com" -s 200 -o my_icon.svg

# Generate PNG (requires Pillow)
jdenticon "user@example.com" -s 200 -o my_icon.png
```

## Common Use Cases

### 1. User Avatars

```python
import jdenticon

def generate_user_avatar(email, size=128):
    """Generate an avatar for a user."""
    svg = jdenticon.to_svg(email, size)
    filename = f"avatar_{email.replace('@', '_at_').replace('.', '_')}.svg"
    with open(filename, "w") as f:
        f.write(svg)
    return filename

# Use it
avatar_file = generate_user_avatar("alice@example.com")
print(f"Avatar saved as {avatar_file}")
```

### 2. Custom Colors

```python
import jdenticon

# Blue theme
config = {
    'hue': [200, 220],
    'colorSaturation': 0.7,
    'padding': 0.1
}

svg = jdenticon.to_svg("user@example.com", 200, config)
with open("blue_icon.svg", "w") as f:
    f.write(svg)
```

### 3. Batch Generation

```python
import jdenticon

users = ['alice@example.com', 'bob@example.com', 'charlie@example.com']

for user in users:
    svg = jdenticon.to_svg(user, 100)
    filename = f"{user.split('@')[0]}.svg"
    with open(filename, "w") as f:
        f.write(svg)
    print(f"Generated {filename}")
```

### 4. Web API Endpoint (Flask)

```python
from flask import Flask, Response
import jdenticon

app = Flask(__name__)

@app.route('/avatar/<user_id>')
def avatar(user_id):
    svg = jdenticon.to_svg(user_id, 128)
    return Response(svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run()
```

### 5. Email Templates

```python
import jdenticon

def create_email_signature(name, email):
    """Create an email signature with an identicon."""
    svg = jdenticon.to_svg(email, 80)
    
    # Inline SVG in HTML
    html = f"""
    <div style="display: flex; align-items: center;">
        {svg}
        <div style="margin-left: 10px;">
            <strong>{name}</strong><br>
            {email}
        </div>
    </div>
    """
    return html

signature = create_email_signature("Alice Smith", "alice@example.com")
print(signature)
```

## Configuration Options

### Global Configuration

```python
import jdenticon

# Set global configuration
jdenticon.configure({
    'hue': [100, 200],              # Allowed hues (degrees)
    'colorSaturation': 0.5,         # 0.0 - 1.0
    'grayscaleSaturation': 0.0,     # 0.0 - 1.0
    'colorLightness': [0.4, 0.8],   # Lightness range
    'grayscaleLightness': [0.3, 0.9],
    'backColor': '#ffffff',         # Background color
    'padding': 0.08                 # 0.0 - 0.5
})

# All icons generated after this will use the configuration
svg1 = jdenticon.to_svg("user1", 100)
svg2 = jdenticon.to_svg("user2", 100)
```

### Per-Icon Configuration

```python
import jdenticon

# Override configuration for specific icon
config = {'padding': 0.15, 'backColor': '#f0f0f0'}
svg = jdenticon.to_svg("user@example.com", 200, config)
```

## CLI Options

```bash
# Basic usage
jdenticon <value> -s <size> -o <output>

# All options
jdenticon <value> \
  -s 200 \                    # Size in pixels
  -f svg \                    # Format (svg or png)
  -o icon.svg \               # Output file
  -p 0.1 \                    # Padding (0.0-0.5)
  -b "#f0f0f0"               # Background color
```

## Troubleshooting

### PNG Generation Fails

If you get an error about Pillow not being installed:

```bash
pip install Pillow
```

### Import Error

If Python can't find the jdenticon module:

```bash
# Make sure you're in the right directory
cd python
pip install -e .  # Install in development mode
```

### Module Not Found in CLI

If the `jdenticon` command is not found:

```bash
# Use Python module syntax instead
python3 -m jdenticon.cli "value" -s 200 -o icon.svg
```

## Next Steps

- See `examples/` for more examples
- Read `README.md` for full API documentation
- Check `FEATURES.md` for complete feature list
- Run `python/tests/test_basic.py` to verify installation

## Getting Help

- Check the examples in the `examples/` directory
- Read the full documentation in `README.md`
- See the original Jdenticon docs: https://jdenticon.com

## Tips

1. **Same input = same icon**: Use email addresses or user IDs as input for consistent icons
2. **Size matters**: Use appropriate sizes (100-200px for avatars)
3. **Test colors**: Try different configurations to find the right look
4. **Cache icons**: Consider caching generated icons to improve performance
5. **Use SVG when possible**: SVG scales better and has smaller file sizes

Happy icon generating! 🎨
