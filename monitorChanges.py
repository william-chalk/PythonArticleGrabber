import time
import hashlib
from urllib.request import urlopen,Request
from grabContent import dc_enq_scrapper,con_brief_scrapper


def monitor_article():

    url1 = Request("https://conservativebrief.com/", headers={'User-agent': 'Mozilla/5.0'})
    url2 = Request("https://dcenquirer.com/", headers={'User-agent': 'Mozilla/5.0'})



    # to preform a GET request and load the 
    # content of the website and store it in a variable
    response1 = urlopen(url1).read()
    response2 = urlopen(url2).read()

    # to create the initial hash
    currentHash1 = hashlib.sha224(response1).hexdigest()
    currentHash2 = hashlib.sha224(response2).hexdigest()
    print("running")
    time.sleep(20)
    while True:
        try:
            # perform the get request and store it in a var
            response1 = urlopen(url1).read()
            response2 = urlopen(url2).read()
            # create a hash
            currentHash1 = hashlib.sha224(response1).hexdigest()
            currentHash2 = hashlib.sha224(response2).hexdigest()

            # wait for 30 seconds
            time.sleep(50)

            # perform the GET request
            response1 = urlopen(url1).read()
            response2 = urlopen(url2).read()

            # create a new hash
            newHash1 = hashlib.sha224(response1).hexdigest()
            newHash2 = hashlib.sha224(response2).hexdigest()

            # check if new hash is same as the previous hash
            if newHash1 == currentHash1 and newHash2 == currentHash2:
                continue

            # if something changed in the hashes 
            else:
                # notifies
                print("Something was updated")

                # again read the website
                response1 = urlopen(url1).read()
                response2 = urlopen(url2).read()
                # create a hash
                currentHash1 = hashlib.sha224(response1).hexdigest()
                currentHash2 = hashlib.sha224(response2).hexdigest()
                # wait for 30 seconds
                time.sleep(30)
                continue
        # handles exceptions 
        except Exception as e:
            print("err")

monitor_article()