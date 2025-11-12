"""
Setup script for Jdenticon Python
"""
from setuptools import setup, find_packages
import os

# Read the README file
readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = 'Python library for generating highly recognizable identicons'

setup(
    name='jdenticon',
    version='0.1.0',
    description='Python library for generating highly recognizable identicons',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Daniel Mester Pirttijärvi (Original JS), Python port by GitHub Copilot',
    author_email='',
    url='https://github.com/dmester/jdenticon',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'png': ['Pillow>=8.0.0'],
    },
    entry_points={
        'console_scripts': [
            'jdenticon=jdenticon.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    keywords='identicon avatar icon generator jdenticon',
)
