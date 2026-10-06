#!/usr/bin/env python3
"""Module for serializing and deserializing dictionaries using XML format."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary containing
        key-value pairs to serialize.
        filename (str): The name of the file to save the XML data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        pass


def deserialize_from_xml(filename):
    """Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict or None: A dictionary populated with elements from the XML file,
        or None if an exception occurs during reading.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text if child.text else ""

        return result_dict
    except Exception:
        return None
