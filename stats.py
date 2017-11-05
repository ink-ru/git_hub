#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib, json, datetime, csv, re, sys, argparse
import urllib.request

# import xlwt, xlutils, xlsxwriter, openpyxl

# TODO: import win32com.client
# TODO: Excel = win32com.client.Dispatch("Excel.Application")

version = "1.0.0"
url = '' # url = 'https://github.com/PyGithub/PyGithub/'
short = False

def createParser (): # http://jenyay.net/Programming/Argparse
    parser = argparse.ArgumentParser(
                prog = sys.argv[0],
                description = '''Сохранение в файл CSV статистики правок GitHub репозитория''',
                epilog = '''george.a.wise@gmail.com'''
                )
    parser.add_argument ('-u', '-url', required=True, help = 'Полный адрес GitHub репозитория')
    parser.add_argument ('-s', '-short', action='store_true', default=False, help = 'Не выводить дни без правок')
 
    return parser

if len(url) < 3:
	parser = createParser()
	namespace = parser.parse_args()
	url = str(namespace.u) # sys.argv[1]
	short = namespace.s

print(url)
purl = re.match('^https?://github\.com/([^/]+)/([^/]+)/?.*', url, re.IGNORECASE)

if purl != None:
	url = 'https://api.github.com/repos/'+purl.group(1)+'/'+purl.group(2)+'/stats/commit_activity'
	rep = purl.group(2) if purl.group(2) else 'github-result'
else:
	parser = createParser()
	parser.print_help()
	sys.exit('Ошибка. Неправильный адрес репозитория') # raise ValueError('Ошибка. Неправильный адрес репозитория')


def get_stats(url):
	# TODO: implement QNetworkRequest and QAbstractNetworkCache
	req = urllib.request.Request(url, method='GET')

	try:
		response = urllib.request.urlopen(req)
	except urllib.error.URLError as e:
		# print(e.reason)
		if hasattr(e, 'code'):
			return e.code
		else:
			return 0
	else:
		html = response.read().decode("utf-8").strip()
		try:
			jdata = json.loads(html)
		except:
			raise ValueError('Сервер вернул пустой ответ')
		return jdata

data = get_stats(url)

with open(rep+'.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for records in data:
		date = datetime.date.fromtimestamp(records['week'])
		for record in records['days']:
			if record != 0 or short == False:
				# TODO: catching and reporting errors
				print(str(date) + ' => ' + str(record))
				csvwriter.writerow([str(date)] + [str(record)])
			date += datetime.timedelta(days=1)
		# print('===============')
pass
