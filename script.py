from pytube import YouTube, Playlist
from progressbar import ProgressBar
import os
import subprocess
import datetime
import re

link = "https://www.youtube.com/watch?v=WwB5w-Rt88k"
bar = ProgressBar()

def merge_and_output():
    print("\n[+++++] Download completed, now it's time to merge the video and audio!\n")
    subprocess.run("ffmpeg -i {} -i {} -c:v copy -c:a aac {}".format((path+'1.mp4'), (path+'2.mp4'), (path+'3.mp4')))
    print("\n***** Sorry for this mess, we almost finished ^_^ *****\n")
    os.rename(path+"3.mp4", path+title+".mp4")
    os.rename(path+"2.mp4", path+title+"-AudioFile"+".mp3")
    os.remove(path+"1.mp4")
    print("\nVideo number {} has been completed, You can play it NOW.".format(counter))


def prog_check(stream=None, chunk=None, bytes_remaining=None):      # this is the progress bar function
    calc_remain = round((siz-bytes_remaining)/siz*100, 2)
    bar.update(calc_remain)


def single_vid(url):
    stream = YouTube(url, on_progress_callback=prog_check)      # prog check to show the progress bar
    res = "480"                                                 # the resolution of the video
    s_vid = stream.streams.filter(res=res + "p", adaptive=True, type="video", mime_type="video/mp4").first()  # to get the video
    s_aud = stream.streams.get_audio_only("mp4")                # to get the audio
    global path, no_merge                                               # path to save files
    no_merge = True
    path = "D:\\exzandar\\"
    global title
    title = stream.title
    title = re.sub('[^a-zA-Z-0-9أ-ي \n]', "", title)
    lenght = stream.length
    lenght = datetime.timedelta(seconds=lenght)                 # to convert the seconds to the proper format
    lenght = str(lenght)
    global siz                                                  # it's global to use it in the progress check function
    siz = s_vid.filesize
    print("\n[*] Title: ", title)
    print("\n[*] Length: ", lenght)
    print("\n[*] Video size is: ", round(((siz+s_aud.filesize)/1024/1024), 2), "Mb\n\n")
    ask = input("Do you wanna download this video? [yes/no/exit] >> ")
    ask = ask.lower()
    if ask == "yes":
        bar.start(max_value=100)
        s_vid.download(output_path=path, filename="1")
        bar.finish()
        siz = s_aud.filesize
        bar.start(max_value=100)
        s_aud.download(output_path=path, filename="2")
        bar.finish()
        print("\n Video download completed! ... ")
    elif ask == "no":
        no_merge = False
        print("\n + + + Skipping this video + + + ")
    else:
        exit(0)


def play_list(url):
    stream = Playlist(url)
    urls = stream.video_urls
    print("\n[+] This playlist contain {} video".format(len(urls)))
    global counter
    counter = 1
    for url in urls:
        print("\n[+++++] Video num: ", counter)
        single_vid(url)
        if no_merge:
            merge_and_output()
        counter += 1


if __name__ == '__main__':
    ban = ["", "", "", "", "", "", "", "", "", "", "", ""]
    ban[0] =        "  \n\n Author: @exzandar     AKA: MagMada   "
    ban[1] =          "                            ______        "
    ban[2] =          "     |\     /|  |\     /|  (  __  \       "
    ban[3] =          "     ( \   / )  | )   ( |  | (  \  )      "
    ban[4] =          "      \ (_) /   | |   | |  | |   ) |      "
    ban[5] =          "       \   /    ( (   ) )  | |   | |      "
    ban[6] =          "        ) (      \ \_/ /   | |   ) |      "
    ban[7] =          "        | |       \   /    | (__/  )      "
    ban[8] =          "        \_/        \_/     (______/       "
    ban[9] =          "                                          "
    ban[10] =         " YouTube    -   Video    -   Downloader   "
    ban[11] =        " To Download videos and audios from youtube.\n\n"
    for i in ban:
        print(i)

    print("Hello, this is a simple script to download videos and audios from YouTube.\n"
          "This script depends on pytube module and the great tool ffmpeg and progressbar module to show you the progress\n"
          "For usage: don't forget to change the path variable 'by default, it will create a folder in the D:// named exzandar'")
    url = input("\n\nWrite a [YouTube] link only, understand! >> ")
    if "youtube" in url:
        if "list" in url:
            print("\n[+] This is a playlist")
            play_list(url)
        else:
            print("\n[+] This is a single video")
            single_vid(url)
            merge_and_output()
    else:
        print("\nFuck You! i told you YouTube only motherfucker! ")
