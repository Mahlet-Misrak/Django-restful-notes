# from django.shortcuts import render
# from django.http import JsonResponse

# def getNotes(request):
#     # Replace this with your actual logic to fetch and return notes
#     notes = [{'title': 'Note 1', 'content': 'This is the content of Note 1'},
#              {'title': 'Note 2', 'content': 'This is the content of Note 2'}]

#     return JsonResponse({'notes': notes})
# # views.py

from django.shortcuts import render
from .models import Note
from django.http import JsonResponse
from django.contrib.auth.models import User as DjangoUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import NoteSerializer
import json
@api_view(['POST'])
@permission_classes([AllowAny])
def createNote(request):
    print(request.data)  # Check the data being received
    data = request.data
    serializer = NoteSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        print(serializer.errors)  # Check the errors in the console or logs
        return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response({'get_notes': serializer.data})

@api_view(['DELETE'])
@permission_classes([AllowAny]) 
# change to isauthenticated
def delete_note(request, note_id):
    if request.method == 'DELETE':
        note = Note.objects.filter(id=note_id).first()
        if note:
            note.delete()
            return Response({"message": f"Note with ID {note_id} has been deleted."}, status=200)
        else:
            return Response({"message": f"Note with ID {note_id} does not exist."}, status=404)
    else:
        return Response({"message": "Only DELETE method is allowed for this endpoint."}, status=405)