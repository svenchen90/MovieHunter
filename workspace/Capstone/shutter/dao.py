from shutter.constant import datasource
from shutter.models import *


#####################################
########### DAO Interface ###########
#####################################
class DAO():
    #User Module
    def addUser(self,account,password,user_type,first,middle,last,birthday,gender,occupation_id,email,phone,city,state_id,zip):
        return
    def findUserByAccount(self,account):
        return 
    def findUserById(self,id):
        return
    def findUserByAccount_Passowrd(self,account,password):
        return
    def updateUserProfileById(self,id,first,middle,last,birthday,gender,occupation_id,email,phone,city,state_id,zip):
        return
    def updateUserShippingById(self,id,shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone):
        return
    def updateUserCreditById(self,id,creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        return
    def updateUserPasswordById(self,id,password):
        return
    def findUserByAccount_First_Last_Birthday_Email_Phone(self,account,first,last,birthday,email,phone):
        return
    
    #Movie Module
    def findMovieInSetByTitle_GenreId(self,movie_set,title,genre_id):
        return
    def findMovieWithPromotion(self,promotion_id):
        return
    def findMovieInList(self,id_list):
        return
    def findMovieNotInList(self,id_list):
        return
    def findMovieById(self,id):
        return
    def findMovieByTitle(self,title):
        return
    def findMovieByGenreId(self,genre_id):
        return
    def findMovieByTitle_GenreId(self,title,genre_id):
        return
    def updateMovieQuantity(self,id,quantity):
        return
    def updateMovieRates(self,id,rates):
        return
    def getMovieOrderByRate(self):
        return
    def getMovie_RatesGTE(self,rates):
        return
    def addMovie(self,title,year,director,actor,description,picture,price,quantity,rates,genre_id_list):
        return
    def deleteMovie(self, movie_id):
        return
    def updateMovieById(self,id,title,year,director,actor,description,picture,price,quantity,genre_id_list):
        return
    def deleteMovieById(self,id):
        return
    
    #Order Module
    def addOrderWithShipping_Credit(self,user_id,time,status,sum,\
        shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone,\
        creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        return
    def updateOrderShipping(self,id,shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone):
        return
    def updateOrderCredit(self,id,creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        return
    def updateOrderSummary(self,id,sum):
        return
    def updateOrderStatus(self,id,status):
        return
    def deleteOrder(self,id):
        return
    def findOrderById(self,id):
        return
    def findOrderByUserId(self,user_id):
        return
    def findOrderByUserId_Status(self,user_id,status):
        return
    def findOrderByItemId(self,item_id):
        return
    def findOrderByAccount_Status(self,account,status):
        return
    
    #Item Module
    def addItem(self,movie_id,order_id,quantity,promotion_id):
        return
    def updateItemQuantity(self,id, quantity):
        return
    def updateItemPromtion(self,id, promotion_id):
        return
    def deleteItem(self,id):
        return
    def findItemById(self,id):
        return
    def findItemByOrderId(self,order_id):
        return
    def findItemByOrderId_MovieID(self,order_id,movie_id):
        return
    
    #Rating Module
    def addRating(self,movie_id,user_id,rates,time):
        return
    def findRatingByUserId_MovieId(self,user_id,movie_id):
        return
    def findRatingByMovieId(self,movie_id):
        return
    def updateRatingByUserId_MovieId(self,user_id,movie_id,rates):
        return
    
    #Log Module
    def addLog(self,user_id,action_id,time,movie_id):
        return
    def findLogByMovieId(self,movie_id):
        return
    def findLogByUserId(self,user_id):
        return
    def findMovieLogByUserId(self,user_id):
        return
    def deleteLogById(self,id):
        return
    def findActionByName(self,name):
        return
    
    #Other Module
    def getAllState(self):
        return
    def getAllOccupation(self):
        return
    def getAllGenre(self):
        return
    def findPromotionById(self,id):
        return
    def findPromotionByCode_MovieId(self,code,movie_id):
        return
    def findPromotionByCode_Begin_End(self,code,begin,end):
        return
    def addPromotion(self,code,begin,end,discount):
        return
    def updatePromotionAt_Begin_End_Discount(self,id,begin,end,discount):
        return
    def addMoviesToPromotion(self,promotion_id,movieid_list):
        return
    def removeMoviesFromPromotion(self,promotion_id,movieid_list):
        return
    def deletePromotion(self,id):
        return
    
    #Admin Module
    def addAdmin(self,account,password,user_type,first,last):
        return
    def findAdminByAccount_Passowrd(self,account,password):
        return
    def findUserByAccount_First_Last(self,account,first,last):
        return
    def findAdminByAccount_First_Last(self,account,first,last):
        return
    def updateAdminProfileById(self,id,first,last):
        return
    def deleteUserById(self,id):
        return
    
#####################################
##### MySQL_Dao Implementation #######
#####################################

class MySQL_DAO(DAO):
    #User Module
    def addUser(self,account,password,user_type,first,middle,last,birthday,gender,occupation_id,email,phone,city,state_id,zip):
        try:
            return User(account = account,\
                        password = password,\
                        user_type = user_type,\
                        first = first,\
                        middle = middle,\
                        last = last,\
                        birthday = birthday,\
                        gender = gender,\
                        occupation_id = occupation_id,\
                        email = email,\
                        phone = phone,\
                        city = city,\
                        state_id = state_id,\
                        zip = zip).save()
        except Exception as err: 
            print(err)
            return

    def findUserByAccount(self,account):
        try:
            return User.objects.filter(account = account)
        except Exception as err: 
            print(err)
            return
         
    def findUserById(self,id):
        try:
            return User.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
        
    def findUserByAccount_Passowrd(self,account,password):
        try:
            return User.objects.filter(account = account, password = password, user_type = 1)
        except Exception as err: 
            print(err)
            return
        
    def updateUserProfileById(self,id,first,middle,last,birthday,gender,occupation_id,email,phone,city,state_id,zip):
        try:
            return User.objects.filter(id = id).update(first = first,\
                                                       middle = middle,\
                                                       last = last,\
                                                       birthday = birthday,\
                                                       gender = gender,\
                                                       occupation = occupation_id,\
                                                       email = email,\
                                                       phone = phone,\
                                                       city = city,\
                                                       state = state_id,\
                                                       zip = zip)
        except Exception as err: 
            print(err)
            return
        
    def updateUserShippingById(self,id,shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone):
        try:
            return User.objects.filter(id = id).update(shipping_to = shipping_to,\
                                                       shipping_address = shipping_address,\
                                                       shipping_city = shipping_city,\
                                                       shipping_state = shipping_state_id,\
                                                       shipping_zip = shipping_zip,\
                                                       shipping_phone = shipping_phone)
        except Exception as err: 
            print(err)
            return
    def updateUserCreditById(self,id,creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        try:
            return User.objects.filter(id = id).update(creidt_number = creidt_number,\
                                                       creidt_type = creidt_type,\
                                                       creidt_expire = creidt_expire,\
                                                       creidt_csc = creidt_csc,\
                                                       creidt_holder = creidt_holder,\
                                                       creidt_address = creidt_address,\
                                                       creidt_city = creidt_city,\
                                                       creidt_state = creidt_state_id,\
                                                       creidt_zip = creidt_zip)
        except Exception as err: 
            print(err)
            return
    
    def updateUserPasswordById(self,id,password):
        try:
            return User.objects.filter(id = id).update(password = password)
        except Exception as err: 
            print(err)
            return
     
    def findUserByAccount_First_Last_Birthday_Email_Phone(self,account,first,last,birthday,email,phone):
        try:
            return User.objects.filter(account = account,first = first,last = last,birthday = birthday,email = email,phone = phone)
        except Exception as err: 
            print(err)
            return
          
    #Movie Module
    def findMovieInSetByTitle_GenreId(self,movie_set,title,genre_id):
        try:
            if movie_set:
                if genre_id :
                    return movie_set.filter(title__icontains = title, genre__id__exact = genre_id)
                else:
                    return movie_set.filter(title__icontains = title)
            else:
                return []
        except Exception as err: 
            print(err)
            return
    def findMovieWithPromotion(self,promotion_id):
        try:
            return Promotion.objects.filter(id=promotion_id)[0].movies.all()
        except Exception as err: 
            print(err)
            return
    def findMovieInList(self,id_list):
        try:
            return Movie.objects.filter(id__in=id_list)
        except Exception as err: 
            print(err)
            return
    def findMovieNotInList(self,id_list):
        try:
            return Movie.objects.filter().exclude(id__in=id_list)
        except Exception as err: 
            print(err)
            return
    def findMovieById(self,id):
        try:
            return Movie.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
    def findMovieByTitle(self,title):
        try:
            return Movie.objects.filter(title__icontains = title)
        except Exception as err: 
            print(err)
            return
    def findMovieByGenreId(self,genre_id):
        try:
            return Movie.objects.filter(genre__id__exact = genre_id)
        except Exception as err: 
            print(err)
            return
    def findMovieByTitle_GenreId(self,title,genre_id):
        try:
            return Movie.objects.filter(title__icontains = title, genre__id__exact = genre_id)
        except Exception as err: 
            print(err)
            return
    def updateMovieQuantity(self,id,quantity):
        try:
            return Movie.objects.filter(id = id).update(quantity = quantity)
        except Exception as err: 
            print(err)
            return
    
    def updateMovieRates(self,id,rates):
        try:
            return Movie.objects.filter(id = id).update(rates = rates)
        except Exception as err: 
            print(err)
            return
    def getMovieOrderByRate(self):
        try:
            return Movie.objects.filter().order_by('-rates')
        except Exception as err: 
            print(err)
            return
    
    def getMovie_RatesGTE(self,rates):
        try:
            return Movie.objects.filter(rates__gte = rates).order_by('-rates')
        except Exception as err: 
            print(err)
            return
        
    def addMovie(self,title,year,director,actor,description,picture,price,quantity,rates,genre_id_list):
        try:
            movie = Movie.objects.create(title = title,\
                                          year = year,\
                                          director = director,\
                                          actor = actor,\
                                          description = description,\
                                          picture = picture,\
                                          price = price,\
                                          quantity = quantity,\
                                          rates = rates)
            movie.genre = genre_id_list
            return movie.id
        except Exception as err: 
            print(err)
            return
    
    def deleteMovie(self, movie_id):
        try:
            Movie.objects.filter(id = movie_id).delete()
        except Exception as err: 
            print(err)
            return
    
    def updateMovieById(self,id,title,year,director,actor,description,picture,price,quantity,genre_id_list):
        try:
            Movie.objects.filter(id = id).update(title = title,\
                                                  year = year,\
                                                  director = director,\
                                                  actor = actor,\
                                                  description = description,\
                                                  picture = picture,\
                                                  price = price,\
                                                  quantity = quantity)
            Movie.objects.get(id = id).genre = genre_id_list
        except Exception as err: 
            print(err)
            return
    def deleteMovieById(self,id):
        try:
            Movie.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return
    #Order Module
    def addOrderWithShipping_Credit(self,user_id,time,status,sum,\
        shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone,\
        creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        try:
            return Order(user_id = user_id,\
                         time = time,\
                         status = status,\
                         sum = sum,\
                         shipping_to=shipping_to,\
                         shipping_address = shipping_address,\
                         shipping_city = shipping_city,\
                         shipping_state_id = shipping_state_id,\
                         shipping_zip = shipping_zip,\
                         shipping_phone = shipping_phone,\
                         creidt_number = creidt_number,\
                         creidt_type = creidt_type,\
                         creidt_expire = creidt_expire,\
                         creidt_csc = creidt_csc,\
                         creidt_holder = creidt_holder,\
                         creidt_address = creidt_address,\
                         creidt_city = creidt_city,\
                         creidt_state_id = creidt_state_id,\
                         creidt_zip = creidt_zip).save()
        except Exception as err: 
            print(err)
            return False
    def updateOrderShipping(self,id,shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone):
        try:
            return Order.objects.filter(id = id).update(shipping_to = shipping_to,\
                                                        shipping_address = shipping_address,\
                                                        shipping_city = shipping_city,\
                                                        shipping_state = shipping_state_id,\
                                                        shipping_zip = shipping_zip,\
                                                        shipping_phone = shipping_phone)
        except Exception as err: 
            print(err)
            return False
    def updateOrderCredit(self,id,creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        try:
            return Order.objects.filter(id = id).update(creidt_number = creidt_number,\
                                                 creidt_type = creidt_type,\
                                                 creidt_expire = creidt_expire,\
                                                 creidt_csc = creidt_csc,\
                                                 creidt_holder = creidt_holder,\
                                                 creidt_address = creidt_address,\
                                                 creidt_city = creidt_city,\
                                                 creidt_state = creidt_state_id,\
                                                 creidt_zip = creidt_zip)
        except Exception as err: 
            print(err)
            return False
    def updateOrderSummary(self,id,sum):
        try:
            return Order.objects.filter(id = id).update(sum = sum)
        except Exception as err: 
            print(err)
            return False
    def updateOrderStatus(self,id,status):
        try:
            return Order.objects.filter(id = id).update(status = status)
        except Exception as err: 
            print(err)
            return False
    def deleteOrder(self,id):
        try:
            return Order.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return False
    
    def findOrderById(self,id):
        try:
            return Order.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
    def findOrderByUserId(self,user_id):
        try:
            return Order.objects.filter(user_id = user_id)
        except Exception as err: 
            print(err)
            return
    def findOrderByUserId_Status(self,user_id,status):
        try:
            return Order.objects.filter(user_id = user_id, status = status)
        except Exception as err: 
            print(err)
            return
    def findOrderByItemId(self,item_id):
        try:
            return Order.objects.filter(item__id = item_id)
        except Exception as err: 
            print(err)
            return
    def findOrderByAccount_Status(self,account,status):
        try:
            if status != '':
                return Order.objects.filter(user__account__icontains = account, status = status).order_by('-time')
            else:
                return Order.objects.filter(user__account__icontains = account).order_by('-time')
        except Exception as err: 
            print(err)
            return
    
    #Item Module
    def addItem(self,movie_id,order_id,quantity,promotion_id):
        try:
            return Item(movie_id = movie_id,\
                        order_id = order_id,\
                        quantity = quantity,\
                        promotion_id = promotion_id).save()
        except Exception as err: 
            print(err)
            return
    def updateItemQuantity(self,id, quantity):
        try:
            return Item.objects.filter(id = id).update(quantity = quantity)
        except Exception as err: 
            print(err)
            return False
    def updateItemPromtion(self,id, promotion_id):
        try:    
            return Item.objects.filter(id = id).update(promotion = promotion_id)
        except Exception as err: 
            print(err)
            return False
    def deleteItem(self,id):
        try:
            return Item.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return False
    def findItemById(self,id):
        try:
            return Item.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
    def findItemByOrderId(self,order_id):
        try:
            return Item.objects.filter(order_id = order_id)
        except Exception as err: 
            print(err)
            return
    
    def findItemByOrderId_MovieID(self,order_id,movie_id):
        try:
            return Item.objects.filter(order_id = order_id,movie_id = movie_id)
        except Exception as err: 
            print(err)
            return      
    
    #Rating Module
    def addRating(self,movie_id,user_id,rates,time):
        try:
            return Rating(movie_id = movie_id,\
                   user_id = user_id,\
                   rates = rates,\
                   time = time).save()
        except Exception as err: 
            print(err)
            return False
    def findRatingByUserId_MovieId(self,user_id,movie_id):
        try:
            return Rating.objects.filter(user_id = user_id, movie_id = movie_id)
        except Exception as err: 
            print(err)
            return
    
    def findRatingByMovieId(self,movie_id):
        try:
            return Rating.objects.filter(movie_id = movie_id)
        except Exception as err: 
            print(err)
            return       
    
    def updateRatingByUserId_MovieId(self,user_id,movie_id,rates):
        try:
            return Rating.objects.filter(user_id = user_id, movie_id = movie_id).update(rates =rates)
        except Exception as err: 
            print(err)
            return False
    
    #Log Module
    def addLog(self,user_id,action_id,time,movie_id):
        try:
            return Log(user_id = user_id, action_id = action_id, time = time, movie_id = movie_id).save()
        except Exception as err: 
            print(err)
            return False
    def findLogByMovieId(self,movie_id):
        try:
            return Log.objects.filter(movie_id = movie_id)
        except Exception as err: 
            print(err)
            return
    def findLogByUserId(self,user_id):
        try:
            return Log.objects.filter(user_id = user_id).order_by('-time')
        except Exception as err: 
            print(err)
            return
        
    def findMovieLogByUserId(self,user_id):
        try:
            return Log.objects.filter(user_id = user_id, movie__isnull = False)
        except Exception as err: 
            print(err)
            return
    def deleteLogById(self,id):
        try:
            return Log.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return
    
    def findActionByName(self,name):
        try:
            return Action.objects.filter(name = name)
        except Exception as err: 
            print(err)
            return
        
    #Other Module
    def getAllState(self):
        try:
            return State.objects.all()
        except Exception as err: 
            print(err)
            return
    def getAllOccupation(self):
        try:
            return Occupation.objects.all()
        except Exception as err: 
            print(err)
            return
    def getAllGenre(self):
        try:
            return Genre.objects.all()
        except Exception as err: 
            print(err)
            return
    def findPromotionById(self,id):
        try:
            return Promotion.objects.filter(id=id)
        except Exception as err: 
            print(err)
            return
    def findPromotionByCode_MovieId(self,code,movie_id):
        try:
            return Promotion.objects.filter(code = code, movies__id = movie_id)
        except Exception as err: 
            print(err)
            return
        
    def findPromotionByCode_Begin_End(self,code,begin,end):
        try:
            if begin and end:
                return Promotion.objects.filter(code__icontains = code, begin__lte = begin, end__gte = end)
            elif begin and not end:
                return Promotion.objects.filter(code__icontains = code, begin__lte = begin)
            elif not begin and end:
                return Promotion.objects.filter(code__icontains = code, end__gte = end)
            else:
                return Promotion.objects.filter(code__icontains = code)
        except Exception as err: 
            print(err)
            return
        
    def addPromotion(self,code,begin,end,discount):
        try:
            return Promotion.objects.create(code = code,\
                                            begin = begin,\
                                            end = end,\
                                            discount = discount)
        except Exception as err: 
            print(err)
            return
    def updatePromotionAt_Begin_End_Discount(self,id,begin,end,discount):
        try:
            return Promotion.objects.filter(id=id).update(begin=begin,end=end,discount=discount)
        except Exception as err: 
            print(err)
            return
    
    def addMoviesToPromotion(self,promotion_id,movieid_list):
        try:
            movies = Promotion.objects.get(id=promotion_id).movies
            movies.add(*movieid_list)
        except Exception as err: 
            print(err)
            return
    def removeMoviesFromPromotion(self,promotion_id,movieid_list):
        try:
            movies = Promotion.objects.get(id=promotion_id).movies
            movies.remove(*movieid_list)
        except Exception as err: 
            print(err)
            return
    def deletePromotion(self,id):
        try:
            Promotion.objects.filter(id=id).delete()
        except Exception as err: 
            print(err)
            return

    #Admin Module
    def addAdmin(self,account,password,user_type,first,last):
        try:
            return User(account = account,\
                        password = password,\
                        user_type = user_type,\
                        first = first,\
                        last = last).save()
        except Exception as err: 
            print(err)
            return
    
    def findAdminByAccount_Passowrd(self,account,password):
        try:
            return User.objects.filter(account = account, password = password, user_type__in = [0,3])
        except Exception as err: 
            print(err)
            return
    def findUserByAccount_First_Last(self,account,first,last):
        try:
            return User.objects.filter(account__icontains = account, first__icontains = first, last__icontains = last, user_type = 1)
        except Exception as err: 
            print(err)
            return
        
    def findAdminByAccount_First_Last(self,account,first,last):
        try:
            return User.objects.filter(account__icontains = account, first__icontains = first, last__icontains = last, user_type = 0)
        except Exception as err: 
            print(err)
            return

    def updateAdminProfileById(self,id,first,last):
        try:
            return User.objects.filter(id = id).update(first = first,last = last)
        except Exception as err: 
            print(err)
            return
        
    def deleteUserById(self,id):
        try:
            return User.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return
#####################################
##### Mong_Dao Implementation #######
#####################################

class Mongo_DAO(DAO):
    def __init__(self,mongodb):
        connect(mongodb)
        
    #User Module
    def addUser(self,account,password,user_type,first,middle,last,birthday,gender,occupation_id,email,phone,city,state_id,zip):
        try:
            return Mongo_User(account = account,\
                        password = password,\
                        user_type = user_type,\
                        first = first,\
                        middle = middle,\
                        last = last,\
                        birthday = birthday,\
                        gender = gender,\
                        occupation = occupation_id,\
                        email = email,\
                        phone = phone,\
                        city = city,\
                        state = state_id,\
                        zip = zip).save()
        except Exception as err: 
            print(err)
            return

    def findUserByAccount(self,account):
        try:
            return Mongo_User.objects.filter(account = account)
        except Exception as err: 
            print(err)
            return 
    def findUserById(self,id):
        try:
            return Mongo_User.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
    def findUserByAccount_Passowrd(self,account,password):
        try:
            return Mongo_User.objects.filter(account = account, password = password, user_type = 1)
        except Exception as err: 
            print(err)
            return
    def updateUserProfileById(self,id,first,middle,last,birthday,gender,occupation_id,email,phone,city,state_id,zip):
        try:
            return Mongo_User.objects.filter(id = id).update(set__first = first,\
                                                       set__middle = middle,\
                                                       set__last = last,\
                                                       set__birthday = birthday,\
                                                       set__gender = gender,\
                                                       set__occupation = occupation_id,\
                                                       set__email = email,\
                                                       set__phone = phone,\
                                                       set__city = city,\
                                                       set__state = state_id,\
                                                       set__zip = zip)
        except Exception as err: 
            print(err)
            return
    def updateUserShippingById(self,id,shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone):
        try:
            return Mongo_User.objects.filter(id = id).update(set__shipping_to = shipping_to,\
                                                       set__shipping_address = shipping_address,\
                                                       set__shipping_city = shipping_city,\
                                                       set__shipping_state = shipping_state_id,\
                                                       set__shipping_zip = shipping_zip,\
                                                       set__shipping_phone = shipping_phone)
        except Exception as err: 
            print(err)
            return
    def updateUserCreditById(self,id,creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        try:
            return Mongo_User.objects.filter(id = id).update(set__creidt_number = creidt_number,\
                                                       set__creidt_type = creidt_type,\
                                                       set__creidt_expire = creidt_expire,\
                                                       set__creidt_csc = creidt_csc,\
                                                       set__creidt_holder = creidt_holder,\
                                                       set__creidt_address = creidt_address,\
                                                       set__creidt_city = creidt_city,\
                                                       set__creidt_state = creidt_state_id,\
                                                       set__creidt_zip = creidt_zip)
        except Exception as err: 
            print(err)
            return
    
    def updateUserPasswordById(self,id,password):
        try:
            return Mongo_User.objects.filter(id = id).update(set__password = password)
        except Exception as err: 
            print(err)
            return
    
    def findUserByAccount_First_Last_Birthday_Email_Phone(self,account,first,last,birthday,email,phone):
        try:
            return Mongo_User.objects.filter(account = account,first = first,last = last,birthday = birthday,email = email,phone = phone)
        except Exception as err: 
            print(err)
            return
    
    #Movie Module
    def findMovieInSetByTitle_GenreId(self,movie_set,title,genre_id):
        try:
            if movie_set:
                if genre_id:
                    return movie_set.filter(title__icontains = title, genre__contains = genre_id)
                else:
                    return movie_set.filter(title__icontains = title)
            else:
                return []
        except Exception as err: 
            print(err)
            return
    def findMovieWithPromotion(self,promotion_id):
        try:
            return Mongo_Promotion.objects.filter(id=promotion_id)[0].movies
        except Exception as err: 
            print(err)
            return
    def findMovieInList(self,id_list):
        try:
            return Mongo_Movie.objects.filter(id__in=id_list)
        except Exception as err: 
            print(err)
            return
    def findMovieNotInList(self,id_list):
        try:
            return Mongo_Movie.objects.filter(id__nin=id_list)
        except Exception as err: 
            print(err)
            return
    def findMovieById(self,id):
        try:
            return Mongo_Movie.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
    def findMovieByTitle(self,title):
        try:
            return Mongo_Movie.objects.filter(title__icontains = title)
        except Exception as err: 
            print(err)
            return
    def findMovieByGenreId(self,genre_id):
        try:
            return Mongo_Movie.objects.filter(genre__contains = genre_id)
        except Exception as err: 
            print(err)
            return
    def findMovieByTitle_GenreId(self,title,genre_id):
        try:
            return Mongo_Movie.objects.filter(title__icontains = title, genre__contains = genre_id)
        except Exception as err: 
            print(err)
            return
    def updateMovieQuantity(self,id,quantity):
        try:
            return Mongo_Movie.objects.filter(id = id).update(set__quantity = quantity)
        except Exception as err: 
            print(err)
            return
    
    def updateMovieRates(self,id,rates):
        try:
            return Mongo_Movie.objects.filter(id = id).update(set__rates = rates)
        except Exception as err: 
            print(err)
            return
    
    def getMovieOrderByRate(self):
        try:
            return Mongo_Movie.objects.filter().order_by('-rates')
        except Exception as err: 
            print(err)
            return
        
    def getMovie_RatesGTE(self,rates):
        try:
            return Mongo_Movie.objects.filter(rates__gte = rates).order_by('-rates')
        except Exception as err: 
            print(err)
            return
    
    def addMovie(self,title,year,director,actor,description,picture,price,quantity,rates,genre_id_list):
        try:
            return Mongo_Movie.objects.create(title = title,\
                                               year = year,\
                                               director = director,\
                                               actor = actor,\
                                               description = description,\
                                               picture = picture,\
                                               price = price,\
                                               quantity = quantity,\
                                               rates = rates,\
                                               genre = genre_id_list).id
        except Exception as err: 
            print(err)
            return
    
    def deleteMovie(self, movie_id):
        try:
            Mongo_Movie.objects.filter(id = movie_id).delete()
        except Exception as err: 
            print(err)
            return
        
    def updateMovieById(self,id,title,year,director,actor,description,picture,price,quantity,genre_id_list):
        try:
            Mongo_Movie.objects.filter(id = id).update(set__title = title,\
                                                       set__year = year,\
                                                       set__director = director,\
                                                       set__actor = actor,\
                                                       set__description = description,\
                                                       set__picture = picture,\
                                                       set__price = price,\
                                                       set__quantity = quantity,\
                                                       set__genre = genre_id_list)
        except Exception as err: 
            print(err)
            return
    def deleteMovieById(self,id):
        try:
            Mongo_Movie.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return
    #Order Module
    def addOrderWithShipping_Credit(self,user_id,time,status,sum,\
        shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone,\
        creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        try:
            return Mongo_Order(user = user_id,\
                         time = time,\
                         status = status,\
                         sum = sum,\
                         shipping_to=shipping_to,\
                         shipping_address = shipping_address,\
                         shipping_city = shipping_city,\
                         shipping_state = shipping_state_id,\
                         shipping_zip = shipping_zip,\
                         shipping_phone = shipping_phone,\
                         creidt_number = creidt_number,\
                         creidt_type = creidt_type,\
                         creidt_expire = creidt_expire,\
                         creidt_csc = creidt_csc,\
                         creidt_holder = creidt_holder,\
                         creidt_address = creidt_address,\
                         creidt_city = creidt_city,\
                         creidt_state = creidt_state_id,\
                         creidt_zip = creidt_zip).save()
        except Exception as err: 
            print(err)
            return
    def updateOrderShipping(self,id,shipping_to,shipping_address,shipping_city,shipping_state_id,shipping_zip,shipping_phone):
        try:
            return Mongo_Order.objects.filter(id = id).update(set__shipping_to = shipping_to,\
                                                        set__shipping_address = shipping_address,\
                                                        set__shipping_city = shipping_city,\
                                                        set__shipping_state = shipping_state_id,\
                                                        set__shipping_zip = shipping_zip,\
                                                        set__shipping_phone = shipping_phone)
        except Exception as err: 
            print(err)
            return
    def updateOrderCredit(self,id,creidt_number,creidt_type,creidt_expire,creidt_csc,creidt_holder,creidt_address,creidt_city,creidt_state_id,creidt_zip):
        try:
            return Mongo_Order.objects.filter(id = id).update(set__creidt_number = creidt_number,\
                                                 set__creidt_type = creidt_type,\
                                                 set__creidt_expire = creidt_expire,\
                                                 set__creidt_csc = creidt_csc,\
                                                 set__creidt_holder = creidt_holder,\
                                                 set__creidt_address = creidt_address,\
                                                 set__creidt_city = creidt_city,\
                                                 set__creidt_state = creidt_state_id,\
                                                 set__creidt_zip = creidt_zip)
        except Exception as err: 
            print(err)
            return
    def updateOrderSummary(self,id,sum):
        try:
            return Mongo_Order.objects.filter(id = id).update(set__sum = sum)
        except Exception as err: 
            print(err)
            return
    def updateOrderStatus(self,id,status):
        try:
            return Mongo_Order.objects.filter(id = id).update(set__status = status)
        except Exception as err: 
            print(err)
            return
    def deleteOrder(self,id):
        try:
            return Mongo_Order.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return
    
    def findOrderById(self,id):
        try:
            return Mongo_Order.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
    def findOrderByUserId(self,user_id):
        try:
            return Mongo_Order.objects.filter(user = user_id)
        except Exception as err: 
            print(err)
            return
    def findOrderByUserId_Status(self,user_id,status):
        try:
            return Mongo_Order.objects.filter(user = user_id, status = status)
        except Exception as err: 
            print(err)
            return
    def findOrderByItemId(self,item_id):
        try:
            return Mongo_Item.objects.filter(id = item_id).values_list('order')
        except Exception as err: 
            print(err)
            return
    def findOrderByAccount_Status(self,account,status):
        try:
            userid_list = [str(id) for id in Mongo_User.objects.filter(account__icontains = account).values_list('id')]
            if status != '':
                return Mongo_Order.objects.filter(user__in = userid_list, status = status).order_by('-time')
            else:
                return Mongo_Order.objects.filter(user__in = userid_list).order_by('-time')
        except Exception as err: 
            print(err)
            return
    
    #Item Module
    def addItem(self,movie_id,order_id,quantity,promotion_id):
        try:
            return Mongo_Item(movie = movie_id,\
                              order = order_id,\
                              quantity = quantity,\
                              promotion = promotion_id).save()
        except Exception as err: 
            print(err)
            return
    def updateItemQuantity(self,id, quantity):
        try:
            return Mongo_Item.objects.filter(id = id).update(set__quantity = quantity)
        except Exception as err: 
            print(err)
            return
    def updateItemPromtion(self,id, promotion_id):
        try:
            return Mongo_Item.objects.filter(id = id).update(set__promotion = promotion_id)
        except Exception as err: 
            print(err)
            return
    def deleteItem(self,id):
        try:
            return Mongo_Item.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return
    def findItemById(self,id):
        try:
            return Mongo_Item.objects.filter(id = id)
        except Exception as err: 
            print(err)
            return
    def findItemByOrderId(self,order_id):
        try:
            return Mongo_Item.objects.filter(order = order_id)
        except Exception as err: 
            print(err)
            return
    
    def findItemByOrderId_MovieID(self,order_id,movie_id):
        try:
            return Mongo_Item.objects.filter(order = order_id, movie = movie_id)
        except Exception as err: 
            print(err)
            return        
    
    #Rating Module
    def addRating(self,movie_id,user_id,rates,time):
        try:
            return Mongo_Rating(movie = movie_id,\
                          user = user_id,\
                          rates = rates,\
                          time = time).save()
        except Exception as err: 
            print(err)
            return
    
    def findRatingByUserId_MovieId(self,user_id,movie_id):
        try:
            return Mongo_Rating.objects.filter(user = user_id, movie = movie_id)
        except Exception as err: 
            print(err)
            return
        
    def findRatingByMovieId(self,movie_id):
        try:
            return Mongo_Rating.objects.filter(movie = movie_id)
        except Exception as err: 
            print(err)
            return
        
    def updateRatingByUserId_MovieId(self,user_id,movie_id,rates):
        try:
            return Mongo_Rating.objects.filter(user = user_id, movie = movie_id).update(set__rates =rates)
        except Exception as err: 
            print(err)
            return
    
    #Log Module
    def addLog(self,user_id,action_id,time,movie_id):
        try:
            return Mongo_Log(user = user_id, action = action_id, time = time, movie = movie_id).save()
        except Exception as err: 
            print(err)
            return
    def findLogByMovieId(self,movie_id):
        try:
            return Mongo_Log.objects.filter(movie = movie_id)
        except Exception as err: 
            print(err)
            return
    def findLogByUserId(self,user_id):
        try:
            return Mongo_Log.objects.filter(user = user_id).order_by('-time')
        except Exception as err: 
            print(err)
            return
        
    def findMovieLogByUserId(self,user_id):
        try:
            return Mongo_Log.objects.filter(user = user_id, movie__exists = True)
        except Exception as err: 
            print(err)
            return
                    
    def deleteLogById(self,id):
        try:
            return Mongo_Log.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return
    
    def findActionByName(self,name):
        try:
            return Mongo_Action.objects.filter(name = name)
        except Exception as err: 
            print(err)
            return
    
    #Other Module
    def getAllState(self):
        try:
            return Mongo_State.objects.all()
        except Exception as err: 
            print(err)
            return
    def getAllOccupation(self):
        try:
            return Mongo_Occupation.objects.all()
        except Exception as err: 
            print(err)
            return
    def getAllGenre(self):
        try:
            return Mongo_Genre.objects.all()
        except Exception as err: 
            print(err)
            return
    def findPromotionById(self,id):
        try:
            return Mongo_Promotion.objects.filter(id=id)
        except Exception as err: 
            print(err)
            return
    def findPromotionByCode_MovieId(self,code,movie_id):
        try:
            return Mongo_Promotion.objects.filter(code = code, movies__contains = movie_id )
        except Exception as err: 
            print(err)
            return
    def findPromotionByCode_Begin_End(self,code,begin,end):
        try:
            if begin and end:
                return Mongo_Promotion.objects.filter(code__icontains = code, begin__lte = begin, end__gte = end)
            elif begin and not end:
                return Mongo_Promotion.objects.filter(code__icontains = code, begin__lte = begin)
            elif not begin and end:
                return Mongo_Promotion.objects.filter(code__icontains = code, end__gte = end)
            else:
                return Mongo_Promotion.objects.filter(code__icontains = code)
        except Exception as err: 
            print(err)
            return
    def addPromotion(self,code,begin,end,discount):
        try:
            return Mongo_Promotion.objects.create(code = code,\
                                            begin = begin,\
                                            end = end,\
                                            discount = discount)
        except Exception as err: 
            print(err)
            return
    def updatePromotionAt_Begin_End_Discount(self,id,begin,end,discount):
        try:
            return Mongo_Promotion.objects.filter(id=id).update(set__begin=begin,set__end=end,set__discount=discount)
        except Exception as err: 
            print(err)
            return
    def addMoviesToPromotion(self,promotion_id,movieid_list):
        try:
            return Mongo_Promotion.objects.filter(id=promotion_id).update(add_to_set__movies = movieid_list)
        except Exception as err: 
            print(err)
            return
    def removeMoviesFromPromotion(self,promotion_id,movieid_list):
        try:
            return Mongo_Promotion.objects.filter(id=promotion_id).update(pull_all__movies = movieid_list)
        except Exception as err: 
            print(err)
            return
    def deletePromotion(self,id):
        try:
            Mongo_Promotion.objects.filter(id=id).delete()
        except Exception as err: 
            print(err)
            return
    #Admin Module
    def addAdmin(self,account,password,user_type,first,last):
        try:
            return Mongo_User(account = account,\
                        password = password,\
                        user_type = user_type,\
                        first = first,\
                        last = last).save()
        except Exception as err: 
            print(err)
            return
    def findAdminByAccount_Passowrd(self,account,password):
        try:
            return Mongo_User.objects.filter(account = account, password = password, user_type__in = [0,3])
        except Exception as err: 
            print(err)
            return
    def findUserByAccount_First_Last(self,account,first,last):
        try:
            return Mongo_User.objects.filter(account__icontains = account, first__icontains = first, last__icontains = last, user_type = 1)
        except Exception as err: 
            print(err)
            return
    def findAdminByAccount_First_Last(self,account,first,last):
        try:
            return Mongo_User.objects.filter(account__icontains = account, first__icontains = first, last__icontains = last, user_type = 0)
        except Exception as err: 
            print(err)
            return
        
    def updateAdminProfileById(self,id,first,last):
        try:
            return Mongo_User.objects.filter(id = id).update(set__first = first,set__last = last)
        except Exception as err: 
            print(err)
            return
        
    def deleteUserById(self,id):
        try:
            return Mongo_User.objects.filter(id = id).delete()
        except Exception as err: 
            print(err)
            return