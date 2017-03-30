def validate_pin(pin):
    # ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
    # If the function is passed a valid PIN string, return true, else return false.

    if pin.isdigit() is True:
        if len(pin) == 4:
            return True
        if len(pin) == 6:
            return True

    return False

print(validate_pin("1234"))
print(validate_pin("123456"))
print(validate_pin("a1234"))