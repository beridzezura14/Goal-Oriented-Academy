# Twice as old

# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)

# Сalculate how many years ago the father was twice as old as his son 
# (or in how many years he will be twice as old). The answer is always greater 
# or equal to 0, no matter if it was in the past or it is in the future.


def twice_as_old(dad_years_old, son_years_old):
    x = dad_years_old - son_years_old * 2
    if x < 0:
        return x * -1
    return  dad_years_old - son_years_old * 2

    # return abs(dad_years_old - son_years_old * 2)


print(twice_as_old(36,7))