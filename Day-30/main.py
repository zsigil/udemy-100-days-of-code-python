# FileNotFound

try:
    file = open('a.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['cccccc'])

except FileNotFoundError:
    file = open('a.txt', 'w')
    file.write('Something')

except KeyError as error_message:
    print(f"the key {error_message} does not exist.")

else:
    # when all 'try' code succeeds
    content = file.read()
    print(content)

finally:
    # no matter what
    # eg raise own exception, because the code can be valid, even if input is nonsense
    raise TypeError('This is my error message')
