# -*- coding: utf-8 -*- 
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
'''
mysql = MySQL_DAO()

State(name = 'WI',tax_rate = 0.08).save()
State(name = 'NY',tax_rate = 0.12).save()
State(name = 'MN',tax_rate = 0.07).save()

Occupation(name = 'student').save()

mysql.addUser('test', 'test', 1, 'test', 'test', 'test', '1990-05-31', 1, 1, 'test@gmail.com', 6084335509, 'test', 1, '54601')

print State.objects.filter(state__account = 'test')
'''
#print mysql.findUserByAccount('abc')
#print mysql.findUserById(2)
#print mysql.findUserByAccount_Passowrd('test', 'test1')
#print mysql.updateUserProfileById(2, 'test1', 'test1', 'test1', '2004-06-10', 2, 1, 'test1@gmail.com', '000', 'test1', 2, '123123')
#print mysql.updateUserShippingById(1, 'test', 'test', 'test', 3, 'test', 'test')
#print mysql.updateUserCreditById(1, '123', 1, '2014-05-31', '212', 'test', 'test', 'test', 3, 'test')
#print mysql.updateUserPasswordById(1, 'password')
#Genre(name = 'action').save()
#Genre(name = 'Fiction').save()
'''
Movie(title = 'title',\
    year = 'year',\
    director = 'director',\
    actor = 'actor',\
    description = 'description',\
    picture = '',\
    price = 20,\
    quantity = 20,\
    rates = 0).save()
'''
#mysql.findMovieById(1)[0].genre.add(2)
#print mysql.findMovieByTitle('TItle')
#mysql.findMovieById(1)[0].genre.add(2)
#print Genre.objects.filter(movie__title = 'title')
#print mysql.findMovieByTitle_GenreId('title', 1)
#print mysql.updateMovieQuantity(1, 100)
#mysql.addOrderWithShipping_Credit(1, datetime.datetime.utcnow(), 1, 0, 'shipping_to', 'shipping_address', 'shipping_city', 1, 'shipping_zip', 'shipping_phone', 'creidt_number', 2, '2014-05-31', 'creidt_csc', 'creidt_holder', 'creidt_address', 'creidt_city', 2, 'creidt_zip')
#print mysql.updateOrderShipping(2, 'test', 'test', 'test', 3, 'test', 'test')
#print mysql.updateOrderCredit(1, 'test', 2, '1990-05-31', 'test', 'test', 'test', 'test', 1, 'test')
#print mysql.updateOrderSummary(1, 100)
#print mysql.updateOrderStatus(1, 1)
#print mysql.addItem(1, 2, 200, None)
#print mysql.updateItemQuantity(2, 500)
'''
Promotion(code = 'test',\
          begin = datetime.datetime.utcnow(),\
          end = datetime.datetime.utcnow(),\
          discount = 20).save()
'''
#Promotion.objects.filter()[0].movies.add(1)
#print mysql.updateItemPromtion(2, 1)
#print mysql.findItemByOrderId(1)
#print mysql.findItemById(2)
#print mysql.findOrderById(1)
#print mysql.findOrderByUserId(1)
#print mysql.findOrderByUserId_Status(2, 1)
#print mysql.findOrderByItemId(2)
#print mysql.deleteOrder(1)
#print mysql.deleteItem(5)
#print mysql.addRating(1, 1, 5, datetime.datetime.utcnow())
#print mysql.findRatingByUserId_MovieId(1, 1)
#print mysql.updateRatingByUserId_MovieId(1, 1, 1)
#Action(name = 'test', point = 100 ).save()
#print mysql.findActionByName('tedt')
#print mysql.addLog(1, 1, datetime.datetime.utcnow(), 1)
#print mysql.findLogByMovieId(1)
#print mysql.findLogByUserId(1)
#print mysql.deleteLogById(1)
#print mysql.getAllGenre()
#print mysql.getAllOccupation()
#print mysql.getAllState()
#print mysql.findPromtotionByCode_MovieId('test', 1)
'''       
    #Other Module
     getAllState(self):
        
     getAllOccupation(self):
        
     getAllGenre(self):
        
     findPromtotionByCode_MovieId(self,code,movie_id):
'''
##########################
########## Mongo #########
##########################

