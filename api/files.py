from fastapi import Request, UploadFile, APIRouter
from fastapi.responses import FileResponse
import os
from helpers import create_zip_obj

router = APIRouter()
base_path = r'P:\Ismayil Bashirli\Elvin Bashirli\DOPS'


@router.post("/upload/{id}")
async def upload_post(id: str, files: list[UploadFile]):
 if len(files) == 0:
  return 'No file'
 path = os.path.join(base_path, id)
 os.makedirs(path, exist_ok=True)
 for file in files:
  dest =  f'{base_path}\\{id}\\{file.filename}'
  with open(dest, "wb+") as file_object:
   file_object.write(file.file.read())   
 return 'Done'

@router.post('/download')
async def download_post(request: Request):
 zip_obj = create_zip_obj()
 jsn = await request.json()
 ids = jsn['ids']
 if (len(ids) == 0):
  zip_obj.close()
  return 'Error: ids is empty'
 else:
  folders = os.listdir(os.path.join(base_path))
  # no_id_list = list(set(ids) - set(folders))
  for id in ids:
   if id in folders:
    files = os.listdir(os.path.join(base_path, id))
    for file in files:
     zip_obj.write(f'{base_path}\\{id}\\{file}',file)
   else:
    continue 
 return 'Done'

@router.get('/download')
async def download_get():
 zip_name = 'files.zip'
 return FileResponse(zip_name, filename=zip_name, media_type='application/zip')