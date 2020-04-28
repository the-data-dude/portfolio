# speedshow

### Project to track internet speed using [speedtest-cli](https://www.speedtest.net/apps/cli) library

## Usage


    $ python speedshow.py --mode [static or monitoring] --storedata [0 or 1] --csv_result [csv_path] --refreshtime [minutes]

## About the parameters:
 - **mode**
	 - **static**: return your internet speed only one time;
	 - **monitoring**: continuously return your internet speed (`--refreshtime` required)
	 
 - **storedata**
	 - **0**: won't store data
	 - **1**: will store data
	 
	 default: 0
	 
	 the data will be stored in a comma delimmited csv called **result.csv**, in the same directory. If the file doesn't exists, it will be created. If you want to change the directory or the name of file, use the parameter `--csv_result`
	 
- **csv_result**
	parameter to change the directory or the name of file that will store the results
	
	default: result.csv

- **refreshtime**
	time (in minutes) to wait before calculate the internet speed again
	
	default: 30

## Result fields:
	

 - **timestamp**: date and hour when test ran;
 - **sponsor**: server used to test the speed;
 - **locality**: locality of the server;
 - **ip**: your ip;
 - **provider**: your internet provider;
 - **download**: your download speed (in mbps);
 - **upload**: your upload speed (in mbps);
 - **ping**: your ping (in ms);

## Examples:

- ### run only one test

        $ python speedshow.py --mode static
    	
    	2020-04-28 19:23:53.130562 - testing speed...                                                           
    	{'timestamp': datetime.datetime(2020, 4, 28, 19, 25, 14, 681909), 'sponsor': 'FIX FIBRA','locality': 'Diadema', 'ip': '186.220.84.243', 'provider': 'Claro NET', 'download': 124.35876169012941, 'upload': 9.921756427755136, 'ping': 14.425}
    ###

- ### monitor speed without save (30min default refreshtime)

    	$ python speedshow.py --mode monitoring
    	
    	2020-04-28 19:39:39.540695 - testing speed...
    	{'timestamp': datetime.datetime(2020, 4, 28, 19, 40, 40, 811508), 'sponsor': 'FIX FIBRA', 'locality': 'Diadema', 'ip': '186.220.84.243', 'provider': 'Claro NET', 'download': 124.92983156624214, 'upload': 9.60541634061166, 'ping': 12.441}
    ###

- ### monitor speed and save results (2min refreshtime)

	    $ python speedshow.py --mode monitoring --storedata 1  --refreshtime 2
	    
	    2020-04-28 19:39:39.540695 - testing speed...
	    {'timestamp': datetime.datetime(2020, 4, 28, 19, 40, 40, 811508), 'sponsor': 'FIX FIBRA', 'locality': 'Diadema', 'ip': '186.220.84.243', 'provider': 'Claro NET', 'download': 124.92983156624214, 'upload': 9.60541634061166, 'ping': 12.441}
		data added to file: csv_result.csv
	###

- ### monitor speed and save results in a different file (or directory) (2min refreshtime)
	    $ python speedshow.py --mode monitoring --storedata 1 --csv_result C:\Users\ewdhe\Desktop\customcsv.csv --refreshtime 2
	    
    	2020-04-28 19:57:57.355382 - testing speed...
    	{'timestamp': datetime.datetime(2020, 4, 28, 19, 59, 18, 533967), 'sponsor': 'FIX FIBRA', 'locality': 'Diadema', 'ip': '186.220.84.243', 'provider': 'Claro NET', 'download': 126.2180598793741, 'upload': 9.402075395173725, 'ping': 12.703}
    	data added to file: C:\Users\ewdhe\Desktop\customcsv.csv 
