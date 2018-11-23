import uuid
from datetime import datetime
from flask_sqlalchemy import event, SessionBase
from app.database import db
# from app import logger

from sqlalchemy.ext.declarative import DeclarativeMeta
from uuid import UUID
import json


class ModelMixin(object):
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)


    def reload(self):
        db.session.refresh(self)

    def save(self):
        db.session.commit()

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
        return None

    def update(self, **kwargs):
        try:
            db.session.query(self.__class__).filter_by(uuid=self.uuid).update(kwargs)
            db.session.commit()
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
        return self

    def to_dict(self, rel=None, backref=None):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                value = getattr(self, attr)
                if value is None:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref=self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref=self.__table__)
                                         for i in value]
        return res     

    def to_json(self, rel=None):
        def extended_encoder(x):
            if isinstance(x, datetime):
                return x.isoformat()
            if isinstance(x, UUID):
                return str(x)
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        return json.dumps(self.to_dict(rel), default=extended_encoder)