import oauth2client
from oauth2client import file, client, tools

import apiclient
from apiclient import discovery, errors

import dateutil.parser as parser
import datetime
import time

from datetime import datetime

import base64
from bs4 import BeautifulSoup

from httplib2 import Http

import csv
import re

#**API setup**
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly' 	# we are using readonly,
store = file.Storage('c.json')								# GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'removeLabelIds': ['UNREAD']}).execute()								
creds = store.get()											#        ^    This will mark the messagea as read
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

user_id =  'me'
label_id_two = 'UNREAD'
label_id_three = 'Label_4337773235218417025'

#beginning = 					(?<=This is)(.*)(?=sentence)
beginning = re.compile(r'(?<=Notes)(.*)(?=\d\d\/\d\d\/\d\d)')
upTO = re.compile(r'(?<=Notes)(.*)(?=\d\d\/\d\d\/\d\d)')
DATEpattern = re.compile(r'\d\d\/\d\d\/\d\d')				#['10/05/23']
CAPSpattern = re.compile(r'\b[A-Z(1,2)]{2,}\b')				#['HENRY', 'TLB', '1L', 'USD']
MRGN = re.compile(r'[^2020.]\d\d\d\b')						#[' 400', ' 100']	  <-floor
ENDpattern = re.compile(r'\d\d+\.\d\d\d')					#['90.000', '95.000']"

unread_msgs = GMAIL.users().messages().list(userId='me',labelIds=[label_id_three, label_id_two]).execute()
mssg_list = unread_msgs['messages']
final_list = [ ]

for mssg in mssg_list:
	temp_dict = { }
	tmp_list = []
	tmp_list2 = []
	tmp_list3 = []
	tmp_list4 = []
	tmp_list5 = []
	m_id = mssg['id'] 						
	message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute() 
	payld = message['payload'] 				
	headr = payld['headers'] 		


	front = upTO.finditer(message['snippet'])
	newCaps = beginning.finditer(message['snippet'])
	caps = CAPSpattern.finditer(message['snippet'])
	date = DATEpattern.finditer(message['snippet'])
	margin = MRGN.finditer(message['snippet'])
	end = ENDpattern.finditer(message['snippet'])		


	for one in headr: 			
		if one['name'] == 'Subject':
			msg_subject = one['value']
			temp_dict['Subject'] = msg_subject
		else:
			pass

	for two in headr: 			
		if two['name'] == 'Date':
			msg_date = two['value']
			date_parse = (parser.parse(msg_date))
			m_date = (date_parse.date())
			temp_dict['Date'] = str(m_date)
		else:
			pass

	for three in headr: 		
		if three['name'] == 'From':
			msg_from = three['value']
			temp_dict['Sender'] = msg_from
		else:
			pass

	temp_dict['Snippet'] = message['snippet'] 

	for match in front:							
		x = match.group(0)
		tmp_list.append(x)
		temp_dict['pattern1'] = tmp_list


	for match in newCaps:							
		x = match.group(0)
		exp = CAPSpattern.finditer(x)
		for y in exp:
			yy = y.group(0)
			tmp_list2.append(yy)
			temp_dict['pattern2'] = tmp_list2

	for match in date:
		x = match.group(0)
		tmp_list3.append(x)
		temp_dict['pattern3'] = tmp_list3

	for match in margin:
		x = match.group(0)
		tmp_list4.append(x)
		temp_dict['pattern4'] = tmp_list4

	for match in end:
		x = match.group(0)
		tmp_list5.append(x)
		temp_dict['pattern5'] = tmp_list5
	

	final_list.append(temp_dict) 				

print(final_list)



#**write to CSV**
with open('new.csv', 'w', encoding='utf-8', newline = '') as csvfile:
    fieldnames = ['Sender','Subject','Date','Snippet', 'pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    writer.writeheader()									#           comma
    for val in final_list:
    	writer.writerow(val)


#*******************************************************************************************************


