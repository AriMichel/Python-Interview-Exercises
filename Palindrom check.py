def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[:: -1]


print(is_palindrome("racecar"))
print(is_palindrome("World"))
print(is_palindrome("Die Liebe ist Sieger stets rege ist sie bei Leid"))
print(is_palindrome("Ein Esel lese nie"))
print(is_palindrome("Rebecca Walpuski"))