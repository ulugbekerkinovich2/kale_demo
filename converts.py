import base64
import os
import time

# decoded_data = base64.b64decode(strs)
#
# with open("new.svg", "wb") as f:
#     f.write(decoded_data)

import requests

username = 'kaleapi'
password = 'kaleapi'
url = 'http://94.158.52.249/Base/hs/info/stocks/'
url_img = 'http://94.158.52.249/Base/hs/info/foto?code=000007'
response = requests.get(url, auth=(username, password))
json_data = response.json()
data = json_data['Товары']
for item in data:
    nomi = item['Наименование']
    kod = item['Код']
    print(nomi)
    print(kod)
    time.sleep(1)
    url = f'http://94.158.52.249/Base/hs/info/foto?code={kod}'
    response_img = requests.get(url, auth=(username, password))
    img_code = response_img.json()['Фото']
    try:
        decoded_data = base64.b64decode(kod)
        file_path = f"media/images_webp/_{nomi}_{kod}.webp"
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(decoded_data)
                # time.sleep(3)
    except:
        padding_chars = (4 - len(img_code) % 4) % 4

        # Add padding characters to the base64-encoded string
        img_code += "=" * padding_chars

        decoded_data = base64.b64decode(img_code)

        with open(f"media/images_webp/__{nomi}_{kod}.webp", "wb") as f:
            f.write(decoded_data)
            # time.sleep(2)
    finally:
        print('topilmadi')
        continue
