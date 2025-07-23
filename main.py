from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from rembg import remove
import io
import uvicorn

app = FastAPI()

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    if file.content_type not in ["image/png", "image/jpeg", "image/jpg", "image/webp"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    input_data = await file.read()
    output_data = remove(input_data)

    return StreamingResponse(io.BytesIO(output_data), media_type="image/png")
