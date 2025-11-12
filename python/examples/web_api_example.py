#!/usr/bin/env python3
"""
Web API Example - Shows how to use Jdenticon in a web service

This is a simple example showing how to create an avatar service.
In production, you would want to add caching, error handling, etc.

Note: This example requires Flask. Install it with:
    pip install Flask

Run the server with:
    python3 web_api_example.py

Then visit:
    http://localhost:5000/avatar/user@example.com
"""
import sys
import os

# Add parent directory to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from flask import Flask, Response, request, render_template_string
    import jdenticon
    
    app = Flask(__name__)
    
    
    @app.route('/')
    def index():
        """Show a demo page."""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Jdenticon Python Avatar Service</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                }
                .avatar-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
                    gap: 20px;
                    margin-top: 20px;
                }
                .avatar-item {
                    text-align: center;
                }
                .avatar-item img {
                    width: 100%;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                code {
                    background: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                }
                pre {
                    background: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }
            </style>
        </head>
        <body>
            <h1>🎨 Jdenticon Python Avatar Service</h1>
            <p>Generate unique avatars for any user identifier!</p>
            
            <h2>API Usage</h2>
            <pre>GET /avatar/&lt;identifier&gt;?size=&lt;size&gt;&amp;format=&lt;svg|png&gt;</pre>
            
            <h3>Examples:</h3>
            <ul>
                <li><code>/avatar/user@example.com</code></li>
                <li><code>/avatar/user123?size=200</code></li>
                <li><code>/avatar/alice?format=svg&amp;size=150</code></li>
            </ul>
            
            <h2>Demo Avatars</h2>
            <div class="avatar-grid">
                <div class="avatar-item">
                    <img src="/avatar/alice@example.com?size=128" alt="Alice">
                    <p>alice@example.com</p>
                </div>
                <div class="avatar-item">
                    <img src="/avatar/bob@example.com?size=128" alt="Bob">
                    <p>bob@example.com</p>
                </div>
                <div class="avatar-item">
                    <img src="/avatar/charlie@example.com?size=128" alt="Charlie">
                    <p>charlie@example.com</p>
                </div>
                <div class="avatar-item">
                    <img src="/avatar/diana@example.com?size=128" alt="Diana">
                    <p>diana@example.com</p>
                </div>
                <div class="avatar-item">
                    <img src="/avatar/eve@example.com?size=128" alt="Eve">
                    <p>eve@example.com</p>
                </div>
                <div class="avatar-item">
                    <img src="/avatar/frank@example.com?size=128" alt="Frank">
                    <p>frank@example.com</p>
                </div>
            </div>
            
            <h2>HTML Usage</h2>
            <pre>&lt;img src="http://localhost:5000/avatar/user@example.com?size=128" alt="User Avatar"&gt;</pre>
            
            <h2>Python Client</h2>
            <pre>import requests

url = "http://localhost:5000/avatar/user@example.com"
response = requests.get(url, params={"size": 128})
svg_content = response.text</pre>
            
        </body>
        </html>
        """
        return html
    
    
    @app.route('/avatar/<identifier>')
    def avatar(identifier):
        """
        Generate an avatar for the given identifier.
        
        Query parameters:
            size: Icon size in pixels (default: 128)
            format: svg or png (default: svg)
            padding: Padding in range 0.0-0.5 (default: 0.08)
        """
        # Get parameters
        size = int(request.args.get('size', 128))
        format = request.args.get('format', 'svg').lower()
        padding = float(request.args.get('padding', 0.08))
        
        # Validate
        size = max(16, min(size, 512))  # Limit size
        padding = max(0.0, min(padding, 0.5))
        
        # Configure
        config = {'padding': padding}
        
        # Generate
        if format == 'png':
            try:
                data = jdenticon.to_png(identifier, size, config)
                return Response(data, mimetype='image/png')
            except ImportError:
                # Pillow not installed, fall back to SVG
                format = 'svg'
        
        if format == 'svg':
            data = jdenticon.to_svg(identifier, size, config)
            return Response(data, mimetype='image/svg+xml')
        
        return "Invalid format", 400
    
    
    if __name__ == '__main__':
        print("=" * 60)
        print("Jdenticon Python Avatar Service")
        print("=" * 60)
        print()
        print("Starting server on http://localhost:5000")
        print()
        print("Try these URLs:")
        print("  http://localhost:5000/")
        print("  http://localhost:5000/avatar/user@example.com")
        print("  http://localhost:5000/avatar/test?size=200")
        print()
        print("Press Ctrl+C to stop")
        print("=" * 60)
        
        app.run(debug=True, port=5000)

except ImportError as e:
    print("=" * 60)
    print("Web API Example")
    print("=" * 60)
    print()
    print("This example requires Flask to run.")
    print()
    print("Install Flask with:")
    print("    pip install Flask")
    print()
    print("Then run this script again:")
    print("    python3 web_api_example.py")
    print()
    print("=" * 60)
    sys.exit(1)
