"""Setup script for AgenticCP Dict plugins"""

from setuptools import setup, find_packages

setup(
    name="agenticcp-dict-plugins",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "author_card = plugins.author_card:AuthorCardPlugin",
        ],
    },
)

