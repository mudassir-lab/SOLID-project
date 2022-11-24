"""Minimum spread temprature and day"""
import Calculator


DAY_COL = 0
MAX_TEMP_COL = 1
MIN_TEMP_COL = 2
calculator_obj = Calculator.Calculator(
    "weather.dat", DAY_COL, MAX_TEMP_COL, MIN_TEMP_COL)
calculator_obj.calculate()
