import re


def count_words(string):
    string = re.findall(r'[a-zA-Z]+[’\']?[a-zA-Z]+|[a-zA-Z]', string.lower())
    string_count = dict(map(lambda x: (x, string.count(x)), string))
    return string_count


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Madam, I'm Adam! i''m"))
print(count_words("""We’ll not be walking We won’t be walking
You’ll not be walking You won’t be walking
You’ll not be walking You won’t be walking won’’t"""))
