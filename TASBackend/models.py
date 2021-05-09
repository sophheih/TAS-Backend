import mongoengine

class Member (mongoengine.Document):
    account = mongoengine.StringField()
    password = mongoengine.StringField()
    weight = mongoengine.IntField()
    height = mongoengine.IntField()
    # add dish model

class dish (mongoengine.Document):
    Name = mongoengine.StringField() # name has to be the same as the string in serializer
    Calories = mongoengine.IntField()
    Total_Fat = mongoengine.IntField()    
    Cholesterol = mongoengine.IntField() 
    Sodium = mongoengine.IntField()
    Total_Carbs = mongoengine.IntField()
    Protein = mongoengine.IntField()