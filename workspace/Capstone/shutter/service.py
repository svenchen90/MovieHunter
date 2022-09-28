from datetime import datetime
import random
import string
import time

from shutter.dao import MySQL_DAO, Mongo_DAO


GENDER = {0 : 'Male', \
          1 : 'Female'}
USER_TYPE = { 0 : 'Admin',\
             1 : 'Customer'}

ORDER_STATUS= {0 : 'In Process',\
                 1 : 'Paid',\
                 2 : 'Shipped'}

CARD_TYPE = {0 : 'Visa', \
             1 : 'Master',\
             2 : 'Debit'}

ACTION_LIST = {'viewdetails' : 2,
               'search' : 1,
               'order' : 3,
               'rating_1' : -1,
               'rating_2' : 0,
               'rating_3' : 1,
               'rating_4' : 2,
               'rating_5' : 3}

MOVIE_PER_PAGE = 6
ORDER_PER_PAGE = 6
CUSTOMER_PER_PAGE = 12
ADMIN_PER_PAGE = 12
ADMIN_MOVIE_PER_PAGE = 12
ADMIN_PROMOTION_PER_PAGE = 12
ADMIN_PROMOTION_MOVIE_PER_PAGE = 8
ADMIN_ORDER_PER_PAGE = 12

IMG_DIR = 'D:\\workspace\\Capstone\\templates\\media\\'
TYPE_DATABASE = 'mysql'

DAO_Proxy = MySQL_DAO() if TYPE_DATABASE == 'mysql' else Mongo_DAO('Mongo_Shutter')

'''
if TYPE_DATABASE == 'mysql':
    DAO = MySQL_DAO()
elif TYPE_DATABASE == 'mongo':
    DAO = Mongo_DAO('Mongo_Shutter')
'''


def preload():
    state =  DAO_Proxy.getAllState()
    genre = DAO_Proxy.getAllGenre()
    occupation = DAO_Proxy.getAllOccupation()
    
    context = {}
    context['genre'] = genre
    context['state'] = state
    context['occupation'] = occupation
    context['gender'] = GENDER
    context['user_type'] = USER_TYPE
    context['order_status'] = ORDER_STATUS
    context['card_type'] = CARD_TYPE
    
    return context

def pagemanager(total,current_page,num_per_page):
    
    if total%num_per_page != 0 :
        max_page = total/num_per_page + 1
    else : 
        max_page = total/num_per_page
    
    if max_page == 1:
        start = 0
        end = total
    else : 
        if current_page <= 1:
            start = 0
            end = num_per_page
        elif current_page >= max_page : 
            start = (max_page-1)*num_per_page
            end = total
        else : 
            start = (current_page-1)*num_per_page
            end = current_page*num_per_page
            
    return start,end,max_page

def autoupdateordersummary(order_id):
    if DAO_Proxy.findOrderById(order_id):
        order = DAO_Proxy.findOrderById(order_id)[0]
        items = DAO_Proxy.findItemByOrderId(order_id)
        
        sub_total = sum([calculateprice_item(item.id) for item in items])
        
        if order.creidt_state:
            DAO_Proxy.updateOrderSummary(order_id, sub_total*(1+order.creidt_state.tax_rate))
            return sub_total,sub_total*order.creidt_state.tax_rate,sub_total*(1+order.creidt_state.tax_rate)
        else:
            DAO_Proxy.updateOrderSummary(order_id, sub_total)
            return sub_total,0,sub_total
    else:
        return

def calculateprice_item(item_id):
    if DAO_Proxy.findItemById(item_id):
        item = DAO_Proxy.findItemById(item_id)[0]
        if item.movie and item.movie.price:
            if item.promotion:
                return item.quantity * item.movie.price * (100- item.promotion.discount)/100
            else:
                return item.quantity * item.movie.price
        else:
            return 0
    else:
        return -1
        
def user_json(user):
    return {'id' : str(user.id), 'first' : user.first, 'user_type' : str(user.user_type)}

def passwordCheck(user_id,password):

    if not DAO_Proxy.findUserById(user_id):
        return False
    elif DAO_Proxy.findUserById(user_id)[0].password != password:
        return False
    else:
        return True

def shippingCheck(shipping):
    return True if shipping.shipping_to else False

def creditCheck(credit):
    return True if credit.creidt_number else False

def quantityCheck(movie_id,quantity):
    if DAO_Proxy.findMovieById(movie_id)[0].quantity and DAO_Proxy.findMovieById(movie_id)[0].quantity >= quantity:
        return True
    else:
        return False
    
def checkpromotiondate(promotion):
    if promotion.begin and datetime.today().date() < promotion.begin:
        return -1
    elif promotion.end and datetime.today().date() > promotion.end:
        return -2
    else:
        return 1
    
def checkitems(items):
    result = []
    for item in items:
        data = {}
        if item.movie.quantity and item.movie.quantity < item.quantity:
            data['quantity'] = item.movie.quantity
        if item.promotion and checkpromotiondate(item.promotion) != 1:
            data['promotion'] = 1
        if data:
            data['title'] = item.movie.title + ' ( ' + item.movie.year + ' )'
            result.append(data)
    return result

# get genrepoints map for user
def getGenrePoints(user_id):
    start = time.time()
    
    genrepoints = {}
    for g in DAO_Proxy.getAllGenre():
        genrepoints[g.name] = 0
    
    logs = DAO_Proxy.findLogByUserId(user_id)[0:100]
    print 'Query log:', time.time() - start
    
    print 'Get Log' ,time.time() - start, len(logs)
    
    for l in logs:
        point = l.action.point
        genres = l.movie.genre.all() if TYPE_DATABASE == 'mysql' else l.movie.genre
        for g in genres:
            genrepoints[g.name] += point
    
    print 'Get Genre Points' ,time.time() - start
    return genrepoints

def getMovieRankByGenrePoints(genrepoints):
    start = time.time()
    
    movies = DAO_Proxy.getMovie_RatesGTE(4)
    moviepoints = {}
    for m in movies:
        moviepoints[m] = 0
        genres = m.genre.all() if TYPE_DATABASE == 'mysql' else m.genre
        for g in genres:
            moviepoints[m] += genrepoints[g.name]
            
    print 'Get Movie Rank', time.time() - start
    return sorted(moviepoints, key=lambda key: moviepoints[key], reverse=True)

def createLog(user_id, movie_id, action_name):
    if DAO_Proxy.findActionByName(action_name):
        DAO_Proxy.addLog(user_id,DAO_Proxy.findActionByName(action_name)[0].id,datetime.utcnow(),movie_id)
    else:
        print "Action not found!"
        
def randomString(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))