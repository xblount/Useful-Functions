def compare_strings(s1,s2):
    #returns highest index to where 2 strings 
    #match. Starts from beginning of string.
    #Ex: 
    #str1 ='Hello World' and str2 ="Hello"
    #highest index = 4
    #case-sensitive
    
    i = 0
    char1 = ''
    char2 = ''
    for j in range(0,min(len(s1),len(s2))):
        if i>len(s1)-1:
            pass
        else:
            char1 += s1[i]
        if i>len(s2)-1:
            pass
        else:
            char2 += s2[i]
        if char1 == char2:
            i += 1
        elif i == 0:
            return -1    
    return i-1
