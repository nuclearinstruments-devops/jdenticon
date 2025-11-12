"""
Icon generator for Jdenticon
"""
from .graphics import Graphics
from .transform import Transform
from .shapes import center_shape, outer_shape
from .color import corrected_hsl
from .hash_utils import parse_hex
from .config import get_configuration


def color_theme(hue, config):
    """
    Gets a set of identicon color candidates for a specified hue and config.
    
    Args:
        hue: Hue value [0, 1]
        config: Configuration object
        
    Returns:
        List of color strings
    """
    hue = config.hue(hue)
    return [
        # Dark gray
        corrected_hsl(hue, config.grayscale_saturation, config.grayscale_lightness(0)),
        # Mid color
        corrected_hsl(hue, config.color_saturation, config.color_lightness(0.5)),
        # Light gray
        corrected_hsl(hue, config.grayscale_saturation, config.grayscale_lightness(1)),
        # Light color
        corrected_hsl(hue, config.color_saturation, config.color_lightness(1)),
        # Dark color
        corrected_hsl(hue, config.color_saturation, config.color_lightness(0))
    ]


def icon_generator(renderer, hash_str, config=None):
    """
    Draws an identicon to a specified renderer.
    
    Args:
        renderer: Renderer instance
        hash_str: Hexadecimal hash string
        config: Configuration (dict, number, or None)
    """
    parsed_config = get_configuration(config, 0.08)
    
    # Set background color
    if parsed_config.back_color:
        renderer.set_background(parsed_config.back_color)
    
    # Calculate padding and round to nearest integer
    size = renderer.icon_size
    padding = int(0.5 + size * parsed_config.icon_padding)
    size -= padding * 2
    
    graphics = Graphics(renderer)
    
    # Calculate cell size and ensure it is an integer
    cell = int(size / 4)
    
    # Center icon since cell size is integer based
    x = int(padding + size / 2 - cell * 2)
    y = int(padding + size / 2 - cell * 2)
    
    # Available colors
    hue = parse_hex(hash_str, -7) / 0xfffffff
    available_colors = color_theme(hue, parsed_config)
    
    # Select color indexes
    selected_color_indexes = []
    
    def is_duplicate(values):
        """Check if color index creates a duplicate."""
        if index in values:
            for v in values:
                if v in selected_color_indexes:
                    return True
        return False
    
    for i in range(3):
        index = parse_hex(hash_str, 8 + i, 1) % len(available_colors)
        # Disallow dark gray and dark color combo
        # Disallow light gray and light color combo
        if is_duplicate([0, 4]) or is_duplicate([2, 3]):
            index = 1
        selected_color_indexes.append(index)
    
    def render_shape(color_index, shapes_func, index_pos, rotation_index, positions):
        """Render a shape at multiple positions."""
        shape_index = parse_hex(hash_str, index_pos, 1)
        r = parse_hex(hash_str, rotation_index, 1) if rotation_index else 0
        
        renderer.begin_shape(available_colors[selected_color_indexes[color_index]])
        
        for i, pos in enumerate(positions):
            graphics.current_transform = Transform(
                x + pos[0] * cell,
                y + pos[1] * cell,
                cell,
                (r + i) % 4
            )
            shapes_func(shape_index, graphics, cell, i)
        
        renderer.end_shape()
    
    # Render shapes
    # Sides
    render_shape(0, outer_shape, 2, 3, [
        [1, 0], [2, 0], [2, 3], [1, 3],
        [0, 1], [3, 1], [3, 2], [0, 2]
    ])
    # Corners
    render_shape(1, outer_shape, 4, 5, [
        [0, 0], [3, 0], [3, 3], [0, 3]
    ])
    # Center
    render_shape(2, center_shape, 1, None, [
        [1, 1], [2, 1], [2, 2], [1, 2]
    ])
    
    renderer.finish()
