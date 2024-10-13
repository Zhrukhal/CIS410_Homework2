# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 02:41:53 2024

@author: admin
"""

# main.py

import conversion_functions as cf
import menu_functions as mf

def main():
    """Main function that handles user input and performs temperature conversions."""
    mf.display_title()

    while True:
        mf.display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = cf.fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is {celsius} Celsius.")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = cf.celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
