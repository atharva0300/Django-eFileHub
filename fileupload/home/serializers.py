from rest_framework import serializers
# importing serializers 

# importing Folder, Files model 
from .models import Folder , Files

# creating a custom serializer
class FileListSerializer(serializers.Serializer) : 
    # creating a field -> file
    files = serializers.ListField(
        child = serializers.FileField(max_length = 1000 , allow_empty_file = False , use_url = False)
        )
    # allowing empty file to false
    # if anyone tries to come via the url -> False 

    # creating a field for the folder 
    folder = serializers.CharField(required = False)

    def create(self , validated_data) : 
        folder = Folder.objects.create()
        # creating a folder

        files = validated_data.pop('files')
        # getting the value with the key files 

        # creating an empty array for the files objects 
        files_objs = []

        for file in files : 
            files_obj = Files.object.create(folder = folder , file = file )

            # serializing the data 
            files_objs.append(files_obj)

        return {'files' : {} , 'folder' : str(folder.uid)}
