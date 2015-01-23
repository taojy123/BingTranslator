
import urllib.request
import urllib.parse
import traceback
import time


while True:
    
    try:
        word = input("Pleace enter the English:")
        if not word:
            break

        word = word.replace(" ", "+")
        t = str(int(time.time()))

        url1 = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?appId=%22TCR6j4j9EuF76bMl9y7f_op8-9pcTEepYsCyYqRbW4i4*%22&texts=%5B%22" + word + "%22%5D&from=%22en%22&to=%22zh-CHS%22&options=%7B%7D&onerror=onError_23&_=" + t
        url2 = "http://www.microsofttranslator.com/dictionary.ashx?from=en&to=zh-CHS&text=" + word + "&_=" + t

        r1 = urllib.request.urlopen(url1).read()
        r2 = urllib.request.urlopen(url2).read()

        r1 = str(r1.decode("utf8").replace('\ufeff', ''))
        r2 = str(r2.decode("utf8"))

        r1 = eval(r1)
        text = r1[0]["TranslatedText"]
        # text = text.decode("utf8")


        r2 = r2.replace('(decodeURIComponent("', "").replace('"));', "")
        dictionary = urllib.parse.unquote(r2)
        dictionary = dictionary.replace('<span class="dictB">', "").replace('</span>', "").replace('<br />', "\n")
        # dictionary = dictionary.decode("utf8")

        print(text)
        print()
        print(dictionary)
        print("------------------------------------")

    except:
        traceback.print_exc()


print("Bye!")

