# Write a function which takes its speed in km per hour and returns it in cm per second, 
# rounded down to the integer (= floored).

# For example:

# 1.08 --> 30


def cockroach_speed(s):
    return s // 0.036          # 1.08 / 0.036 = 30

print(cockroach_speed(1.08))  # 30  

# formula cm/s = km/h ÷ 0.036