file_name = str(input("File name: ")).strip().lower()
split_name = file_name.split(".")
extention = split_name[-1]

if extention == "gif":
    print("image/gif")

elif extention == "jpg" or extention == "jpeg":
    print("image/jpeg")

elif extention == "png":
    print("image/png")

elif extention == "pdf":
    print("application/pdf")

elif extention == "txt":
    print("text/plain")

elif extention == "zip":
    print("application/zip")

else:
    print("application/octet-stream")
