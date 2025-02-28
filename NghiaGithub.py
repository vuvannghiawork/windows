import os


folderNghiaGithub = os.path.expanduser("~/Desktop/NghiaGithub")


if not os.path.exists(folderNghiaGithub):
    print("The folder does not exist.")
    os.makedirs(folderNghiaGithub, exist_ok=True)
    print("Created the folder.")
