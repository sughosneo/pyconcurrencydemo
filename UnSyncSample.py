'''
    In this sample we would actually talk about one Unsync library which would
        be helpful to control both Network I/O and CPU based computation with easy decorators.
'''
import asyncio
from .helpers.ThumbnailMgr import *
from .helpers.TimeStatsProfiler import *
from .constants.Constant import *
from unsync import unsync

class UnSyncSample:

    @timeStatsProfiler
    def process(self):

        tasks = [
            self.__computeSomething(),
            self.__createThumbnail()
        ]

        [t.result() for t in tasks]

    @unsync(cpu_bound=True) # Specifically letting library know that it's a CPU bound process, where computation would be expensive.
    def __computeSomething(self):

        print("Starting my heavy computation ...")

        # Pls consider this could be the actual CPU intensive operations along with __createThumbnail()
            # which is basically a network I/O intensive work.

        for eachIndex in range(0, 5000000000000):
            pass

        print("Computation is over !...")

    @unsync # It's the
    async def __createThumbnail(self):

        try:

            tasks = [
                self.__processOne(),
                self.__processTwo()
            ]

            [t.result() for t in tasks]

            # both processes finished
            print("Done!")

        except Exception as error:
            print(error)


    @unsync
    async def __processOne(self):

        print("Starting process 1 ...")

        await asyncio.sleep(0)

        videoFilePath1 = Constant.VIDEO_1_FILE_PATH
        thumbnailMgr1 = ThumbnailMgr()
        thumbnailMgr1.generateThumbnails(videoFilePath1,"frame_7")

    @unsync
    async def __processTwo(self):

        print("Starting process 2 ...")

        await asyncio.sleep(0)

        videoFilePath2 = Constant.VIDEO_2_FILE_PATH
        thumbnailMgr2 = ThumbnailMgr()
        thumbnailMgr2.generateThumbnails(videoFilePath2,"frame_8")