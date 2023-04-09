from django.db import models

import uuid
import os
# importing uuid

# Create your models here.


# creating a class for folder 
class Folder(models.Model) : 
    # a uid ( a unique id )
    uid = models.UUIDField(primary_key=True , editable=False , default = uuid.uuid4)
    # treating it as a primary key 
    # making it not editable
    created_at = models.DateTimeField(auto_now=True)


    # creating a dynamic function 
def get_upload_path(instance , filename ) :
    # we are created a random, where all the files will be stored and zipped
    return os.path.join(str(instance.folder.uuid , filename))

class Files(models.Model) :
    folder = models.ForeignKey(Folder , on_delete = models.CASCADE)

    file = models.FileField(upload_to=get_upload_path)
    # upload to is the path where the file will be stored
    # we want it to be dynamically created
    # the get_upload_path function will create a fucntion to generate the file path

    created_at = models.DateTimeField(auto_now=True)