from datetime import datetime
from email.mime.text import MIMEText
import operator
import os
import random
import re
import smtplib
import threading
import time

from django.core.mail.message import EmailMultiAlternatives
from django.db.models import Q
from mongoengine.connection import disconnect

from shutter.dao import MySQL_DAO, Mongo_DAO
from shutter.models import *
from shutter.service import ACTION_LIST, randomString


mysql = MySQL_DAO()
mongo = Mongo_DAO('Mongo_Shutter')
DAO_Proxy = Mongo_DAO('Mongo_Shutter')

User.objects.create(account = 'superadmin', password = 'password', user_type = 3)
Mongo_User.objects.create(account = 'superadmin', password = 'password', user_type = 3)
#EmailMultiAlternatives('subject','content','movieshutter@gmail.com',['movieshutter@gmail.com','svenchen9005@gmail.com']).send()
#reload price(20) & quantity(100) & rates


'''
Movie.objects.filter().update(price = 20, quantity = 100, rates = 0)
connect('Mongo_Shutter')
Mongo_Movie.objects.filter().update(set__price = 20, set__quantity =100, set__rates = 0)

for m in Movie.objects.filter():
    rates = mysql.findRatingByMovieId(m.id)
    count_rates = 0.0
    for r in rates:
        count_rates += float(r.rates)
    if rates.count() != 0:
        mysql.updateMovieRates(m.id, count_rates/rates.count())

for index, m in enumerate(Mongo_Movie.objects.filter()):
    print index
    rates = mongo.findRatingByMovieId(m.id)
    count_rates = 0.0
    for r in rates:
        count_rates += r.rates
    if rates.count() != 0:
        mongo.updateMovieRates(m.id, count_rates/rates.count())

'''





'''
connect('Mongo_Shutter')
movies = Mongo_Movie.objects.all()
#print movies.count()
for m in movies:
    Mongo_Movie.objects.filter(id = m.id).update(set__picture = '/media/' + m.picture)
'''
'''
for a in ACTION_LIST :
    print a, ACTION_LIST[a], Action.objects.filter(name = a).first()
    #Action(name = a, point = ACTION_LIST[a]).save()

connect('Mongo_Shutter')
for a in ACTION_LIST :
    print a, ACTION_LIST[a], Mongo_Action.objects.filter(name = a).first().point
    #Mongo_Action(name = a, point = ACTION_LIST[a]).save()
'''
#Log(user_id = User.objects.all().first().id, action_id = Action.objects.all().first().id, time = datetime.now(), movie_id = Movie.objects.all().first().id).save()
#DAO_Proxy = MySQL_DAO()
#DAO_Proxy.addLog(User.objects.all().first().id, Action.objects.all().first().id, datetime.now(), Movie.objects.all().first().id)
#print DAO_Proxy.findLogByUserId(User.objects.all().first().id).first().movie.genre.all().first()

#DAO_Proxy = Mongo_DAO('Mongo_Shutter')

#print DAO_Proxy.getAllGenre()
#DAO_Proxy.addLog(Mongo_User.objects.all().first().id, Mongo_Action.objects.all().first().id, datetime.now(), Mongo_Movie.objects.all().first().id)
#print DAO_Proxy.findLogByUserId(Mongo_User.objects.all().first().id).first().action.point

#print Mongo_Movie.objects.all().first().genre[0].name

def mysql_fillMovie():
    for m in Movie.objects.all():
        id = m.id
        list_rates = [float(x['rates']) for x in Rating.objects.filter(movie_id = id).values('rates')]
        rates = sum(list_rates)/len(list_rates) if len(list_rates) else 0
        price = random.randint(19,40)
        quantity = random.randint(19,40)
        points = 0
        picture = '/media/' + m.picture
        print id, rates, price, quantity,points, picture
        Movie.objects.filter(id = id).update(picture = picture, price = price, quantity = quantity, rates = rates ,points = points)

def mongo_fillMovie():
    for m in Mongo_Movie.objects.all():
        id = m.id
        list_rates = [float(x) for x in Mongo_Rating.objects.filter(movie = id).values_list('rates')]
        rates = sum(list_rates)/len(list_rates) if len(list_rates) else 0
        price = random.randint(19,40)
        quantity = random.randint(19,40)
        points = 0
        picture = '/media/' + m.picture
        print id, rates, price, quantity,points, picture
        Mongo_Movie.objects.filter(id = id).update(set__picture = picture, set__price = price, set__quantity = quantity, set__rates = rates ,set__points = points)


