#!/usr/bin/env python
# coding: utf-8

# ## Q. Python If-Else
# 
# Given an integer,perform the following conditional actions:
# 
# If n is odd, print Weird, If n is even and in the inclusive range of  to , print Not Weird, If n is even and in the inclusive range of  to , print Weird, If n is even and greater than , print Not Weird
# https://www.hackerrank.com/challenges/py-if-else/problem

# In[9]:


if __name__ == '__main__':
    n = int(input().strip())

if n%2 == 1:
    print('Weird')
elif (n%2==0) and (2<=n<=5):
    print('Not Weird')
elif (n%2==0) and (6<=n<=20):
    print('Weird')
else:
    print('Not Weird')


# ## Q. Find the Runner-Up Score!
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# In[11]:


#Solution 1
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
lst=list()
lst2 = list()
for i in arr:
    lst.append(i)
    tmp = sorted(lst,reverse=True)
    for s in tmp:
        if s not in lst2: 
            lst2.append(s)
            lst2.sort(reverse=True)                 
print(lst2[1])


# In[12]:


#Solution 2
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
newset = set(i for i in arr)
lst = (sorted([x for x in newset],reverse=True))[1]
print(lst)


# ### Q. Nested Lists:
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# https://www.hackerrank.com/challenges/nested-list/problem

# In[ ]:


#Solution 1
marksheet = []
lst = []
di = dict()
for _ in range(int(input())):
    name = input()
    score = float(input())
    tmp = (name,score)
    marksheet.append(tmp)
    marksheet.sort()
for name,score in marksheet: 
    di.setdefault(name, []).append(score) 

lowscore = None
for n,s in sorted(di.items()):
    if (lowscore is None or s < lowscore) and s != min(di.values()):
        lowscore = s
listOfKeys = [key  for (key, value) in di.items() if value == lowscore]
for people in listOfKeys:
    print(people)


# In[ ]:


#Solution 2
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([score for name,score in marksheet])))[1]

finallist = [key for key,value in sorted(marksheet) if value == second_highest]
for name in finallist:
    print(name)


# ### Q.Find a string
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# https://www.hackerrank.com/challenges/find-a-string/problem

# In[13]:


def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        if string[i:len(sub_string)+i] == sub_string:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# Q. You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
# https://www.hackerrank.com/challenges/text-wrap/problem

# In[5]:


def wrap(string, max_width):
    word = "\n".join(string[x:x+max_width] for x in range(len(string)) if x%max_width==0)
    return word

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# ### Q. Finding the percentage
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.https://www.hackerrank.com/challenges/finding-the-percentage/problem

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


for name,score in student_marks.items():
    if name == query_name:
        avg = round(sum(score),2)/len(score)
avg = '{:.2f}'.format(avg)
print(avg)


# ### Q. sWAP cASE
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. https://www.hackerrank.com/challenges/swap-case/problem

# In[14]:


def swap_case(s):
    result = ""
    for l in s:
        if l == l.lower():
            result = result + l.upper()
        else:
            result = result + l.lower()   
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# ### Q. What's Your Name?
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following: "Hello firstname lastname! You just delved into python."
# https://www.hackerrank.com/challenges/whats-your-name/problem 

# In[15]:


def print_full_name(a, b):
    lst = []
    lst.append(a)
    lst.append(b)
    final = " ".join(lst)
    print("Hello "+ final + "!" + " You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# ### Q. Mutations
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed). Let's try to understand this with an example. You are given an immutable string, and you want to make changes to it.https://www.hackerrank.com/challenges/python-mutations/problem

# In[ ]:


def mutate_string(string, position, character):
    final = string[:position] + character + string[position+1:]
    return final

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# ### Q. Capitalize
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# https://www.hackerrank.com/challenges/capitalize/problem

# In[ ]:


def solve(s):
    for x in s[:].split():
        s= s.replace(x,x.capitalize())
    return s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


# ### Q. itertools.product()
# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
# You are given a two lists A and B. Your task is to compute their cartesian product AXB.
# https://www.hackerrank.com/challenges/itertools-product/problem

# In[ ]:


from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*product(a,b))


# Q. collections.Counter()
# Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop. There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size. Your task is to compute how much money Raghu earned.
# https://www.hackerrank.com/challenges/collections-counter/problem

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
#import collections
##not my solution
numShoes = int(input())
shoes = Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)


# ### Q. itertools.permutations()
# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
# https://www.hackerrank.com/challenges/itertools-permutations/problem

# In[ ]:


from itertools import permutations
word, num = input().split()
perm=list(permutations(sorted(word),int(num)))
for p in perm:
    x=''.join(p)
    print(x)


# ### Q. Introduction to Sets
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
# Formula used: sum of distinct height/total number of distinct height
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

# In[ ]:


def average(array):
    distitems = len(list(set(arr)))
    distarray = list(set(arr))
    tot = 0
    for i in distarray:
        tot = i + tot
    avg = tot/distitems
    return avg


# ### Q. DefaultDict Tutorial
# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# In[ ]:


from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(list)
for i in range(0,n):
    d[input()].append(i+1)

