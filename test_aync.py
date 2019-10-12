import asyncio


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
    return "Hello again!"




def run(coroutine_fn):
    try:
        coroutine_fn.send(None)
    except StopIteration as e:
        return e.value


async def async_function():
    # yield 1
    # return 1
    await hello()


async def await_coroutine():
    result = await async_function()
    print(result)


run(await_coroutine())