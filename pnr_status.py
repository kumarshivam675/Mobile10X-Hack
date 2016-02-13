import urllib2
import json
import sys

#pnr = 4627941857
def waypoints(pnr):
    base = "http://api.railwayapi.com/pnr_status/pnr/"
    pnr_val = str(pnr)
    apikey = "/apikey/icoyi9743"
    url = base+pnr_val+apikey
    response = urllib2.urlopen(url)
    data = json.load(response)
    print url
    print "date of journey : " + data["doj"]
    print "total passengers : " + str(data["total_passengers"])
    passengers = data["total_passengers"]
    for i in range(0, passengers):
        print "booking status :" + str(data["passengers"][i]["current_status"])


waypoints(sys.argv[1])
