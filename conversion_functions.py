# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 02:37:21 2024

@author: admin
"""

# conversion_functions.py

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius)

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit)