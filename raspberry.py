import picamera
from time import sleep, ctime
import subprocess

# Run this function on startup everytime
def main():
    # If running for first time, learn the faces of students
    num_pics = 5
    # Take pictures at spaced intervals
    camera = picamera.PiCamera()
    camera.resolution = (3264, 2448)
    for i in range(num_pics):
        filename = "uploads/{}.jpg".format(ctime())
        camera.capture("./{}".format(filename))
        subprocess.run(["bluetooth-sendto", "--device=60:F8:1D:C2:CA:31", filename])
        print("sent a file to macbook")

if __name__ == "__main__":
    main()