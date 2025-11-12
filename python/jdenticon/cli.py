#!/usr/bin/env python3
"""
Command-line interface for Jdenticon
"""
import sys
import argparse
from . import to_svg, to_png, __version__


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Generates an identicon as a PNG or SVG file for a specified value.'
    )
    
    parser.add_argument('value', 
                       help='Value to generate identicon for')
    parser.add_argument('-s', '--size', 
                       type=int, 
                       default=100,
                       help='Icon size in pixels (default: 100)')
    parser.add_argument('-o', '--output', 
                       help='Output file (default: stdout)')
    parser.add_argument('-f', '--format', 
                       choices=['svg', 'png'],
                       help='Format of generated icon (default: detected from output path or png)')
    parser.add_argument('-b', '--back-color',
                       help='Background color on format #rgb, #rgba, #rrggbb or #rrggbbaa')
    parser.add_argument('-p', '--padding',
                       type=float,
                       help='Padding in percent in range 0 to 0.5 (default: 0.08)')
    parser.add_argument('-v', '--version',
                       action='version',
                       version=f'Jdenticon Python {__version__}')
    
    args = parser.parse_args()
    
    # Determine format
    if args.format:
        generate_svg = args.format == 'svg'
    elif args.output:
        generate_svg = args.output.lower().endswith('.svg')
    else:
        generate_svg = False
    
    # Build config
    config = {}
    if args.padding is not None:
        if args.padding < 0 or args.padding >= 0.5:
            print("WARN: Invalid padding specified. Defaults to 0.08.", file=sys.stderr)
            args.padding = 0.08
        config['padding'] = args.padding
    
    if args.back_color:
        import re
        if not re.match(r'^#[0-9a-f]{3,8}$', args.back_color, re.IGNORECASE):
            print("WARN: Invalid background color specified. Defaults to transparent.", 
                  file=sys.stderr)
        else:
            config['backColor'] = args.back_color
    
    # Generate icon
    try:
        if generate_svg:
            output = to_svg(args.value, args.size, config if config else None)
            output_bytes = output.encode('utf-8')
        else:
            output_bytes = to_png(args.value, args.size, config if config else None)
    except ImportError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error generating identicon: {e}", file=sys.stderr)
        return 1
    
    # Write output
    if args.output:
        try:
            with open(args.output, 'wb') as f:
                f.write(output_bytes)
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            return 1
    else:
        sys.stdout.buffer.write(output_bytes)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
