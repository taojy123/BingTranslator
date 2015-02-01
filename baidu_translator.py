#coding=utf8
import urllib.request
import urllib.parse
import traceback
import time


while True:
    
    try:
        # 接收用户输入的单词
        word = input("Pleace enter the English:")
        if not word:
            break

        # 为了在url中使用,空格替换为+号
        word = word.replace(" ", "+")
        t = str(int(time.time()))

        # 百度翻译接口
        url = "http://fanyi.baidu.com/v2transapi?from=en&to=zh&transtype=realtime&simple_means_flag=3&query=" + word

        # 打开网址, 得到对应的结果
        r1 = urllib.request.urlopen(url).read()

        # 处理一下结果, 因为中文是utf8编码的, 所以要转一下码, 并替换到开头的干扰字符 
        r1 = str(r1.decode("utf8").replace('\ufeff', '').replace('null', 'None'))

        # eval函数用于将字符串转换为相应的python对象, 这里是一个list
        r1 = eval(r1)
        # 对应的翻译结果在r1对象的第一个元素(一个dict)的TranslatedText键值
        text = r1["trans_result"]["data"][0]["dst"]

        # 打印结果
        print(text)
        print("------------------------------------")

    except:
        # 遇到错误的话, 就打印错误信息
        traceback.print_exc()


print("Bye!")

