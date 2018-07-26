from flask import Flask, render_template
from time import sleep
import conf, json
from boltiot import Bolt, Sms
from threading import Thread


app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('sign-in.html')


@app.route('/Elife')
def main():
    try:
        t = Thread(target=security)
        t.start()
    except Exception as err:
        print('Login failed with exception: ', str(err))
    return render_template('Ecolife.html')


def security():
    def laser():
        API_KEY = "d1c0747d-cf58-4b22-b97a-cfae6ba9ae2e"
        DEVIVE_ID = "BOLT7487042"
        Mybolt = Bolt(API_KEY, DEVIVE_ID)
        sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

        print(json.loads(Mybolt.isOnline())['value'])
        while True:
            response = Mybolt.analogRead('A0')
            data = json.loads(response)
            print(data['value'])
            try:
                sensor_value = int(data['value'])
                print(sensor_value)
                if sensor_value < 1020:
                    #response = sms.send_sms(" an unwanted access")
                    response = Mybolt.digitalWrite('4', 'HIGH')
                    sleep(0)

                else:
                   response = Mybolt.digitalWrite('4', 'LOW')

            except Exception as e:
                print("error", e)
                sleep(10000)
    laser()


if __name__ == '__main__':
    app.run(debug=True)
