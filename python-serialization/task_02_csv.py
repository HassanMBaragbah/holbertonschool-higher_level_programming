#!/usr/bin/env python3
"""Module for converting CSV dataset files to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON format and writes the output to data.json.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
