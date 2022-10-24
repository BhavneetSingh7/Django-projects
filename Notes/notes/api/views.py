from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from notes.api.serializers import NoteSerializer
from notes.models import Note, ApiToken

# @api_view(['GET',])
# def get_notes(request,API_TOKEN):
#     notes = Note.objects.all()
#     serializer = NoteSerializer(notes,many=True)
#     return Response(serializer.data)

@api_view(['GET',])
@login_required(login_url='notes:login')
def get_notes_list(request,API_TOKEN):
    notes_api_user = ApiToken.objects.get(key=API_TOKEN).user
    notes = Note.objects.filter(user=notes_api_user)
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)