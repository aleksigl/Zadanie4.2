def check_if_palindrome(word):
    """
    Checks whether inserted word is a palindrome
    Aruments:
    word - a string inserted by user, to be chcecked whether a palindrome
    Return:
    A boolean value describing if a word is a palindrome
    """
    return word == word[::-1]
word = input("Please insert a word: ")
print(f"Is your word a palindrome? {check_if_palindrome(word)}")