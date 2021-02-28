import requests
from __future__ import print_function
from googleapiclient.discovery import build
from apiclient import errors
from httplib2 import Http
from email.mime.text import MIMEText
import base64
from google.oauth2 import service_account

class Emailer:

	EMAIL_FROM = "automatedfileemailer@automatedfileemailer.iam.gserviceaccount.com"
	EMAIL_TO = "jakelucasnyc_TzoApU@kindle.com"
	EMAIL_TEXT = ""


	def __init__(self, file):
		self.file = file

	def create(self):
		message = MIMEText(Emailer.EMAIL_TEXT)
		message['to'] = Emailer.EMAIL_TO
		message['from'] = Emailer.EMAIL_FROM
		return {'raw': base64.urlsafe_b64encode(message.as_string())}


	def attach(self):
		pass

	def send(self):
		pass

	

