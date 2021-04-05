import mongoengine

class Member (mongoengine.Document):
    account = mongoengine.StringField()
    password = mongoengine.StringField()
    weight = mongoengine.IntField()
    height = mongoengine.IntField()
