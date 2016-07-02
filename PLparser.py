#parse Youtube URL's given the playlist link.
#usage: python PLparser.py playlist-url

import urllib.error, urllib.request
import re
import sys
import time 



if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Wrong command! Please type in the following format: python PLparser.py playlist-url")
    
    else:
        url = sys.argv[1]
        if "https://" not in url:
            url = "https://" + url

        parse(url)
