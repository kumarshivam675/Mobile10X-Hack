import csv


def complaintLodge(lat, long, url, caption):
    hello = [[lat,long,url,caption]]

    print lat, long, url, caption
    with open('complaint.csv', 'a') as testfile:
        csv_writer = csv.writer(testfile)
        csv_writer.writerow(hello[0])
