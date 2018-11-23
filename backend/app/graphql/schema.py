from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_note

 
class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()

    note = graphene.relay.Node.Field(schema_note.Note)
    noteList = SQLAlchemyConnectionField(schema_note.Note)


class Mutation(graphene.ObjectType):
    createNote = schema_note.CreateNote.Field()
    updateNote = schema_note.UpdateNote.Field()
    deleteNote = schema_note.DeleteNote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)