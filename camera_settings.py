#!/usr/bin/python3
import subprocess
import sys

result = subprocess.run(["/usr/bin/v4l2-ctl", "--list-devices"], stdout=subprocess.PIPE, encoding='utf-8')
list = result.stdout.splitlines()

print(sys.argv[1])

for index, line in enumerate(list):
    if "Webcam" in line:
        device=list[index+1].strip()
        print(device)
        result=subprocess.run(["/usr/bin/v4l2-ctl", "-c", "saturation=" + sys.argv[1], "--device", device])

