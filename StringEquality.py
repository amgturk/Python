def SearchCharacter(string,character):
    return string.find(character) 

def SanitizeString(string,character):
    # How many special character('#') available in the string
    characterCounter=string.count(character)
    
    # Until each special character removed, clean the string
    while(characterCounter != 0):
        characterPosition=string.find(character)
        if(characterPosition>0):
            string=string[:characterPosition-1]+string[characterPosition+1:]
        elif (characterPosition == 0):
            string=string[characterPosition+1:]
            
        characterCounter-=1
    
    # Return sanitized string
    return string
    
def CheckEquality(str1,str2):
    
    # If character is available in the string  
    result1=SearchCharacter(str1,"#")
    result2=SearchCharacter(str2,"#")
    
    #--------------------------------------------  
    
    sanitizedStr1=sanitizedStr2=""
    
    # If character is in the string then sanitize he string from characters and its effects----     
    if(result1==-1):
        sanitizedStr1=str1
    else:
        sanitizedStr1= SanitizeString(str1,'#')
   
    if(result2==-1):
        sanitizedStr2=str2
    else:
        sanitizedStr2= SanitizeString(str2,'#')        
    #------------------------------------------
    
    return sanitizedStr1 == sanitizedStr2    
