# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:57:16 2020

@author: OLLIVANDER
"""
# Infix to Postfix Expression

preference = {'+':1 , '-':1, '*':2, '/':2, '^':3}
operators= set(['+', '-','*','/','^','(',')'])

expression = input("Enter infix expression: ")
fin =''
st=[]
flag=0
for i in expression:
    #print(i)
    if i not in operators:
        fin+=i
       # print("operand" , fin)
    elif i=='(':
        st.append('(')
       # print('hi',st)
        #print(st)
    elif i ==')':
        while st[-1]!='(':
            fin+=st.pop()
        st.pop()
        print(" ) " , fin)
    elif flag==0:
        st.append(i)
        flag=9
    else:
        while( len(st)!=0 and st[-1]!='(' and preference[st[-1]]>=preference[i]):
            fin+=st.pop()
        st.append(i)
    print('i = ', i)
    print("stack = ", st)
    print("fin = " , fin)
while len(st)!=0:
    fin+=st.pop()
print(len(st))
print(fin)