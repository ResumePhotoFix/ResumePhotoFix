import requests
import base64

# Replace with your actual endpoint ID
ENDPOINT_URL = "https://api.runpod.ai/v2/YOUR_ENDPOINT_ID_HERE/runsync"

# Load test image
with open("test.jpg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

payload = {
    "input": {
        "image_base64": image_data
    }
}

res = requests.post(ENDPOINT_URL, json=payload, headers={"Authorization": "YOUR_API_KEY"})
print(res.json())
