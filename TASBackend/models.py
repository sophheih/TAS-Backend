import mongoengine

class Member (mongoengine.Document):
    account = mongoengine.StringField()
    password = mongoengine.StringField()
    weight = mongoengine.IntField()
    height = mongoengine.IntField()
    # add dish model

class Dish (mongoengine.Document):
    dishName = mongoengine.StringField()
    totalcal = mongoengine.IntField()
    totalfat = mongoengine.IntField()    
    cholesterol = mongoengine.IntField() 
    sodium = mongoengine.IntField()
    totalCarbs = mongoengine.IntField()
    protein = mongoengine.IntField()