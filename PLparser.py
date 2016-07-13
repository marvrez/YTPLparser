#parse Youtube URL's given the playlist link.
#usage: python PLparser.py playlist-url
#TODO: try implementing threading!
import re
import urllib.error
import urllib.request
import sys
import time 
import threading

start = time.time()

def parse(url):
    final_url = []
    all_urls = []
    if ("list=" in url):
        eq = url.rfind("=")+1
        pl_code = url[eq:]
    else:
        print("Incorrect playlist, please try again with a correct Youtube playlist URL!")
        exit(1)
    try:
        yt_page = str(urllib.request.urlopen(url).read())
    except urllib.error.URLError as e:
        print (e.reason)

    pattern = re.compile(r"watch\?v=\S+?list="+ pl_code)
    match = re.findall(pattern,yt_page)

    if match:
        for __video in match:
            video = str(__video)
            if "&" in video:
                amp = video.index("&") 
                video_url = video[:amp]
                final_url.append("https://youtube.com/"+ video_url[:amp])
        all_urls = list(set(final_url))
        for video in all_urls:
            print(video)
    else:
        print ("No videos found in playlist")
        exit(1)


if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Wrong command! Please type in the following format: python PLparser.py playlist-url")
    
    else:
        url = sys.argv[1]
        if "https://" not in url:
            url = "https://" + url
        parse(url) #leggo
        print ("Elapsed time: %ss" % (time.time()-start) )
