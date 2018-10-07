Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def prt_user():
    name=input('name: ')
    age=int(input('age: '))
    year=2018+100-age
    r=f'{name}在{year}年为100岁'
    print(r)
    return year

>>> prt_user()
name: cc
age: 16
cc在2102年为100岁
2102
>>> def get():
    num = int(input("请输入一个整数!"))
    if num % 2==1:
        print("你输入的是奇数")
    else:
        print("你输入的是偶数")

        
>>> get()
请输入一个整数!5
你输入的是奇数
>>> def listnull(lst1):
    all(lst1)==True
    if  all(lst1):
        print('列表里没有空对象')
    else:
        print('列表里有空对象')

        
>>> lst1=['','a','b']
>>> listnull(lst1)
列表里有空对象
>>> def list(lst):
    for a in lst:
            print(a)
            if not bool(a):
                    print("have 空对象")
                    return True
            else:
                    pass
    return False

>>> lst=[1,2,3,'']
>>> list(lst)
1
2
3

have 空对象
True
>>> def x(lst):
    a=lambda x: bool(x)
    for x in lst:
        b=a(x)
        if not b:
            print("有空对象")
            return True
        else:
            pass
    print("没有空对象")
    return False

>>> lst=['a','c','']
>>> x(lst)
有空对象
True
>>> def double(lst1):
    lst2=[x*x for x in lst1]
    return lst2

>>> lst1=[1,2,3,4]
>>> double(lst1)
[1, 4, 9, 16]
>>> def double2(lst1):
    lst2=map(lambda x:x*x,lst1)
    return list(lst2)

>>> lst1=[1,3,4,5]
>>> double2(lst1)
1
9
16
25
False
>>> from functools import reduce
>>> def add(x,y):
    return x + y

>>> 
>>> lst1=[1,2,3,4]
>>> print(reduce(add,lst1))
10
>>> def cube(lst1):
  return  [x*x*x for x in lst1]

>>> lst1=[1,2,3,4]
>>> cube(lst1)
[1, 8, 27, 64]
>>> def Is(lst1,lst2):
    lst3=list(set(lst1).intersection(set(lst2)))
    return lst3

>>> lst1=['a','b','v']
>>> lst2=['a','b','c']
>>> Is(lst1,lst2)
a
b
False
>>> def M(a,b,c):
    return max(a,b,c)

>>> M(9,4,6)
9
>>> def M2(a,b,c):
    if a>b:
        max=a
    else:
        max=b
    if c>max:
        max=c
    return max

>>> M2(9,8,7)

9
>>> 
