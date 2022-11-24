"""Minumum diffrence in goals of football team"""
import Calculator

TEAM_COL = 1
F_COL = 6
A_COL = 8
calculator_obj = Calculator.Calculator("football.dat", TEAM_COL, F_COL, A_COL)
calculator_obj.calculate()
