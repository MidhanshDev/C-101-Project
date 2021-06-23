import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for name in files:
                localPath = os.path.join(root, name)
                relativePath = os.path.relpath(localPath,file_from)
                dropboxPath = os.path.join(file_to,relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath,mode=WriteMode("overwrite"))
            
                

def main():
    access_token = 'sl.AzSm_smwvEy1wx311B8A4Dp_lovAJNMEQRy2VKBzup4qjw_sgpyEjMG9ehKooc45KsVZiHXsWixKOHAeVe7d-5pmk8O34OLfrrZHuXu6hbYKpnqIlTqkBKpVtH1Um7kVkr7nWwo'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to transfer: ")
    file_to = input("Enter the full path upload to dropbox: ")  

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Folder has been moved")

if __name__ == '__main__':
    main()