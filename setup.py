from setuptools import setup, find_packages

setup(
    name="assignment",               # Package name (shown in pip list)
    version="0.1",                 # Version (follow semver: major.minor.patch)
    description="A simple intriduction package",  # Short description
    author="Immidi Jayasurya",            # Author info
    author_email="immidijayasurya@gmail.com",
    packages=find_packages(),      # Automatically finds all folders with __init__.py
    install_requires=[],           # List of dependencies (empty here)
)
