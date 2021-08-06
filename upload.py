from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post('/upload')
async def upload(file: UploadFile = File(...)):
    contents = await file.read(100)
    print(contents.decode('utf-8'))
    return {'filename': file.filename, 'content_type': file.content_type}
