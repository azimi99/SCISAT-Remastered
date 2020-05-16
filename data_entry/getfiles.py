import pandas as pd
from urllib.request import urlopen
import json
import io
import requests	
import csv
from collections import defaultdict
import sys
import re
import pymongo


def date(main_url):
	url1 = urlopen(main_url).read().decode('utf_8')
	yr = []
	for word in url1.split():
		if(("200" in word or "201" in word) and int(word.split('-')[0]) <= 2004):
			yr.append(word)
	return yr	

def sun(main_url, time_frame):	
	ss = []
	url2 = urlopen(main_url +  '/' + time_frame + '/').read().decode('utf_8')
	for occult in url2.split():
		if(("ss" in occult or "sr" in occult) and not "-" in occult ):
			ss.append(occult)
	return ss

def runForSunData(main_url, time_frame, sundata):
	data = {}
	page_source = urlopen(main_url + '/' + time_frame + '/' + sundata + '/' + sundata + '_InfoMetadata%20.txt').read().decode('utf_8')
	lines = page_source.splitlines()

	for word in lines:
		if(word.startswith("occultation_name =")):
			occultation_name = word[19:]

		if(word.startswith("event_type =")):
			event_type = word[13:]

		if(word.startswith("date =")):
			date = word[7:]			

		if(word.startswith("date_MJD2000 =")):
			date_MJD2000 = word[15:]

		if(word.startswith("latitude =")):
			latitude = word[11:]

		if(word.startswith("longitude =")):
			longitude = word[12:]

		if(word.startswith("beta_angle =")):
			beta_angle = word[13:]

		if(word.startswith("start_timetag =")):
			start_timetag = word[16:]

		if(word.startswith("end_timetag =")):
			end_timetag = word[14:]

		if(word.startswith("start_time =")):
			start_time = word[13:]

		if(word.startswith("end_time =")):
			end_time = word[11:]
	
	molecule_range = "5-95"
	molecule_name = "O3"
	molecule_csv = pd.read_csv(main_url + '/' + time_frame + '/' + sundata + '/' + 'Data-L2_1km_grid/' + 'O3.csv',  header=None)
	z_csv = pd.read_csv(main_url + '/' + time_frame + '/' + sundata + '/' + 'Data-L2_1km_grid/' + 'z.csv',  header=None)

	df_new = pd.concat([molecule_csv, z_csv], axis =1, names=["Sequence", "Concentration", "Height"])
	df_new.iloc[1:, 1:]
	df_new.to_csv("df_new.csv")
	
	csvFilePath= 'df_new.csv'
	jsonFilePath = 'df.json'

	df_new.to_json(jsonFilePath,orient='values')
	with open(jsonFilePath, 'r') as f:
		data3 = json.loads(f.read())

	data["occultation_name"] = []
	data["occultation_name"].append(occultation_name)
	data["event_type"] = []
	data['event_type'].append(event_type)
	data["date"] = []
	data['date'].append(date)
	data["date_MJD2000"] = []
	data['date_MJD2000'].append(date_MJD2000)
	data["latitude"] = []
	data['latitude'].append(latitude)
	data["longitude"] = []
	data['longitude'].append(longitude)
	data["beta_angle"] = []
	data['beta_angle'].append(beta_angle)
	data["start_timetag"] = []
	data['start_timetag'].append(start_timetag)
	data["end_timetag"] = []
	data['end_timetag'].append(end_timetag)
	data["start_time"] = []
	data['start_time'].append(start_time)
	data["end_time"] = []
	data['end_time'].append(end_time)
	data["molecule_range"] = []
	data['molecule_range'].append(molecule_range)
	data["molecule_name"] = []
	data['molecule_name'].append(molecule_name)
	data["alt_conc"] = []
	data['alt_conc'].append(data3)
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

	with open(r'C:\Users\Haren\Desktop\SCISAT (April 2020)\getFiles\data.json', 'r') as data_file:
	    data_json = json.load(data_file)

	mng_client = pymongo.MongoClient('mongodb+srv://admin:q4QbxT9vVV5WW6DO@cluster0-hc4da.mongodb.net/test?retryWrites=true&w=majority')
	mng_db = mng_client['SCISAT_Data'] # Replace mongo db name
	collection_name = 'TimePeriod' # Replace mongo db collection name
	db_cm = mng_db[collection_name]
	db_cm.insert(data_json)

def main():
	main_url = 'ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format%20CSV'
	time_frame_list = date(main_url)
	for time_frame in time_frame_list:
		sundata_list = sun(main_url, time_frame)
		for sundata in sundata_list:
			# print(sundata + " " + time_frame + "\n")
			runForSunData(main_url, time_frame, sundata)
			

if __name__ == "__main__":
	main()