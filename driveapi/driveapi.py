from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import re

def create_folder(foldername, creds):
    """ Create a folder and prints the folder ID
    Returns : Folder Id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': foldername,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': ['18Hsy0xFgHAqDJGhYL5w5J9Q5hMv3rk4K'], # "Data" Folder
            'driveId':'0AMIGWx53zKa9Uk9PVA' # "EDP Research Project"
        }

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, fields='id'
                                      ,supportsAllDrives=True).execute()
        print(F'Folder named "{foldername}" has created with ID: "{file.get("id")}".')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')



def upload_to_folder(real_folder_id, file_upload, creds):
    """Upload a file to the specified folder and prints file ID, folder ID
    Args: Id of the folder
    Returns: ID of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        folder_id = real_folder_id
        file_upload_name = re.findall('data/(.+)', file_upload)[0]
        file_metadata = {
            'name': file_upload_name,
            'parents': [folder_id],
            'driveId':'0AMIGWx53zKa9Uk9PVA' # EDP Research Project
        }
        media = MediaFileUpload(file_upload,
                                mimetype='text/csv', resumable=True)
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id',
                                      supportsAllDrives = True).execute()
        parentFolderName = getFilebyID(real_folder_id, creds)['name']
        print(F'File named "{file_upload_name}" has added to the folder named "{parentFolderName}".')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')

def search_folder(folder2find, creds):
    """Search file in drive location

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        files = []
        page_token = None
        while True:
            # pylint: disable=maybe-no-member
            response = service.files().list(q=f"(mimeType='application/vnd.google-apps.folder') and (name = '{folder2find}') and '18Hsy0xFgHAqDJGhYL5w5J9Q5hMv3rk4K' in parents",
                                            spaces='Drive',
                                            corpora = 'drive',
                                            fields='nextPageToken, '
                                                   'files(id, name)',
                                            driveId='0AMIGWx53zKa9Uk9PVA', 
                                            includeItemsFromAllDrives = True,
                                            supportsAllDrives = True,
                                            pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                print(F'Found file: {file.get("name")}, {file.get("id")}')
            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    except HttpError as error:
        print(F'An error occurred: {error}')
        files = None

    return files

def getFilebyID(ID, creds):
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        # pylint: disable=maybe-no-member
        file = service.files().get(fileId = ID, 
                                   fields = 'id, name, mimeType, parents', 
                                   supportsAllDrives = True,
                                   ).execute()
        # print(F'Found file: {file.get("name")}')

    except HttpError as error:
        print(F'An error occurred: {error}')

    return file

def getCreds(filepath):
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/drive']
    if os.path.exists(filepath):
        creds = Credentials.from_authorized_user_file(filepath, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'driveapi/client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('driveapi/token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

# if __name__ == '__main__':
#     # search_folder(creds)
#     folderid = create_folder('_EDP_stage2_2022-08-12-2305', creds)
#     upload_to_folder(folderid, '_EDP_stage2_2022-08-12-2305.csv', creds)

# creds = getCreds('token.json')
# print(search_folder('test',creds)[0]['id'])