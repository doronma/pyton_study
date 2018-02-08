import pytz
import datetime

utc_time = datetime.datetime.utcnow()
print("UTC Time {}".format(utc_time))
aware_local_time = pytz.utc.localize(utc_time).astimezone()
print ("Native time aware {} time zone {}".format(aware_local_time,aware_local_time.tzinfo))
