def check_if_palindrome(word):
    return word == word[::-1]
word = input("Please insert a word: ")
print(check_if_palindrome(word))