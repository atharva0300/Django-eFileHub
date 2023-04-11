from django.shortcuts import render

# importing api views 
from rest_framework.views import APIView
from rest_framework.response import Response


# importing response 
from rest_framework.response import Response

# importing the API view
from rest_framework.views import APIView

from .serializers import FileListSerializer


def home(request) : 
    return render(request , 'home.html') 


def download(request , uid ): 
    print('uid : ' , uid )
    return render(request , 'download.html' , context = {'uid' : uid})

# Create your views here.
class HandleFileUpload(APIView) :

    def post(self , request ) : 
        try : 
            data = request.data

            print("data : " , data)

            # serialize the data 
            serializer = FileListSerializer(data = data)
            # passing the data to the data paramter

            print("serializer : " , serializer)

            if serializer.is_valid() : 
                serializer.save() 
                # saving the serizliazer in the database 

                print("serializer is valid")
                return Response(
                    {
                    'status' : 200,
                    'message' : 'files uploaded successfully',
                    'data' : serializer.data
                    }

                    # serializer.data -> gives the data response data of the serializer 
                )


            # if not valid 
            print("serializer is not valid")
            print(serializer.errors)
            return Response({
                'status' : 400,
                'message' : 'Something went wrong'
            })
        

        except Exception as e : 
            # if failed
            print(e)
