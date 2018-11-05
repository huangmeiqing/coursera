#1
from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import asyncio
def NUMBER():
    lst=[]
    for i in range(10,23):
        lst.append(i)
    yield lst

def fib(n):
    if n<=2:
        return 1
    return fib(n-2)+fib(n-1)
if __name__=='__main__':
    start=NUMBER().__next__()
    with ProcessPoolExecutor(max_workers=3) as executor:
        for num,result in zip(start,executor.map(fib,start)):
            print(f"fib({num})={result}")



#2
import asyncio
async def g1():
    for i in range(10):
        yield i


async def g2():
    async for v in g1():
        print(v)
    return [v * 2 async for v in g1()]


loop = asyncio.get_event_loop()
try:
    result = loop.run_until_complete(g2())
    print(f'Result is {result}')
finally:
    loop.close()
