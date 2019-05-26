import os
import cv2

class ThumbnailMgr:

    def generateThumbnails(self,fileName,dirName):

      '''
        Extract frames from the video and creates thumbnails for one of each
      :return:
      '''

      try:

          self.__waitTime()

          print("Extracting frames from video ....")

          frames = self.__getVideoFrames(fileName)

          print("Generating and save thumbnails ...")

          for i in range(len(frames)):
              thumb = self.__convertImageToThumbs(frames[i])
              os.makedirs(dirName + '/%d' % i)
              for k, v in thumb.items():
                  cv2.imwrite(dirName + '/%d/%s.png' % (i, k), v)

      except Exception as error:
          print(error)
          return "failed"

      return "success"

    def __waitTime(self):

        x = 1000000000
        while x > 0:
            x -= 1

    def __getVideoFrames(self,video_filename):

        '''
            Extract frames from video
        :return:
        '''

        cap = cv2.VideoCapture(video_filename)
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        frames = []
        if cap.isOpened() and video_length > 0:
            frame_ids = [0]
            if video_length >= 4:
                frame_ids = [0,
                             round(video_length * 0.25),
                             round(video_length * 0.5),
                             round(video_length * 0.75),
                             video_length - 1]
            count = 0
            success, image = cap.read()
            while success:
                if count in frame_ids:
                    frames.append(image)
                success, image = cap.read()
                count += 1
        return frames

    def __convertImageToThumbs(self,img):
        '''
            Create thumbs from image
        :return:
        '''

        height, width, channels = img.shape
        thumbs = {"original": img}
        sizes = [640, 320, 160]
        for size in sizes:
            if (width >= size):
                r = (size + 0.0) / width
                max_size = (size, int(height * r))
                thumbs[str(size)] = cv2.resize(img, max_size, interpolation=cv2.INTER_AREA)

        return thumbs