####### Log data generation(1M)####
def mysql_action():
    for x,y in ACTION_LIST.items():
        Action.objects.create(name = x, point = y)


def mongo_action():
    for x,y in ACTION_LIST.items():
        Mongo_Action.objects.create(name = x, point = y)


def mysql_log_generator(size, size_chunk ,location):
    movie_id = [ x['id'] for x in Movie.objects.values('id')]
    user_id = [x['id'] for x in User.objects.values('id')]
    action_id = [x['id'] for x in Action.objects.values('id')]

    count = 0
    file = None
    bat_file = file = open(location + 'import.bat','a')
    
    while count != size:
        if count == 0:
            file = open(location + str(count/size_chunk) +'.sql','a')
            bat_file.write('mysql --login-path=local shutter < ' + str(count/size_chunk) + '.sql\n')
            file.write("USE `shutter`;\nINSERT INTO `shutter_log` (user_id, action_id,time,movie_id)\nVALUES")
        elif count == size - 1:
            file.write("\n(" + str(random.choice(user_id)) + "," + str(random.choice(action_id)) + ",'" + str(datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))))  + "'," + str(random.choice(movie_id)) + ");")
            file.close()
        elif count%size_chunk == 0:
            print 'mysql : ',count/(size_chunk-1)
            file.write("\n(" + str(random.choice(user_id)) + "," + str(random.choice(action_id)) + ",'" + str(datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))))  + "'," + str(random.choice(movie_id)) + ");")
            file.close()
            file = open(location + str(count/size_chunk) +'.sql','a')
            bat_file.write('mysql --login-path=local shutter < ' + str(count/size_chunk) + '.sql\n')
            file.write("USE `shutter`;\nINSERT INTO `shutter_log` (user_id, action_id,time,movie_id)\nVALUES")
        else:
            file.write("\n(" + str(random.choice(user_id)) + "," + str(random.choice(action_id)) + ",'" + str(datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))))  + "'," + str(random.choice(movie_id)) + "),")
        count += 1
        
    bat_file.close()
    

    
    
def mongo_log_generator(size, size_chunk, location):
    connect('Mongo_Shutter')
    movie_id = [str(x) for x in Mongo_Movie.objects.values_list('id')]
    user_id = [str(x) for x in Mongo_User.objects.values_list('id')]
    action_id = [str(x) for x in Mongo_Action.objects.values_list('id')]

    count = 0
    bat_file = open(location + 'import.bat','a')
    
    while count != size:
        if count == 0:
            file = open(location + str(count/size_chunk) +'.dat','a')
            bat_file.write('mongoimport -d Mongo_Shutter -c mongo__log ' + str(count/size_chunk) + '.dat\n')
        elif count == size-1:
            file.write("{\"user\" : { \"$oid\" : \"" + str(random.choice(user_id)) + "\" }, \"action\" : { \"$oid\" : \"" + str(random.choice(action_id)) + "\" }, \"time\" : { \"$date\" : \"" + datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))).strftime("%Y-%m-%dT%H:%M:%S.000-0600") + "\" }, \"movie\" : { \"$oid\" : \"" + str(random.choice(movie_id)) + "\" } }\n")        
            file.close()
        elif count%size_chunk == 0:
            print 'mongo : ', count/(size_chunk-1)
            file.write("{\"user\" : { \"$oid\" : \"" + str(random.choice(user_id)) + "\" }, \"action\" : { \"$oid\" : \"" + str(random.choice(action_id)) + "\" }, \"time\" : { \"$date\" : \"" + datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))).strftime("%Y-%m-%dT%H:%M:%S.000-0600") + "\" }, \"movie\" : { \"$oid\" : \"" + str(random.choice(movie_id)) + "\" } }\n")        
            file.close()
            file = open(location + str(count/size_chunk) +'.dat','a')
            bat_file.write('mongoimport -d Mongo_Shutter -c mongo__log ' + str(count/size_chunk) + '.dat\n')
        else:
            file.write("{\"user\" : { \"$oid\" : \"" + str(random.choice(user_id)) + "\" }, \"action\" : { \"$oid\" : \"" + str(random.choice(action_id)) + "\" }, \"time\" : { \"$date\" : \"" + datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))).strftime("%Y-%m-%dT%H:%M:%S.000-0600") + "\" }, \"movie\" : { \"$oid\" : \"" + str(random.choice(movie_id)) + "\" } }\n")        
        
        count += 1
    
    bat_file.close()
    

    
    
