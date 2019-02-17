import os
import sys
import lnetatmo
from shyft.api import StringVector, UtcPeriod, TimeAxis, TimeSeries, POINT_INSTANT_VALUE, TsVector, TsInfoVector, TsInfo

if not 'WEATHER_AUTH' in os.environ:
    raise EnvironmentError('Cannot find path to app authentication codes.')

sys.path.append(os.environ['WEATHER_AUTH'])

from authentication import CLIENT_ID, CLIENT_SECRET, USER, PASSWORD

auth = lnetatmo.ClientAuth(clientId=CLIENT_ID, clientSecret=CLIENT_SECRET, username=USER, password=PASSWORD,
                           scope='read_station')

devices = lnetatmo.DeviceList(auth)


class NetatmoCallbacks:
    schema = 'netatmo'

    def __init__(self, username: str, password: str, client_id: str, client_secret: str) -> None:
        self.auth = lnetatmo.ClientAuth(clientId=client_id, clientSecret=client_secret, username=username, password=password,
                                        scope='read_station')
        pass

    def read_callback(self, ts_ids: StringVector, read_period: UtcPeriod) -> TsVector:
        pass

    def find(self, query: str) -> TsInfoVector:
        pass


# !/usr/bin/python
# coding=utf-8

# 2013-01 : philippelt@users.sourceforge.net

# This is an example of graphing Temperature and Humidity from a module on the last 3 days
# The Matplotlib library is used and should be installed before running this sample program

import datetime, time

from matplotlib import pyplot as plt
from matplotlib import dates
from matplotlib.ticker import FormatStrFormatter

# Access to the sensors
auth = lnetatmo.ClientAuth()
dev = lnetatmo.DeviceList(auth)

# Time of information collection : 3*24hours windows to now
now = time.time()
start = now - 3 * 24 * 3600

# Get Temperature and Humidity with GETMEASURE web service (1 sample every 30min)
resp = dev.getMeasure(device_id='xxxx',  # Replace with your values
                      module_id='xxxx',  # "      "    "    "
                      scale="30min",
                      mtype="Temperature,Humidity",
                      date_begin=start,
                      date_end=now)

# Extract the timestamp, temperature and humidity from the more complex response structure
result = [(int(k), v[0], v[1]) for k, v in resp['body'].items()]
# Sort samples by timestamps (Warning, they are NOT sorted by default)
result.sort()
# Split in 3 lists for use with Matplotlib (timestamp on x, temperature and humidity on two y axis)
xval, ytemp, yhum = zip(*result)

# Convert the x axis values from Netatmo timestamp to matplotlib timestamp...
xval = [dates.date2num(datetime.datetime.fromtimestamp(x)) for x in xval]

# Build the two curves graph (check Matplotlib documentation for details)
fig = plt.figure()
plt.xticks(rotation='vertical')

graph1 = fig.add_subplot(111)

graph1.plot(xval, ytemp, color='r', linewidth=3)
graph1.set_ylabel(u'Température', color='r')
graph1.set_ylim(0, 25)
graph1.yaxis.grid(color='gray', linestyle='dashed')
for t in graph1.get_yticklabels(): t.set_color('r')
graph1.yaxis.set_major_formatter(FormatStrFormatter(u'%2.0f °C'))

graph2 = graph1.twinx()

graph2.plot(xval, yhum, color='b', linewidth=3)
graph2.set_ylabel(u'Humidité', color='b')
graph2.set_ylim(50, 100)
for t in graph2.get_yticklabels(): t.set_color('b')
graph2.yaxis.set_major_formatter(FormatStrFormatter(u'%2i %%'))

graph1.xaxis.set_major_locator(dates.HourLocator(interval=6))
graph1.xaxis.set_minor_locator(dates.HourLocator())
graph1.xaxis.set_major_formatter(dates.DateFormatter("%d-%Hh"))
graph1.xaxis.grid(color='gray')
graph1.set_xlabel(u'Jour et heure de la journée')

# X display the resulting graph (you could generate a PDF/PNG/... in place of display).
# The display provides a minimal interface that notably allows you to save your graph
plt.show()
