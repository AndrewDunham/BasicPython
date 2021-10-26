#!/bin/bash env python3 
inp = input('Enter Celsius Temperature:')
print("You Entered ",inp,"cel")
cel = float(inp)
fahr = (cel * 9.0) / 5.0 + 32.0
print("Tempreture in fahr is ",fahr)
