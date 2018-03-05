import feedparser
import time


#Create a function that will parse feed urls
def parsefeed(link=None):

#Parse each link and append the titles of the entries in each feed to a file called 'outfile.txt'
    d = feedparser.parse(link)
    with open('entries_file.txt', 'ab') as outfile:
        for entry in d.entries:
            outfile.write(entry.title.encode("utf-8") + b'\n')


#Timer start
start = time.time()

#Read urls from file and pass them as arguments to the parsing function
with open('feed_urls.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        parsefeed(link=line)

print ("Elapsed Time: %s" % (time.time() - start))