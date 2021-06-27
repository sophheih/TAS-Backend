import mongoengine
from mongoengine.fields import StringField

class Member (mongoengine.Document):
    account = mongoengine.StringField()
    password = mongoengine.StringField()
    weight = mongoengine.IntField()
    height = mongoengine.IntField()
    timestamp = mongoengine.IntField()
    
    # data = mongoengine.DictField()
    # add dish model

class dish (mongoengine.Document):
    Name = mongoengine.StringField() # name has to be the same as the string in serializer
    Calories = mongoengine.IntField()
    Total_Fat = mongoengine.FloatField()    
    Cholesterol = mongoengine.IntField() 
    Sodium = mongoengine.IntField()
    Total_Carbs = mongoengine.IntField()
    Protein = mongoengine.IntField()
    Index = mongoengine.IntField()
    Timestamp = mongoengine.IntField()

class data(mongoengine.Document): # member's daily nutrition data
    Member_id = mongoengine.StringField()
    Timestamp = mongoengine.IntField()
    Calories = mongoengine.IntField()
    Total_Fat = mongoengine.FloatField()    
    Cholesterol = mongoengine.IntField() 
    Sodium = mongoengine.IntField()
    Total_Carbs = mongoengine.IntField()
    Protein = mongoengine.IntField()

class dailyMenu(mongoengine.Document):
    Date = mongoengine.DateTimeField()
    RestName = mongoengine.StringField()
    Main = mongoengine.ListField(StringField())
    Side = mongoengine.ListField(StringField())
    Fruit = mongoengine.ListField(StringField())

class constantMenu(mongoengine.Document):
    
    dailyCarbs = mongoengine.ListField(StringField())
    drinks = mongoengine.ListField(StringField())
    saladBar = mongoengine.ListField(StringField())
    pizzaBar = mongoengine.ListField(StringField())
    snackBarPastries = mongoengine.ListField(StringField())
    snackBarCookies = mongoengine.ListField(StringField())
    snackBarOther = mongoengine.ListField(StringField())
    snackBarDesserts = mongoengine.ListField(StringField())
    snackBarPies = mongoengine.ListField(StringField())
    snackBarMisc = mongoengine.ListField(StringField())



