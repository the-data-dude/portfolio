import speedtest #pip install speedtest-cli
import csv
import datetime
import time

while True:

	print("{} - Mensurando velocidade...".format(datetime.datetime.now()))

	test = speedtest.Speedtest()
	test.get_best_server()
	test.download()
	test.upload()

	result = test.results.dict()

	print("")

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


	print(resultDict)

	with open('results.csv', 'a', newline = '') as csvfile:

		fieldnames = ['timestamp', 'sponsor', 'locality', 'ip', 'provider','download','upload','ping']

		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		
		writer.writerow(resultDict)

	print("")

	time.sleep(3600)




	