lst = []
for x in range(0,m):
    lst = lst + [input()]

for l in lst:
    if l in d:
        print(*d[l])
    else: 
        print(-1)


# ### Q. Calendar Module
# You are given a date. Your task is to find what the day is on that date.
# https://www.hackerrank.com/challenges/calendar-module/problem

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date = input().split()
y = int(date[2])
m = int(date[0])
d = int(date[1])

day = calendar.weekday(y,m,d)

if day==0:
    print('MONDAY')
elif day==1:
    print('TUESDAY')
elif day==2:
    print('WEDNESDAY')
elif day==3:
    print('THURSDAY')
elif day==4:
    print('FRIDAY')
elif day==5:
    print('SATURDAY')
else:
    print('SUNDAY')


# ### Q. Exceptions
# https://www.hackerrank.com/challenges/exceptions/problem

# In[ ]:


num = input()
for i in range(int(num)):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)


# ### Q. Collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# In[ ]:


from collections import namedtuple
n = int(input())
fields = input().split()
s=0
for i in range(n):
    students = namedtuple('student', fields)
    field1,field2,field3,field4 = input().split()
    student = students(field1,field2,field3,field4)
    s = s + int(student.MARKS)
avg = s/n
print('{:.2f}'.format(avg))


# ### Q. Collections.OrderedDict()
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

# In[ ]:


from collections import OrderedDict
ordered_dictionary = OrderedDict()
num = int(input())
for i in range(num):
    items,space,price = input().rpartition(' ')
    ordered_dictionary[items] = ordered_dictionary.get(items,0) + int(price)
for k,v in ordered_dictionary.items():
    print(k,v)


# ### Q. itertools.combinations()
# https://www.hackerrank.com/challenges/itertools-combinations/problem

# In[16]:


import itertools
from itertools import combinations

word, num = input().split()
lst = []
for i in range(1,int(num)+1):
    lst.append(list(combinations(sorted(word),int(i))))
lst2=list(itertools.chain(*lst))
for x in lst2:
    print(''.join(x))


# ### Q. Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

# In[ ]:


m = int(input())
numbersm = set(map(int, input().split()))

n = int(input())
numbersn = set(map(int, input().split()))

dif1 = numbersm.difference(numbersn) 
dif2 = numbersn.difference(numbersm)
symdif = list(dif1.union(dif2))
for i in sorted(symdif):
    print(i)


# ### Q. Set.add()
# Output the total number of distinct country stamps on a single line.
# https://www.hackerrank.com/challenges/py-set-add/problem

# In[ ]:


s = set()
for i in range(int(input())):
    s.add(input())
print(len(s))


# ### Q. itertools.combinations_with_replacement()
# Print the combinations with their replacements of string S on separate lines.
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

# In[ ]:


from itertools import combinations_with_replacement
word, num = input().split()
comb = list(combinations_with_replacement(sorted(word),int(num)))
for c in comb:
    print(''.join(c))


# ### Q. Set.discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

# In[ ]:


#Solution 1
n = int(input())
s = set(map(int, input().split()))
n1= int(input())
for i in range(n1):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))


# In[ ]:


#Solution 2
n = int(input())
s = set(map(int, input().split()))
m = int(input())
for  i in range(m):
    attr, *kw = input().split()
    if kw:
        getattr(s,attr)(int(*kw))
    else:
        getattr(s,attr)()
print(sum(s))


# ### Q. Collections.deque()
# https://www.hackerrank.com/challenges/py-collections-deque/problem

# In[ ]:


from collections import deque
n = int(input())
d = deque()

for i in range(n):
    attr, *kw = input().split() #*kw means that kw will take the any values that can't be assigned to attr, this also means that kw can be empty
    if kw:
        getattr(d,attr)(int(*kw))
    else:
        getattr(d,attr)()
print(*d)


# ### Q. Set.union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem

# In[ ]:


numofeng = int(input())
engrolls = set(map(int,input().split()))
numoffr = int(input())
frrolls = set(map(int,input().split()))

common = engrolls.union(frrolls)
print(len(common))


# ### Q. Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# In[ ]:


numofeng = int(input())
engrolls = set(map(int,input().split()))
numoffr = int(input())
frrolls = set(map(int,input().split()))
print(len(engrolls.intersection(frrolls)))


# ### Q. Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

# In[ ]:


numofeng = int(input())
engrolls = set(map(int,input().split()))
numoffr = int(input())
frrolls = set(map(int,input().split()))

uncommon = engrolls.symmetric_difference(frrolls)
print(len(uncommon))


# ### Q. The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

# In[17]:


import collections
groups = int(input())
rooms = collections.Counter(list(map(int,input().split())))

for k,v in rooms.items():
    if v == 1:
        print(k)


# ### Q. Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# In[ ]:


lstbool = []
setA = set(map(int,input().split()))
for i in range(int(input())):
    seti = set(map(int,input().split()))
    if (len(seti) < len(setA)) and (setA.union(seti) == setA):
        lstbool.append(True)
    else:
        lstbool.append(False)
print(all(lstbool))


# In[ ]:




