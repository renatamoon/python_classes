import threading
import time
import asyncio

# def new():
#     while True():
#         time.sleep(1)
#         print("THIS IS A NEW FUNCTION")


# def second():
#     while True:
#         time.sleep(0.8)
#         print("HELLO THIS IS THE SECOND")

# threading.Thread(target=new).start()
# threading.Thread(target=second).start()


# -------------

# counter = 0

# async def function1():
#     global counter

#     while True:
#         counter += 1
#         counter -= 1
#         await asyncio.sleep(0)


# async def function2():
#     global counter
    
#     while True:
#         counter += 1
#         counter -= 1
#         await asyncio.sleep(0)


# threading.Thread(target=function1).start()
# threading.Thread(target=function2).start()

# asyncio.gather(function1(), function2())
# asyncio.get_event_loop().run_forever()

# ----------- using asyncio

"""Getting the documentation to study"""

# async def main():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("world")

# # asyncio.run(main())

# main()

# ------------- examples

# async def hello(i):
#     print(f"hello {i} STARTED")
#     await asyncio.sleep(4)
#     print(f"hello {i} DONE")


# async def main():
#     task1 = asyncio.create_task(hello(1))
#     await asyncio.sleep(3)
#     task2 = asyncio.create_task(hello(2))
#     await task1
#     await task2

# asyncio.run(main()) # here's the main loop

# ----------------

async def count():
    print("Um")
    await asyncio.sleep(1)
    print("Dois")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed: 0.2f} seconds.")