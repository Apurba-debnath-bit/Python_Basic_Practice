#file object = open(<file-name>, <access-mode>, <buffering>)
try:
    f = open("my", "a")
    print(f.write("Sagor"))
except:
    f.close()