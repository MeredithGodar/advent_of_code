def inverse_captcha(input_number):

    sum = 0

    previous_digit = str(input_number)[-1:]

    for digit in str(input_number):
        if digit == previous_digit:
            sum += int(digit)

        previous_digit = digit

    return sum