'''
print Mongo_User.objects.filter(first='abc')[0].id
print [str(x) for x in Mongo_Log.objects.filter(user='54661aa5b5f5b71e9c605395').values_list('id')]
print [str(x) for x in Mongo_Rating.objects.filter(user='54661aa5b5f5b71e9c605395').values_list('id')]
print [str(x) for x in Mongo_Order.objects.filter(user='54661aa5b5f5b71e9c605395').values_list('id')]
print [str(x) for x in Mongo_Item.objects.filter(order='54661f37b5f5b71e9c6053a7').values_list('id')]
54661aa5b5f5b71e9c605395
['54661abbb5f5b71e9c605396', '54661cc0b5f5b71e9c6053a1', '54661cc1b5f5b71e9c6053a3', '54661f1eb5f5b71e9c6053a4', '54661f20b5f5b71e9c6053a6', '54661f37b5f5b71e9c6053a9']
['54661f20b5f5b71e9c6053a5']
['54661f37b5f5b71e9c6053a7']
['54661f37b5f5b71e9c6053a8']
print Mongo_Log.objects.filter(id__in=['54661abbb5f5b71e9c605396', '54661cc0b5f5b71e9c6053a1', '54661cc1b5f5b71e9c6053a3', '54661f1eb5f5b71e9c6053a4', '54661f20b5f5b71e9c6053a6', '54661f37b5f5b71e9c6053a9'])
print Mongo_Rating.objects.filter(id__in=['54661f20b5f5b71e9c6053a5'])
print Mongo_Order.objects.filter(id__in=['54661f37b5f5b71e9c6053a7'])
print Mongo_Item.objects.filter(id__in=['54661f37b5f5b71e9c6053a8'])
'''
#User.objects.create(account='admin1',password='123456',first='Gong',last='Chen',user_type=0)

'''
id_all = Mongo_Movie.objects.values_list('id')
id_list = []
for id in id_all[0:20]:
    id_list.append(str(id))
print len(id_all)
print len(id_list)
print len(mongo.findMovieNotInList(id_list))
'''
#print Promotion.objects.first().movies.values_list('id')
#print Mongo_Promotion.objects.first().movies
#print mysql.findMovieByTitle('toy').filter(title = 'Toy Story')
#print Mongo_Movie.objects.filter().filter(title__icontains = 'toy').filter(title__icontains = 'toydfds')
'''
user_size = User.objects.all().count()
movie_size = Movie.objects.all().count()
action_size = Action.objects.all().count()
start_date = time.mktime(time.strptime('01 01 13', '%d %m %y'))
end_date = time.mktime(time.strptime('31 05 14', '%d %m %y'))
'''
#print user_size, movie_size, action_size
#print random.randint(0,2)
#print time.mktime(time.strptime('01 01 13', '%d %m %y'))
#print time.mktime(time.strptime('31 05 14', '%d %m %y'))
#print random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))
#print datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y'))))
#Log(user_id = User.objects.all().first().id, action_id = Action.objects.all().first().id, time = datetime.fromtimestamp(time.mktime(time.strptime('01 01 13', '%d %m %y'))), movie_id = Movie.objects.all().first().id).save()

