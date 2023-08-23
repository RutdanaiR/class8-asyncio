from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queqe,id):
    print(f'{time.ctime()} Producer {id}: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(id*0.1)
        # add to the queqe
        await queqe.put(value)
    print(f'{time.ctime()} Producer {id}: Done')


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
    product = [producer(queue,_) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*product)
    # wait for the consumer to process all item
    await queue.join()
# start the asyncio program
asyncio.run(main())

# Wed Aug 23 15:28:34 2023 Consumer: Running
# Wed Aug 23 15:28:34 2023 Producer 0: Running
# Wed Aug 23 15:28:34 2023 Producer 1: Running
# Wed Aug 23 15:28:34 2023 Producer 2: Running
# Wed Aug 23 15:28:34 2023 Producer 3: Running
# Wed Aug 23 15:28:34 2023 Producer 4: Running
# Wed Aug 23 15:28:34 2023 >got 0.25748088011885295
# Wed Aug 23 15:28:34 2023 >got 0.426196563374858
# Wed Aug 23 15:28:35 2023 >got 0.7447442879218729
# Wed Aug 23 15:28:35 2023 >got 0.5315058582971597
# Wed Aug 23 15:28:36 2023 >got 0.1925566222224333
# Wed Aug 23 15:28:36 2023 >got 0.5918054415390822
# Wed Aug 23 15:28:37 2023 >got 0.10348846497334452
# Wed Aug 23 15:28:37 2023 >got 0.8636576361398225
# Wed Aug 23 15:28:38 2023 >got 0.5742506349495176
# Wed Aug 23 15:28:38 2023 >got 0.49326054899824456
# Wed Aug 23 15:28:39 2023 >got 0.8405762202936518
# Wed Aug 23 15:28:40 2023 >got 0.221797601777461
# Wed Aug 23 15:28:40 2023 >got 0.4212060480308195
# Wed Aug 23 15:28:40 2023 >got 0.5295112739727214
# Wed Aug 23 15:28:41 2023 >got 0.47472791658603963
# Wed Aug 23 15:28:41 2023 >got 0.703452519254769
# Wed Aug 23 15:28:42 2023 >got 0.7666839809557323
# Wed Aug 23 15:28:43 2023 >got 0.46920839321125885
# Wed Aug 23 15:28:43 2023 >got 0.03716692944520916
# Wed Aug 23 15:28:43 2023 >got 0.4592549359003586
# Wed Aug 23 15:28:44 2023 >got 0.28584424979813805
# Wed Aug 23 15:28:44 2023 >got 0.31119036967112124
# Wed Aug 23 15:28:45 2023 >got 0.029447214311666192
# Wed Aug 23 15:28:45 2023 >got 0.8819493016767846
# Wed Aug 23 15:28:45 2023 >got 0.8142772760014059
# Wed Aug 23 15:28:46 2023 >got 0.01618203425643583
# Wed Aug 23 15:28:46 2023 >got 0.997010043674465
# Wed Aug 23 15:28:47 2023 >got 0.33986703879735414
# Wed Aug 23 15:28:47 2023 Producer 0: Done
# Wed Aug 23 15:28:48 2023 >got 0.30568277948872846
# Wed Aug 23 15:28:48 2023 >got 0.02883931448136634
# Wed Aug 23 15:28:48 2023 >got 0.5799569340049054
# Wed Aug 23 15:28:49 2023 >got 0.7165594754216872
# Wed Aug 23 15:28:49 2023 >got 0.16420907900394277
# Wed Aug 23 15:28:49 2023 >got 0.7524656436041901
# Wed Aug 23 15:28:50 2023 >got 0.6286804568271979
# Wed Aug 23 15:28:51 2023 >got 0.056631414860769946
# Wed Aug 23 15:28:51 2023 >got 0.24680075854073213
# Wed Aug 23 15:28:51 2023 >got 0.8732803195872529
# Wed Aug 23 15:28:52 2023 >got 0.8999692869681009
# Wed Aug 23 15:28:53 2023 >got 0.5097132501913465
# Wed Aug 23 15:28:54 2023 >got 0.3271405178793082
# Wed Aug 23 15:28:54 2023 >got 0.5660434567256297
# Wed Aug 23 15:28:54 2023 >got 0.04141583529735626
# Wed Aug 23 15:28:54 2023 >got 0.5782439715432277
# Wed Aug 23 15:28:54 2023 Producer 1: Done
# Wed Aug 23 15:28:55 2023 >got 0.5918924238444465
# Wed Aug 23 15:28:55 2023 Producer 3: Done
# Wed Aug 23 15:28:56 2023 >got 0.9133841248261351
# Wed Aug 23 15:28:57 2023 >got 0.8850725553756715
# Wed Aug 23 15:28:57 2023 Producer 2: Done
# Wed Aug 23 15:28:57 2023 >got 0.324340012769442
# Wed Aug 23 15:28:57 2023 Producer 4: Done
# Wed Aug 23 15:28:58 2023 >got 0.38918775307518205
# Wed Aug 23 15:28:58 2023 >got 0.8266142436030798
