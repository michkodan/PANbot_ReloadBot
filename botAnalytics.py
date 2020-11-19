from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

CREDENTIALS_FILE = 'credentials.json'
spreadsheet_id = '1h1imj1rj4bbSwET9w7JBER9SvQAT0_aXVERUGm5Zdg4'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

