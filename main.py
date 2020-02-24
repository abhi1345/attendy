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
    for filename in listdir("./uploads"):
        # filename = "uploads/full.jpg" # 'class_pic_{}.jpg'.format(ctime())
        # camera.capture(filename)
        people_found = give_match(filename)
        update_count(people_found, count_map)
        sleep(10)
    print(count_map)
    # Delete all the pictures we took this session
    print("Deleting uploads")
    delete_files("./uploads")

if __name__ == "__main__":
    main()