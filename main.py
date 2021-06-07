import argparse
from urllib.request import Request, urlopen
import hashlib
from playsound import playsound
import sched, time
from datetime import datetime

parser = argparse.ArgumentParser(description='Check if a website has changed.')
parser.add_argument('url', metavar='url', type=str, help='The website URL to check')
parser.add_argument('--interval', type=int, default=5, help='Check interval (seconds)')

args = parser.parse_args()

def getWebsiteChecksum(url):
    req = Request(args.url, headers={'User-Agent': 'Mozilla/5.0'})
    fp = urlopen(req)
    checksum = hashlib.md5(fp.read()).hexdigest()
    fp.close()
    return checksum


oldMd5 = getWebsiteChecksum(args.url)
s = sched.scheduler(time.time, time.sleep)

def checkWebsite(sc):
    global oldMd5

    newMd5 = getWebsiteChecksum(args.url)

    if (newMd5 != oldMd5):
        print(f'Website ({args.url}) has changed!', end='\r')
        playsound('alarm.mp3')
    else:
        print(f'Website ({args.url}) has not changed – Last checked: {datetime.now().time()}', end='\r')

    oldMd5 = newMd5

    s.enter(args.interval, 1, checkWebsite, (sc,))


s.enter(args.interval, 1, checkWebsite, (s,))
s.run()
