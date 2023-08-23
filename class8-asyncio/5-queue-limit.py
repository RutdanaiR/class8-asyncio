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
    print(f'{time.ctime()} Producer: Done')


async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queqe.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark as completed
        queqe.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine


async def main():
    # create the shared queqe
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many product
    product = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*product)
    # wait for the consumer to process all item
    await queue.join()
# start the asyncio program
asyncio.run(main())

Wed Aug 23 15:08:50 2023 Consumer: Running
Wed Aug 23 15:08:50 2023 Producer: Running
Wed Aug 23 15:08:50 2023 Producer: Running
Wed Aug 23 15:08:50 2023 Producer: Running
Wed Aug 23 15:08:50 2023 Producer: Running
Wed Aug 23 15:08:50 2023 Producer: Running
Wed Aug 23 15:08:50 2023 >got 0.065765155068926
Wed Aug 23 15:08:51 2023 >got 0.3330589754662562
Wed Aug 23 15:08:51 2023 >got 0.2185835914394133
Wed Aug 23 15:08:51 2023 >got 0.5910554609677944
Wed Aug 23 15:08:52 2023 >got 0.7326111159325681
Wed Aug 23 15:08:53 2023 >got 0.6595577764058402
Wed Aug 23 15:08:53 2023 >got 0.9005637478595621
Wed Aug 23 15:08:54 2023 >got 0.40353147935598754
Wed Aug 23 15:08:55 2023 >got 0.27753378262655715
Wed Aug 23 15:08:55 2023 >got 0.5606747863121694
Wed Aug 23 15:08:55 2023 >got 0.9925477655410125
Wed Aug 23 15:08:56 2023 >got 0.6087815741709243
Wed Aug 23 15:08:57 2023 >got 0.6377957687755632
Wed Aug 23 15:08:58 2023 >got 0.820910289269063
Wed Aug 23 15:08:59 2023 >got 0.4767425509836266
Wed Aug 23 15:08:59 2023 >got 0.2161482133919863
Wed Aug 23 15:08:59 2023 >got 0.6074149624794524
Wed Aug 23 15:09:00 2023 >got 0.9372085482107917
Wed Aug 23 15:09:01 2023 >got 0.14224537262251769
Wed Aug 23 15:09:01 2023 >got 0.0749824185488226
Wed Aug 23 15:09:01 2023 >got 0.6533171812373836
Wed Aug 23 15:09:02 2023 >got 0.41460525222947264
Wed Aug 23 15:09:02 2023 >got 0.12806244654492427
Wed Aug 23 15:09:02 2023 >got 0.7585903236328259
Wed Aug 23 15:09:03 2023 >got 0.13603676767628514
Wed Aug 23 15:09:03 2023 >got 0.004977959745441796
Wed Aug 23 15:09:03 2023 >got 0.530813342092644
Wed Aug 23 15:09:04 2023 >got 0.30965620326444254
Wed Aug 23 15:09:04 2023 >got 0.973742190983368
Wed Aug 23 15:09:05 2023 >got 0.5424367650337759
Wed Aug 23 15:09:06 2023 >got 0.6379930150646592
Wed Aug 23 15:09:06 2023 >got 0.4933723719782036
Wed Aug 23 15:09:07 2023 >got 0.054938529068172315
Wed Aug 23 15:09:07 2023 >got 0.8981660843773498
Wed Aug 23 15:09:08 2023 >got 0.5065558726971312
Wed Aug 23 15:09:08 2023 >got 0.5881598615531523
Wed Aug 23 15:09:09 2023 >got 0.5929072983845898
Wed Aug 23 15:09:09 2023 >got 0.6599274803286366
Wed Aug 23 15:09:10 2023 >got 0.6136726673280648
Wed Aug 23 15:09:11 2023 >got 0.3896346017836293
Wed Aug 23 15:09:11 2023 >got 0.9333476790083498
Wed Aug 23 15:09:12 2023 >got 0.2341470555066637
Wed Aug 23 15:09:12 2023 Producer: Done
Wed Aug 23 15:09:12 2023 >got 0.49038463653247877
Wed Aug 23 15:09:12 2023 Producer: Done
Wed Aug 23 15:09:13 2023 >got 0.0745930273817822
Wed Aug 23 15:09:13 2023 >got 0.47522612392614305
Wed Aug 23 15:09:13 2023 Producer: Done
Wed Aug 23 15:09:13 2023 >got 0.43504479786402406
Wed Aug 23 15:09:14 2023 >got 0.6534551704372087
Wed Aug 23 15:09:14 2023 Producer: Done
Wed Aug 23 15:09:15 2023 >got 0.7762306238418041
Wed Aug 23 15:09:15 2023 Producer: Done
Wed Aug 23 15:09:15 2023 >got 0.08053187832315079
Wed Aug 23 15:09:15 2023 >got 0.656097263718612
