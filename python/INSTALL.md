# Installation Guide

## Installation

### Option 1: Install from source (for development)

```bash
cd python
pip install -e .
```

### Option 2: Install with SVG support only

```bash
cd python
pip install .
```

### Option 3: Install with PNG support

```bash
cd python
pip install .[png]
```

Or install Pillow separately:

```bash
cd python
pip install .
pip install Pillow
```

## Verifying Installation

After installation, you can verify it works:

```bash
# Test the CLI
jdenticon "test" -s 100 -o test.svg

# Test in Python
python3 -c "import jdenticon; print(jdenticon.to_svg('test', 100))"
```

## Running Examples

```bash
cd examples

# Run basic usage examples
python3 basic_usage.py

# Run custom configuration examples
python3 custom_config.py

# Run batch generation examples
python3 batch_generation.py

# Run CLI examples (Unix/Linux/Mac)
bash cli_examples.sh
```

## Running Tests

```bash
cd tests
python3 test_basic.py
```

## Requirements

- Python 3.6 or higher
- Pillow (optional, for PNG generation)

## Uninstallation

```bash
pip uninstall jdenticon
```
