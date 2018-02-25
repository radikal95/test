# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
#
# gauth = GoogleAuth()
# auth_url = gauth.GetAuthUrl()
# print(auth_url)
# gauth.LocalWebserverAuth()
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

textfile = drive.CreateFile()
textfile.SetContentFile('eng.txt')
textfile.Upload()
print (textfile)

