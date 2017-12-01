def inverse_captcha(input_number):

    sum = 0

    previous_digit = str(input_number)[-1:]

    for digit in str(input_number):
        if digit == previous_digit:
            sum += int(digit)

        previous_digit = digit

    return sum


def halfway_captcha(input_number):

    sum = 0

    sequence = str(input_number)
    halfway = int(len(sequence)/2)
    adjusted_sequence = sequence[halfway:] + sequence[:halfway]

    for i in range(0, len(sequence)):
        if sequence[i] == adjusted_sequence[i]:
            sum += int(sequence[i])

    return sum