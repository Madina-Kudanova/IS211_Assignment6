class ConversionNotPossible(Exception):
    pass

CONVERSIONS = {
    "Celsius": {"Kelvin": lambda x: x + 273.15, "Fahrenheit": lambda x: (x * 9/5) + 32},
    "Kelvin": {"Celsius": lambda x: x - 273.15, "Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32},
    "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9, "Kelvin": lambda x: (x - 32) * 5/9 + 273.15},
    "Miles": {"Yards": lambda x: x * 1760, "Meters": lambda x: x * 1609.34},
    "Yards": {"Miles": lambda x: x / 1760, "Meters": lambda x: x * 0.9144},
    "Meters": {"Miles": lambda x: x / 1609.34, "Yards": lambda x: x / 0.9144},
}

def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value
    if fromUnit in CONVERSIONS and toUnit in CONVERSIONS[fromUnit]:
        return CONVERSIONS[fromUnit][toUnit](value)
    raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}")
