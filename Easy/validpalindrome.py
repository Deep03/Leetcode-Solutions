def isPalindrome(s: str) -> bool:

    reverse_str = s[::-1]
    print("Reverse string is: %s" % reverse_str)
    print("Original string is: %s" % s)
    return s.lower() == reverse_str.lower()


print(isPalindrome("A man, a plan, a canal: Panama"))