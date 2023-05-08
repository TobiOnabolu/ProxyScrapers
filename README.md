# ProxyScrapers

Ensemble of proxy scrapers gathered from other repos that I have modified to pool a list of proxies into one text file.

## Current List of Proxies Being Used
* [proxy-scraper-checker](https://github.com/monosans/proxy-scraper-checker) - Referenced as LongWaitScraper (takes several minutes to finish scraping)
* [proxy-scraper](https://github.com/iw4p/proxy-scraper) - Referenced as ShortWaitScraper (takes 2 seconds to scrape)
  *  Note that this scraper also had a proxy checker functionality that I referenced as ProxyChecker

## Installation
* Fork and clone the repo onto your computer.
* From the command line cd into root project folder and use this command to install dependencies. ```bash pip3 install -r requirements.txt ```

## Usage
* Each scraper/checker has a seperate command to run them. I have not made 1 command to run all of them at once because it easier to run them seperately depending on the use case, i.e. not having to wait a long time for the LongWaitScraper
* Each Scraper outputs their list of proxies to the ```bash allProxies.txt``` file. This file contents is saved to a set before overwriting so the proxy list continues to grow and has no duplicates.

## LongWaitScraper Usage
* From the command line cd into the LongWaitScraper folder. 
* On Windows run ```bash ./start.cmd ```
* On Mac run ```bash ./start.sh ```
* These commands will install anything needed if it wasn't installed already, and runs the scraper to start collecting proxies.

###  Modifications to LongWaitScraper 
* ```bash gatherProxies.py ``` has been added to grab all proxies that the scraper produced and put them in the parent directory into a file named ```bash allProxies.txt ```
* The start command has an extra final step of calling ```bash gatherProxies.py ``` after scraper has produced all proxies

## ShortWaitScraper Usage
* From the command line cd into the ShortWaitScraper folder. 
* Run ```bash python3 proxyScraper.py -v ```
* This will run the scraper to start collecting proxies

###  Modifications to ShortWaitScraper 
* -p option on the command has been modified to run all options simultaneously, so we can collect all http, https, and socks proxies. It has also been made the default option.
* -o option default has become the parent folder directory's allProxies.txt file
* Visit the original repo attached above for more information on the options.

## ProxyChecker
* From the command line cd into the ProxyChecker folder. 
* Run ```bash python3 proxyChecker.py -v -s buyee.jp -t 3```
* This will run the checker to check all proxies in ```bash allProxies.txt ``` against a website and output the working ones to ```bash workingProxies.txt  ```

###  Modifications to ProxyChecker 
* Seperated input and output files so that it reads a list of proxies from an input file and output the working proxies to a seperate output file
* -l option has been changed to -i for input list and it's default has become the parent folder directory's allProxies.txt file 
* -o option has been added to change the path of the output file for working proxies. Default is the parent folder directory's workingProxies.txt file 
* Visit the original repo attached above for more information on the options.
