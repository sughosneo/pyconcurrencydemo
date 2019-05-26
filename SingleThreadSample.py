from .helpers.ThumbnailMgr import *
from .helpers.TimeStatsProfiler import *
from .constants.Constant import *

class SingleThreadSample:

    @timeStatsProfiler
    def process(self):

        videoFilePath1 = Constant.VIDEO_1_FILE_PATH
        thumbnailMgr1 = ThumbnailMgr()
        print(thumbnailMgr1.generateThumbnails(fileName=videoFilePath1, dirName="frame_1"))

        videoFilePath2 = Constant.VIDEO_2_FILE_PATH
        thumbnailMgr2 = ThumbnailMgr()
        print(thumbnailMgr2.generateThumbnails(fileName=videoFilePath2, dirName="frame_2"))

        print("Done!")