from attendy import *
from os import listdir, mkdir
from collections import Counter
import picamera
import random
from time import sleep, ctime

# Run this function on startup everytime
def main():
    # If running for first time, learn the faces of students
    num_pics = 30
    if "faces.txt" not in listdir():
        learn_faces()
    # Get roster
    known_faces_names = []
    with open("names.txt", "wb") as fp:
		pickle.dump(known_faces_names, fp)
    # Setup attendance tracking for current class
    count_map = Counter()
    # Take pictures at spaced intervals
    camera = picamera.PiCamera()
    camera.resolution = (3264, 2448)
    for i in range(num_pics):
        filename = "./uploads/class_pic_{}.jpg".format(ctime())
        camera.capture(filename)
        print(filename)
        people_found = give_match(filename)
        update_count(people_found, count_map)
        print(count_map)
    print(count_map)
    # Email results
    presentlist, absentlist = count_to_lists(count_map, known_faces_names, num_pics)
    send_email(presentlist, absentlist)
    # Delete all the pictures we took this session
    print("Deleting uploads")
    delete_files("./uploads")

if __name__ == "__main__":
    main()