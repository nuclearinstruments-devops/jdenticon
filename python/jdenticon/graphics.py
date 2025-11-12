"""
Graphics helper functions for rendering shapes
"""
from .transform import NO_TRANSFORM


class Graphics:
    """Provides helper functions for rendering common basic shapes."""
    
    def __init__(self, renderer):
        """
        Initialize graphics helper.
        
        Args:
            renderer: The renderer to draw to
        """
        self._renderer = renderer
        self.current_transform = NO_TRANSFORM
    
    def add_polygon(self, points, invert=False):
        """
        Adds a polygon to the underlying renderer.
        
        Args:
            points: List of coordinates [x0, y0, x1, y1, ..., xn, yn]
            invert: Whether to invert the polygon
        """
        di = -2 if invert else 2
        transformed_points = []
        
        start_i = len(points) - 2 if invert else 0
        
        i = start_i
        while (invert and i >= 0) or (not invert and i < len(points)):
            point = self.current_transform.transform_icon_point(points[i], points[i + 1])
            transformed_points.append(point)
            i += di
        
        self._renderer.add_polygon(transformed_points)
    
    def add_circle(self, x, y, size, invert=False):
        """
        Adds a circle to the underlying renderer.
        
        Args:
            x: The x-coordinate of the upper left corner
            y: The y-coordinate of the upper left corner
            size: The size of the ellipse
            invert: Whether to invert the circle
        """
        p = self.current_transform.transform_icon_point(x, y, size, size)
        self._renderer.add_circle(p, size, invert)
    
    def add_rectangle(self, x, y, w, h, invert=False):
        """
        Adds a rectangle to the underlying renderer.
        
        Args:
            x: The x-coordinate of the upper left corner
            y: The y-coordinate of the upper left corner
            w: The width of the rectangle
            h: The height of the rectangle
            invert: Whether to invert the rectangle
        """
        self.add_polygon([
            x, y,
            x + w, y,
            x + w, y + h,
            x, y + h
        ], invert)
    
    def add_triangle(self, x, y, w, h, r, invert=False):
        """
        Adds a right triangle to the underlying renderer.
        
        Args:
            x: The x-coordinate of the upper left corner
            y: The y-coordinate of the upper left corner
            w: The width of the triangle
            h: The height of the triangle
            r: The rotation of the triangle (clockwise)
            invert: Whether to invert the triangle
        """
        points = [
            x + w, y,
            x + w, y + h,
            x, y + h,
            x, y
        ]
        # Remove two coordinates based on rotation
        splice_index = ((r or 0) % 4) * 2
        del points[splice_index:splice_index + 2]
        self.add_polygon(points, invert)
    
    def add_rhombus(self, x, y, w, h, invert=False):
        """
        Adds a rhombus to the underlying renderer.
        
        Args:
            x: The x-coordinate of the upper left corner
            y: The y-coordinate of the upper left corner
            w: The width of the rhombus
            h: The height of the rhombus
            invert: Whether to invert the rhombus
        """
        self.add_polygon([
            x + w / 2, y,
            x + w, y + h / 2,
            x + w / 2, y + h,
            x, y + h / 2
        ], invert)
