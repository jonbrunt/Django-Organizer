# pylint: disable=E1101
from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        note = Note.objects.create(user=user, **validated_data)
        return note
        
    class Meta:
        model = Note
        fields = ('title', 'content')
    
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()