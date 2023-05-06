#!/usr/bin/env python3
import os

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
PARENT_FOLDER_PATH = os.path.dirname(FOLDER_PATH)

def gatherProxies():

    # Create a set to store all the proxies
    proxies = set()

    # Loop through all the files in the proxies folder
    try:
        print("Collecting Proxies from proxies folder...")
        for filename in os.listdir(f'{FOLDER_PATH}/proxies'):
            # Check if the file is a text file
            if filename.endswith('.txt'):
                # Open the file and read its contents
                with open(os.path.join(f'{FOLDER_PATH}/proxies', filename), 'r') as file:
                    # Loop through each line in the file and add the proxy to the set
                    for line in file:
                        proxies.add(line.strip())
    except:
        print("Proxies folder not created")
        exit()

    # Open the existing all_proxies.txt file and load its contents into the set
    try:
        with open(f'{PARENT_FOLDER_PATH}/allProxies.txt', 'r') as file:
            for line in file:
                proxies.add(line.strip())
    except:
        pass

    # Write all the proxies in the set to the all_proxies.txt file
    print(f'Writing {len(proxies)} proxies to file...')
    with open(f'{PARENT_FOLDER_PATH}/allProxies.txt', 'w') as file:
        for proxy in proxies:
            file.write(proxy + '\n')

    print("Done!")

if __name__ == '__main__':
    gatherProxies()