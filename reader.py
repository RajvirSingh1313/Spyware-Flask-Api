import requests
import base64

r = requests.get(API_ENDPOINT,
                 auth=(API_USERNAME, API_PASSWORD))

with open('lastest_img.bin','w') as b:
    b.write(r.json()["data"][-1][0])


file = open('lastest_img.bin', 'rb')
byte = file.read()
file.close()

decodeit = open('lastest_image.jpeg', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()
