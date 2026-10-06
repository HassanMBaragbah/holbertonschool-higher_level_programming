#!/usr/bin/env python3
"""Module for basic JSON serialization and
deserialization of dictionary data."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Name of the destination file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Deserializes data from a JSON file back into a Python dictionary.

    Args:
        filename (str): Name of the JSON file to read.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
