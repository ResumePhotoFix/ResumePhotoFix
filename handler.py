import io
import base64
from rembg import remove
from PIL import Image
from runpod import serverless

def handler(job):
    try:
        # Input validation
        if not job.get('input'):
            return {"error": "No input provided"}
            
        image_bytes = base64.b64decode(job['input']['image_bytes'])
        input_image = Image.open(io.BytesIO(image_bytes))
        
        # Process image
        output_image = remove(input_image)
        
        # Prepare output
        output_buffer = io.BytesIO()
        output_image.save(output_buffer, format='PNG')
        
        return {
            "image_bytes": base64.b64encode(output_buffer.getvalue()).decode('utf-8')
        }
        
    except Exception as e:
        return {"error": f"Processing failed: {str(e)}"}

serverless.start({"handler": handler})
