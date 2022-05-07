from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import FileResponse
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
import shutil

import os
from helpers import create_zip_obj

base_path = r'P:\Ismayil Bashirli\Elvin Bashirli\DOPS'

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post("/upload/{id}")
async def upload(id: str, files: list[UploadFile], folder: str | None = None):
  if len(files) == 0:
    return 'No file'
  path = os.path.join(base_path, id)

  if folder:
    path = os.path.join(path, folder)
  
  os.makedirs(path, exist_ok=True)

  if folder:
    dest =  f'{base_path}\\{id}\\{folder}\\'
  else:
    dest =  f'{base_path}\\{id}\\'
  
  for file in files:
    file_dest = dest + file.filename
    with open(file_dest, "wb+") as file_object:
        file_object.write(file.file.read())
    
  return 'Done'

@app.post('/download')
async def download_post(request: Request, folder: str | None = None):
  zip_obj = create_zip_obj()
  jsn = await request.json()
  ids = jsn['ids']
  if (len(ids) == 0):
    zip_obj.close()
    return 'Error: ids is empty'
  else:
    folders = os.listdir(os.path.join(base_path))
    for id in ids:
      if id in folders:
        if folder:
          end_folder_path = os.path.join(base_path, id, folder)
        else:
          end_folder_path = os.path.join(base_path, id)
        shutil.make_archive('files', 'zip', end_folder_path)
        
      else:
        continue 
  return 'Done'

@app.get('/download')
async def download_get():
  zip_name = 'files.zip'
  return FileResponse(zip_name, filename=zip_name, media_type='application/zip')

@app.get('/download/{id}/{name}')
async def download_get_file(id, name, folder: str | None = None):
  if folder:
    file_path = base_path + '\\' + id + '\\' + folder + '\\' + name
  else:
    file_path = base_path + '\\' + id + '\\' + name
  
  _, file_extension = os.path.splitext(name)
  return FileResponse(file_path, filename=name, media_type=f'application/{file_extension}')

if __name__ == '__main__':
  run("main:app", host="0.0.0.0", port=5000, reload=True)