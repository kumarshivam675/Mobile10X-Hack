import urllib2
import json
import sys

#pnr = 4627941857
def PNR(pnr):
    ans = ""
    base = "http://api.railwayapi.com/pnr_status/pnr/"
    pnr_val = str(pnr)
    apikey = "/apikey/icoyi9743"
    url = base+pnr_val+apikey
    response = urllib2.urlopen(url)
    data = json.load(response)
    print url
    ans += "date of journey : " + data["doj"] + "\n"
    ans += "Total passengers : " + str(data["total_passengers"]) + "\n"
    passengers = data["total_passengers"]
    for i in range(0, passengers):
        ans += "booking status :" + str(data["passengers"][i]["current_status"])
    return ans


#waypoints(sys.argv[1])
