from django import forms
from django.db import models
from mongoengine import *

############################################
################ MySQL Model ###############
############################################
class State(models.Model):
    name = models.CharField(max_length = 45, unique = True)
    tax_rate = models.FloatField()
    
    def __unicode__(self):
        return self.name + '_' + str(self.tax_rate)

class Occupation(models.Model):
    name = models.CharField(max_length = 45, unique = True)
    
    def __unicode__(self):
        return self.name 


class User(models.Model):
    account = models.CharField(max_length = 45, unique = True)
    password = models.CharField(max_length = 45)
    # 0 : Admin ; 1 : Customer; 
    user_type = models.IntegerField()
    
    first = models.CharField(max_length = 45,blank =True, null = True)
    middle = models.CharField(max_length = 45, blank =True, null = True)
    last = models.CharField(max_length = 45,blank =True, null = True)
    birthday = models.DateField(blank =True, null = True)
    gender = models.IntegerField(max_length = 10, blank =True, null = True)
    occupation = models.ForeignKey(Occupation, blank =True, null = True)
    email = models.EmailField(max_length = 45,blank =True, null = True)
    phone = models.CharField(max_length = 45,blank =True, null = True)
    city = models.CharField(max_length = 45,blank =True, null = True)
    state = models.ForeignKey(State, blank =True, null = True, related_name='state')
    zip = models.CharField(max_length = 45,blank =True, null = True)
    
    shipping_to =models.CharField(max_length = 45,blank =True, null = True)
    shipping_address = models.CharField(max_length = 255,blank =True, null = True)
    shipping_city = models.CharField(max_length = 45,blank =True, null = True)
    shipping_state = models.ForeignKey(State,blank =True, null = True,related_name='shipping_state')
    shipping_zip = models.CharField(max_length = 45,blank =True, null = True)
    shipping_phone = models.CharField(max_length = 45,blank =True, null = True)
    
    creidt_number = models.CharField(max_length = 45,blank =True, null = True)
    creidt_type = models.IntegerField(blank =True, null = True)
    creidt_expire = models.DateField(blank =True, null = True)
    creidt_csc = models.CharField(max_length = 10,blank =True, null = True)
    creidt_holder = models.CharField(max_length = 45,blank =True, null = True)
    creidt_address = models.CharField(max_length = 255,blank =True, null = True)
    creidt_city = models.CharField(max_length = 45,blank =True, null = True)
    creidt_state = models.ForeignKey(State,blank =True, null = True,related_name='creidt_state')
    creidt_zip = models.CharField(max_length = 45,blank =True, null = True)
    
    def __unicode__(self):
        return self.account


