import asyncio
import time

now = lambda: time.time()

async def hello(index):
    print("hello, i am ", index)
    await asyncio.sleep(2)
    print("return, ", index)
    return "done, " + str(index)

start = now()

# 协程对象
h1 = hello(1)
h2 = hello(2)
h3 = hello(3)

# 创建一个事件loop
loop = asyncio.get_event_loop()

# 任务（task）对象
tasks = [
    asyncio.ensure_future(h1),
    asyncio.ensure_future(h2),
    asyncio.ensure_future(h3),
]

# 将协程加入到事件循环loop
loop.run_until_complete(asyncio.wait(tasks))

loop.close()

for task in tasks:
    print(task.result())

print(now()-start)
"""
hello
hello
hello
done
done
done
2.005011796951294
"""

