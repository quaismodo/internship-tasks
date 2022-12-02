import re


def is_palindrome(string):
    string = re.sub(r'[\W_]', '', str(string).lower())
    if bool(string):
        return string == string[::-1]
    return False


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
