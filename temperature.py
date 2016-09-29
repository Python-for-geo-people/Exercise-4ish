# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:14:13 2016

@author: root
"""

def celsius_to_kelvin(temp_c):
    return temp_c + 273.15 
    
def fahr_to_celsius(temp_f):
    return 5/9 * temp_f - 32
    
def fahr_to_kelvin(temp_f):
    return 5/9 * (temp_f + 459.67)
    
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15
    
def celsius_to_fahr(temp_c):
    return 9/5 * temp_c + 32
    
def kelvin_to_fahrenheit(temp_k):
    temp_c = kelvin_to_celsius(temp_k)
    temp_f = celsius_to_fahr(temp_c)
    return temp_f
    
def temp_calculator(temp, convert_from, convert_to):
    if convert_from == "K":
        if convert_to == "C":
            converted_temp = kelvin_to_celsius(temp_k = temp)
    elif convert_to == "F":
        converted_temp = kelvin_to_fahrenheit(temp_k = temp)
    else: 
        converted_temp = None 
        return converted_temp
        
    if convert_from == "C":
        if convert_to == "F":
            converted_temp = celsius_to_fahr(temp_c = temp)
        if convert_to == "K":
            converted_temp = celsius_to_kelvin(temp_c = temp)
        else:
            converted_temp = None 
            return converted_temp 
    
    if convert_from == "F":
        if convert_to == "C":
            converted_temp = fahr_to_celsius(temp_f = temp)
        elif convert_to == "K":
            converted_temp = fahr_to_kelvin(temp_f = temp)
        else: 
            converted_temp = None
            return converted_temp
            print("input temperature type", convert_from, "was not detected. Possible valuer are 'C' for Celsius, 'K' for Kelvin and 'F' for Farenheit")
            
        
    
    
#Quite nice but I get completely wrong values. But the function works. TADAA!     
#False. Only getting Nones. 
    
    
"""
    Function for converting temperatures between Celsius, Kelvin and Fahrenheit.

    Parameters:
    -----------
    temp: Temperature in Kelvin <numerical>
    convert_to: Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Possible values: 'C' | 'F'
    convert_from: Source temperature that can be Kelvin ('K') or Celsius ('C'). Possible values: 'K' or 'C'.
    """

    