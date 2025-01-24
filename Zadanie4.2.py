def check_if_palindrome(word):
    return word == word[::-1]
word = input("Please insert a word: ")
print(f"Is your word a palindrome? {check_if_palindrome(word)}")