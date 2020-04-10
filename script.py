from pytube import YouTube, Playlist
from progressbar import ProgressBar


def prog_check(stream = None, chunk = None, remaining = None):
    x = round((siz-remaining)/siz*100, 2)
    bar.update(x)


def single_aud(url):
    audio = YouTube(url, on_progress_callback=prog_check)
    stream = audio.streams.get_audio_only()
    print("Title: {}".format(audio.title))
    print("Size: ", round(stream.filesize/1024/1024, 2), "Mb")
    global siz
    siz = stream.filesize
    d = input("Do you want to download this in D:/exzandar/? write (yes/no) or write (exit) to exit: ")
    if d == "yes":
        bar.start(max_value=100)
        stream.download("D:/exzandar/")
    elif d == "no":
        print("This audio won't be downloaded! ")
    else:
        print("\nBye Idiot! \n")
        exit()


def list_aud(url):
    list = Playlist(url)
    num = len(list.video_urls)
    whole_list = list.video_urls
    print("\nThis playlist contain {} audio and they are: \n\n".format(num))
    for vid in whole_list:
        single_aud(vid)
        print("\n\n")


if __name__ == '__main__':
    bar = ProgressBar()
    url = input("\nEnter the full URL: ")
    what = ""
    if "list" in url:
        print("\nNote: this is a playlist not a single audio! ")
        list_aud(url)
    else:
        print("\nNote: this is a single audio! ")
        single_aud(url)
