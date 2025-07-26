import io
import base64
from rembg import remove
from PIL import Image
from runpod import serverless

def handler(job):
    """ Handler function that will process the job """
    try:
        job_input = job['input']
        
        # Handle base64 encoded input
        if 'image_bytes' in job_input:
            image_bytes = base64.b64decode(job_input['image_bytes'])
            input_image = Image.open(io.BytesIO(image_bytes))
        else:
            return {"error": "Please provide 'image_bytes' with base64 encoded image"}

        # Process image
        output_image = remove(input_image)
        
        # Prepare output
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')
        
        # Return base64 if requested
        if job_input.get('return_bytes', False):
            return {
                "image_bytes": base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
            }
        return {
            "image_bytes": img_byte_arr.getvalue(),
            "message": "Background removed successfully"
        }
        
    except Exception as e:
        return {"error": str(e)}

serverless.start({"handler": handler})
