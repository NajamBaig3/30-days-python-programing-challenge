def is_palindrome(word):
    # Convert the word to lowercase to make the comparison case-insensitive
    word = word.lower()
    
    # Remove spaces from the word
    word = word.replace(" ", "")
    
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Example usage:
user_word = input("Enter a word: ")
if is_palindrome(user_word):
    print(f"{user_word} is a palindrome.")
else:
    print(f"{user_word} is not a palindrome.")
