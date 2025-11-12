"""
Main API for Jdenticon Python
"""
from .hash_utils import is_valid_hash, compute_hash
from .svg_renderer import SvgWriter, SvgRenderer
from .icon_generator import icon_generator
from .config import configure as config_func


def to_svg(hash_or_value, size, config=None):
    """
    Draws an identicon as an SVG string.
    
    Args:
        hash_or_value: A hexadecimal hash string or any value that will be hashed
        size: Icon size in pixels
        config: Optional configuration (dict or number for padding)
        
    Returns:
        SVG string
    """
    writer = SvgWriter(size)
    hash_str = is_valid_hash(hash_or_value) or compute_hash(hash_or_value)
    icon_generator(SvgRenderer(writer), hash_str, config)
    return writer.to_string()


def to_png(hash_or_value, size, config=None):
    """
    Draws an identicon as PNG.
    
    Args:
        hash_or_value: A hexadecimal hash string or any value that will be hashed
        size: Icon size in pixels
        config: Optional configuration (dict or number for padding)
        
    Returns:
        PNG data as bytes
    """
    try:
        from PIL import Image, ImageDraw
        from io import BytesIO
        from .renderer import Renderer
        from .color import parse_color
        from .hash_utils import parse_hex
        import math
    except ImportError:
        raise ImportError(
            "PNG generation requires Pillow. Install it with: pip install Pillow"
        )
    
    class PngRenderer(Renderer):
        """Renderer producing PNG output."""
        
        def __init__(self, size):
            super().__init__(size)
            self.image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            self.draw = ImageDraw.Draw(self.image)
            self._current_color = None
            self._current_shapes = []
        
        def set_background(self, fill_color):
            """Sets the background color."""
            parsed_color = parse_color(fill_color)
            if not parsed_color:
                return
            
            # Parse color and alpha
            r = parse_hex(parsed_color, 1, 2)
            g = parse_hex(parsed_color, 3, 2)
            b = parse_hex(parsed_color, 5, 2)
            
            alpha = 255
            if len(parsed_color) > 7:
                alpha = parse_hex(parsed_color, 7, 2)
            
            # Draw background rectangle
            self.draw.rectangle([(0, 0), (self.icon_size, self.icon_size)], 
                              fill=(r, g, b, alpha))
        
        def begin_shape(self, color):
            """Begins a new shape."""
            self._current_color = color
            self._current_shapes = []
        
        def add_polygon(self, points):
            """Adds a polygon to the current shape."""
            if points:
                coords = [(p.x, p.y) for p in points]
                self._current_shapes.append(('polygon', coords))
        
        def add_circle(self, point, diameter, invert):
            """Adds a circle to the current shape."""
            radius = diameter / 2
            x = point.x
            y = point.y
            bbox = [x, y, x + diameter, y + diameter]
            self._current_shapes.append(('ellipse', bbox))
        
        def end_shape(self):
            """Ends the current shape."""
            if self._current_color and self._current_shapes:
                # Parse color
                r = parse_hex(self._current_color, 1, 2)
                g = parse_hex(self._current_color, 3, 2)
                b = parse_hex(self._current_color, 5, 2)
                fill_color = (r, g, b, 255)
                
                # Draw all shapes
                for shape_type, shape_data in self._current_shapes:
                    if shape_type == 'polygon':
                        self.draw.polygon(shape_data, fill=fill_color)
                    elif shape_type == 'ellipse':
                        self.draw.ellipse(shape_data, fill=fill_color)
        
        def finish(self):
            """Finishes rendering."""
            pass
        
        def to_png(self):
            """Converts the image to PNG bytes."""
            buffer = BytesIO()
            self.image.save(buffer, format='PNG')
            return buffer.getvalue()
    
    # Generate PNG
    hash_str = is_valid_hash(hash_or_value) or compute_hash(hash_or_value)
    renderer = PngRenderer(size)
    icon_generator(renderer, hash_str, config)
    return renderer.to_png()


# Export configure function
configure = config_func
