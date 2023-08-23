from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queqe):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queqe.put(value)
    # send an all done signal
    await queqe.put(None)
    print(f'{time.ctime()} Producer: Done')

# consume work
async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        try:
            # retrieve the get() awaitable
            get_await = queqe.get()
            # await the awaitable with a timeout
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print('Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queqe
    queqe = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queqe), consumer(queqe))

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 15:01:14 2023 Consumer: Running
# Wed Aug 23 15:01:15 2023 Consumer: gave up waiting...
# Wed Aug 23 15:01:15 2023 >got 0.5845648731846529
# Wed Aug 23 15:01:16 2023 Consumer: gave up waiting...
# Wed Aug 23 15:01:16 2023 >got 0.48872813586395836
# Wed Aug 23 15:01:16 2023 Consumer: gave up waiting...
# Wed Aug 23 15:01:16 2023 >got 0.7417113064444801
# Wed Aug 23 15:01:17 2023 Consumer: gave up waiting...
# Wed Aug 23 15:01:17 2023 >got 0.8953408107704389
# Wed Aug 23 15:01:17 2023 >got 0.1749200668203622
# Wed Aug 23 15:01:18 2023 >got 0.44831450301138187
# Wed Aug 23 15:01:18 2023 Consumer: gave up waiting...
# Wed Aug 23 15:01:18 2023 >got 0.5015416511339539
# Wed Aug 23 15:01:18 2023 >got 0.07052864799855374
# Wed Aug 23 15:01:19 2023 >got 0.20492132759813797
# Wed Aug 23 15:01:19 2023 Producer: Done
# Wed Aug 23 15:01:19 2023 Consumer: gave up waiting...
# Wed Aug 23 15:01:19 2023 >got 0.522110647222721
