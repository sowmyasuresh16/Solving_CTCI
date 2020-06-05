#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# CTCI - Chapter 1 (Arrays and Strings)


# In[59]:


'''1.1) Given a string, Determine if the string has all unique characters.'''

'''With using additional data structures'''
def isUnique(string):
    
    if(len(set(string)) == len(string)):
        print("String has no duplicates")
        return False
    print("String has duplicates")
    return True

'''Without using additional data structures'''

def isUnique2(str2):
    
    str2 = sorted(str2)
    
    for i in range(len(str2)-1):
        if str2[i] == str2[i+1]:
            print("String has duplicates")
            return True
    print("String has no duplicates")
    return False
    


# In[61]:


# string = "abcddefg"
# isUnique(string)

str2 = "abcdefgg"
isUnique2(str2)


# In[92]:


'''1.2) Given two strings, check if one is a permutation of another (Anagram)'''

'''BruteForce - Time Complexity: O(n logn)'''

def anagram(str1,str2):
    
    if len(str1) != len(str2):
        print("Not an anagram")
        return False
    
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    if(str1 == str2):
        print("Two strings are an anagram")
        return True
    else:
        print("Not an anagram")
        return False
    
'''Using hashmap - Time complexity: O(n)'''

import collections

def anagram2(str1,str2):
    
    d = collections.defaultdict(int)
    
    for i in str1:
        d[i] += 1
        
    for i in str2:
        if i in d:
            d[i] -= 1
        
    return not any(d.values())
            
    
    


# In[94]:


str1 = "rat"
str2 = "tai"
# anagram(str1,str2)
anagram2(str1,str2)


# In[97]:


'''1.3) URLify a string - Replace all white spaces with %20'''

def urlify(string):
    
    string = string.strip()
    string = string.replace(" ","%20")
    return string

string = "Mr John  Smith"
urlify(string)


# In[98]:


'''1.4) Palindrome permutation - Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.'''

def palindromPermutation(string):
    
    string = string.replace(" ", "").lower()
    d = {}
    
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
    oddCount = 0
    
    for v in d.values():
        if v%2 !=0:
            oddCount += 1
    
    if oddCount !=1:
        print("Not a palindrome permutation")
        return False
    else:
        print("It is a palindrome permutation")
        return True


# In[103]:


string = "radar"
palindromPermutation(string)


# In[124]:


'''1.5) One Away - There are three types of edits that can be performed on strings: insert a char, remove a char and
replace a char. Given two strings, write a function to check if they are one edit away.'''

def oneReplaceAway(str1,str2):
    
    i,j,count = 0,0,0
       
    while i < len(str1) and j < len(str2):
        if(str1[i] != str2[j]):
            count += 1
            if count > 1:
                return False
        i += 1
        j += 1

    return True
    
def oneRemoveAway(str1, str2):
    
    i,j,count = 0,0,0
    
    while i < len(str1) and j < len(str2):
        if(str1[i] != str2[j]):
            i += 1
            count += 1
            if count > 1:
                return False
            
        else:
            i += 1
            j += 1
            
    return True
    
def oneEditAway(str1,str2):
    
    if(abs(len(str1) - len(str2)) > 1):
        return False
    
    if(len(str1) == len(str2)):
        return oneReplaceAway(str1,str2)
    
    elif(len(str1) > len(str2)):
        return oneRemoveAway(str1,str2)
        
    else:
        return oneRemoveAway(str2,str1)   


# In[130]:


str1 = "pale"
str2 = "ple"

oneEditAway(str1,str2)


# In[149]:


'''1.6) String Compression - Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.'''

def stringCompression(string):
    count = 1
    compressedString = ''
    
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count += 1        
        else:
            compressedString += string[i] + str(count)
            count = 1
    compressedString += string[i+1] + str(count)
    
    if len(string) < len(compressedString):
        return string
    else:
        return compressedString
    


# In[153]:


string = "aaabbcccaab"
stringCompression(string)


# In[154]:


'''1.7) Rotate Matrix - You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).'''

def rotateMatrix(m):
    
    m = m[::-1]
    
    for i in range(len(m)):
        for j in range(i):
            
            m[i][j], m[j][i] = m[j][i], m[i][j]
            
    return m
        


# In[155]:


m = [[1,2,3],
     [4,5,6],
    [7,8,9]]

rotateMatrix(m)


# In[173]:


'''Zero Matrix - Given a m x n matrix, if an element is 0, set its entire row and column to 0.'''

def nullify_row(m,i):
    for j in range(len(m[0])):
        m[i][j] = 0
        
def nullify_col(m,j):
    for i in range(len(m)):
        m[i][j] = 0
        
def zero_matrix(m):
    
    row_zero = False
    col_zero = False
    
    for i in range(len(m)):
        if m[i][0] == 0:
            col_zero = True
    
    for j in range(len(m[0])):
        if m[0][j] == 0:
            row_zero = True
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0
                
    for i in range(1, len(m)):
        if m[i][0] == 0:
            nullify_row(m, i)
    
    for j in range(1, len(m[0])):
        if m[0][j] == 0:
            nullify_col(m, j)
            
    if row_zero:
        nullify_row(m, 0)
    
    if col_zero:
        nullify_col(m, 0)
    
    return m
            
        


# In[174]:


m = [[1,2,3],
     [4,0,6],
     [7,8,9]]

zero_matrix(m)


# In[165]:


'''1.9) String Rotation - Given 2 strings s1,s2 check if s2 is a rotation of s1 '''

def stringRotation(s1,s2):
    
    if len(s1) != len(s2):
        print("s2 is not a rotation of s1")
        return False
    
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    
    s1 = s1 + s1
    
    if(s2 in s1):
        print("s2 is a rotation of s1")
        return True
    else:
        print("s2 is not a rotation of s1")
        return False


# In[168]:


s1 = "abcde"
s2= "deabc"

stringRotation(s1,s2)

