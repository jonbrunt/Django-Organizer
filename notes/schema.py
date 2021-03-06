# pylint: disable=E1101
from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note as NoteModel

class Note(DjangoObjectType):
    class Meta:
        model = NoteModel
        # describe the data as a node
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    notes = graphene.List(Note)
    def resolve_notes(self, info):
        user = info.context.user
        if settings.DEBUG:
            return NoteModel.objects.all()
        elif user.is_anonymous:
            return NoteModel.objects.none()
        else:
            return NoteModel.objects.filter(user=user)

# Add a schema and attach a query
schema = graphene.Schema(query=Query)
