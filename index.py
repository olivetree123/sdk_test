import requests

url1 = "http://127.0.0.1:8080/ListenSdkService/sdk/getDeviceList.php"
url2 = "http://127.0.0.1:8080/ListenSdkService/sdk/lsPublishProgram.fgl"
url3 = "http://127.0.0.1:8080/ListenSdkService/sdk/deviceHeartBeatCallBack.php"


def get_device_list():
    r = requests.get(url1)
    print(r.status_code)
    print(r.text)


def publish_content():
    params = {
        "programId":
        "12",  # 数据类型varchar[32],节目ID，用于标识节目的唯一性（注，要与定时节目清单计划节点的节目ID一致），不同节目，对应的节目ID肯定不同，每个节目都有一个ID值
        "programName":
        "12",  # 数据类型varchar[60] 节目名称（注，要与定时节目清单计划节点的节目名称一致）	
        "pageResolution": [{
            "resolution":
            "1920X1080"  # 数据类型varchar[32],节目分辨率（宽=1920，高=1080），即屏幕的实际分辨率，譬如某LED屏幕分辨率为192*96，那这里就设置为192*96，即宽度为192，高度为96；
        }],
        "playTimesFlag":
        "1",  # 数据类型varchar[1],节目按播放次数播放开关,1标识为关闭，0标识为打开，默认为关闭状态
        "playTimes":
        "0",  # 数据类型varchar[4],节目播放次数（注：使用前提条件是节目播放次数开关打开）
        "page": [  # 节目页面，一个节目包含多个页面，一个页面包含多个区域
            {
                "name": "页面1",  # 数据类型varchar[60],页面名称 
                "pagTime": 10,  # 数据类型int,页面停留时长
                "areaList": {
                    "pageEle": [  # 页面属性集合
                        {
                            "bgImg":
                            "http://image.zxlink.cn/img/20190516/b3a12c48808749c7a176315c62eeaadd.jpg",  # 数据类型 text,页面背景图片,格式为http超链接地址路径（注：务必保证所设地址是有效的http地址,否则，会引起节目播放异常）
                            "bgColor": "#000000",  # 数据类型varchar[8],页面背景颜色
                            "bgName": "页面1",  # 数据类型varchar[60],页面背景图片名称
                            "pageTime": 10,  # 数据类型int,页面停留时长
                            "eqType":
                            "q5"  # 数据类型varchar[10],设备类型，如Q5/x3m/x3/vp1000u/Q4/Q7/X4/H2
                        }
                    ],
                    "mediaEle": [  # 区域属性
                        {
                            "id":
                            5,  # 数据类型int,区域id，在节目页面中的唯一标志，一个节目可以包含多个页面，而每个节目页面可以包含多个相同或不同类型区域，但每个区域ID，在每个页面中必须是唯一的。在不同页面中的区域，其ID是可以相同的
                            "type":
                            2,  # 数据类型int,区域类型，如视频（0）、图片（1）、字幕(2)、天气（3）、时钟(4)、混播(5)、网页(9)、音频(10)、流媒体(12)、交通诱导图(15),地图诱导图(16),倒计时(23)等类型，他们分别用数字0,1,2,3,4,5,9,10,12,15等表示
                            "top":
                            0,  # 数据类型int,Y坐标偏离值
                            "left":
                            0,  # 数据类型int,X坐标偏离值
                            "width":
                            50,  # 数据类型int,区域宽度，不能超过节目分辨率的宽
                            "height":
                            50,  # 数据类型int,区域高度，不能超过节目分辨率的高
                            "zIndex":
                            2,  # 数据类型int,显示的层级顺序
                            "siderType":
                            "0",  # 数据类型vachar[2],字幕特效  0:静止显示  1:向左移动  2:连续左移  3:向右移动  4:连续右移 9:首尾相接
                            "siderDirection":
                            "0",  # 数据类型vachar[2],备用，不需要填数据
                            "pauseTime":
                            "5",  # 数据类型int,停留时间
                            "text":
                            "请输入文字",  # 数据类型vachar[100],字幕内容，预留属性，目前设置内容不生效
                            "fontSize":
                            "48",  # 数据类型vachar[4],字体大小
                            "fontWeight":
                            "bold",  # 数据类型vachar[10],加粗    为空：不加粗，bold:加粗
                            "textDecoration":
                            "",  # 数据类型vachar[20],underline：下划线、line-through：删除线
                            "fontStyle":
                            "",  # 数据类型vachar[10],斜体   为空：不是斜体，italic：斜体
                            "textAlign":
                            "",  # 数据类型vachar[12],文本对齐方式  left:左对齐    center：居中    right：右对齐
                            "fontFamily":
                            "Arial",  # 数据类型vachar[22],字体
                            "fontColor":
                            "#ff0000",  # 数据类型vachar[10],字体颜色
                            "lineHeight":
                            "20",  # 数据类型vachar[4],行高，文本多行显示，设置才会生效
                            "background":
                            "",  # 数据类型int,背景颜色   不填默认为黑色
                            "listType":
                            "",  # 预留字段属性，不需要填数据
                            "textShow":
                            "0",  # 数据类型vachar[1],文本显示方式：0.单行    1.多行
                            "scrollSpeed":
                            "0",  # 数据类型vachar[2],滚动速度  值为1~15，值越大，速度则表示越快
                            "isEdit":
                            False,  # 数据类型bool,预留字段属性，固定值，默认为false
                            "borderSW":
                            0,  # 数据类型int,是否开启边框，0标识为关闭，1标识为打开
                            "borderType":
                            1,  # 数据类型int,边框类型，取值范围为0-9，请参见【灵信云平台二次开发接口文档_V2.1.0.doc】关于区域边框类型说明;
                            "borderEffect":
                            1,  # 数据类型int,边框特技，提供三种选择：0、静止; 1、旋转;  2、闪烁;
                            "borderSpeed":
                            1,  # 数据类型int,边框滚动速度，值越大，速度越快，取值范围为1-15
                            "borderColoreffect":
                            "0",  # 数据类型vachar[1],色彩效果   0：无   1:彩色斜角渐变
                            "textGroup": [  # 文本集合，即可录入多条文本记录，或多个文本文件内容;
                                {
                                    "id": 0,  # 字幕id 数据类型int,
                                    "name": "字幕1",  # 数据类型vachar[60],字幕名称
                                    "text": "请输入文字"  # 数据类型 text,字幕内容
                                },
                                {
                                    "id": 1,  # 数据类型int,字幕id
                                    "name": "字幕2",  # 数据类型vachar[60],字幕名称
                                    "text": "欢迎光临灵信视觉技术股份有限公司"  # 数据类型text,字幕内容
                                }
                            ]
                        }
                    ]
                }
            }
        ],
        "programPlan": [  # 节目清单计划属性
            {
                "defaultPid":
                "",  # 数据类型int,默认节目的ID
                "onlyCut":
                1,  #  数据类型int,是否全部为定时节目，若全为定时节目值为1，否则值为0
                "program": [  # 节目list
                    {
                        "createDate":
                        1605089419000,  # 数据类型long,节目创建时间
                        "date": [  # 节目日程（轮播节目没有日程限制）
                            {
                                "dateEnd": 1553961599000,  # 数据类型long, 截止日期
                                "dateStart": 1553788800000  # 数据类型long, 起始日期
                            }
                        ],
                        "isDefault":
                        0,  # 数据类型int,是否为默认节目，若为默认节目值为1，否则值为0
                        "planWeekDay": [  # 数据类型int,节目的周计划（轮播节目没有周计划）
                            1,  # 数据类型int,周一,1启用、0关闭
                            1,  # 数据类型int,周二,1启用、0关闭
                            1,  # 数据类型int,周三,1启用、0关闭
                            1,  # 数据类型int,周四,1启用、0关闭
                            1,  # 数据类型int,周五,1启用、0关闭
                            1,  # 数据类型int,周六,1启用、0关闭
                            1  # 数据类型int,周日,1启用、0关闭
                        ],
                        "programId":
                        "12",  # 数据类型varchar[32],节目ID
                        "programName":
                        "12",  # 数据类型vachar[60],节目ID
                        "programType":
                        2,  # 数据类型int,节目类型，1：轮播节目；2：定时节目，
                        "time": [  # 节目的时段计划（轮播节目没有时段计划）
                            {
                                "timeEnd": "23:59:59",  # 数据类型varchar[12],截止时间
                                "timeStart": "00:00:00"  # 数据类型varchar[12],起始时间
                            }
                        ],
                        "updateDate":
                        1605089419000  # 数据类型long,节目更新时间
                    }
                ]
            }
        ]
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    r = requests.post(url2,
                      headers=headers,
                      data={
                          "devCode": "123456",
                          "strProgramList": params
                      })
    print(r.status_code)
    print(r.text)


def heart_beat():
    r = requests.post(url2)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    get_device_list()
    publish_content()