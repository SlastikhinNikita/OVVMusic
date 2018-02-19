# -*- coding: utf-8 -*-

import os

from random import shuffle
from pydub import AudioSegment

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
SimpleProgress, Timer


MUSICDIR = "./music/"
FILENAMES = ''
IGNORLIST = './ignorlist.txt'


def deleteIgnorListTracks():
    with open(IGNORLIST) as f:
        IGNOR = f.read().splitlines()
    FILENAMES = os.listdir(MUSICDIR)
    random.shuffle(FILENAMES)
    FILENAMES = list(set(FILENAMES) - set(IGNOR)) 
    for e in FILENAMES[:]:
        for i in IGNOR:
            if e.find(i) > -1:
                fullname = MUSICDIR + e
                if os.path.isfile(fullname):
                    os.remove(fullname)        

def getListOfSongs():
    namemp3 = 0
    deleteIgnorListTracks()
    FILENAMES = os.listdir(MUSICDIR)
    random.shuffle(FILENAMES)
    
    megasong = AudioSegment.empty()
    
    nametxt = MUSICDIR + "music" + str(namemp3) + ".txt"
    txtfile = open(nametxt, "w")
    txtfile.write('If you like some track - support author, buy his track on iTunes.\nAll videos are introductory and not provided as commercials.\nIf you liked the format, you can help the project, for its development.\nIf you author and you didn\'t want see you track here, please contact me.\n\nPayPal: ovvXmusic@gmail.com\nBitCoin: 15QoCC14iTJ21P2TnqPXwtsYuRPkC6N5fh\n\nTrackList:\n')
    
    pbar = ProgressBar()
    i = 0
    #while i < 9:
    for element in pbar(FILENAMES):
        fullname = MUSICDIR + element
        song = AudioSegment.from_file(fullname)
        os.remove(fullname)
        fulltime = len(megasong) / 1000
        if len(megasong) == 0:
            megasong = song
        else:
            megasong = megasong.append(song, crossfade=5000)
        name = MUSICDIR + "music" + str(namemp3) + ".mp3"

        lenM = fulltime // 60
        lenS = fulltime % 60
        if lenS < 10:
            lenS = '0' + str('{:.0f}'.format(lenS))
        else:
            lenS = '{:.0f}'.format(lenS) 
        filename = FILENAMES[i]
        txtfile.write("{0}\t{1:.0f}:{2}\n".format(filename[:-4],lenM,lenS))
        i = i + 1
        if len(megasong) > 3600000:
            megasong.export(name, format="mp3")
            namemp3 = namemp3 + 1
            megasong = AudioSegment.empty()
            txtfile.close()
            if namemp3 == 10: 
                break
            nametxt = MUSICDIR + "music" + str(namemp3) + ".txt"
            txtfile = open(nametxt,"w")
            txtfile.write('If you like some track - support author, buy his track on iTunes.\nAll videos are introductory and not provided as commercials.\nIf you liked the format, you can help the project, for its development.\nIf you author and you didn\'t want see you track here, please contact me.\n\nPayPal: ovvXmusic@gmail.com\nBitCoin: 15QoCC14iTJ21P2TnqPXwtsYuRPkC6N5fh\n\nTrackList:\n')
    if namemp3 < 10 :
        name = MUSICDIR + "music" + str(namemp3) + ".mp3"
        megasong.export(name, format="mp3")
    txtfile.close()
    print("Well Done!")


    
def makeVideo():
    FILENAMES = os.listdir(MUSICDIR)
    num = max(FILENAMES)
    num = num[5:num.find('.')]
    i = 0
    while i <= int(num):
        print(i)
        cmd = "ffmpeg -loop 1 -framerate 1 -i " + MUSICDIR + "image" +str(i)+ ".png -i " + MUSICDIR + "music" +str(i)+ ".mp3 -c:v libx264 -crf 0 -preset veryfast -tune stillimage -c:a copy -shortest " + MUSICDIR + "video" +str(i)+ ".mkv"
        os.system(cmd)
        i = i + 1
'''
ffmpeg -loop 1 -framerate 1 -i image9.png -i music9.mp3 -c:v libx264 -crf 0 -preset veryfast -tune stillimage -c:a copy -shortest video9.mkv
'''    






def uploadVideo():

    CATEGORY = '10'			# Music
    TITLE = ''				# 'Synthpop #X (OVV MUSIC)'
    DESCRIPTION = ''		# LOAD FORM musicX.txt
    KEYWORDS = ''
    
    print("Enter TITLE (Style):")
    TITLE = input()
    KEYWORDS = TITLE + ', OVVMUSIC'
    i=0
    while i < 10:
        FINALTITLE = TITLE + '#' +str(i)+ ' (OVV MUSIC)' 
        FILENAME = MUSICDIR + 'music' +str(i)+ '.txt'

        with open(FILENAME, 'r') as myfile:
            DESCRIPTION=myfile.read().replace('\n', '')

        cmd = 'python3 upload.py --file="' +MUSICDIR+ 'video' +str(i)+ '.mkv" --category "' +CATEGORY+ '" --title "' +FINALTITLE+ '" --description "' +DESCRIPTION+ '" --keywords "' +KEYWORDS+ '"'
        os.system(cmd)
        #print(cmd)
        i=i+1
'''
usage: upload.py [--auth_host_name AUTH_HOST_NAME] [--noauth_local_webserver]
                 [--auth_host_port [AUTH_HOST_PORT [AUTH_HOST_PORT ...]]]
                 [--logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] --file
                 FILE [--title TITLE] [--description DESCRIPTION]
                 [--category CATEGORY] [--keywords KEYWORDS]
                 [--privacyStatus {public,private,unlisted}]
				 		 
				 
CategoryID: 				 
2 - Autos & Vehicles
1 -  Film & Animation
10 - Music
15 - Pets & Animals
17 - Sports
18 - Short Movies
19 - Travel & Events
20 - Gaming
21 - Videoblogging
22 - People & Blogs
23 - Comedy
24 - Entertainment
25 - News & Politics
26 - Howto & Style
27 - Education
28 - Science & Technology
29 - Nonprofits & Activism
30 - Movies
31 - Anime/Animation
32 - Action/Adventure
33 - Classics
34 - Comedy
35 - Documentary
36 - Drama
37 - Family
38 - Foreign
39 - Horror
40 - Sci-Fi/Fantasy
41 - Thriller
42 - Shorts
43 - Shows
44 - Trailers
'''    
    


def menuCase(case):
    if case == '0':
        print("Exit")
        exit()
    elif case == '1':
        print("Create single files ...")
        getListOfSongs()
    elif case == '2':
        print("Making video...")
        makeVideo()
    elif case == '3':
        print("Uploading video on YouTube...")
        uploadVideo()

        
        
        
        
def main():
    case = -1
    while case != '0':
        print("0. Exit")
        print("1. Make one-song files")
        print("2. Make video! (Don't forget insert image")
        print("3. Load on YouTube. (Chack you client_secrets.json")
        print("Enter menu step:")
        case = input()
        menuCase(case)
        print()

if __name__ == "__main__":
    main()

