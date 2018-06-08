# https://adventofcode.com/2017/day/4


# Part 1:

# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password.
# # A passphrase consists of a series of words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

#    aa bb cc dd ee is valid.
#    aa bb cc dd aa is not valid - the word aa appears more than once.
#    aa bb cc dd aaa is valid - aa and aaa count as different words.

# The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

# Part 2:

# For added security, yet another system policy has been put in place.
# # Now, a valid passphrase must contain no two words that are anagrams of each other - that is,
# a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

# For example:

#     abcde fghij is a valid passphrase.
#     abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
#     a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
#     iiii oiii ooii oooi oooo is valid.
#     oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

# Under this new system policy, how many passphrases are valid?


def count_valid_passphrases(input_file):

    total = 0

    with open(input_file) as txt:
        for line in txt:
            words = line.split()

            if len(set(words)) == len(words):
                total += 1

    return total


def count_valid_passphrases_no_anagrams(input_file):

    total = 0

    with open(input_file) as txt:
        for line in txt:
            words = line.split()

            sorted_words = [''.join(sorted(word)) for word in words]

            if len(set(sorted_words)) == len(sorted_words):
                total += 1

    return total


if __name__ == '__main__':
    print("The number of valid passphrases is %d" % count_valid_passphrases('input.txt'))
    print("The number of valid passphrases (excluding anagrams) is %d" % count_valid_passphrases_no_anagrams('input.txt'))
