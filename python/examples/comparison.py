#!/usr/bin/env python3
"""
Comparison example - Shows Python implementation output
"""
import sys
import os

# Add parent directory to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import jdenticon


def generate_comparison_examples():
    """Generate examples to compare with JavaScript version."""
    print("=" * 60)
    print("Jdenticon Python - Comparison Examples")
    print("=" * 60)
    print()
    print("Generating identicons that can be compared with JS version...")
    print()
    
    test_values = [
        'test@example.com',
        'user123',
        'alice',
        'bob',
        'hello world',
    ]
    
    for value in test_values:
        svg = jdenticon.to_svg(value, 200)
        filename = f'python_{value.replace("@", "_at_").replace(" ", "_")}.svg'
        
        with open(filename, 'w') as f:
            f.write(svg)
        
        print(f"✓ Created {filename}")
        print(f"  Value: '{value}'")
        print(f"  Size: {len(svg)} bytes")
        print()
    
    print("=" * 60)
    print("To compare with JavaScript version, run:")
    print("  node -e \"const j=require('../dist/jdenticon-node.js'); console.log(j.toSvg('test@example.com', 200));\"")
    print("=" * 60)


if __name__ == '__main__':
    generate_comparison_examples()
