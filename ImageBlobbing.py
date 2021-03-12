#change code so we can do the actual threading

import time
import picamera
max_frames = 60

def filenames():
    frame = 0
    while frame < max_frames:
        yield 'image%02d.jpg' % frame
        frame += 1
        
        
with picamera.PiCamera(resolution='720p', framerate=30) as camera:
    camera.start_preview()
    time.sleep(2)
    start = time.time()
    print('start', start)
    camera.capture_sequence(filenames(), use_video_port=True)
    finish = time.time()
    print('finish', finish)
print('Captured %d frames at %.2ffps' %(
    max_frames,
    max_frames / (finish-start)))


