#!/usr/bin/env python3
"""
Basic tests for Jdenticon Python
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import jdenticon


def test_svg_generation():
    """Test basic SVG generation."""
    print("Testing SVG generation...")
    
    svg = jdenticon.to_svg("test", 100)
    
    assert isinstance(svg, str), "SVG should be a string"
    assert svg.startswith('<svg'), "SVG should start with <svg tag"
    assert svg.endswith('</svg>'), "SVG should end with </svg> tag"
    assert 'width="100"' in svg, "SVG should have correct width"
    assert 'height="100"' in svg, "SVG should have correct height"
    
    print("  ✓ SVG generation works")


def test_hash_consistency():
    """Test that same input produces same output."""
    print("Testing hash consistency...")
    
    value = "consistency-test"
    svg1 = jdenticon.to_svg(value, 100)
    svg2 = jdenticon.to_svg(value, 100)
    
    assert svg1 == svg2, "Same input should produce same output"
    
    print("  ✓ Hash consistency works")


def test_different_values():
    """Test that different inputs produce different outputs."""
    print("Testing different values...")
    
    svg1 = jdenticon.to_svg("value1", 100)
    svg2 = jdenticon.to_svg("value2", 100)
    
    assert svg1 != svg2, "Different inputs should produce different outputs"
    
    print("  ✓ Different values produce different icons")


def test_size_parameter():
    """Test different sizes."""
    print("Testing size parameter...")
    
    svg_small = jdenticon.to_svg("test", 50)
    svg_large = jdenticon.to_svg("test", 200)
    
    assert 'width="50"' in svg_small, "Small SVG should have correct width"
    assert 'width="200"' in svg_large, "Large SVG should have correct width"
    assert svg_small != svg_large, "Different sizes should produce different SVG"
    
    print("  ✓ Size parameter works")


def test_config_padding():
    """Test configuration with padding."""
    print("Testing configuration...")
    
    svg_default = jdenticon.to_svg("test", 100)
    svg_padded = jdenticon.to_svg("test", 100, 0.15)
    
    # They should be different due to padding
    assert svg_default != svg_padded, "Different padding should produce different output"
    
    print("  ✓ Configuration works")


def test_png_generation():
    """Test PNG generation if Pillow is available."""
    print("Testing PNG generation...")
    
    try:
        png = jdenticon.to_png("test", 100)
        
        assert isinstance(png, bytes), "PNG should be bytes"
        assert len(png) > 0, "PNG should not be empty"
        # PNG files start with specific magic bytes
        assert png[:8] == b'\x89PNG\r\n\x1a\n', "PNG should have correct magic bytes"
        
        print("  ✓ PNG generation works")
    except ImportError:
        print("  ⊘ PNG generation skipped (Pillow not installed)")


def test_valid_hash():
    """Test using a pre-computed hash."""
    print("Testing with pre-computed hash...")
    
    # Use a valid SHA1 hash
    hash_str = "a665a45920422f9d417e4867efdc4fb8a04a1f3f"  # SHA1 of "123"
    svg = jdenticon.to_svg(hash_str, 100)
    
    assert isinstance(svg, str), "Should generate SVG from hash"
    assert '<svg' in svg, "Should contain SVG content"
    
    print("  ✓ Pre-computed hash works")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Jdenticon Python - Basic Tests")
    print("=" * 60)
    print()
    
    tests = [
        test_svg_generation,
        test_hash_consistency,
        test_different_values,
        test_size_parameter,
        test_config_padding,
        test_png_generation,
        test_valid_hash,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ Test error: {e}")
            failed += 1
    
    print()
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
