import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "D:/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("file created :)")

    def on_deleted(self, event):
        print(" file got deleted :(")

    def on_modified(self, event):
        print("YOU CHANGED THE FILE")

    def on_moved(self, event):
        print("uh-oh, you moved it")
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

while True:
    time.sleep(2)
    print("running...")






