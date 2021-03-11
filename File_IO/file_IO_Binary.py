try:
    f2 = open("download.jpg", "rb")
    #print(f2.read(10))
    # for data in f2:
    #     print(data)

    f3 = open("download23.jpg", "wb")
    for data in f2:
        f3.write(data)
except:
    f2.close()
    f3.close()



