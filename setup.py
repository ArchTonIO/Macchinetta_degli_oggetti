"""
    Setup file for macchinetta degli oggetti.
"""
import json
from setuptools import setup, find_packages

with open("version.json", encoding="UTF-8") as f:
    version = json.load(f)

setup(
    name='macchinetta degli oggetti',
    version=version["version"],
    packages=find_packages()
)
