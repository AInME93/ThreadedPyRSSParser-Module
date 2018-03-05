ThreadedPyRSSParser-Module
===

This happens to be a sneak peek into one of the modules that I will be integrating to my final year project. It basically parses RSS feeds stored in one file and 
returns the titles of entries in the RSS feed to another file. I created two files inside it that perform the same basic task. However one of them is configured using 
the Queue and Threading libraries so it finishes the tasks faster. I felt someone might benefit from this example while implementing a similar project.

Getting Started
===

Install virtualenv in your machine if you don't have one yet.

```
pip install virtualenv
```

Create virtualenv directory inside the project folder

```
virtualenv venv
```

Activate your virtual environment from the Scripts folder.

```
cd venv/Scripts
```

```
activate
```

Install the library and module requirements from the main directory

```
pip install -r requirements.txt
```

And now you should be good to go. Run the python files and balk at the difference in execution time between the two.

```
python parsing.py

```

```
python threadedparsing.py
```


Built With
===

Python 3.6  
[Queue module] : https://docs.python.org/3/library/queue.html  
[Threading module] : https://docs.python.org/3/library/threading.html  
[Universal feedparser] : https://pypi.python.org/pypi/feedparser  

Author
===

Imran Abdallah