import time,json, math
from boltiot import Bolt, Sms

API_KEY = "b42f36a3-9e5b-440c-8fa4-c57de4e5c4ca"
DEVIVE_ID = "BOLT3732040"       # SELF NOTE need to change
SSID = 'ACce54c48ff0e1271d7d50012d96ec89a3'
AUTH_TOKEN = 'edaf33cf519a6efe6c8991f8bd397047'
FROM_NUMBER = '+15083926124 '
TO_NUMBER = '+918077423699'
Diameter = 14

Mybolt = Bolt(API_KEY, DEVIVE_ID)
twillioMessage = Sms(SSID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER)

status = Mybolt.isOnline()
print(status)
previousWaterLevel = 0
totalWaterConsumed = 0
criticalConsumption = 15  # Try 1
errorMaxValue = 350


def messageToUser(level='CRITICAL LEVEL'):
    twillioMessage.send_sms("ALERT!!!!!!! \nDear User, " + str(level) + " is crossed. Control excess water usages.")
    print('msg sent')


while True:
    if status:

        response = Mybolt.serialRead('10')
        currentWaterLevel = json.loads(response)
        print(currentWaterLevel)
        if totalWaterConsumed >= criticalConsumption:
            messageToUser(totalWaterConsumed)
            time.sleep(10000)
        elif previousWaterLevel < int(currentWaterLevel['value']) < errorMaxValue:
            totalWaterConsumed = totalWaterConsumed + int(currentWaterLevel['value']) - previousWaterLevel
            previousWaterLevel = int(currentWaterLevel['value'])
        elif int(currentWaterLevel['value']) > errorMaxValue:
            print("Error retrying other loop")
        else:
            previousWaterLevel = currentWaterLevel['value']
    print('total:', totalWaterConsumed, '\nCurrent:', currentWaterLevel['value'], '\nPrevious:', previousWaterLevel)
    time.sleep(3)
