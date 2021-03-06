import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import json
# Replace <Subscription Key> with your valid subscription key.
# You can check your key with the url: https://azure.microsoft.com/en-us/try/cognitive-services/my-apis/
subscription_key = "c2625dbf28bc4b9ab0595ea26637a5d1"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://japaneast.api.cognitive.microsoft.com/vision/v1.0/"

analyze_url = vision_base_url + "analyze"

# Set image_url to the URL of an image that you want to analyze.
#image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + \
#    "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

# image_url = "http://inews.gtimg.com/newsapp_bt/0/5011199284/641" # remote image

image_path = "/Users/zhangjiwang/PycharmProjects/AI-Learning/testAzureVisionAPI/test3.jpg"

image_data = open(image_path, "rb").read()

headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}

params = {'visualFeatures': 'Categories,Description,Color'}

response = requests.post(analyze_url, headers=headers, params = params, data=image_data)

response.raise_for_status()
#
# headers = {'Ocp-Apim-Subscription-Key': subscription_key }
# params  = {'visualFeatures': 'Categories,Description,Color'}
# data    = {'url': image_url}
# response = requests.post(analyze_url, headers=headers, params=params, json=data)
# response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(json.dumps(analysis, indent=4))
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1, color='blue')

plt.show()