"""
Transform utilities for Jdenticon
"""


class Point:
    """Represents a 2D point."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Transform:
    """
    Translates and rotates a point before rendering.
    """
    
    def __init__(self, x, y, size, rotation):
        """
        Initialize transform.
        
        Args:
            x: The x-coordinate of the upper left corner
            y: The y-coordinate of the upper left corner
            size: The size of the transformed rectangle
            rotation: Rotation (0 = 0 rad, 1 = 0.5π rad, 2 = π rad, 3 = 1.5π rad)
        """
        self._x = x
        self._y = y
        self._size = size
        self._rotation = rotation
    
    def transform_icon_point(self, x, y, w=0, h=0):
        """
        Transforms the specified point based on translation and rotation.
        
        Args:
            x: x-coordinate
            y: y-coordinate
            w: Width (optional)
            h: Height (optional)
            
        Returns:
            Point object with transformed coordinates
        """
        right = self._x + self._size
        bottom = self._y + self._size
        rotation = self._rotation
        
        if rotation == 1:
            return Point(right - y - h, self._y + x)
        elif rotation == 2:
            return Point(right - x - w, bottom - y - h)
        elif rotation == 3:
            return Point(self._x + y, bottom - x - w)
        else:
            return Point(self._x + x, self._y + y)


NO_TRANSFORM = Transform(0, 0, 0, 0)
