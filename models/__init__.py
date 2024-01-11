#!/usr/bin/python3
"""models init that reloading the storage with every execution"""
from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
