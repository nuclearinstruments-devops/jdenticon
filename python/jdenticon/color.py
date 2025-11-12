"""
Color utilities for Jdenticon
"""
import math


def dec_to_hex(v):
    """Converts decimal to 2-digit hex string."""
    v = int(v)
    if v < 0:
        return "00"
    elif v < 16:
        return "0" + hex(v)[2:]
    elif v < 256:
        return hex(v)[2:]
    else:
        return "ff"


def hue_to_rgb(m1, m2, h):
    """Converts hue to RGB component."""
    h = h + 6 if h < 0 else h - 6 if h > 6 else h
    
    if h < 1:
        value = m1 + (m2 - m1) * h
    elif h < 3:
        value = m2
    elif h < 4:
        value = m1 + (m2 - m1) * (4 - h)
    else:
        value = m1
    
    return dec_to_hex(255 * value)


def rgb(r, g, b):
    """
    Creates a color from RGB components.
    
    Args:
        r: Red channel [0, 255]
        g: Green channel [0, 255]
        b: Blue channel [0, 255]
        
    Returns:
        Color string in format #rrggbb
    """
    return "#" + dec_to_hex(r) + dec_to_hex(g) + dec_to_hex(b)


def hsl(hue, saturation, lightness):
    """
    Converts HSL color to hexadecimal RGB color.
    
    Args:
        hue: Hue in range [0, 1]
        saturation: Saturation in range [0, 1]
        lightness: Lightness in range [0, 1]
        
    Returns:
        Color string in format #rrggbb
    """
    if saturation == 0:
        partial_hex = dec_to_hex(lightness * 255)
        result = partial_hex + partial_hex + partial_hex
    else:
        m2 = lightness * (saturation + 1) if lightness <= 0.5 else lightness + saturation - lightness * saturation
        m1 = lightness * 2 - m2
        result = (hue_to_rgb(m1, m2, hue * 6 + 2) +
                  hue_to_rgb(m1, m2, hue * 6) +
                  hue_to_rgb(m1, m2, hue * 6 - 2))
    
    return "#" + result


def corrected_hsl(hue, saturation, lightness):
    """
    Converts HSL color to hexadecimal RGB color with lightness correction.
    
    Args:
        hue: Hue in range [0, 1]
        saturation: Saturation in range [0, 1]
        lightness: Lightness in range [0, 1]
        
    Returns:
        Color string in format #rrggbb
    """
    # The corrector specifies the perceived middle lightness for each hue
    correctors = [0.55, 0.5, 0.5, 0.46, 0.6, 0.55, 0.55]
    corrector = correctors[int(hue * 6 + 0.5) % len(correctors)]
    
    # Adjust the input lightness relative to the corrector
    if lightness < 0.5:
        lightness = lightness * corrector * 2
    else:
        lightness = corrector + (lightness - 0.5) * (1 - corrector) * 2
    
    return hsl(hue, saturation, lightness)


def parse_color(color):
    """
    Parses a color string.
    
    Args:
        color: Color value to parse (hex format #rgb[a] or #rrggbb[aa])
        
    Returns:
        Normalized color string or None
    """
    import re
    if re.match(r'^#[0-9a-f]{3,8}$', color, re.IGNORECASE):
        color_length = len(color)
        
        if color_length < 6:
            r = color[1]
            g = color[2]
            b = color[3]
            a = color[4] if color_length > 4 else ""
            return "#" + r + r + g + g + b + b + a + a
        
        if color_length == 7 or color_length > 8:
            return color
    
    return None
