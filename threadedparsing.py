import feedparser
import queue
import threading
import time

#Create an instance of queue.Queue()
q = queue.Queue()

with open('feed_urls.txt', 'r') as file:
    lines = file.readlines()

#create a class 
class threadParseFeed(threading.Thread):

    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            line = self.q.get()

            d = feedparser.parse(line)
            with open('entries_file.txt', 'ab') as outfile:
                for entry in d.entries:
                    outfile.write(entry.title.encode("utf-8") + b'\n')

	    #Send signal to queue the task is done
            self.q.task_done()

start = time.time()
def main():
    # spawn a pool of threads, and pass them queue instance
    for i in range(10):
        t = threadParseFeed(q)
        t.setDaemon(True)
        t.start()
        # populate queue with data

	#populate queue with data   
    for line in lines:
        q.put(line)

        # wait on the queue until everything has been processed
    q.join()

def displayTitles():
    with open('entries_file.txt','r') as displayfeed:
        for line in displayfeed:
            print(line)


main()
displayTitles()
print ("Elapsed Time: %s" % (time.time() - start))
