import urllib2
import json
import sys

#pnr = 4627941857
def waypoints(train, date_val):
    #base = http://api.railwayapi.com/live/train/22351/doj/20160212/apikey/icoyi9743/
    base = "http://api.railwayapi.com/live/train/"
    pnr_val = str(train)
    date = "/doj/" + str(date_val)
    apikey = "/apikey/icoyi9743"
    url = base+pnr_val+date+apikey
    response = urllib2.urlopen(url)
    data = json.load(response)
    print url
    #print data["position"].split(" ")[-2]
    location = data["position"]
    time = data["position"].split(" ")[-2]
    #print location
    value = divmod(int(time), 60)
    print location
    print value
    print str(value[0])+" hrs"+" and "+str(value[1])+" mins"
    #print data["position"].split(" ")[-2]

waypoints(sys.argv[1], sys.argv[2])
