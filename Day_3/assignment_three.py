# Assignment:
# Implement a decorator mod_div() which assures that the numerator is always greater than the denominator. e.g. if a = 2, b = 4, then div(a, b) should return 2.0 as the output and not 0.5

def mod_div(user_func):
    # checking if numerator is greater than the denominator, and if required it will swap the values.
    def inner_func(a, b):
        if a < b:
            a, b = b, a
        
        user_func(a, b)    
    
    return inner_func

# adding decorator to the division function.
@mod_div
def div(a,b):
    print(a/b)


div(9,81)