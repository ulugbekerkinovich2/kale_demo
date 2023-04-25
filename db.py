# import base64
import time
import requests
import os
import base64
base641 = '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\r\nGxxRtDWMaMBoAwABzADmXoCwshGKmUIQoQ//2Q=='


decoded_data = base64.b64decode(base641)
#
with open("new12d2s.svg", "wb") as f:
    f.write(decoded_data)

# username = 'kaleapi'
# password = 'kaleapi'
# url = 'http://94.158.52.249/Base/hs/info/stocks/'
# url_img = 'http://94.158.52.249/Base/hs/info/foto?code=000007'
# response = requests.get(url, auth=(username, password))
# json_data = response.json()
# data = json_data['Товары']
# for item in data:
#     nomi = item['Наименование']
#     kod = item['Код']
#     print(nomi)
#     print(kod)
#     time.sleep(1)
#     url = f'http://94.158.52.249/Base/hs/info/foto?code={kod}'
#     response_img = requests.get(url, auth=(username, password))
#     img_code = response_img.json()['Фото']
#     try:
#         decoded_data = base64.b64decode(kod)
#         file_path = f"media/KALE_IMAGES/_{nomi}.svg"
#         if not os.path.exists(file_path):
#             with open(file_path, "wb") as f:
#                 f.write(decoded_data)
#     except:
#         print('rasm yoq')
