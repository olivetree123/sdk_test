import json
import requests

# text1 是轮播节目，text2是定时节目
from params.text2 import params as text_params
from params.image import params as image_params
from params.video import params as video_params
from params.mixed import params as mixed_params
from params.html import params as html_params
from params.html2 import params as html2_params
from params.schedule import params as schedule_params

url1 = "http://10.104.82.20:8080/ListenSdkService/sdk/getDeviceList.php"
url2 = "http://10.104.82.20:8080/ListenSdkService/sdk/lsPublishProgram.fgl"
url3 = "http://10.104.82.20:8080/ListenSdkService/sdk/deviceHeartBeatCallBack.php"


def get_device_list():
    r = requests.get(url1)
    print(r.status_code)
    print(r.text)


def publish(params):
    print(params)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    r = requests.post(url2,
                      headers=headers,
                      data={
                          "devCode": "QC202101080005",
                          "strProgramList": json.dumps(params)
                      })
    print(r.status_code)
    print(r.text)


def publish_content():
    publish(text_params)


def publish_image():
    publish(image_params)

def publish_html():
    publish(html2_params)

def publish_video():
    publish(video_params)


def publish_mixed():
    publish(mixed_params)


def publish_schedule_task():
    publish(schedule_params)


def heart_beat():
    r = requests.post(url2)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    get_device_list()
    # publish_content()
    publish_image()
    # publish_video()
    # publish_mixed()
    # publish_html()
    # publish_schedule_task()
