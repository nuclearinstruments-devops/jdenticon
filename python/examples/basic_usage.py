#!/usr/bin/env python3
"""
Basic usage examples for Jdenticon Python
"""
import sys
import os

# Add parent directory to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import jdenticon


def generate_svg_example():
    """Generate an SVG identicon."""
    print("Generating SVG identicon...")
    
    # Generate SVG for a user email
    svg_string = jdenticon.to_svg("user@example.com", 200)
    
    # Save to file
    output_file = "example_icon.svg"
    with open(output_file, "w") as f:
        f.write(svg_string)
    
    print(f"SVG saved to {output_file}")
    print(f"SVG length: {len(svg_string)} bytes\n")


def generate_png_example():
    """Generate a PNG identicon."""
    print("Generating PNG identicon...")
    
    try:
        # Generate PNG for a username
        png_bytes = jdenticon.to_png("johndoe", 200)
        
        # Save to file
        output_file = "example_icon.png"
        with open(output_file, "wb") as f:
            f.write(png_bytes)
        
        print(f"PNG saved to {output_file}")
        print(f"PNG size: {len(png_bytes)} bytes\n")
    except ImportError as e:
        print(f"Skipping PNG example: {e}\n")


def generate_different_sizes():
    """Generate icons at different sizes."""
    print("Generating icons at different sizes...")
    
    sizes = [32, 64, 128, 256]
    value = "demo@test.com"
    
    for size in sizes:
        svg = jdenticon.to_svg(value, size)
        filename = f"example_icon_{size}x{size}.svg"
        with open(filename, "w") as f:
            f.write(svg)
        print(f"Created {filename}")
    
    print()


def generate_from_different_values():
    """Generate icons from different input values."""
    print("Generating icons from different values...")
    
    values = [
        "user1@example.com",
        "user2@example.com",
        "12345",
        "test-user",
        "Alice Smith"
    ]
    
    for i, value in enumerate(values):
        svg = jdenticon.to_svg(value, 100)
        filename = f"example_user_{i+1}.svg"
        with open(filename, "w") as f:
            f.write(svg)
        print(f"Created {filename} for '{value}'")
    
    print()


def generate_with_custom_padding():
    """Generate icons with custom padding."""
    print("Generating icons with different padding...")
    
    paddings = [0.0, 0.08, 0.15, 0.25]
    
    for padding in paddings:
        svg = jdenticon.to_svg("padding-test", 100, padding)
        filename = f"example_padding_{int(padding*100)}.svg"
        with open(filename, "w") as f:
            f.write(svg)
        print(f"Created {filename} with padding {padding}")
    
    print()


def main():
    """Run all examples."""
    print("=" * 60)
    print("Jdenticon Python - Basic Usage Examples")
    print("=" * 60)
    print()
    
    generate_svg_example()
    generate_png_example()
    generate_different_sizes()
    generate_from_different_values()
    generate_with_custom_padding()
    
    print("=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
