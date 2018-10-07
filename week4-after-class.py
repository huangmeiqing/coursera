# 1、编写一个Animal类，属性有name，方法有call()；现有Dog类和Cat类继承Animal类，请根据实际情况重写call() （比如，狗叫可以打印汪汪，猫叫可以打印喵喵）

class Animal():
    def __init__(self, name):
        self.name = name
        print("Animal name: %s" % (self.name))

    def call():
        print("")


class Dog(Animal):
    def call():
        print("汪汪")


class Cat(Animal):
    def call():
        print("喵喵")


if __name__ == '__main__':
    dog = Dog('dog')
    Dog.call()
    cat = Cat('cat')
    Cat.call()

#2、使用递归实现10以内的斐波那契数列
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


for n in range(11):
    print(recur_fibo(n))






#3、使用列表推导获取100以内的奇数
def odd(n):
    l=list(x for x in range(n) if x % 2 !=0)
    return l


print(odd(100))




#4、使用异常处理结构实现add(x, y) / sub(x, y) / mul(x, y) / div(x, y)

def add(x,y):
    try:
        print(int(int(x)+int(y)))
    except ValueError:
        print("value Error")
    else:
        print("no Error")
    finally:
        print('执行finally语句')


print(add(1,2))
print(add('a',1))



def sub(x,y):
    try:
        print(int(int(x)-int(y)))
    except ValueError:
        print("value Error")
    else:
        print("no Error")
    finally:
        print('执行finally语句')


print(sub(1,2))
print(sub('a',1))

def mul(x,y):
    try:
        print(int(int(x)*int(y)))
    except ValueError:
        print("value Error")
    else:
        print("no Error")
    finally:
        print('执行finally语句')


print(mul(1,2))
print(mul('a',1))

def div(x,y):
    try:
        result=x/y
    except ZeroDivisionError as e:
        print(e)
    else:
        print(result)
    finally:
        print('执行finally语句')



print(div(2,1))
print(div(2,0))




#5、将Python之禅（import this）写入文件，并统计有多少单词及其出现的次数，将统计结果序列化至文件中保存
#首先在桌面新建一个note.txt

import this
f=open('note.txt','w')
f.writelines(this.s)
f.close()


word=this.s
list1=word.split()
set1=set(list1)
list2=list(set1)
dir1={}
dir2={}
for x in range(len(list2)):
    dir1[list2[x]]=0
    for y in range(len(list1)):
        if list2[x]==list1[y]:
            dir1[list2[x]]+=1



print(dir1) #单词的个数

dir2={'length':len(dir1)}
print(dir2)

import json
json_data=json.dumps(dir1)
json_data2=json.dumps(dir2)
json_data
json_data2


with open('note.txt','a') as f:
    f.write(json_data)

with open('note.txt','a') as f:
    f.write(json_data2)


#最后进入cmd命令  桌面路径>note.txt   查看写入内容








