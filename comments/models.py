from mongoengine import Document, StringField, DateTimeField
import datetime

class Comment(Document):
    name = StringField(max_length=100, required=True)
    content = StringField(max_length=200, required=True)
    published_date = DateTimeField(default=datetime.datetime.now)
    meta = {
        'ordering': ['-published_date']
    }
    
    def __repr__(self):
        return "%s By %s" %(self.content, self.name)
