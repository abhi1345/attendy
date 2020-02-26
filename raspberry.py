import picamera
from time import sleep, ctime
import subprocess

# Run this function on startup everytime

bluetooth_address = REDACTED

def main():
    # If running for first time, learn the faces of students
    num_pics = 5
    # Take pictures at spaced intervals
    camera = picamera.PiCamera()
    camera.resolution = (3264, 2448)
    for i in range(num_pics):
        filename = "uploads/{}.jpg".format(ctime())
        camera.capture("./{}".format(filename))
        subprocess.run(["bluetooth-sendto", "--device={}".format(bluetooth_address), filename])
        print("sent a file to macbook")

if __name__ == "__main__":
    main()
