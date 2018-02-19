# -*- coding: utf-8 -*-

import os

import random
from pydub import AudioSegment
from multiprocessing import Process

MUSICDIR = "./music/"
FILENAMES = ''
IGNORLIST = './ignorlist.txt'




class getListOfSongs:
    def __call__(self, namenum=0):
	
        namemp3 = namenum
        print('Start Thread {0}...'.format(namemp3))

        nametxt = MUSICDIR + "music" + str(namemp3) + ".txt"
        txtfile = open(nametxt, "w")
        txtfile.write('If you like some track - support author, buy his track on iTunes.\nAll videos are introductory and not provided as commercials.\nIf you author and you didn\'t want see you track here, please contact me.\n\nIf you liked the format, you can help the project, for its development.\nDONATE:\nPayPal: ovvXmusic@gmail.com\nBitCoin: 15QoCC14iTJ21P2TnqPXwtsYuRPkC6N5fh\n\nTrackList:\n')

        megasong = AudioSegment.empty()
        while len(megasong) < 3600000:
            FILENAMES = os.listdir(MUSICDIR)
            random.shuffle(FILENAMES)		
            fullname = MUSICDIR + FILENAMES[0]
            if os.path.isfile(fullname):
                song = AudioSegment.from_file(fullname)
                os.remove(fullname)
                fulltime = len(megasong) / 1000
                if len(megasong) == 0:
                    megasong = song
                else:
                    megasong = megasong.append(song, crossfade=5000)	
                lenM = fulltime // 60
                lenS = fulltime % 60
                if lenS < 10:
                    lenS = "{:.0f}".format(lenS)
                    lenS = '0' + str(lenS)
                else:
                    lenS = "{:.0f}".format(lenS) 
				
                filename = FILENAMES[0]
                txtfile.write("{0}\t{1:.0f}:{2}\n".format(filename[:-4],lenM,lenS))	
        name = MUSICDIR + "music" + str(namemp3) + ".mp3"
        megasong.export(name, format="mp3")	
        txtfile.close()
        print('Thread {0} DONE'.format(namemp3))



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
		
		
def runProcess():
    a = getListOfSongs()

	
    deleteIgnorListTracks()
    p1 = Process(target=a, args=(0,))
    p2 = Process(target=a, args=(1,))
    p3 = Process(target=a, args=(2,))
    p4 = Process(target=a, args=(3,))
    p5 = Process(target=a, args=(4,))
    p6 = Process(target=a, args=(5,))
    p7 = Process(target=a, args=(6,))
    p8 = Process(target=a, args=(7,))
    p9 = Process(target=a, args=(8,))
    p10 = Process(target=a, args=(9,))
	
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
	
	
def makeVideo():
    FILENAMES = os.listdir(MUSICDIR)
    num = max(FILENAMES)
    num = num[5:num.find('.')]
    i = 0
    while i <= int(num):
        print(i)
        cmd = "ffmpeg -loop 1 -i " + MUSICDIR + "image" +str(i)+ ".png -i " + MUSICDIR + "music" +str(i)+ ".mp3 -c:a aac -c:v libx264 -crf 0 -preset veryfast -shortest " + MUSICDIR + "video" +str(i)+ ".mp4"
        os.system(cmd)
        i = i + 1


'''
ffmpeg -loop 1 -i image.png -i music.mp3 -c:a aac -c:v libx264 -crf 0 -preset veryfast -shortest output.mp4
'''    

def menuCase(case):
    if case == '0':
        print("Exit")
        exit()
    elif case == '1':
        print("Create single files ...")
        runProcess()
    elif case == '2':
        print("Making video...")
        makeVideo()

def main():
    case = -1
    while case != '0':
        print("0. Exit")
        print("1. Make one-song files")
        print("2. Make video! (Don't forget insert image")
        print("Enter menu step:")
        case = input()
        menuCase(case)
        print()

if __name__ == "__main__":
    main()

