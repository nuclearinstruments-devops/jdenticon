#!/usr/bin/env python3
"""
Custom configuration examples for Jdenticon Python
"""
import sys
import os

# Add parent directory to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import jdenticon


def example_custom_colors():
    """Generate icons with custom color configuration."""
    print("Generating icons with custom colors...")
    
    # Blue theme
    blue_config = {
        'hue': [200, 220],  # Blue hues
        'colorSaturation': 0.7,
        'colorLightness': [0.4, 0.8],
        'padding': 0.1
    }
    
    svg = jdenticon.to_svg("blue-theme", 200, blue_config)
    with open("example_blue_theme.svg", "w") as f:
        f.write(svg)
    print("Created example_blue_theme.svg")
    
    # Green theme
    green_config = {
        'hue': [90, 150],  # Green hues
        'colorSaturation': 0.6,
        'colorLightness': [0.3, 0.7],
        'padding': 0.1
    }
    
    svg = jdenticon.to_svg("green-theme", 200, green_config)
    with open("example_green_theme.svg", "w") as f:
        f.write(svg)
    print("Created example_green_theme.svg")
    
    # Red theme
    red_config = {
        'hue': [0, 20],  # Red hues
        'colorSaturation': 0.8,
        'colorLightness': [0.4, 0.7],
        'padding': 0.1
    }
    
    svg = jdenticon.to_svg("red-theme", 200, red_config)
    with open("example_red_theme.svg", "w") as f:
        f.write(svg)
    print("Created example_red_theme.svg\n")


def example_background_colors():
    """Generate icons with different background colors."""
    print("Generating icons with background colors...")
    
    backgrounds = [
        ('#ffffff', 'white'),
        ('#000000', 'black'),
        ('#f0f0f0', 'lightgray'),
        ('#2c3e50', 'darkblue'),
    ]
    
    for bg_color, name in backgrounds:
        config = {
            'backColor': bg_color,
            'padding': 0.1
        }
        
        svg = jdenticon.to_svg("background-test", 200, config)
        filename = f"example_bg_{name}.svg"
        with open(filename, "w") as f:
            f.write(svg)
        print(f"Created {filename} with background {bg_color}")
    
    print()


def example_global_config():
    """Use global configuration."""
    print("Using global configuration...")
    
    # Set global configuration
    jdenticon.configure({
        'hue': [280, 320],  # Purple hues
        'colorSaturation': 0.6,
        'padding': 0.12,
        'backColor': '#f5f5f5'
    })
    
    # Generate multiple icons with the global config
    users = ['alice', 'bob', 'charlie']
    for user in users:
        svg = jdenticon.to_svg(user, 150)
        filename = f"example_global_{user}.svg"
        with open(filename, "w") as f:
            f.write(svg)
        print(f"Created {filename}")
    
    # Reset to default configuration
    jdenticon.configure(None)
    print()


def example_grayscale():
    """Generate grayscale icons."""
    print("Generating grayscale icons...")
    
    grayscale_config = {
        'colorSaturation': 0.0,  # No color saturation = grayscale
        'grayscaleSaturation': 0.0,
        'padding': 0.1
    }
    
    for i in range(3):
        svg = jdenticon.to_svg(f"grayscale-{i}", 150, grayscale_config)
        filename = f"example_grayscale_{i+1}.svg"
        with open(filename, "w") as f:
            f.write(svg)
        print(f"Created {filename}")
    
    print()


def example_high_contrast():
    """Generate high contrast icons."""
    print("Generating high contrast icons...")
    
    high_contrast_config = {
        'colorSaturation': 1.0,  # Maximum saturation
        'colorLightness': [0.2, 0.9],  # Wide lightness range
        'padding': 0.1
    }
    
    svg = jdenticon.to_svg("high-contrast", 200, high_contrast_config)
    with open("example_high_contrast.svg", "w") as f:
        f.write(svg)
    print("Created example_high_contrast.svg\n")


def main():
    """Run all configuration examples."""
    print("=" * 60)
    print("Jdenticon Python - Custom Configuration Examples")
    print("=" * 60)
    print()
    
    example_custom_colors()
    example_background_colors()
    example_global_config()
    example_grayscale()
    example_high_contrast()
    
    print("=" * 60)
    print("Configuration examples completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
