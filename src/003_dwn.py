import cv2
import glob
import os
import json
import requests

path = "../../viewer/static/data/face/100241606.json"

with open(path) as f:
    df = json.load(f)

    members = df["selections"][0]["members"]

    for i in range(len(members)):
        opath = '../../viewer/static/data/karuta/raw/{}.jpg'.format(str(i + 1).zfill(3))

        if os.path.exists(opath):
            continue

        member = members[i]
        image  = member["thumbnail"]

        image = image.replace("/200,/", "/600,800/")

        f = open(opath,'wb')
        response = requests.get(image)
        f.write(response.content)
        f.close()