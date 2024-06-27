#Complex Soln

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=[]
        if(numRows==1 or numRows>=len(s)):
            return s
        l=list(s)
        for i in range(0,len(l),(numRows*2)-3+1):
            res.append(l[i])
            l[i]=""
        numRows-=1
        s=''.join(l)
        l=list(s)
        while(numRows>=2):
            res.append(l[0])
            l[0]=""
            for i in range(numRows*2-2,len(l),numRows*2-1):
                    res.append(l[i])
                    if(i+1<len(l)):
                        res.append(l[i+1])
                        l[i+1]=""
                    l[i]=""
            numRows-=1
            s=''.join(l)
            l=list(s)
        print(l)
        for i in l:
            res.append(i)
        return "".join(res)
        


    
        
'''
 >Initial Setup:
Create an empty list res to store characters of the ZigZag pattern.
If numRows is greater than or equal to the length of the input string s, return s itself, as there won't be any ZigZag pattern to create.

>Construction of ZigZag Pattern:
Break the string s into a list of characters l.
Iterate over the list l in steps of (numRows*2)-3+1, considering the distance between two characters in the same row of the ZigZag pattern.

>First Phase of ZigZag Construction:
Append characters at regular intervals to the res list and remove them from the original list l.
Decrement numRows by 1.

>Second Phase of ZigZag Construction:
Continue constructing the ZigZag pattern until numRows reduces to 2.
In each iteration, append characters from specific indices in l to res and remove them from l.

>Concatenation and Return:
Concatenate the remaining characters in l to res.
Join the characters in res to form the final ZigZag pattern and return it.

>The time complexity of the solution is O(n)
>The space complexity is also O(n) because additional space is used to store characters in res and l.'''