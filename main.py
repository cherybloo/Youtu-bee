import googleapiclient.discovery
import json,random,webbrowser as wb

fName="baca.json"
userFile="userInput.json"
prevInput=""
userInput=""

youtube = googleapiclient.discovery.build(
    "youtube","v3",developerKey="YOUR_DEVELOPER_KEY" #change this to your developer key from YOUTUBE API v3
)

with open(userFile,"r") as uf: #clear all before user input in userInput.json
    userData=json.load(uf,)
del userData['user']

with open(userFile,"w") as wu: #updating userInput.json to and assign userInput variable
    userData["user"]=""
    userInput=userData["user"]
    json.dump(userData,wu)

while True: #looping every time a new user input is detected
    with open(userFile,"r") as uf:
        userData=json.load(uf,)
        userInput=userData['user']
    if (prevInput != userInput):
        request=youtube.search().list(
        part="snippet",
        maxResults=1,
        q=userInput
        )

        response = request.execute()

        with open(fName,"w") as f:
            f.write(json.dumps(response))
            f.close()
        print("success")

        with open(fName) as fuckMe:
            data=json.load(fuckMe)
            fuckMe.close()

        videoId=data['items'][0]['id']['videoId']
        print("Video-ID:",videoId)
        urlLink=f"https://www.youtube.com/watch?v={videoId}"
        prevInput = userInput
        wb.open(urlLink)
        print("success all")