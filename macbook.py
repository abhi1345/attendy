from attendy import *
from os import listdir, mkdir
from collections import Counter
import random
from time import sleep, ctime

def clean_name(name):
    return ''.join([i for i in name.replace("_", " ") if not i.isdigit()])


# Run this function on startup everytime
def main():
    num_pics = 1
    # If running for first time, learn the faces of students
    if "faces.txt" not in listdir():
        learn_faces()
    # Get roster
    with open("names.txt", "rb") as fp:
        known_faces_names = pickle.load(fp)
    known_faces_names = list(set([clean_name(x) for x in known_faces_names]))
    # Setup attendance tracking for current class
    count_map = Counter()
    checked_files = set()
    # Listen for new pictures every 30 sec
    print("Listening for new files")
    for i in range(num_pics):
        sleep(5)
        for filename in listdir("./uploads"):
            if filename[0] != "." and filename not in checked_files:
                print(filename)
                checked_files.add(filename)
                people_found = give_match("./uploads/" + filename)
                update_count(people_found, count_map)
        print(count_map)
    print(count_map)
    # Email results
    presentlist, absentlist = count_to_lists(count_map, known_faces_names, len(checked_files))
    send_email(presentlist, absentlist)
    # Delete all the pictures we took this session
    print("Deleting uploads")
    # delete_files("./uploads")

if __name__ == "__main__":
    main()