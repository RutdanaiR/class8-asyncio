# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queqe):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queqe.put(value)
        #print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queqe.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queqe.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queqe
    queqe = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queqe), consumer(queqe))

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:59:48 2023 Producer: Running
# Wed Aug 23 14:59:48 2023 Consumer: Running
# Wed Aug 23 14:59:49 2023 >got 0.6958648369607222
# Wed Aug 23 14:59:49 2023 >got 0.566203086383541
# Wed Aug 23 14:59:50 2023 >got 0.3803464408021009
# Wed Aug 23 14:59:50 2023 >got 0.37767993519203646
# Wed Aug 23 14:59:51 2023 >got 0.7966902116537696
# Wed Aug 23 14:59:52 2023 >got 0.527810232090489
# Wed Aug 23 14:59:52 2023 >got 0.0412795537000884
# Wed Aug 23 14:59:52 2023 >got 0.8529768128882157
# Wed Aug 23 14:59:53 2023 >got 0.8788952117701866
# Wed Aug 23 14:59:54 2023 Producer: Done
# Wed Aug 23 14:59:54 2023 >got 0.2294396014327934
# Wed Aug 23 14:59:54 2023 Consumer: Done
