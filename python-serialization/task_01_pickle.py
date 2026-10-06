#!/usr/bin/env python3
"""Module for serializing and deserializing
custom Python objects with pickle."""
import pickle


class CustomObject:
    """A custom class representing a person with serialization capabilities."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes a new CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the CustomObject
        in the specified format."""
        print(f"Name: {self.name}\nAge: {self.age}"
              f"\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance to a file using pickle.

        Args:
            filename (str): The destination file path.

        Returns:
            None: Returns None if an exception occurs during serialization.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes and returns a CustomObject instance from a file.

        Args:
            filename (str): The source file path.

        Returns:
            CustomObject or None: The deserialized object instance, or None if
            the file is missing, malformed, or an exception occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
