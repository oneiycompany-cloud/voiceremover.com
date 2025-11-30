from fastapi import FastAPI, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from demucs_utils import run_demucs
from auth import user_is_active
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-vocals")
async def remove_vocals(
    customer_id: str = Form(...),
    file: UploadFile = Form(...)
):

    if not user_is_active(customer_id):
        raise HTTPException(status_code=403, detail="Suscripción no activa")

    file_path = f"uploads/{file.filename}"
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        vocals, instrumental, file_id = run_demucs(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando audio: {e}")

    return {
        "file_id": file_id,
        "vocals_url": f"/download/{file_id}/vocals",
        "instrumental_url": f"/download/{file_id}/instrumental",
    }
