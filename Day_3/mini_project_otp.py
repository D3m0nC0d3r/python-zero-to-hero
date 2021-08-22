# Generate every time a 6 character OTP and print it.

import random
import string


# method for generating 6 digits otp, and return the otp.
def generate_otp():
    new_otp = ''
    chars_lists = list(string.ascii_letters + string.digits)
    for i in range(6):
        new_otp += random.choice(chars_lists)

    return new_otp

# storing the 6 digit otp from generate_otp method in the variable.
otp = generate_otp()

print(otp)