"""
Jdenticon Python
https://github.com/dmester/jdenticon
Python port by GitHub Copilot

A Python library for generating highly recognizable identicons.
"""

from .generator import to_svg, to_png, configure

__version__ = "0.1.0"
__all__ = ["to_svg", "to_png", "configure"]
