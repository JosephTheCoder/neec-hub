from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.note import Note as NoteModel
import graphene
from datetime import datetime
from app.database import db
from graphql_utils import input_to_dictionary


# Create a generic class to mutualize description of category attributes for both queries and mutations
class NoteAttribute:
    text = graphene.String(description="Name of the note.")
    author = graphene.String(description="Author of the note.")
 

class Note(SQLAlchemyObjectType, NoteAttribute):
    """Note node."""

    class Meta:
        model = NoteModel
        interfaces = (graphene.relay.Node,)


class CreateNoteInput(graphene.InputObjectType, NoteAttribute):
    """Arguments to create a note."""
    pass


class CreateNote(graphene.Mutation):
    """Mutation to create a note."""
    note = graphene.Field(lambda: Note, description="Note created by this mutation.")

    class Arguments:
        input = CreateNoteInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()

        note = NoteModel(**data)
        db.session.add(note)
        db.session.commit()

        return CreateNote(note=note)


class UpdateNoteInput(graphene.InputObjectType, NoteAttribute):
    """Arguments to update a note."""
    id = graphene.ID(required=True, description="Global Id of the note.")


class UpdateNote(graphene.Mutation):
    """Update a note."""
    note = graphene.Field(lambda: Note, description="Note updated by this mutation.")

    class Arguments:
        input = UpdateNoteInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['updated_at'] = datetime.utcnow()

        note = db.session.query(NoteModel).filter_by(id=data['id'])
        note.update(data)
        db.session.commit()
        note = db.session.query(NoteModel).filter_by(id=data['id']).first()

        return UpdateNote(note=note)


class DeleteNoteInput(graphene.InputObjectType, NoteAttribute):
    """Arguments to delete a note."""
    id = graphene.ID(required=True, description="Global Id of the note.")


class DeleteNote(graphene.Mutation):
    """Delete a note."""
    note = graphene.Field(lambda: Note, description="Note deleted by this mutation.")

    class Arguments:
        input = DeleteNoteInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['updated_at'] = datetime.utcnow()

        note = db.session.query(NoteModel).filter_by(id=data['id']).first()

        db.session.delete(note)
        db.session.commit()
        
        return "Sucessfully deleted"