#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib, json, datetime, csv, re, sys, argparse
import urllib.request

mode = 'CSV'

# import xlwt, xlutils, xlsxwriter, openpyxl

if mode == 'CSV':
	try:
		import xlwt 
		mode = 'xlwt'
	except ImportError:
		print("xlwt module havn't been found.")

# if mode == 'CSV':
# 	try:
# 		import xlsxwriter 
# 		mode = 'xlsxwriter'
# 	except ImportError:
# 		print("xlsxwriter module havn't been found.")

# if mode == 'CSV':
# 	try:
# 		import xlutils 
# 		mode = 'xlutils'
# 	except ImportError:
# 		print("xlutils module havn't been found.")

# if mode == 'CSV':
# 	try:
# 		import openpyxl 
# 		mode = 'openpyxl'
# 	except ImportError:
# 		print("openpyxl module havn't been found.")


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

class write:
	def lookupMethod(self, command):
		return getattr(self, 'write_' + command.lower(), None)

	def write_csv(self, fname, data):
		with open(fname+'.csv', 'w', newline='') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

			for records in data:
				date = datetime.date.fromtimestamp(records['week'])
				for record in records['days']:
					if record != 0 or short == False:
						# TODO: catching and reporting errors
						rdate = str(date.strftime("%d-%m-%Y"))
						print(rdate + ' => ' + str(record))
						csvwriter.writerow([rdate] + [str(record)])
					date += datetime.timedelta(days=1)
				# print('======= week row =======')
		print("Excel modules not found. Only CSV mode aviable.")
		return True

	def write_xlwt(self, fname, data):
		total = 0
		# print('xlwt have been found')
		wb = xlwt.Workbook()
		ws = wb.add_sheet(fname)
		for records in data:
				date = datetime.date.fromtimestamp(records['week'])
				for record in records['days']:
					if record != 0 or short == False:
						# TODO: catching and reporting errors
						rdate = str(date.strftime("%d-%m-%Y"))
						print(rdate + ' => ' + str(record))
						
						ws.write(total, 0, rdate)
						ws.write(total, 1, str(record))

						total += 1
					date += datetime.timedelta(days=1)
				# print('======= week row =======')
		wb.save(fname + '.xls')
		return True

	def write_xlsxwriter(self, fname, data):
		print('xlsxwriter have been found')
		pass
		return True

	def write_xlutils(self, fname, data):
		print('xlutils have been found')
		pass
		return True

	def write_openpyxl(self, fname, data):
		print('openpyxl have been found')
		pass
		return True

data = get_stats(url)

write().lookupMethod(mode)(rep, data)

exit(0)
