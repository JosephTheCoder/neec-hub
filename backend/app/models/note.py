from app.database import db
from app.database.model import ModelMixin
import uuid


class Note(ModelMixin, db.Model):
    __tablename__ = "note"

    id = db.Column(db.UUID, default=uuid.uuid1, primary_key=True, nullable=True)

    text = db.Column(db.String(255), nullable=False)

    author = db.Column(db.String(30), nullable=True)

    # harvests = db.relationship("Harvest", backref="farm")
    # products = db.relationship("Product", back_populates="farm")
    # baskets = db.relationship("Basket", backref="farm")

    # producer_id = db.Column(db.UUID, db.ForeignKey('producer.id'))
    # prodcuer = db.relationship("Producer", back_populates="farms")

    def __init__(self, **kwargs):
        if 'text' in kwargs:
            self.text = kwargs.pop('text')
        if 'author' in kwargs:
            self.author = kwargs.pop('author')


    def __repr__(self):
        return '<Author: {}  |  Text: {}>'.format(self.author, self.text)