class Genre(models.Model):
    name = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length = 200)
    year = models.CharField(max_length = 20,blank = True,null = True)
    director = models.CharField(max_length = 45,blank = True,null=True)
    actor = models.CharField(max_length = 80,blank = True,null=True)
    genre = models.ManyToManyField(Genre,blank = True,null=True)
    description = models.TextField(max_length = 255,blank = True,null=True)
    picture = models.CharField(max_length = 200)
    #picture = models.ImageField(upload_to = 'images/',blank =True, null = True)
    price = models.FloatField(blank = True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    rates = models.FloatField(blank=True,null=True)
    points = models.IntegerField(blank=True,null=True)
    
    class Meta:
        unique_together = ('title', 'year')
    
    def __unicode__(self):
        return self.title + '_' + self.year

class Promotion(models.Model):
    movies = models.ManyToManyField(Movie,blank =True, null = True)
    code = models.CharField(max_length = 45,unique = True)
    begin = models.DateField(blank = True,null = True)
    end = models.DateField(blank = True,null = True)
    discount = models.FloatField(blank =True, null = True)
    
    def __unicode_(self):
        return self.code

class Rating(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    rates = models.CharField(max_length = 45)
    time = models.DateTimeField()
    
    def __unicode__(self):
        return self.movie.title + '_' + self.user.account

class Order(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField()
    status = models.IntegerField(blank = True, null = True)
    sum = models.CharField(max_length = 45,blank = True, null = True)
    
    shipping_to =models.CharField(max_length = 45,blank =True, null = True)
    shipping_address = models.CharField(max_length = 255,blank =True, null = True)
    shipping_city = models.CharField(max_length = 45,blank =True, null = True)
    shipping_state = models.ForeignKey(State,blank =True, null = True,related_name='order_shipping_state')
    shipping_zip = models.CharField(max_length = 45,blank =True, null = True)
    shipping_phone = models.CharField(max_length = 45,blank =True, null = True)
    
    creidt_number = models.CharField(max_length = 45,blank =True, null = True)
    creidt_type = models.IntegerField(blank =True, null = True)
    creidt_expire = models.DateField(blank =True, null = True)
    creidt_csc = models.CharField(max_length = 10,blank =True, null = True)
    creidt_holder = models.CharField(max_length = 45,blank =True, null = True)
    creidt_address = models.CharField(max_length = 255,blank =True, null = True)
    creidt_city = models.CharField(max_length = 45,blank =True, null = True)
    creidt_state = models.ForeignKey(State,blank =True, null = True,related_name='order_creidt_state')
    creidt_zip = models.CharField(max_length = 45,blank =True, null = True)
    
    def __unicode__(self):
        return self.user.account + ' ' + unicode(self.time)
    
class Item(models.Model):
    movie = models.ForeignKey(Movie)
    order = models.ForeignKey(Order)
    quantity = models.IntegerField()
    promotion = models.ForeignKey(Promotion, blank = True, null =True)
    
    def __unicode__(self):
        return  str(self.order.id) + ' ' + self.movie.title + '_' + self.movie.year
    
class Action(models.Model):
    name = models.CharField(max_length = 45, unique = True)
    point = models.IntegerField(blank =True, null = True)
    
    def __unicode__(self):
        return self.name + '_' + unicode(self.point)
        
class Log(models.Model):
    user = models.ForeignKey(User)
    action = models.ForeignKey(Action)
    time = models.DateTimeField()
    movie = models.ForeignKey(Movie,blank = True, null =True)
    
    def __unicode__(self):
        return self.user.account + '_' + self.action.name + " " + unicode(self.time)

############################################
################ Mongo Model ###############
############################################
class Mongo_State(Document):
    name = StringField()
    tax_rate = FloatField()


class Mongo_Occupation(Document):
    name = StringField()

class Mongo_User(Document):
    account = StringField()
    password = StringField()
    # 0 : Admin ; 1 : Customer; 
    user_type = IntField()
    
    first = StringField()
    middle = StringField()
    last = StringField()
    birthday = DateTimeField()
    gender = IntField()
    occupation = ReferenceField(Mongo_Occupation)
    email = EmailField()
    phone = StringField()
    city = StringField()
    state = ReferenceField(Mongo_State)
    zip = StringField()
    
    shipping_to = StringField()
    shipping_address = StringField()
    shipping_city = StringField()
    shipping_state = ReferenceField(Mongo_State)
    shipping_zip = StringField()
    shipping_phone = StringField()
    
    creidt_number = StringField()
    creidt_type = IntField()
    creidt_expire = DateTimeField()
    creidt_csc = StringField()
    creidt_holder = StringField()
    creidt_address = StringField()
    creidt_city = StringField()
    creidt_state = ReferenceField(Mongo_State)
    creidt_zip = StringField()


class Mongo_Genre(Document):
    name = StringField()
    
    def __unicode__(self):
        return self.name
    
class Mongo_Movie(Document):
    title = StringField()
    year = StringField()
    director = StringField()
    actor = StringField()
    genre = ListField(ReferenceField(Mongo_Genre,reverse_delete_rule=PULL))
    description = StringField()
    picture = StringField()
    price = FloatField()
    quantity = IntField()
    rates = FloatField()
    points = LongField()

class Mongo_Promotion(Document):
    movies = ListField(ReferenceField(Mongo_Movie,reverse_delete_rule=PULL))
    code = StringField()
    begin = DateTimeField()
    end = DateTimeField()
    discount = IntField()

class Mongo_Rating(Document):
    movie = ReferenceField(Mongo_Movie,reverse_delete_rule=CASCADE)
    user = ReferenceField(Mongo_User,reverse_delete_rule=CASCADE)
    rates = IntField()
    time = DateTimeField()

class Mongo_Order(Document):
    user = ReferenceField(Mongo_User,reverse_delete_rule=CASCADE)
    time = DateTimeField()
    status = IntField()
    sum = FloatField()
    
    shipping_to = StringField()
    shipping_address = StringField()
    shipping_city = StringField()
    shipping_state = ReferenceField(Mongo_State)
    shipping_zip = StringField()
    shipping_phone = StringField()
    
    creidt_number = StringField()
    creidt_type = IntField()
    creidt_expire = DateTimeField()
    creidt_csc = StringField()
    creidt_holder = StringField()
    creidt_address = StringField()
    creidt_city = StringField()
    creidt_state = ReferenceField(Mongo_State)
    creidt_zip = StringField()

class Mongo_Item(Document):
    movie = ReferenceField(Mongo_Movie,reverse_delete_rule=CASCADE)
    order = ReferenceField(Mongo_Order,reverse_delete_rule=CASCADE)
    quantity = IntField()
    promotion = ReferenceField(Mongo_Promotion,reverse_delete_rule=CASCADE)
    
class Mongo_Action(Document):
    name = StringField()
    point = IntField()
        
class Mongo_Log(Document):
    user = ReferenceField(Mongo_User,reverse_delete_rule=CASCADE)
    action = ReferenceField(Mongo_Action,reverse_delete_rule=CASCADE)
    time = DateTimeField()
    movie = ReferenceField(Mongo_Movie,reverse_delete_rule=CASCADE)
