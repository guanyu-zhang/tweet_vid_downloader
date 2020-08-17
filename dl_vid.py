import os, sys
import requests
import argparse

def dl(url, id, pkg_name):
    res = requests.get(url,stream=True)
    vid_name = pkg_name + "/" + str(id) + ".mp4"
    with open(vid_name, 'wb') as file:
        file.write(res.content)
    file.close()

parser = argparse.ArgumentParser(description="download .mp4 files")
parser.add_argument("--user", "-u", help="twitter user name", type=str)
args = parser.parse_args()
pkg_name = args.user + "_vid_data"
if os.path.exists(pkg_name):
    pass
else:
    os.mkdir(pkg_name)
file_name = args.user + "_vid_list.txt"
f = open(file_name, "r")
count = 1
for line in f:
    sys.stdout.write("downloading No." + str(count) + " link\n")
    sys.stdout.flush()
    dl(line, count, pkg_name)
    count += 1


