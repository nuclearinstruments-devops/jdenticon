"""
Configuration for Jdenticon
"""


class Configuration:
    """Jdenticon configuration."""
    
    def __init__(self):
        self.hue = lambda h: h
        self.color_saturation = 0.5
        self.grayscale_saturation = 0.0
        self.color_lightness = lambda l: 0.4 + l * 0.3
        self.grayscale_lightness = lambda l: 0.3 + l * 0.4
        self.back_color = None
        self.icon_padding = 0.08
    
    @staticmethod
    def default():
        """Returns default configuration."""
        return Configuration()


# Global configuration
_global_config = Configuration.default()


def configure(config_dict=None):
    """
    Configures the Jdenticon renderer.
    
    Args:
        config_dict: Dictionary with configuration options:
            - hue: Function or list for hue adjustment
            - colorSaturation: Color saturation [0.0, 1.0]
            - grayscaleSaturation: Grayscale saturation [0.0, 1.0]
            - colorLightness: Function or list for color lightness
            - grayscaleLightness: Function or list for grayscale lightness
            - backColor: Background color
            - padding: Icon padding [0.0, 0.5)
    """
    global _global_config
    
    if config_dict is None:
        _global_config = Configuration.default()
        return
    
    if isinstance(config_dict, dict):
        if 'hue' in config_dict:
            hue_val = config_dict['hue']
            if callable(hue_val):
                _global_config.hue = hue_val
            elif isinstance(hue_val, (list, tuple)):
                _global_config.hue = lambda h: hue_val[int(h * len(hue_val)) % len(hue_val)]
            else:
                _global_config.hue = lambda h: hue_val
        
        if 'colorSaturation' in config_dict:
            _global_config.color_saturation = float(config_dict['colorSaturation'])
        
        if 'grayscaleSaturation' in config_dict:
            _global_config.grayscale_saturation = float(config_dict['grayscaleSaturation'])
        
        if 'colorLightness' in config_dict:
            val = config_dict['colorLightness']
            if callable(val):
                _global_config.color_lightness = val
            elif isinstance(val, (list, tuple)):
                _global_config.color_lightness = lambda l: val[int(l * len(val)) % len(val)]
            else:
                _global_config.color_lightness = lambda l: val
        
        if 'grayscaleLightness' in config_dict:
            val = config_dict['grayscaleLightness']
            if callable(val):
                _global_config.grayscale_lightness = val
            elif isinstance(val, (list, tuple)):
                _global_config.grayscale_lightness = lambda l: val[int(l * len(val)) % len(val)]
            else:
                _global_config.grayscale_lightness = lambda l: val
        
        if 'backColor' in config_dict:
            _global_config.back_color = config_dict['backColor']
        
        if 'padding' in config_dict:
            _global_config.icon_padding = float(config_dict['padding'])


def get_configuration(config=None, default_padding=0.08):
    """
    Gets the configuration to use for rendering.
    
    Args:
        config: Configuration override (dict, number, or None)
        default_padding: Default padding value
        
    Returns:
        Configuration object
    """
    if config is None:
        result = Configuration()
        result.hue = _global_config.hue
        result.color_saturation = _global_config.color_saturation
        result.grayscale_saturation = _global_config.grayscale_saturation
        result.color_lightness = _global_config.color_lightness
        result.grayscale_lightness = _global_config.grayscale_lightness
        result.back_color = _global_config.back_color
        result.icon_padding = _global_config.icon_padding if _global_config.icon_padding is not None else default_padding
        return result
    
    if isinstance(config, (int, float)):
        # Backward compatibility: padding value
        result = Configuration()
        result.hue = _global_config.hue
        result.color_saturation = _global_config.color_saturation
        result.grayscale_saturation = _global_config.grayscale_saturation
        result.color_lightness = _global_config.color_lightness
        result.grayscale_lightness = _global_config.grayscale_lightness
        result.back_color = _global_config.back_color
        result.icon_padding = float(config)
        return result
    
    # Override configuration
    result = Configuration()
    if isinstance(config, dict):
        configure(config)
        result.hue = _global_config.hue
        result.color_saturation = _global_config.color_saturation
        result.grayscale_saturation = _global_config.grayscale_saturation
        result.color_lightness = _global_config.color_lightness
        result.grayscale_lightness = _global_config.grayscale_lightness
        result.back_color = _global_config.back_color
        result.icon_padding = _global_config.icon_padding if _global_config.icon_padding is not None else default_padding
    
    return result
