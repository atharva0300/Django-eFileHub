from rest_framework import serializers
# importing serializers 

# importing Folder, Files model 
from .models import Folder , Files

# importing shutil to get the make_archive function 
# to create a zip file
import shutil


# creating a file serializer 
class FileSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Files
        fields = '__all__'

# creating a custom serializer
class FileListSerializer(serializers.Serializer) : 
    # creating a field -> file
    files = serializers.ListField(
        child = serializers.FileField(max_length = 1000 , allow_empty_file = False , use_url = False )
        )
    # allowing empty file to false
    # if anyone tries to come via the url -> False 

    # creating a field for the folder 
    folder = serializers.CharField(required = False)

    # file zipper function 
    def zip_files(self , folder) : 
        shutil.make_archive(f"public/static/zip/{folder}"  , 'zip', f'public/static/{folder}')

    def create(self , validated_data) : 
        folder = Folder.objects.create()
        # creating a folder

        files = validated_data.pop('files')
        # getting the value with the key files 

        # creating an empty array for the files objects 
        filesObjArray = []

        for file in files : 
            filesObj = Files.objects.create(folder = folder , file = file )

            # serializing the data 
            filesObjArray.append(filesObj)
        

        # zipping the file 
        # calling the zip_files function
        self.zip_files(folder.uid)

        return {'files' : {} , 'folder' : str(folder.uid)}
