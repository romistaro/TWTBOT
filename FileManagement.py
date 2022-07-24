import os

def deletefiles(Dir):
    folder = '/home/kamui/Documents/PROGRAMMING/TWTBOT/downloads/' + Dir
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    os.rmdir(folder)
