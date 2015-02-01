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

        # url1 是英文翻译的接口地址,替换其中的关键词
        url1 = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?appId=%22TLQKtq6xnM98ue2rH8ybmnBViK162aQhgn1NGrCPCT3MhGCm8XZuSjjwOeVEjQzgj%22&texts=%5B%22" + word + "%22%5D&from=%22en%22&to=%22zh-CHS%22&options=%7B%7D&onerror=onError_23&_=" + t
        # url2 是词典翻译的接口地址,替换其中的关键词
        url2 = "http://www.microsofttranslator.com/dictionary.ashx?from=en&to=zh-CHS&text=" + word + "&_=" + t
        # url1 和 url2 都是通过分析在网页上每一次翻译时的网络数据请求得知的

        # 打开 url1 和 url2 网址, 得到对应的结果
        r1 = urllib.request.urlopen(url1).read()
        r2 = urllib.request.urlopen(url2).read()

        # 处理一下结果, 因为中文是utf8编码的, 所以要转一下码, 并替换到开头的干扰字符 
        r1 = str(r1.decode("utf8").replace('\ufeff', ''))
        r2 = str(r2.decode("utf8"))

        # eval函数用于将字符串转换为相应的python对象, 这里是一个list
        r1 = eval(r1)
        # 对应的翻译结果在r1对象的第一个元素(一个dict)的TranslatedText键值
        text = r1[0]["TranslatedText"]

        # 处理r2, 删除开头和结尾的干扰字符
        r2 = r2.replace('(decodeURIComponent("', "").replace('"));', "")
        # 用 unquote 函数还原url编码为真实字符
        dictionary = urllib.parse.unquote(r2)
        # 再处理一下, 删掉不必要的html标记
        dictionary = dictionary.replace('<span class="dictB">', "").replace('</span>', "").replace('<br />', "\n")

        # 打印结果
        print(text)
        print()
        print(dictionary)
        print("------------------------------------")

    except:
        # 遇到错误的话, 就打印错误信息
        traceback.print_exc()


print("Bye!")

