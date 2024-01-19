# This is the response that we will return
from rest_framework.response import Response
# This is the model that we will use
from .models import Note
# This is the serializer that we will use
from .serializers import NoteSerializer
from .serializers import UserSerializer


# This function will return the notes list
def getNotesList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


# This function will return the note detail
def getNoteDetail(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

# def getUsersList(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# This function will create a user
# def createUser(request):
#     data = request.data
#     # Assuming you send 'username', 'password', and other required fields
#     django_user = DjangoUser.objects.create_user(username=data['username'], password=data['password'])
    
#     user = User.objects.create(
#         django_user=django_user,
#         # Add any additional fields as needed
#     )
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)
# This function will create a note
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# This function will update a note
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# This function will delete a note
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')