#log genneration
'''
count = 0

while count != 1000:
    Log(user_id = User.objects.all()[random.randint(0,user_size-1)].id, \
        action_id = Action.objects.all()[random.randint(0,action_size-1)].id, \
        time = datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))), \
        movie_id = Movie.objects.all()[random.randint(0,movie_size-1)].id).save()
    if count%10000 == 0:
        print '<<<<<<' , count ,'>>>>>>' 
    count += 1

connect('Mongo_Shutter')
user_size = Mongo_User.objects.count()
movie_size = Mongo_Movie.objects.count()
action_size = Mongo_Action.objects.count()
start_date = time.mktime(time.strptime('01 01 13', '%d %m %y'))
end_date = time.mktime(time.strptime('31 05 14', '%d %m %y'))

print user_size, movie_size, action_size, start_date, end_date

count = 0

while count != 60000:
    Mongo_Log(user = Mongo_User.objects.all()[random.randint(0,user_size-1)].id, \
        action = Mongo_Action.objects.all()[random.randint(0,action_size-1)].id, \
        time = datetime.fromtimestamp(random.randint(time.mktime(time.strptime('01 01 13', '%d %m %y')),time.mktime(time.strptime('31 05 14', '%d %m %y')))), \
        movie = Mongo_Movie.objects.all()[random.randint(0,movie_size-1)].id).save()
    if count%10000 == 0:
        print '<<<<<<' , count ,'>>>>>>' 
    count += 1
'''

'''
Mongo_State(name = 'WI', tax_rate = 0.08).save()
Mongo_State(name = 'MN', tax_rate = 0.09).save()
Mongo_State(name = 'NY', tax_rate = 0.12).save()

Mongo_Occupation(name = 'student').save()
Mongo_Occupation(name = 'businessman').save()
Mongo_Occupation(name = 'teacher').save()
'''
'''
states = Mongo_State.objects.all()
occupations = Mongo_Occupation.objects.all()
genres = Mongo_Genre.objects.all()
movies = Mongo_Movie.objects.all()
promotions = Mongo_Promotion.objects.all()
actions = Mongo_Action.objects.all()

movies = Movie.objects.all()
for m in movies:
    Movie.objects.filter(id = m.id).update(picture = '/media/' + m.picture)
'''

