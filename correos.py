import requests
import time
import ccard
import random
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

scrapper = Scrapper(category='ALL', print_err_trace=False)

url = 'https://correeos.whole.delivery/porta/pay.php'
common_resolutions = [(1024,768), (1280,720), (1920,1080), (2560,1440), (360, 640), (480, 640), (720, 1280), (1080, 1920)]

data = scrapper.getProxies()

sent_msgs = 1
while(True):
    tarjeta = ccard.visa()
    caducidad_mes = random.randint(1, 12)
    caducidad_anyo = random.randint(23, 30)
    cvv = random.randint(100, 999)
    i = random.randint(0, len(common_resolutions) - 1)
    rand = random.choice(data.proxies)
    proxies = {'http' : rand.ip + ':' +  rand.port}
    print(proxies)
    form_data = {
        "Sis_Numero_Tarjeta": str(tarjeta),
        "Sis_Caducidad_Tarjeta_Mes": str(caducidad_mes),
        "Sis_Caducidad_Tarjeta_Anno":str(caducidad_anyo),
        "Sis_Tarjeta_CVV2": str(cvv),
        "Sis_Divisa": "",
        "browserJavaEnabled": "false",
        "browserLanguage": "en-US",
        "browserColorDepth": "24",
        "browserScreenHeight": str(common_resolutions[i][0]),
        "browserScreenWidth": str(common_resolutions[i][1]),
        "browserTZ": "0",
        "browserUserAgent": "Mozilla/5.0+(Windows+NT+6.3;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/77.0.3865.90+Safari/537.36",
        "threeDSCompInd": "U",
        "bcancel": ""
    }
    try:
        res = requests.post(url, data = form_data, timeout=2.50, proxies=proxies)
        print(f"Proxy {proxies}")
        print(f"Sending {tarjeta} - {caducidad_mes}/{caducidad_anyo} - {cvv} - {common_resolutions[i][0]}x{common_resolutions[i][1]}")
        print(f"response {res}")
        print(f"sent messages: {sent_msgs}")
        sent_msgs += 1
    except:
        print("Timeout Error")
    time.sleep(1)
