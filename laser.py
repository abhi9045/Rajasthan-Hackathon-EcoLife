import conf, json, time
from boltiot import Bolt, Sms

API_KEY = "b42f36a3-9e5b-440c-8fa4-c57de4e5c4ca"
DEVIVE_ID = "BOLT3732040"
Mybolt = Bolt(API_KEY, DEVIVE_ID)
SSID = 'ACce54c48ff0e1271d7d50012d96ec89a3'
AUTH_TOKEN = 'edaf33cf519a6efe6c8991f8bd397047'
FROM_NUMBER = '+15083926124 '
TO_NUMBER = '+918077423699'

sms = Sms(SSID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER)

print(json.loads(Mybolt.isOnline())['value'])
while True:
    response = Mybolt.analogRead('A0')
    data = json.loads(response)
    print (data['value'])
    try:
        sensor_value = int(data['value'])
        print(sensor_value)
        if sensor_value < 1020:
            #response = sms.send_sms(" an unwanted access")
            response = Mybolt.digitalWrite('4', 'HIGH')
            break

    except Exception as e:
        print ("error", e)
        time.sleep(10000)