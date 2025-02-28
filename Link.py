import os


folderLink = os.path.expanduser("~/Desktop/_Link")


if not os.path.exists(folderLink):
    print("The folder does not exist.")
    os.makedirs(folderLink, exist_ok=True)
    print("Created the folder.")
