
import io

import numpy as np
import picamera


camera = picamera.PiCamera()

camera.resolution = (640,480)
camera.framerate = 30

camera.start_preview()

try:
    stream = io.BytesIO()
    for _ in camera.capture_continuous(stream
                                        ,format='rgb'
                                        ,use_video_port=True
                                        ,resize=(640,480)):
        stream.truncate()
        stream.seek(0)
        image = np.frombuffer(stream.getvalue(),dtype=np.uint8)
        print(image.shape)

finally:
    camera.stop_preview()

