# handler.py 
from PIL import Image
import base64
from io import BytesIO

def handler(event):
    try:
        # Load base64 image from input
        image_b64 = event["input"].get("image_base64")
        if not image_b64:
            return {"error": "Missing 'image_base64' in input."}

        image_bytes = base64.b64decode(image_b64)
        image = Image.open(BytesIO(image_bytes)).convert("RGBA")

        # Simple background remover: make all white pixels transparent
        datas = image.getdata()
        newData = []
        for item in datas:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))  # Transparent
            else:
                newData.append(item)
        image.putdata(newData)

        # Convert output image to base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        output_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return {"output_base64": output_b64}

    except Exception as e:
        return {"error": str(e)}
