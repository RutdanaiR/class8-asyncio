from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queue.put(value)
        #print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queue.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()

 # entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 15:03:28 2023 Consumer: Running
# Wed Aug 23 15:03:28 2023 Producer: Running
# Wed Aug 23 15:03:28 2023 >got 0.06432802537524762
# Wed Aug 23 15:03:28 2023 >got 0.4269205230725701
# Wed Aug 23 15:03:29 2023 >got 0.3498211691591909
# Wed Aug 23 15:03:29 2023 >got 0.03333453727227209
# Wed Aug 23 15:03:30 2023 >got 0.8579119899474277
# Wed Aug 23 15:03:31 2023 >got 0.39430994443162504
# Wed Aug 23 15:03:31 2023 >got 0.42806857404584797
# Wed Aug 23 15:03:31 2023 >got 0.2799333056419442
# Wed Aug 23 15:03:32 2023 >got 0.7102581887550593
# Wed Aug 23 15:03:32 2023 Producer: Done
# Wed Aug 23 15:03:32 2023 >got 0.2996469211037215
# Wed Aug 23 15:03:33 2023 >got None
