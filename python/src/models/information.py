import sys
sys.path.append('/src')

from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, Integer, Float, String, DateTime
from models.settings import Base, DATABASE_ENGINE

from flask_marshmallow.fields import fields
# Use flask_marshmallow
from flask_marshmallow import Marshmallow
ma = Marshmallow()

class Information(Base):
    """
    Information model
    """

    def __init__(self, x, y, image_url, info):
        self.x = x
        self.y = y
        self.image_url = image_url,
        self.info = info

    __tablename__ = 'informations'
    
    id = Column('id', 
                Integer, 
                primary_key=True, 
                autoincrement=True, 
                nullable=False
        )
    x = Column('x',
               Float,
               nullable=False
        )
    y = Column('y',
               Float,
               nullable=False
        )
    image_url = Column('image_url',
                       String(200),
                       nullable=False
                )
    info = Column('info',
                  String(200),
                  nullable=False
           )
    created_at = Column('created_at',
                        DateTime,
                        nullable=False,
                        server_default=current_timestamp()
                 )

class InformationSchema(ma.ModelSchema):
    class Meta:
        model = Information
    
    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')

def main(args):
    Base.metadata.create_all(bind=DATABASE_ENGINE)

if __name__ == '__main__':
    main(sys.argv)
