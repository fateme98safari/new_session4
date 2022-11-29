import getpass
import instaloader

old_followers=[]
f=open("my-project/forth_session.py/followers.txt" , "r")
for line in f:
    old_followers.append(line)
f.close()

L=instaloader.Instaloader()

username=input("enter username: ")
password=getpass.getpass("enter password: ")

L.login(username,password)
print("successfully logged in")

profile = instaloader.Profile.from_username(L.context, "fateme.safari70")

new_followers=[]
for follower in profile.get_followers:
    new_followers.append(follower)

f=open("followers.txt" , "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)