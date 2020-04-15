#!/usr/bin/python3 -i
"""
Author: Cameron Gillette
Course: MIS_429
Date: 14.April.2020
Program: connect_to_sheets.py
Requirements: gspread, oauth2client
Description: This program is a proof of concept for how a python program can open and edit
             an excel or csv file hosted on google drive. credit to youtube.com/JayMartMedia
             for the helpful tutorial.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)

client = gspread.authorize(creds)

sheet = client.open('sample_sheet').sheet1
students = sheet.get_all_records()
for student in students:
    id = student['id']
    fName = student['first_name']
    lName = student['last_name']
    email = student['email']
    gender = student['gender']
    ip_address = student['ip_address']
    print("Name: " + fName + " " + lName +"\nGender: " + gender + "\nEmail: " + email + "\nip: " + ip_address+"\n\n")