str = input("File name: ")
parts = str.strip().split(".")
extension = parts[len(parts) - 1].lower()
# Check if there's an extension in the name
if (len(parts) == 1):
    # If there is no extension
    print("application/octet-stream")
# If there is an extension
else:
    extension = parts[len(parts) - 1].lower()
    if (extension == 0):
        print("application/octet-stream")
    elif (extension in ["gif", "png"]):
        print("image/" + extension)
    elif (extension in ["jpg", "jpeg"]):
        print("image/jpeg")
    elif (extension in ["pdf", "zip"]):
        print("application/" + extension)
    elif (extension == "txt"):
        print("text/plain")
    # If the extension is not supported
    else:
        print("application/octet-stream")
