import os
for root,dirs,files in os.walk("."):
    print(files)
pth=os.walk(".")
print ("this is my path ",pth)
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(file)
print(os.stat("python_auto1.py"))
print(os.chmod("python_auto1.py",0o777))
print (os.stat("python_auto1.py"))
print (os.getpid())
for root, dirs, files in os.walk("/"):
    for file in files:
        if os.access(file,os.W_OK):
            print(file)
import os
import stat

for root, dirs, files in os.walk("/"):
    for file in files:
        path = os.path.join(root, file)

        try:
            mode = os.stat(path).st_mode# 👈 yaha define karo

            if mode & 0o4000:  # SUID ch eck
                print(path)
        except:
                       pass
import os
for root, dirs, files in os.talk(os.getcwd()):
    for file in files:
        path = os.path.join(root, file)