# Assumes string, no floats in input
def sum_earnings(s):
    """Determines streak sum of earnings from string of comma separated values"""
    earnings = 0
    x = s.split(',')                            # Splits input into list based on comma separation
    try:
        x = [int(val) for val in x]             # Casts all values as ints, exception if not int
        for i in x:
            if i < 0 and abs(i) > earnings:     # Checks if next value is negative and greater than sum, if so reset sum
                earnings = 0
            else:                               # Else, add earnings/purchases
                earnings += i
    except ValueError:                          # Returns 0 if input is invalid
        return 0
    return earnings
