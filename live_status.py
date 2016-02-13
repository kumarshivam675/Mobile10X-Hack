import urllib2
import json
import sys


# pnr = 4627941857
def live_status(train, date_val):
    # base = http://api.railwayapi.com/live/train/22351/doj/20160212/apikey/yourapikey/
    ans = ""
    base = "http://api.railwayapi.com/live/train/"
    pnr_val = str(train)
    date = "/doj/" + str(date_val)
    apikey = "/apikey/icoyi9743"
    url = base + pnr_val + date + apikey
    response = urllib2.urlopen(url)
    data = json.load(response)
    # print url
    # print data["position"].split(" ")[-2]
    location = data["position"]
    print "hello ", location
    time = data["position"].split(" ")[-2]
    # print location
    value = divmod(int(time), 60)
    # ans += location
    # print location
    ans += location + " "
    # print value
    in_hrs = str(value[0]) + " hrs" + " and " + str(value[1]) + " mins"
    ans += in_hrs
    print ans
    return ans
    # print data["position"].split(" ")[-2]

# live_status(sys.argv[1], sys.argv[2])
