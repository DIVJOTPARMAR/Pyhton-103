import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Divjot singh/OneDrive/Pictures"
to_dir = "C:/Users/Divjot singh/OneDrive/Desktop/coding/image"
to_dir_2 = "C:/Users/Divjot singh/OneDrive/Desktop/coding/Image2"
to_dir_vids="C:/Users/Divjot singh/OneDrive/Desktop/coding/video or music"


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)

# Initializing event handler class
event_handler = FileMovementHandler() 

# Initializing the observer 
observer = Observer()

# Scheduling the observer 
observer.schedule(event_handler, from_dir, recursive=True)

# Start the observer 
observer.start()

while True:
    list_of_files = os.listdir(from_dir)

    for file_name in list_of_files:
        name, extention = os.path.splitext(file_name)

        if extention == "":
            continue

        if extention in [".png"]:
            path1 = os.path.join(from_dir, file_name)
            path2 = os.path.join(to_dir, "Image_Files")
            path3 = os.path.join(to_dir, "Image_Files", file_name)

            print("Path 1", path1)
            print("Path 3", path3)

            if os.path.exists(path2):
                print("Moving " + file_name + ".....")
                # Move from path1 ---> path3 
                shutil.move(path1, path3)
            else:
                os.makedirs(path2) 
                print("Moving " + file_name + ".....") 
                shutil.move(path1, path3)

        elif extention in [".jpg"]:
            path_1 = os.path.join(from_dir, file_name)
            path_2 = os.path.join(to_dir_2, "Image_Files")
            path_3 = os.path.join(to_dir_2, "Image_Files", file_name)

            print("Path 1", path_1)
            print("Path 3", path_3)

            if os.path.exists(path_2):
                print("Moving " + file_name + ".....")
                # Move from path1 ---> path3 
                shutil.move(path_1, path_3)
            else:
                os.makedirs(path_2) 
                print("Moving " + file_name + ".....") 
                shutil.move(path_1, path_3)

            # for video and music.
                    
        elif extention in [".mp4",".mp3"]:
            path_1_ = os.path.join(from_dir, file_name)
            path_2_ = os.path.join(to_dir_vids, "Video and Music")
            path_3_ = os.path.join(to_dir_vids, "Video and Music", file_name)

            print("Path 1", path_1_)
            print("Path 3", path_3_)

            if os.path.exists(path_2_):
                print("Moving " + file_name + ".....")
                # Move from path1 ---> path3 
                shutil.move(path_1_, path_3_)
            else:
                os.makedirs(path_2_) 
                print("Moving " + file_name + ".....") 
                shutil.move(path_1_, path_3_)
        
