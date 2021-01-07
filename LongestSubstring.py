def SubStringCheck(inputString):
    inputLength=len(inputString)
    longestSubstring="" # default initialization
    subStringList=[]    # keep substrings in the list
    maxLengthofSubstring=0

    for i in range(inputLength):
        result=longestSubstring.find(inputString[i]) # find current character in the available substring
               
        # New character isn't available in substring, then add that character          
        if result == -1:
            longestSubstring+=inputString[i]

        # Character already in substring             
        else:  
            subLength=len(longestSubstring)
            
            # check if substring is longer or equal to the existing longest substring             
            if(subLength > maxLengthofSubstring):
                del subStringList[:] #new max length found discard previous substrings
                subStringList.append(longestSubstring) # Add substring to list
                maxLengthofSubstring=subLength            # new max length                
            elif(subLength == maxLengthofSubstring):   # Another substring with the same length of max length found
                if longestSubstring not in subStringList: # check if same length substring already in the list
                    subStringList.append(longestSubstring)# if not in the list, add it

            longestSubstring+=inputString[i] # add new character
            longestSubstring=longestSubstring[result+1:len(longestSubstring)+1] #remove part of string ending with repeating character
    

        # reached to the end of input string, check if current substring is ok to add to the list
        if(len(longestSubstring) > maxLengthofSubstring and i==inputLength-1):
            del subStringList[:]  
            subStringList.append(longestSubstring)
        if(len(longestSubstring) == maxLengthofSubstring and i==inputLength-1 and (longestSubstring not in subStringList)):
            subStringList.append(longestSubstring)
      
    if(not subStringList):
        return (len(subStringList),subStringList)
    else:
        return (max(len(substr) for substr in subStringList),subStringList)
 
