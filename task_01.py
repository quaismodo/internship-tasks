import re


def is_palindrome(string):
    string = re.sub(r'[\W_]', '', str(string).lower())
    return string == string[::-1] if bool(string) else False


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
print(is_palindrome("   "))
