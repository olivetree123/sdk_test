import json
import requests

from params.text import params as text_params
from params.image import params as image_params
from params.video import params as video_params

url1 = "http://127.0.0.1:8080/ListenSdkService/sdk/getDeviceList.php"
url2 = "http://127.0.0.1:8080/ListenSdkService/sdk/lsPublishProgram.fgl"
url3 = "http://127.0.0.1:8080/ListenSdkService/sdk/deviceHeartBeatCallBack.php"


def get_device_list():
    r = requests.get(url1)
    print(r.status_code)
    print(r.text)


def publish(params):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    r = requests.post(url2,
                      headers=headers,
                      data={
                          "devCode": "123456",
                          "strProgramList": json.dumps(params)
                      })
    print(r.status_code)
    print(r.text)


def publish_content():
    publish(text_params)


def publish_image():
    publish(image_params)


def publish_video():
    publish(video_params)


def heart_beat():
    r = requests.post(url2)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    get_device_list()
    publish_content()
    # publish_image()
    # publish_video()