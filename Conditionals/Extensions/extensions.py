str = input("File name: ")
parts = str.split(".")
if (len(parts) == 1):
    print("application/octet-stream")
else:
    extension = parts[len(parts) - 1].lower()
    if (extension == 0):
        print("application/octet-stream")
    elif (extension in ["gif", "png"]):
        print("image/" + parts[1].lower())
    elif (extension in ["jpg", "jpeg"]):
        print("image/jpeg")
    elif (extension in ["pdf", "txt", "zip"]):
        print("application/" + parts[1].lower())
    else:
        print("application/octet-stream")
