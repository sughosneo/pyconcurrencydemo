import asyncio
from .helpers.ThumbnailMgr import *
from .helpers.TimeStatsProfiler import *
from .constants.Constant import *

class AsyncIOSample:

    '''
        - This async keyword tells python it's async coroutine.
        - When we declare wrapper method as async then corresponding other methods also needs to be async
    '''
    @timeStatsProfiler
    def process(self):
        asyncio.run(self.__createThumbnail())

    async def __createThumbnail(self):

        firstTask = asyncio.create_task(self.__processOne())

        # If someone is using python any other version than 3.7 then following line would be used instead of above one.
        # firstTask = asyncio.ensure_future(self.__processOne())

        secondTask = asyncio.create_task(self.__processTwo())

        await firstTask
        await secondTask

        # both processes finished
        print("Done!")

    async def __processOne(self):

        print("Starting process 1 ...")

        videoFilePath1 = Constant.VIDEO_1_FILE_PATH
        thumbnailMgr1 = ThumbnailMgr()
        thumbnailMgr1.generateThumbnails(videoFilePath1,"frame_7")

    async def __processTwo(self):

        print("Starting process 2 ...")

        videoFilePath2 = Constant.VIDEO_2_FILE_PATH
        thumbnailMgr2 = ThumbnailMgr()
        thumbnailMgr2.generateThumbnails(videoFilePath2,"frame_8")