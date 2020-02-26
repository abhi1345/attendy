# attendy
Facial Recognition Based Classroom Attendance with Email Notification

This code is intended for a Raspberry Pi/Laptop combination system to identify students present in a class and notify instructors of absences by using facial recognition.

Hardware Specifications:

* Microcomputer:  Raspberry Pi Zero W
* Case: Raspberry Pi Official Camera Case (modified to fit larger lens)
* Camera Module:  Raspberry Pi Camera Module v2 8MP Board
* Camera Sensor Upgrade:  MX219 8MP Sensor (Arducam)
* Camera Lens Upgrade:  175 Degree Fisheye Lens (Arducam)
* Connected Computer: Macbook Pro
## How it works

1. The raspberry pi runs the raspberry.py script, which makes it take and send pictures to the macbook via bluetooth.
2. The macbook simultaneously runs macbook.py, which makes it check for new files every minute and run facial recognition to generate and email the attendance report.

## File Descriptions
* *attendy.py:* Main code for facial recognition, email-sending, and other helper functions. This code is used by other files which are run on the Raspberry Pi and Macbook.
* *raspberry.py:* The script run on the Raspberry Pi. Takes pictures and sends them to the macbook using bluetooth connection (to circumvent Wi-Fi issues in Donner).
* *macbook.py:* The script run on the Macbook. Uses macbook's increased computing power to run facial recognition and email attendance report to the instructors.
