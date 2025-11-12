#!/bin/bash
# Command-line interface examples for Jdenticon Python

echo "=============================================="
echo "Jdenticon Python - CLI Examples"
echo "=============================================="
echo ""

# Make sure we're using the local jdenticon module
export PYTHONPATH="$(dirname "$0")/..:$PYTHONPATH"

echo "1. Basic SVG generation to file"
python3 -m jdenticon.cli "user@example.com" -s 200 -f svg -o example_cli_1.svg
echo "   Created example_cli_1.svg"
echo ""

echo "2. Basic PNG generation to file (requires Pillow)"
python3 -m jdenticon.cli "user@example.com" -s 200 -f png -o example_cli_2.png 2>/dev/null
if [ $? -eq 0 ]; then
    echo "   Created example_cli_2.png"
else
    echo "   Skipped (Pillow not installed)"
fi
echo ""

echo "3. SVG with custom size"
python3 -m jdenticon.cli "test123" -s 128 -f svg -o example_cli_3.svg
echo "   Created example_cli_3.svg (128x128)"
echo ""

echo "4. SVG with custom padding"
python3 -m jdenticon.cli "padded" -s 200 -f svg -p 0.15 -o example_cli_4.svg
echo "   Created example_cli_4.svg (padding: 0.15)"
echo ""

echo "5. SVG with background color"
python3 -m jdenticon.cli "colored-bg" -s 200 -f svg -b "#f0f0f0" -o example_cli_5.svg
echo "   Created example_cli_5.svg (light gray background)"
echo ""

echo "6. Auto-detect format from extension (.svg)"
python3 -m jdenticon.cli "auto-svg" -s 150 -o example_cli_6.svg
echo "   Created example_cli_6.svg (auto-detected SVG)"
echo ""

echo "7. Auto-detect format from extension (.png)"
python3 -m jdenticon.cli "auto-png" -s 150 -o example_cli_7.png 2>/dev/null
if [ $? -eq 0 ]; then
    echo "   Created example_cli_7.png (auto-detected PNG)"
else
    echo "   Skipped (Pillow not installed)"
fi
echo ""

echo "8. Small icon (32x32)"
python3 -m jdenticon.cli "small" -s 32 -o example_cli_8.svg
echo "   Created example_cli_8.svg (32x32)"
echo ""

echo "9. Large icon (512x512)"
python3 -m jdenticon.cli "large" -s 512 -o example_cli_9.svg
echo "   Created example_cli_9.svg (512x512)"
echo ""

echo "10. Combined options"
python3 -m jdenticon.cli "combined" -s 200 -f svg -b "#ffffff" -p 0.1 -o example_cli_10.svg
echo "    Created example_cli_10.svg (all options)"
echo ""

echo "=============================================="
echo "CLI Examples completed!"
echo "=============================================="
echo ""
echo "Note: Some examples may be skipped if Pillow is not installed."
echo "Install with: pip install Pillow"
