from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 
from base.models import User
from .serializers import UserSerializer




@api_view(['GET'])
def get_Users(request):
    Users=User.objects.all()
    serializer=UserSerializer(Users,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_User(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def userDetail(request,pk):
    try:
       user=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   