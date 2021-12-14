#Check if string is a palindrome

def ispalindrome(input):
    max = len(input) - 1
    for i in range(len(input) // 2):
        if(input[i] != input[max-i]):
            return False
    return True

assert ispalindrome("frog") == False, "Frog case incorrect"
assert ispalindrome("noon") == True, "noon case incorrect"
assert ispalindrome("racecar") == True, "Racecar case incorrect"
assert ispalindrome("rockstar") == False, "rockstar case incorrect"

print("Test cases completed!")