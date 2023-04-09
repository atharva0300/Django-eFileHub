from django.shortcuts import render

# importing api views 
from rest_framework.views import APIView
from rest_framework.response import Response


# importing response 
from rest_framework.response import Response

# importing the API view
from rest_framework.views import APIView

from .serializers import FileListSerializer

# Create your views here.
class HandleFileUpload(APIView) :
    def post(self , request ) : 
        try : 
            data = request.data

            # serialize the data 
            serializer = FileListSerializer(data = data)
            # passing the data to the data paramter

            if serializer.is_valid() : 
                serializer.save() 
                # saving the serizliazer in the database 

                return Response(
                    {
                    'status' : 200,
                    'message' : 'files uploaded successfully'
                    }
                )


            # if not valid 
            return Response({
                'status' : 400,
                'message' : 'Something went wrong'
            })
        

        except Exception as e : 
            # if failed
            print(e)
