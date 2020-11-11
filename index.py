import requests

url1 = "http://127.0.0.1:8080/ListenSdkService/sdk/getDeviceList.php"
url2 = "http://127.0.0.1:8080/ListenSdkService/sdk/lsPublishProgram.fgl"
url3 = "http://127.0.0.1:8080/ListenSdkService/sdk/deviceHeartBeatCallBack.php"


def get_device_list():
    r = requests.get(url1)
    print(r.status_code)
    print(r.text)


def publish_content():
    r = requests.post(url2)
    print(r.status_code)
    print(r.text)


def heart_beat():
    r = requests.post(url2)
    print(r.status_code)
    print(r.text)

if __name__ == "__main__":
    get_device_list()