import os
import shutil

source=r"C:\Users\meeth\Downloads"

image_folder=os.path.join(source,"image")
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

Videos_folder=os.path.join(source,'videos')
if not os.path.exists(Videos_folder):
    os.makedirs(Videos_folder)

documents_folder=os.path.join(source,'documents')
if not os.path.exists(documents_folder):
    os.makedirs(documents_folder)

codes_folder=os.path.join(source,'codes')
if not os.path.exists(codes_folder):
    os.makedirs(codes_folder)

Pdfs_folder=os.path.join(source,'Pdfs')
if not os.path.exists(Pdfs_folder):
    os.makedirs(Pdfs_folder)

Archive_folder=os.path.join(source,'Archives')
if not os.path.exists(Archive_folder):
    os.makedirs(Archive_folder)

for files_name in os.listdir(source):
    file_path=os.path.join(source,files_name)

    if os.path.isdir(file_path):
        continue

    if files_name.endswith(('.jpg','.png')):
        shutil.move(file_path,image_folder)
        

    if files_name.endswith((".mp4",".mkv",".mov")):
        shutil.move(file_path,Videos_folder)
       

    if files_name.endswith(('.docx', '.txt', '.xlsx', '.csv')):
        shutil.move(file_path,documents_folder)
    
    if files_name.endswith(('.py', '.html', '.css', '.js')):
        shutil.move(file_path,codes_folder)
       

    if files_name.endswith(('.pdf')):
        shutil.move(file_path,Pdfs_folder)
       

    if files_name.endswith(('.zip', '.rar', '.7z')):
        shutil.move(file_path,Archive_folder)
        

        