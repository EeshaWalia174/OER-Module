
import schedule
import time
import cdsapi
from datetime import datetime,timedelta

c = cdsapi.Client()
def job():
    print("I'm executing in 10 every second ...")
    c = cdsapi.Client()
    now = datetime.now()

    # newdate = now + timedelta(year=1)
    newdate = datetime.now() - timedelta(days=365)  # To get one year old date

    day = newdate.strftime("%d")  # to get day
    #print(day)
    year = newdate.strftime("%y")  # to get year
    years = str("20" + str(year))  # to add 20 before (21) in year because we are getting 21 from year and we need 2021

    sixmonthlater = datetime.now() + timedelta(
        days=180)  # to get 6 month later month i.e december month it is dynamic it will chanage

    month = int(sixmonthlater.strftime("%m"))

    #print(years, month, day)
# below this is api code from webpage
    res = c.retrieve(
        'efas-forecast',
        {
            'format': 'grib',
            'originating_centre': 'ecmwf',
            'variable': 'river_discharge_in_the_last_6_hours',
            'product_type': 'control_forecast',
            'model_levels': 'surface_level',
            'year': str(years),
            'month': str(month),
            'day': str(day),
            'time': '00:00',
            'leadtime_hour': '216',
        },
        'download.grib')
    #print("res", type(str(res)))
    result = str(res)               #converting res to string
    newvar = result[68:-1]          #getting url present in specific line


    print(len(result))
    import urllib.request
    filename = '/Users/eeshaahluwalia/flooddata/1.grib'  # replace old grib file
    urllib.request.urlretrieve(newvar, filename)
    print('data saved successfully!!')


schedule.every(10).seconds.do(job)   # to run every 10 second
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)                      #uncomment this to run every monday
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# schedule.every().day.at("09:00").do(job,'It is 09:00')

while True:
    schedule.run_pending()
    time.sleep(1)






