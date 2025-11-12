"""
Base renderer for Jdenticon
"""


class Renderer:
    """Base class for renderers."""
    
    def __init__(self, icon_size):
        """
        Initialize renderer.
        
        Args:
            icon_size: Icon width and height in pixels
        """
        self.icon_size = icon_size
    
    def set_background(self, fill_color):
        """
        Sets the background color.
        
        Args:
            fill_color: Fill color in format #rrggbb[aa]
        """
        raise NotImplementedError()
    
    def begin_shape(self, color):
        """
        Begins a new shape.
        
        Args:
            color: Fill color in format #rrggbb
        """
        raise NotImplementedError()
    
    def add_polygon(self, points):
        """
        Adds a polygon to the current shape.
        
        Args:
            points: List of Point objects
        """
        raise NotImplementedError()
    
    def add_circle(self, point, diameter, invert):
        """
        Adds a circle to the current shape.
        
        Args:
            point: Center point (Point object)
            diameter: Circle diameter
            invert: Whether to invert the circle
        """
        raise NotImplementedError()
    
    def end_shape(self):
        """Ends the current shape."""
        raise NotImplementedError()
    
    def finish(self):
        """Finishes rendering."""
        raise NotImplementedError()
