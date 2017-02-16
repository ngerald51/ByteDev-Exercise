def is_palindrome(string):
    reverse = ""
    reverse = string[::-1]
    if reverse == string:
        return True
    else:
        return False


print(is_palindrome("ALAN"))