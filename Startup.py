import os


startup_folder = os.path.expanduser("~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")

folderLink = os.path.expanduser("~/Desktop/_Link")
StartupCopy = os.path.expanduser("~/Desktop/_Link/StartupCopy")
startup_folder_link = os.path.join(folderLink, "Startup")


if not os.path.exists(StartupCopy):
    print("The folder does not exist.")
    os.makedirs(StartupCopy, exist_ok=True)
    print("Created the folder.")


try:
    if os.path.exists(startup_folder_link):
        os.remove(startup_folder_link)
        print(f"Đã xóa symlink: {startup_folder_link}")
    os.symlink(startup_folder, startup_folder_link)
    print(f"Tạo link: {startup_folder_link}")
except OSError as e:
    print(f"Lỗi: {e}")
