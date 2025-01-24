def check_if_palindrome(word):
    return word == word[::-1]
word = input()
print(check_if_palindrome(word))