forbidden = ('.', '?', '!', ':', ';', '-', '--',
             '(', ')', '[', ']', "'", '"', '/', ',')


def changeMode(text):
    text = text.lower().replace(' ', '')
    for each in text:
        if each in forbidden:
            text = text.replace(each, '')
    return text


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter Text: ")
something = changeMode(something)
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")