from attendy import *
from os import listdir, mkdir
from collections import Counter
# import picamera
import random
from time import sleep, ctime

# Run this function on startup everytime
def main():
    # If running for first time, learn the faces of students
    if "faces.txt" not in listdir():
        learn_faces()
    # Setup attendance tracking for current class
    count_map = Counter()
    # Take pictures at spaced intervals
    # camera = picamera.PiCamera()
    for i in range(100):
        filename = 'class_pic_{}.jpg'.format(ctime())
        # camera.capture(filename)
        people_found = give_match(filename)
        update_count(people_found, count_map)
        sleep(60)
    # Delete all the pictures we took this session
    delete_files("./uploads")
