import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)
from conversions_refactored import convert, ConversionNotPossible

class TestTemperatureConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        test_cases = [(0, 273.15), (100, 373.15), (-273.15, 0), (300, 573.15), (-50, 223.15)]
        for celsius, expected in test_cases:
            self.assertAlmostEqual(convertCelsiusToKelvin(celsius), expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [(0, 32), (100, 212), (-40, -40), (300, 572), (-50, -58)]
        for celsius, expected in test_cases:
            self.assertAlmostEqual(convertCelsiusToFahrenheit(celsius), expected, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [(32, 0), (212, 100), (-40, -40), (572, 300), (-58, -50)]
        for fahrenheit, expected in test_cases:
            self.assertAlmostEqual(convertFahrenheitToCelsius(fahrenheit), expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases = [(32, 273.15), (212, 373.15), (-40, 233.15), (572, 573.15), (-58, 223.15)]
        for fahrenheit, expected in test_cases:
            self.assertAlmostEqual(convertFahrenheitToKelvin(fahrenheit), expected, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases = [(273.15, 0), (373.15, 100), (0, -273.15), (573.15, 300), (223.15, -50)]
        for kelvin, expected in test_cases:
            self.assertAlmostEqual(convertKelvinToCelsius(kelvin), expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases = [(273.15, 32), (373.15, 212), (0, -459.67), (573.15, 572), (223.15, -58)]
        for kelvin, expected in test_cases:
            self.assertAlmostEqual(convertKelvinToFahrenheit(kelvin), expected, places=2)

class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertAlmostEqual(convert("Celsius", "Kelvin", 0), 273.15)
        self.assertAlmostEqual(convert("Kelvin", "Celsius", 273.15), 0)
        self.assertAlmostEqual(convert("Celsius", "Fahrenheit", 100), 212)
        self.assertAlmostEqual(convert("Fahrenheit", "Kelvin", 32), 273.15)

    def test_distance_conversions(self):
        self.assertAlmostEqual(convert("Miles", "Yards", 1), 1760)
        self.assertAlmostEqual(convert("Yards", "Meters", 1), 0.9144)
        self.assertAlmostEqual(convert("Meters", "Miles", 1609.34), 1)

    def test_identity_conversion(self):
        self.assertAlmostEqual(convert("Miles", "Miles", 5), 5)
        self.assertAlmostEqual(convert("Celsius", "Celsius", -10), -10)

    def test_invalid_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Meters", 100)

if __name__ == '__main__':
    unittest.main()
