import speedtest #pip install speedtest-cli
import csv
import datetime
import time
import sys
import argparse
import os

def testspeed():

	test = speedtest.Speedtest()
	test.get_best_server()
	test.download()
	test.upload()

	result = test.results.dict()

	resultDict = {
			'timestamp': datetime.datetime.now(),
			'sponsor': result['server']['sponsor'],
			'locality': result['server']['name'],
			'ip': result['client']['ip'],
			'provider': result['client']['isp'],
			'download': result['download']/1e+6,
			'upload': result['upload']/1e+6,
			'ping': result['ping']
			}

	return resultDict


def storeData(csv_path, resultDict):

	csv_exists = os.path.exists(csv_path)

	if csv_exists:

		with open(csv_path, 'a', newline = '') as csvfile:

			fieldnames = ['timestamp', 'sponsor', 'locality', 'ip', 'provider','download','upload','ping']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writerow(resultDict)

	else:

		with open(csv_path, 'a', newline = '') as csvfile:

			fieldnames = ['timestamp', 'sponsor', 'locality', 'ip', 'provider','download','upload','ping']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writerow({i:i for i in fieldnames})
			writer.writerow(resultDict)

	print("data added to file: {}".format(csv_path))


class commandLine:

	def __init__(self):
		
		parser = argparse.ArgumentParser(description = "Descriptions of arguments")
		parser.add_argument("-m", "--mode", help = "static (return result only one time) or monitoring (continously return results)", required = True, default = "static", type =str)
		parser.add_argument("-s", "--storedata", help = "bin to check if you want to store data (0 to false, 1 to true)", required = False, default = 0, type = int)
		parser.add_argument("-d", "--csv_result", help = "path of csv result file", required = False, default = "csv_result.csv", type = str)
		parser.add_argument("-t", "--refreshtime", help = "refresh time (in minutes) for monitoring mode", required = False, default = 1800, type = int)
		self.arguments = parser.parse_args()

	def main(self):

		arguments = self.arguments

		if arguments.mode == 'static':

			print("")
			print("{} - testing speed...".format(datetime.datetime.now()))
		
			resultDict = testspeed()
			print(resultDict)

			if (arguments.storedata == 1): 
				
				storeData(arguments.csv_result, resultDict)

			elif (arguments.storedata == 0):
				
				pass

			else:
				
				print("storedata argument invalid, please insert 0 for false or 1 for true")


		elif arguments.mode == 'monitoring':

			if (arguments.refreshtime > 0):

				while True:

					print("")
					print("{} - testing speed...".format(datetime.datetime.now()))

					resultDict = testspeed()
					print(resultDict)

					if (arguments.storedata == 1):
						
						storeData(arguments.csv_result, resultDict)
						time.sleep(arguments.refreshtime*60)


					elif (arguments.storedata == 0):
						
						time.sleep(arguments.refreshtime*60)
						

					else:

						print("storedata argument invalid, please insert 0 for false or 1 for true")
						break

			else:

				print("invalid refreshtime")
			

		else:

			print("invalid mode, please insert static (return result only one time) or monitoring (continously return results)")

			
			

if __name__== "__main__":

	app = commandLine().main()
