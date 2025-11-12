"""
SVG renderer for Jdenticon
"""
from .renderer import Renderer
from .hash_utils import parse_hex
import math


class SvgWriter:
    """Writer for SVG output."""
    
    def __init__(self, icon_size):
        """
        Initialize SVG writer.
        
        Args:
            icon_size: Icon width and height in pixels
        """
        self.icon_size = icon_size
        self._s = (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{icon_size}" height="{icon_size}" '
            f'viewBox="0 0 {icon_size} {icon_size}">'
        )
    
    def set_background(self, fill_color, opacity):
        """
        Fills the background with the specified color.
        
        Args:
            fill_color: Fill color on format #rrggbb
            opacity: Opacity in range [0.0, 1.0]
        """
        if opacity:
            self._s += (
                f'<rect width="100%" height="100%" '
                f'fill="{fill_color}" opacity="{opacity:.2f}"/>'
            )
    
    def append_path(self, color, data_string):
        """
        Writes a path to the SVG string.
        
        Args:
            color: Fill color on format #rrggbb
            data_string: The SVG path data string
        """
        self._s += f'<path fill="{color}" d="{data_string}"/>'
    
    def to_string(self):
        """Gets the rendered image as an SVG string."""
        return self._s + "</svg>"


class SvgPath:
    """Builder for SVG path data."""
    
    def __init__(self):
        self._path_data = []
    
    def add_polygon(self, points):
        """
        Adds a polygon to the path.
        
        Args:
            points: List of Point objects
        """
        if not points:
            return
        
        path = f"M{points[0].x:.2f} {points[0].y:.2f}"
        for point in points[1:]:
            path += f"L{point.x:.2f} {point.y:.2f}"
        path += "Z"
        self._path_data.append(path)
    
    def add_circle(self, point, diameter, counter_clockwise):
        """
        Adds a circle to the path.
        
        Args:
            point: Center point (Point object)
            diameter: Circle diameter
            counter_clockwise: Whether to draw counter-clockwise
        """
        sweep_flag = 0 if counter_clockwise else 1
        radius = diameter / 2
        
        # SVG path for circle using two arc commands
        path = (
            f"M{point.x:.2f} {point.y + radius:.2f}"
            f"a{radius:.2f},{radius:.2f} 0 1,{sweep_flag} {diameter:.2f},0"
            f"a{radius:.2f},{radius:.2f} 0 1,{sweep_flag} {-diameter:.2f},0"
        )
        self._path_data.append(path)
    
    def to_string(self):
        """Gets the path data as a string."""
        return "".join(self._path_data)


class SvgRenderer(Renderer):
    """Renderer producing SVG output."""
    
    def __init__(self, writer):
        """
        Initialize SVG renderer.
        
        Args:
            writer: SvgWriter instance
        """
        super().__init__(writer.icon_size)
        self._writer = writer
        self._current_color = None
        self._current_path = None
    
    def set_background(self, fill_color):
        """Sets the background color."""
        from .color import parse_color
        from .hash_utils import parse_hex
        
        parsed_color = parse_color(fill_color)
        if not parsed_color:
            return
        
        opacity = 1.0
        if len(parsed_color) > 7:
            # Has alpha channel
            alpha = parse_hex(parsed_color, 7, 2)
            if not math.isnan(alpha):
                opacity = alpha / 255.0
                parsed_color = parsed_color[:7]
        
        self._writer.set_background(parsed_color, opacity)
    
    def begin_shape(self, color):
        """Begins a new shape."""
        self._current_color = color
        self._current_path = SvgPath()
    
    def add_polygon(self, points):
        """Adds a polygon to the current shape."""
        if self._current_path:
            self._current_path.add_polygon(points)
    
    def add_circle(self, point, diameter, invert):
        """Adds a circle to the current shape."""
        if self._current_path:
            self._current_path.add_circle(point, diameter, invert)
    
    def end_shape(self):
        """Ends the current shape."""
        if self._current_path and self._current_color:
            path_string = self._current_path.to_string()
            if path_string:
                self._writer.append_path(self._current_color, path_string)
    
    def finish(self):
        """Finishes rendering."""
        pass