#mongo.addUser('account', 'password', 1, 'first', 'middle', 'last', '1990-05-31', 1, occupations[0].id, 'email@gmail.com', 'phone', 'city', states[0].id, 'zip')
#print mongo.findUserByAccount('account')[0].id
#print mongo.findUserById('539a146db5f5b72108f3b308')
#print mongo.findUserByAccount_Passowrd('account', 'password')
#mongo.updateUserProfileById('539a146db5f5b72108f3b308', 'test', 'test', 'test', '2014-05-20', 2, occupations[1].id, 'test@gmail.com', 'test', 'test', states[1].id, 'test')
#mongo.updateUserShippingById('539a146db5f5b72108f3b308', 'shipping_to', 'shipping_address', 'shipping_city', states[2].id, 'shipping_zip', 'shipping_phone')
#mongo.updateUserCreditById('539a146db5f5b72108f3b308', 'creidt_number', 1, '2015-05-31', 'creidt_csc', 'creidt_holder', 'creidt_address', 'creidt_city', states[0].id, 'creidt_zip')
#mongo.updateUserPasswordById('539a146db5f5b72108f3b308', 'newpassword')
'''
Mongo_Genre(name = 'action').save()
Mongo_Genre(name = 'crime').save()
Mongo_Genre(name = 'drama').save()
Mongo_Genre(name = 'fiction').save()


Mongo_Movie(title = 'title',\
    year = 'year',\
    director = 'director',\
    actor = 'actor',\
    genre = [genres[0]],\
    description = 'description',\
    picture = 'picture',\
    price = 100,\
    quantity = 200,\
    rates = 0,\
    points = 0).save()
'''
#print mongo.findMovieById('539a2934b5f5b7176805a003')[0].genre[0].name\
#print mongo.findMovieByTitle('TIt')[0].genre[0].name
#print mongo.findMovieByGenreId(genres[1].id)
#print mongo.findMovieByTitle_GenreId('tile', genres[1].id)
#mongo.updateMovieQuantity('539a2934b5f5b7176805a003', 500)
'''
mongo.addOrderWithShipping_Credit('539a146db5f5b72108f3b308', datetime.datetime.utcnow(), 1, 0,\
                                   'shipping_to', 'shipping_address', 'shipping_city', states[0].id, 'shipping_zip', 'shipping_phone',\
                                    'creidt_number', 1, '2014-05-31', 'creidt_csc', 'creidt_holder', 'creidt_address', 'creidt_city', states[1].id, 'creidt_zip')
'''
#mongo.updateOrderShipping('539a7e2db5f5b703c8904681', 'test', 'test', 'test', states[2].id, 'test', 'test')
#mongo.updateOrderCredit('539a7e2db5f5b703c8904681', 'test', 2, '2016-05-31', 'test', 'test', 'test', 'test', states[1].id, 'test')
#mongo.updateOrderSummary('539a7e2db5f5b703c8904681', 500)
#mongo.updateOrderStatus('539a7e2db5f5b703c8904681', 5)
#print mongo.findOrderById('539a7e2db5f5b703c8904681')
#print mongo.findOrderByUserId('539a146db5f5b72108f3b308')
#print mongo.findOrderByUserId_Status('539a146db5f5b72108f3b308', 5)
#mongo.addItem(movies[0].id, '539a86d3b5f5b71bf4d41766', 50, None)
#print mongo.findOrderByItemId('539a8283b5f5b71bf4371586')[0].id
#mongo.updateItemQuantity('539a8283b5f5b71bf4371586', 1000)
'''
Mongo_Promotion(
    movies = movies,\
    code = 'test',\
    begin = datetime.datetime.utcnow(),\
    end = datetime.datetime.utcnow(),\
    discount = 20).save()
'''
#mongo.updateItemPromtion('539a8283b5f5b71bf4371586', promotions[0].id)
#print mongo.findItemById('539a8283b5f5b71bf4371586')
#print mongo.findItemByOrderId('539a7e2db5f5b703c8904681')
#mongo.deleteOrder('539a7e2db5f5b703c8904681')
#print Mongo_Item.objects.all()[0].id
#mongo.deleteItem('539a871ab5f5b71b181b6f1c')
#mongo.addRating(movies[0], '539a146db5f5b72108f3b308', 10, datetime.datetime.utcnow())
#print mongo.findRatingByUserId_MovieId('539a146db5f5b72108f3b308', movies[0])
#mongo.updateRatingByUserId_MovieId('539a146db5f5b72108f3b308', movies[0], 500)
'''
Mongo_Action(name = 'login', point = 5).save()
Mongo_Action(name = 'logout', point = 6).save()
Mongo_Action(name = 'search', point = 10).save()
Mongo_Action(name = 'buy', point = 20).save()
'''
#mongo.addLog('539a146db5f5b72108f3b308', actions[0], datetime.datetime.utcnow(), movies[0])
#print mongo.findLogByMovieId(movies[0])
#print mongo.findLogByUserId('539a146db5f5b72108f3b308')
#mongo.deleteLogById(Mongo_Log.objects.all()[0].id)
#print mongo.findMovieLogByUserId('539a146db5f5b72108f3b308')
#print Mongo_Log.objects.filter(movie__exists = 1)
#print Log.objects.filter(movie__isnull = True)
#print mysql.findMovieLogByUserId(1)
#print mongo.getAllGenre()
#print mongo.getAllOccupation()
#print mongo.getAllState()
#Mongo_Promotion.objects.all().update(pull__movies = movies[0].id)
#print mongo.findPromtotionByCode_MovieId('test', movies[1].id)
'''
text = "asfd safsfsa fsf s sfs`3士大夫似的6s565f士大夫士大夫4 f6&^%*丰盛的&(%&Tda fsda safsa\n"
pattern = re.compile(r'[^\x00-\x7F]+')
x = re.sub(r'\n',r'', text)
print x
print text
print x
'''
#pattern = re.compile(r'\w*')
#match = pattern.match('  dshel lo world')
#if match:
#    print match.group()
#print datetime.datetime.utcfromtimestamp(978300760)
#Movie(title = u'\xc9va Ig\xf3', year = 1000).save()
#Mongo_Movie(title = u'\xc9va Ig\xf3', year = '1000').save()
#Mongo_Movie.objects.filter(year = '1000').delete()
#print Mongo_Movie.objects.filter(year = '1000')
#print u'\xc9va Ig\xf3'
'''
Mongo_Rating(movie = Mongo_Movie.objects.first().id,\
             user = Mongo_User.objects.first().id,\
             rates = '5',\
             time = str(datetime.datetime.utcfromtimestamp(978300760))).save()
'''
#print Mongo_Movie.objects.all()[160].title
#for g in Mongo_Movie.objects.all()[160].genre:
#    print g.name
