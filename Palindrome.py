def Palindrome(string):
    # sanitize string by lowering and removing non alphanumerical characters
    string=string.lower()
    string="".join([ch for ch in string if ch.isalpha()])
    #------------------------
    stringLength=len(string)

    for i in range(int(stringLength/2)):
        if string[i]!=string[stringLength-1-i]:
            return False
    return True
