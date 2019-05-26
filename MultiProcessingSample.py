import multiprocessing
from .helpers.ThumbnailMgr import *
from .helpers.TimeStatsProfiler import *
from .constants.Constant import *

class MultiProcessingSample:

    @timeStatsProfiler
    def process(self):

        videoFilePath1 = Constant.VIDEO_1_FILE_PATH
        thumbnailMgr1 = ThumbnailMgr()
        p1 = multiprocessing.Process(target=thumbnailMgr1.generateThumbnails, args=(videoFilePath1, "frame_3"))

        videoFilePath2 = Constant.VIDEO_2_FILE_PATH
        thumbnailMgr2 = ThumbnailMgr()
        p2 = multiprocessing.Process(target=thumbnailMgr2.generateThumbnails, args=(videoFilePath2, "frame_4"))

        # starting process 1
        p1.start()
        # starting process 2
        p2.start()

        # wait until process 1 is finished
        p1.join()
        # wait until process 2 is finished
        p2.join()

        # both processes finished
        print("Done!")
