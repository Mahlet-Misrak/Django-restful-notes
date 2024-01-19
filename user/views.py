# views.py (inside the user app)
from django.http import JsonResponse
from django.contrib.auth.models import User as DjangoUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserSerializer

# This function will return the users list
@api_view(['GET'])
@permission_classes([AllowAny])
def getUsersList(request):
    users = UserProfile.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({'get_users': serializer.data})
# This function will create a user
@api_view(['POST'])
@permission_classes([AllowAny])
# @csrf_exempt
def createUser(request):
    print(request.data)  # Check the data being received
    data = request.data
    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        print(serializer.errors)  # Check the errors in the console or logs
        return Response(serializer.errors, status=400)
    
@api_view(['DELETE'])
@permission_classes([AllowAny]) 
# change to isauthenticated
def delete_user(request, user_id):
    if request.method == 'DELETE':
        user = UserProfile.objects.filter(id=user_id).first()
        if user:
            user.delete()
            return Response({"message": f"User with ID {user_id} has been deleted."}, status=200)
        else:
            return Response({"message": f"User with ID {user_id} does not exist."}, status=404)
    else:
        return Response({"message": "Only DELETE method is allowed for this endpoint."}, status=405)