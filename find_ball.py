from SimpleCV import *
import create2api
import time

class FindBall():
    def __init__(self, show_gui=False):
        self.cam = Kinect()
        if show_gui:
            self.display = SimpleCV.Display()
        self.previous = None
        self.time = time.time()

    def find(self):
        print "dt:", time.time() - self.time
        self.time = time.time()
        depth = self.cam.getDepth()
        if self.previous:
            self.filtered = depth - self.previous
            self.filtered = self.filtered.binarize(20).invert()
            blobs = self.filtered.findBlobs()
            if blobs:
                for blob in blobs:
                    d = depth.getPixel(blob.x, blob.y)[0]
                    if d < 254:
                        print blob.x, blob.y, d
        else:
            self.filtered = depth
        self.previous = depth

if __name__ == '__main__':
    bot = create2api.Create2()
    bot.start()
    bot.safe()
    bot.kinect_power()

    find_ball = FindBall(False)

    while True:
        find_ball.find()
        #find_ball.filtered.show()
