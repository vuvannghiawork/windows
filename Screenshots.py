import os


Screenshots_folder = os.path.expanduser("~/Pictures/Screenshots")

folderLink = os.path.expanduser("~/Desktop/_Link")
Screenshots_folder_link = os.path.join(folderLink, "Screenshots")

 


try:
    if os.path.exists(Screenshots_folder_link):
        os.remove(Screenshots_folder_link)
        print(f"Đã xóa symlink: {Screenshots_folder_link}")
    os.symlink(Screenshots_folder, Screenshots_folder_link)
    print(f"Tạo link: {Screenshots_folder_link}")
except OSError as e:
    print(f"Lỗi: {e}")
