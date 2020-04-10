from pytube import YouTube, Playlist


def single_aud(url):
    audio = YouTube(url)
    stream = audio.streams.get_audio_only()
    print("Title: {}".format(audio.title))
    print("Size: ", round(stream.filesize/1024/1024, 2), "Mb")
    d = input("Do you want to download this? write (yes/no) or write (exit) to exit: ")
    if d == "yes":
        stream.download("D:/exzandar/") # don't forget to change that to your directory!
        print("audio: {} Downloaded in D:/exzandar/".format(audio.title))
    elif d == "no":
        print("This audio won't be downloaded! ")
    else:
        print("Bye Idiot! ")
        exit(0)

def list_aud(url):
    list = Playlist(url)
    num = len(list.video_urls)
    whole_list = list.video_urls
    print("\nThis playlist contain {} audio and they are: \n\n".format(num))
    for vid in whole_list:
        single_aud(vid)
        print("\n\n")

url = input("\nEnter the full URL: ")
what = ""
if "list" in url:
    print("\nNote: this is a playlist not a single audio! ")
    list_aud(url)
else:
    print("\nNote: this is a single audio! ")
    single_aud(url)
