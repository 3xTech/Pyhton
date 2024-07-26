
s = 'azcbobobegghakl'

def longest(s):
        '''
        Input: A string of lower case characters
        Output: The logest substring in alphabetical order
        '''
        longest = ""
        plongest = ""
        for l in s:
             print("l",longest)
             if longest == "":
                 longest = l
             else:
                 if l >= longest[len(longest)-1]:
                     
                     longest += l
                 else:
                     longest = l
             if len(plongest)< len(longest) :
                      plongest = longest
        return plongest
    
print("Longest substring in alphabetical order is:", longest(s))