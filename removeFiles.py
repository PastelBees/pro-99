import time
import os
import shutil

path = input("Enter your directory's name: ")

days = int(input("Enter your file's maximum days of existence: "))

seconds = time.time() - (days * 24 * 60 * 60)

if(os.path.exists(path)):

    for root,dirs,files in os.walk(path,topdown=True):

        for name in files:

            path=os.path.join(root,name)

            ctime=os.stat(path).st_ctime
            
            if (seconds>=ctime):

                os.remove(path)

                print("You have deleted the path " + path + " successfully!")

        for name in dirs:

            path = os.path.join(root, name)

            ctime = os.stat(path).st_ctime

            if (seconds >= ctime):

                shutil.rmtree(path)

                print("You have deleted the path " + path + " successfully!")

else:
    print("That path was not found. Please enter a valid path.")
