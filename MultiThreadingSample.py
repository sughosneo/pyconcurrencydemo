import threading
from .helpers.ThumbnailMgr import *
from .helpers.TimeStatsProfiler import *
from .constants.Constant import *

class MultiThreadingSample:

    @timeStatsProfiler
    def process(self):

        videoFilePath1 = Constant.VIDEO_1_FILE_PATH
        thumbnailMgr1 = ThumbnailMgr()
        t1 = threading.Thread(target=thumbnailMgr1.generateThumbnails, args=(videoFilePath1, "frame_5"))

        videoFilePath2 = Constant.VIDEO_2_FILE_PATH
        thumbnailMgr2 = ThumbnailMgr()
        t2 = threading.Thread(target=thumbnailMgr2.generateThumbnails, args=(videoFilePath2, "frame_6"))

        # starting process 1
        t1.start()
        # starting process 2
        t2.start()

        # wait until process 1 is finished
        t1.join()
        # wait until process 2 is finished
        t2.join()

        # both processes finished
        print("Done!")

