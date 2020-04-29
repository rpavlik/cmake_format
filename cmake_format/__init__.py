"""
Parse cmake listfiles and format them nicely
"""
from __future__ import unicode_literals

VERSION = '0.6.0'

from .configuration import Configuration
from .__main__ import process_file
