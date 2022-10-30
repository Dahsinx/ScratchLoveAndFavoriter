import scratchclient
from random import randint
from time import sleep

input("I CANT BE HELD RESPONSIBLE IF YOUR SCRATCH ACCOUNT GETS BLOCKED/BANNED! USE AT YOUR OWN RISK! (press enter to continue)")
print("-----------------------------------")
print("Scratch project Love and Favoriter")
print("-----------------------------------")
print("Made by Dahsinx on GitHub")
username = input("Enter your scratch username: ")
password = input("Password: ")
times = int(input("How many random projects do you want to favourite and like? "))
session = scratchclient.ScratchSession(username,password)
for i in range(1,times):
    id = randint(5000,743255779)
    try:
        project = session.get_project(id)
    except:
        print(f"Project probably doesnt exist or an error occured ID: {id}")
    else:
        try:
            project.love()
            project.favorite()
        except:
            print(f"And error occured loving and favouriting project {project.title} ID: {id}, trying again in 30 seconds.")
            sleep(30)
            try:
                project.love()
                project.favorite()
            except:
                print("Project failed to love and favourite 2nd time, skipping.")
            else:
                 print(f"Loved and favourited project {project.title} ID: {id}")
        else:
            print(f"Loved and favourited project {project.title} ID: {id}")