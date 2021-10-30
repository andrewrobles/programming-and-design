def isPalindrome(phrase):
    phrase=phrase.lower()
    length=len(phrase)
    if(length<=1):
        return True
    else:
        #we are checking for the first and the last letter. SO we need to send the middle to the MID_PHRASE
        MID_PHRASE=phrase[1:length-1]#we slice it from 2nd letter to last but 1. each time.
        if((phrase[0]==phrase[length-1]) and isPalindrome(MID_PHRASE)==True):
            return True
        else:
            return False



print(isPalindrome('Kayak'))