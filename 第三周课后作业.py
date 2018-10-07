Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def xx2(number,lst):
    b=-1
    c=0
    d=[]
    for a in lst:
        if a==number:
            print("列表里有元素%d" %(number))
            c=1
            break
    if c==0:
            print("列表里不存在元素%d,将返回None" %(number))
            return None
    else:
        try:
            while True:
                b=lst.index(number,b+1) #该方法返回查找对象的索引位置，如果没有找到对象则抛出异常
                d.append(b)
        except:
            print("进入except")
        finally:
            for a in d:
                if (len(lst)-1)/2>a:
                     print("左边有一个")
                elif (len(lst)-1)/2<a:
                     print("右边有一个")
                else:
                     print("正好在中间有一个")

>>> lst=[1,2,3]
>>> xx2(1,lst)
列表里有元素1
进入except
左边有一个
>>> def prime(x):
    for num in range(1,x + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)

                
>>> prime(100)
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
>>> def minnumber(lst1):
    lst2=min(lst1)
    return lst2

>>> lst1=[1,2,4,6]
>>> minnumber(lst1)
1
>>> 
