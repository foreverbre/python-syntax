def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    """To convert temperatures in degrees Fahrenheit to Celsius, 
    subtract 32 and multiply by .5556 (or 5/9)

    To convert temperatures in degrees Celsius to Fahrenheit, 
    multiply by 1.8 (or 9/5) and add 32
    
    1. if statement if c or f isn't equal then return "invalid unit in"
    2. if statement if c or f isn't equal then return "invalid unit out"
    3. if statement if f == in and out == c insert coversion f to c
    4. if statement if c == in and out == f insert coversion c to f
"""
    if unit_in != "f" and unit_in != "c": 
        return f"Invalid unit {unit_in}"
    if unit_out != "f" and unit_out != "c": 
        return f"Invalid unit {unit_out}"
    if unit_in == "f" and unit_out == "c": 
        temp = (temp - 32) / 9*5
    if unit_in == "c" and unit_out == "f": 
        temp = (temp * 5/9) + 32
    
    return temp

print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

