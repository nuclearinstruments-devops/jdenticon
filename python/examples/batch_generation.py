#!/usr/bin/env python3
"""
Batch generation examples for Jdenticon Python
"""
import sys
import os

# Add parent directory to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import jdenticon


def generate_user_avatars():
    """Generate avatars for a list of users."""
    print("Generating user avatars...")
    
    users = [
        'alice@example.com',
        'bob@example.com',
        'charlie@example.com',
        'diana@example.com',
        'eve@example.com',
        'frank@example.com',
        'grace@example.com',
        'henry@example.com',
        'iris@example.com',
        'jack@example.com',
    ]
    
    # Create output directory
    output_dir = 'batch_avatars'
    os.makedirs(output_dir, exist_ok=True)
    
    for user in users:
        # Generate SVG
        svg = jdenticon.to_svg(user, 128)
        
        # Create filename from username
        safe_name = user.split('@')[0]
        filename = os.path.join(output_dir, f"{safe_name}.svg")
        
        with open(filename, "w") as f:
            f.write(svg)
        
        print(f"Created {filename}")
    
    print(f"\nGenerated {len(users)} avatars in '{output_dir}/' directory\n")


def generate_size_variants():
    """Generate the same icon at multiple sizes."""
    print("Generating size variants...")
    
    value = "size-variants@example.com"
    sizes = [16, 32, 48, 64, 96, 128, 192, 256, 512]
    
    # Create output directory
    output_dir = 'size_variants'
    os.makedirs(output_dir, exist_ok=True)
    
    for size in sizes:
        svg = jdenticon.to_svg(value, size)
        filename = os.path.join(output_dir, f"icon_{size}x{size}.svg")
        
        with open(filename, "w") as f:
            f.write(svg)
        
        print(f"Created {filename}")
    
    print(f"\nGenerated {len(sizes)} size variants in '{output_dir}/' directory\n")


def generate_with_metadata():
    """Generate icons and save metadata."""
    print("Generating icons with metadata...")
    
    users_data = [
        {'name': 'Alice Johnson', 'email': 'alice.j@corp.com', 'id': '001'},
        {'name': 'Bob Smith', 'email': 'bob.s@corp.com', 'id': '002'},
        {'name': 'Carol White', 'email': 'carol.w@corp.com', 'id': '003'},
        {'name': 'David Brown', 'email': 'david.b@corp.com', 'id': '004'},
    ]
    
    # Create output directory
    output_dir = 'metadata_avatars'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate icons and metadata file
    metadata_lines = []
    
    for user in users_data:
        # Use email as the unique identifier
        svg = jdenticon.to_svg(user['email'], 100)
        
        filename = f"user_{user['id']}.svg"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, "w") as f:
            f.write(svg)
        
        metadata_lines.append(f"{user['id']},{user['name']},{user['email']},{filename}")
        print(f"Created {filepath}")
    
    # Save metadata
    metadata_file = os.path.join(output_dir, 'metadata.csv')
    with open(metadata_file, 'w') as f:
        f.write("ID,Name,Email,Icon File\n")
        f.write("\n".join(metadata_lines))
    
    print(f"\nMetadata saved to {metadata_file}\n")


def generate_hash_consistency_test():
    """Demonstrate that same value always generates same icon."""
    print("Testing hash consistency...")
    
    test_value = "consistency-test@example.com"
    
    # Generate the same icon 5 times
    icons = []
    for i in range(5):
        svg = jdenticon.to_svg(test_value, 100)
        icons.append(svg)
    
    # Check if all are identical
    all_same = all(icon == icons[0] for icon in icons)
    
    if all_same:
        print(f"✓ Generated icon for '{test_value}' 5 times - all identical!")
        
        # Save one copy
        with open("example_consistency.svg", "w") as f:
            f.write(icons[0])
        print("  Saved example_consistency.svg")
    else:
        print(f"✗ Icons are not consistent!")
    
    print()


def main():
    """Run all batch generation examples."""
    print("=" * 60)
    print("Jdenticon Python - Batch Generation Examples")
    print("=" * 60)
    print()
    
    generate_user_avatars()
    generate_size_variants()
    generate_with_metadata()
    generate_hash_consistency_test()
    
    print("=" * 60)
    print("Batch generation examples completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
