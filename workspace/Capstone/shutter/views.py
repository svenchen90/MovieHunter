# Create your views here.

from datetime import datetime
import json
import os

from PIL import Image
from django import forms
from django.core import serializers
from django.core.mail.message import EmailMultiAlternatives
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

from shutter.service import preload, pagemanager, MOVIE_PER_PAGE, \
    autoupdateordersummary, ORDER_PER_PAGE, DAO_Proxy, user_json, passwordCheck, \
    shippingCheck, creditCheck, quantityCheck, checkpromotiondate, checkitems, \
    getMovieRankByGenrePoints, getGenrePoints, createLog, CUSTOMER_PER_PAGE, \
    ADMIN_PER_PAGE, ADMIN_MOVIE_PER_PAGE, IMG_DIR, ADMIN_PROMOTION_PER_PAGE, \
    ADMIN_PROMOTION_MOVIE_PER_PAGE, randomString, ADMIN_ORDER_PER_PAGE


def home(request):
    context = preload()
    if 'user' in request.session:
        recommend = getMovieRankByGenrePoints(getGenrePoints(request.session['user']['id']))[0:6]
    else:
        recommend = DAO_Proxy.getMovieOrderByRate()[6:12]
    
    tops = DAO_Proxy.getMovieOrderByRate()[0:6]
    
    context['tops'] = tops
    
    context['recommend'] = recommend
    return render(request, 'index.html',context)

def ajax_rating(request):
    if 'user' not in request.session:     
        return HttpResponse('login!')
    else :
        DAO_Proxy.updateRatingByUserId_MovieId(request.session['user']['id'], request.GET['id'], request.GET['rate'])\
        if DAO_Proxy.findRatingByUserId_MovieId(request.session['user']['id'], request.GET['id']) else \
        DAO_Proxy.addRating(request.GET['id'], request.session['user']['id'], request.GET['rate'], datetime.utcnow())
        
        #Put Log here
        createLog(request.session['user']['id'], request.GET['id'], 'rating_'+request.GET['rate'])
        return HttpResponse('success!')

def toprating(request):
    context = preload()
    
    tops = DAO_Proxy.getMovieOrderByRate()
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(tops.count(),current_page,MOVIE_PER_PAGE)
    
    movies = tops[start:end]                                
    
    context['totalpage'] = totalpage
    context['movies'] = movies
    return  render (request, 'movie-list.html',context)

def recommend(request):
    context = preload()
    
    #Pull out recommend list
    if 'user' in request.session:
        # Pull out the recommend list
        recommend = getMovieRankByGenrePoints(getGenrePoints(request.session['user']['id']))
    else:
        #Recommend list
        recommend = DAO_Proxy.getMovieOrderByRate()[0:6]
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(len(recommend),current_page,MOVIE_PER_PAGE)
    
    movies = recommend[start:end]                                
    
    context['totalpage'] = totalpage
    context['movies'] = movies
    return  render (request, 'movie-list.html',context)

def login_page(request):
    context = preload()
    return render(request, 'login.html')

def logout(request):
    #Put log here
    request.session.flush()
    return redirect('/')

def register_page(request):
    context = preload()
    return render(request, 'register.html',context)

def searchmovie(request):
    context = preload()
    
    movies = DAO_Proxy.findMovieByTitle(request.GET['title']) if request.GET['genre'] == '' \
                                else DAO_Proxy.findMovieByTitle_GenreId(request.GET['title'], request.GET['genre'])
    
    #put log here
    if 'user' in request.session:
        for movie in movies[0:6]:
            createLog(request.session['user']['id'], movie.id, 'search')
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(movies.count(),current_page,MOVIE_PER_PAGE)
    
    movies = movies[start:end]
    
    context['totalpage'] = totalpage
    context['movies'] = movies
    return  render (request, 'movie-list.html',context)

def moviedetail(request):
    context = preload()
    
    if DAO_Proxy.findMovieById(request.GET['id']):
        movie = DAO_Proxy.findMovieById(request.GET['id'])[0]
        
        #put log here
        if 'user' in request.session:
            createLog(request.session['user']['id'], movie.id, 'viewdetails')
    
    context['movie'] = movie
    return render(request, 'movie-detail.html',context)

def customerhome(request):
    context = preload()
    
    return render(request, 'customer-base.html',context)

def viewprofile(request):
    context = preload()
    
    context['profile'] = DAO_Proxy.findUserById(request.session['user']['id'])[0] if DAO_Proxy.findUserById(request.session['user']['id']) else None
    
    return render(request, 'customer-viewprofile.html',context)

def ajax_modify_profile(request):
    DAO_Proxy.updateUserProfileById(request.session['user']['id'], request.POST['first'], request.POST['middle'], request.POST['last'], \
                                    request.POST['birthday'],request.POST['gender'], request.POST['occupation'], request.POST['email'], \
                                    request.POST['phone'], request.POST['city'], request.POST['state'], request.POST['zip'])
    request.session['user'] = user_json(DAO_Proxy.findUserById(request.session['user']['id'])[0] if DAO_Proxy.findUserById(request.session['user']['id']) else None)
    request.session.set_expiry(3600)
    
    return HttpResponse(1)

def modify_profile_page(request):
    context = preload()
    
    context['profile'] = DAO_Proxy.findUserById(request.session['user']['id'])[0] if DAO_Proxy.findUserById(request.session['user']['id']) else None
    
    return render(request, 'customer-modifyprofile.html',context)

def ajax_password_modify(request):
    if passwordCheck(request.session['user']['id'], request.POST['oldpassword']):
        DAO_Proxy.updateUserPasswordById(request.session['user']['id'], request.POST['newpassword'])
        return HttpResponse(1)
    else:
        return HttpResponse(0)
     
def change_password_page(request):
    context = preload()
    return render(request, 'customer-changepassword.html',context)

def forgetpassword(request):
    context = preload()
    
    if request.method == 'GET':
        return render(request, 'customer-forgetpassword.html',context)
    elif request.method == 'POST':
        customers =  DAO_Proxy.findUserByAccount_First_Last_Birthday_Email_Phone(request.POST['account'],request.POST['first'],request.POST['last'],request.POST['birthday'],request.POST['email'],\
                                                                request.POST['phone'])
        if customers:
            new_password = randomString()
            DAO_Proxy.updateUserPasswordById(customers[0].id,new_password)
            subject = 'FORGET PASSWORD'
            content = 'Dear ' + customers[0].first + ':\n Your new password of Movie Shutter account is ' +  new_password + '.\nThank You!\n\nMovie Shutter'
            mail_from = 'movieshutter@gmail.com'
            to_list = [customers[0].email]
            EmailMultiAlternatives(subject,content,mail_from,to_list).send()
        
        return redirect('/')
    else:
        return render(request, 'error.html',context)
        
def viewshipping(request):
    context = preload()
    
    context['shipping'] = DAO_Proxy.findUserById(request.session['user']['id'])[0] \
                    if DAO_Proxy.findUserById(request.session['user']['id']) else None
    if shippingCheck(context['shipping']):
        return render(request, 'customer-viewshipping.html',context)
    else:
        return redirect('/modify_shipping/')

def modifyshipping_page(request):
    context = preload()
    
    context['shipping'] = DAO_Proxy.findUserById(request.session['user']['id'])[0] \
                    if DAO_Proxy.findUserById(request.session['user']['id']) else None
    return render(request, 'customer-modifyshipping.html',context)
                                          
def ajax_usershipping_modify(request):
    DAO_Proxy.updateUserShippingById(request.session['user']['id'], request.POST['shipping_to'], request.POST['shipping_address'], \
                                   request.POST['shipping_city'], request.POST['shipping_state'], request.POST['shipping_zip'], request.POST['shipping_phone'])
    return HttpResponse(1)

def viewcredit(request):
    context = preload()
    
    context['credit'] = DAO_Proxy.findUserById(request.session['user']['id'])[0] \
                    if DAO_Proxy.findUserById(request.session['user']['id']) else None

    if creditCheck(context['credit']):    
        return render(request, 'customer-viewcredit.html', context)
    else:
        return redirect('/modify_credit/')

def modifycredit_page(request):
    context = preload()
    
    context['credit'] = DAO_Proxy.findUserById(request.session['user']['id'])[0] \
                if DAO_Proxy.findUserById(request.session['user']['id']) else None
    return render(request, 'customer-modifycredit.html',context)

def ajax_usercredit_modify(request):
    DAO_Proxy.updateUserCreditById(request.session['user']['id'],request.POST['creidt_number'],request.POST['creidt_type'],request.POST['creidt_expire'],\
                                   request.POST['creidt_csc'],request.POST['creidt_holder'],request.POST['creidt_address'],request.POST['creidt_city'],\
                                   request.POST['creidt_state'],request.POST['creidt_zip'])
    return HttpResponse(1)

def ajax_additem(request):
    if 'user' not in request.session:
        return HttpResponse(-1)
    elif quantityCheck(request.GET['id'],1):
            # id refer to movie id
            user = DAO_Proxy.findUserById(request.session['user']['id'])[0] if DAO_Proxy.findUserById(request.session['user']['id']) else None
            if not  DAO_Proxy.findOrderByUserId_Status(request.session['user']['id'], 0):
                DAO_Proxy.addOrderWithShipping_Credit(user.id, datetime.utcnow(), 0, 0, user.shipping_to, user.shipping_address, \
                                                user.shipping_city, user.shipping_state.id if user.shipping_state else None, user.shipping_zip, user.shipping_phone, \
                                                user.creidt_number, user.creidt_type, user.creidt_expire, user.creidt_csc, user.creidt_holder, \
                                                user.creidt_address, user.creidt_city,user.creidt_state.id if user.creidt_state else None, user.creidt_zip)
                
            order = DAO_Proxy.findOrderByUserId_Status(request.session['user']['id'], 0)[0]
            
            if DAO_Proxy.findItemByOrderId_MovieID(order.id, request.GET['id']):
                return HttpResponse(2)
            else:
                DAO_Proxy.addItem(request.GET['id'], order.id, 1, None)
                autoupdateordersummary(order.id)
                
                #Put log here
                createLog(request.session['user']['id'], request.GET['id'], 'order')
                
                return HttpResponse(1)
    else:
        return HttpResponse(0)
    
def vieworderlist(request):
    context = preload()
    
    orders = DAO_Proxy.findOrderByUserId_Status(request.session['user']['id'], 1).order_by('-time')
    
    current_page = int(request.GET['page'])
    start,end,totalpage = pagemanager(orders.count(),current_page,ORDER_PER_PAGE)
    
    orders = orders[start:end]
    
    context['orders'] = orders
    context['totalpage'] = totalpage
    return  render (request, 'customer-vieworderlist.html',context)

def vieworderdetail(request):
    context = preload()
    
    autoupdateordersummary(request.GET['id'])
    order = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
    items = DAO_Proxy.findItemByOrderId(request.GET['id'])
    
    context['order'] = order
    context['items'] = items
    context['subtotal'],context['tax'],context['total'] = autoupdateordersummary(order.id)
    return render(request, 'customer-vieworderdetail.html',context)

def modifyorder_page(request):
    context = preload()
    
    orders = DAO_Proxy.findOrderByUserId_Status(request.session['user']['id'], 0)
    
    if orders:
        autoupdateordersummary(orders[0].id)
        order = DAO_Proxy.findOrderByUserId_Status(request.session['user']['id'], 0)[0]
        items = DAO_Proxy.findItemByOrderId(order.id)
        
        context['order'] = order
        context['items'] = items
        context['subtotal'],context['tax'],context['total'] = autoupdateordersummary(order.id)
        
        return render(request, 'customer-modifyorder.html',context) 
    else:
        return redirect('/view_order_list/?page=1')

def ajax_updateitemquantity(request):
    if request.POST['quantity'] == '0':
        DAO_Proxy.deleteItem(request.POST['id'])
    else:
        DAO_Proxy.updateItemQuantity(request.POST['id'], request.POST['quantity'])
    return HttpResponse(1)

def ajax_check_deleteorder(request):
    if DAO_Proxy.findItemByOrderId(request.POST['id']):
        return HttpResponse(1)
    else:
        DAO_Proxy.deleteOrder(request.POST['id'])
        return HttpResponse(0)

def ajax_updateitempromotion(request):
    if request.POST['code']:
        promotions = DAO_Proxy.findPromotionByCode_MovieId(request.POST['code'], request.POST['movie_id'])
        if promotions:
            if checkpromotiondate(promotions[0]) == -1:
                return HttpResponse(-1)
            elif checkpromotiondate(promotions[0]) == -2:
                return HttpResponse(-2)
            else:
                DAO_Proxy.updateItemPromtion(request.POST['id'], promotions[0].id)
                autoupdateordersummary(request.POST['order_id'])
                return HttpResponse(1)
        else:
            return HttpResponse(0)
    else:
        DAO_Proxy.updateItemPromtion(request.POST['id'], None)
        autoupdateordersummary(request.POST['order_id'])
        return HttpResponse(2)

def viewordershipping(request):
    context = preload()
    
    context['order'] = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
    
    return render(request, 'customer-viewordershipping.html',context)

def modifyordershipping_page(request):
    context = preload()
    
    context['order'] = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
    
    return render(request, 'customer-updateshipping.html',context)

def ajax_ordershipping_modify(request):
    DAO_Proxy.updateOrderShipping(request.POST['id'], request.POST['shipping_to'], request.POST['shipping_address'], \
                                   request.POST['shipping_city'], request.POST['shipping_state'], request.POST['shipping_zip'], request.POST['shipping_phone'])
    return HttpResponse(1)

def viewordercredit(request):
    context = preload()
    
    context['order'] = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
    
    return render(request, 'customer-viewordercredit.html',context)

def modifyordercredit_page(request):
    context = preload()
    
    context['order'] = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
    
    return render(request, 'customer-updatecredit.html',context)

def ajax_ordercredit_modify(request):
    DAO_Proxy.updateOrderCredit(request.POST['id'], request.POST['creidt_number'], request.POST['creidt_type'], request.POST['creidt_expire'], \
                              request.POST['creidt_csc'], request.POST['creidt_holder'], request.POST['creidt_address'], request.POST['creidt_city'], \
                              request.POST['creidt_state'], request.POST['creidt_zip'])
    return HttpResponse(1)
    
def ajax_checkout(request):    
    if DAO_Proxy.findOrderById(request.POST['id']):
        if not DAO_Proxy.findOrderById(request.POST['id'])[0].shipping_to:
            return HttpResponse(-1)
        if not DAO_Proxy.findOrderById(request.POST['id'])[0].creidt_number:
            return HttpResponse(-2)
        message = checkitems(DAO_Proxy.findItemByOrderId(request.POST['id']))
        if message:
            return HttpResponse(json.dumps(message), content_type="application/json")
        else:
            for item in DAO_Proxy.findItemByOrderId(request.POST['id']):
                DAO_Proxy.updateMovieQuantity(item.movie.id, item.movie.quantity-item.quantity)
            autoupdateordersummary(request.POST['id'])
            DAO_Proxy.updateOrderStatus(request.POST['id'], 1)
            return HttpResponse(1)
    else:
        return HttpResponse(0)

def ajax_validate_account(request):
    return HttpResponse(1) if DAO_Proxy.findUserByAccount(request.POST['account']) else HttpResponse(0)

    # return vlalue is different from the old one
    '''
    if len(User.objects.filter(account=request.POST['account'])) == 0:
        return HttpResponse(1)
    else:
        return HttpResponse(0)
    '''

def ajax_register(request):
    new_user = DAO_Proxy.addUser(request.POST['account'], request.POST['password'], 1, request.POST['first'], request.POST['middle'], \
                request.POST['last'], request.POST['birthday'], request.POST['gender'], request.POST['occupation'], \
                request.POST['email'], request.POST['phone'], request.POST['city'], request.POST['state'], request.POST['zip'])
    
    return HttpResponse(1) if new_user else HttpResponse(0)
    
    # return vlalue is different from the old one
    #return HttpResponse()

def ajax_login(request):
    user = DAO_Proxy.findUserByAccount_Passowrd(request.POST['account'], request.POST['password'])
    if user:
        request.session['user'] = user_json(user[0])
        request.session.set_expiry(3600)
        #put log here
        return HttpResponse(1)
    else:
        return HttpResponse(0)
    
    
    
#Admin functions
def admin_home(request):
    context = preload()
    
    return render(request, 'admin-base.html',context)

#Login and out
def admin_login_page(request):
    context = preload()
    
    if 'admin' in request.session:
        return redirect('/admin_home/')
    else:
        return render(request, 'admin-login.html')

def admin_ajax_login(request):
    admin = DAO_Proxy.findAdminByAccount_Passowrd(request.POST['account'], request.POST['password'])
    if admin:
        request.session['admin'] = user_json(admin[0])
        request.session.set_expiry(3600)
        #put log here
        return HttpResponse(1)
    else:
        return HttpResponse(0)
    
def admin_logout(request):
    #Put log here
    request.session.flush()
    return redirect('/admin_login/')

#User
#Customer
def admin_findcustomer(request):
    context = preload()
    
    customers = DAO_Proxy.findUserByAccount_First_Last(request.GET['account'], request.GET['first'],request.GET['last'])
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(customers.count(),current_page,CUSTOMER_PER_PAGE)
    
    context['customers'] = customers[start:end]
    context['totalpage'] = totalpage
    context['account'] = request.GET['account']
    context['first'] = request.GET['first']
    context['last'] = request.GET['last']
        
    return render(request, 'admin-customerlist.html',context)

def admin_viewcustomer(request):
    context = preload()
    
    customers = DAO_Proxy.findUserById(request.GET['id'])
    
    context['customer'] = customers[0] if customers else None

    return render(request, 'admin-customerdetails.html',context)

def admin_update_profile_page(request):
    context = preload()
    
    context['customer'] = DAO_Proxy.findUserById(request.GET['id'])[0] if DAO_Proxy.findUserById(request.GET['id']) else None
    
    return render(request, 'admin-customerupdate.html',context)

def admin_ajax_modify_profile(request):
    DAO_Proxy.updateUserProfileById(request.POST['id'], request.POST['first'], request.POST['middle'], request.POST['last'], \
                                    request.POST['birthday'],request.POST['gender'], request.POST['occupation'], request.POST['email'], \
                                    request.POST['phone'], request.POST['city'], request.POST['state'], request.POST['zip'])
    
    return HttpResponse(1)

#Admin
def admin_addadmin(request):
    context = preload()
    
    if request.method == 'GET':
        return render(request, 'admin-addadmin.html',context)
    elif request.method == 'POST':
        new_admin = DAO_Proxy.addAdmin(request.POST['account'], request.POST['password'], 0, request.POST['first'], request.POST['last'])
    
        return HttpResponse(1) if new_admin else HttpResponse(0)
    else:
        return render(request, 'error.html',context)
    
def admin_findadmin(request):
    context = preload()
    
    admins = DAO_Proxy.findAdminByAccount_First_Last(request.GET['account'], request.GET['first'],request.GET['last'])
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(admins.count(),current_page,ADMIN_PER_PAGE)
    
    context['admins'] = admins[start:end]
    context['totalpage'] = totalpage
    context['account'] = request.GET['account']
    context['first'] = request.GET['first']
    context['last'] = request.GET['last']
        
    return render(request, 'admin-adminlist.html',context)

def admin_viewadmin(request):
    context = preload()
    
    admins = DAO_Proxy.findUserById(request.GET['id'])
    
    context['admin'] = admins[0] if admins else None

    return render(request, 'admin-admindetails.html',context)

def admin_update_adminprofile_page(request):
    context = preload()
    
    context['admin'] = DAO_Proxy.findUserById(request.GET['id'])[0] if DAO_Proxy.findUserById(request.GET['id']) else None
    
    return render(request, 'admin-adminupdate.html',context)

def admin_ajax_modify_adminprofile(request):
    DAO_Proxy.updateAdminProfileById(request.POST['id'], request.POST['first'], request.POST['last'])
    
    
    admin = DAO_Proxy.findUserById(request.session['admin']['id'])
    if admin:
        request.session['admin'] = user_json(admin[0])
        request.session.set_expiry(3600)
    
    return HttpResponse(1)

#Shared by Admin & Customer
def admin_updatepassword_page(request):
    context = preload()
    
    context['user_id'] = request.GET['id']
    context['user_type'] = request.GET['user_type']
    return render(request, 'admin-updatepassword.html',context)

def admin_ajax_password_modify(request):
    DAO_Proxy.updateUserPasswordById(request.POST['id'], request.POST['newpassword'])
    return HttpResponse(1)

def admin_deleteuser(request):
    context = preload()
    
    #check priority here
    if request.method == 'GET':
        DAO_Proxy.deleteUserById(request.GET['id'])
        return redirect('/admin_findcustomer/?account=&first=&last=&page=1')
    else:
        return render(request, 'error.html',context)

#Movie
def admin_findmovie(request):
    context = preload()
    
    movies = DAO_Proxy.findMovieByTitle(request.GET['title']) if request.GET['genre'] == '' \
                                else DAO_Proxy.findMovieByTitle_GenreId(request.GET['title'], request.GET['genre'])
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(movies.count(),current_page,ADMIN_MOVIE_PER_PAGE)
    
    movies = movies[start:end]
    
    context['totalpage'] = totalpage
    context['movies'] = movies
    context['title'] = str(request.GET['title'])
    context['genreid'] = str(request.GET['genre'])
    
    return  render (request, 'admin-movielist.html',context)

def admin_moviedetail(request):
    context = preload()

    context['movie'] = DAO_Proxy.findMovieById(request.GET['id'])[0] if DAO_Proxy.findMovieById(request.GET['id']) else None
    
    return  render (request, 'admin-moviedetail.html',context)

def admin_addmovie_page(request):
    context = preload()
    
    return render(request, 'admin-addmovie.html',context)
    
def admin_addmovie(request):
    context = preload()
    
    if request.method == 'POST':
        if 'ImageField' in request.FILES:
            img_name = datetime.now().strftime('%Y%m%d%H%M%S') + '_' + str(request.FILES['ImageField'])
            while os.path.isfile(IMG_DIR + img_name):
                img_name = '_' + img_name
            try:
                img = Image.open(request.FILES['ImageField'])
                #img.thumbnail((500,500),Image.ANTIALIAS)
                img.save(IMG_DIR + img_name,"JPEG")
            except Exception,e:
                print Exception,e
        else:
            img_name = 'default.png'
        id = DAO_Proxy.addMovie(request.POST['title'],request.POST['year'],request.POST['director'],request.POST['actor'],request.POST['description'],\
                           '/media/' +  img_name ,request.POST['price'],request.POST['quantity'],0.0,request.POST.getlist('genres'))

    return redirect('/admin_moviedetail/?id=' + str(id))

def admin_updatemovie_page(request):
    context = preload()
    
    context['movie'] = DAO_Proxy.findMovieById(request.GET['id'])[0] if DAO_Proxy.findMovieById(request.GET['id']) else None
    
    return render(request, 'admin-movieupdate.html',context)

def admin_updatemovie(request):
    context = preload()
    
    if request.method == 'POST':
        img_name = ""
        if'ImageField' in request.FILES:
            img_name = datetime.now().strftime('%Y%m%d%H%M%S') + '_' + str(request.FILES['ImageField'])
            while os.path.isfile(IMG_DIR + img_name):
                img_name = '_' + img_name
            
            try:
                img = Image.open(request.FILES['ImageField'])
                #img.thumbnail((500,500),Image.ANTIALIAS)
                img.save(IMG_DIR + img_name,"JPEG")
                img_name = '/media/' + img_name
            except Exception,e:
                print Exception,e
        else:
            img_name = request.POST['picture']
            
        DAO_Proxy.updateMovieById(request.POST['id'],request.POST['title'],request.POST['year'],request.POST['director'],request.POST['actor'],request.POST['description'],\
                           img_name,request.POST['price'],request.POST['quantity'],request.POST.getlist('genres'))
    
    return redirect('/admin_moviedetail/?id=' + request.POST['id'])

def admin_deletemovie(request):
    context = preload()
    if request.method == 'GET':
        DAO_Proxy.deleteMovieById(request.GET['id'])
        return redirect('/admin_findmovie/?title=&genre=&page=1')
    else:
        return render(request, 'error.html',context)
    
#Promotion
def admin_findpromotion(request):
    context = preload()
    
    promotions = DAO_Proxy.findPromotionByCode_Begin_End(request.GET['code'],request.GET['begin'],request.GET['end'])
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(promotions.count(),current_page,ADMIN_PROMOTION_PER_PAGE)
    
    context['totalpage'] = totalpage
    context['promotions'] = promotions[start:end]
    context['code'] = request.GET['code']
    context['begin'] = request.GET['begin']
    context['end'] = request.GET['end']
    
    return render(request, 'admin-promotionlist.html',context)

def admin_addpromotion_page(request):
    context = preload()
    
    return render(request, 'admin-addpromotion.html',context)

def admin_ajax_code_isexisted(request):
    
    if DAO_Proxy.findPromotionByCode_Begin_End(request.POST['code'],'',''):
        return HttpResponse(1)
    else:
        return HttpResponse(0)
    
def admin_addpromotion(request):
    context = preload()
    
    id = DAO_Proxy.addPromotion(request.POST['code'],request.POST['begin'],request.POST['end'],request.POST['discount']).id
    
    return redirect('/admin_viewpromotionviewdetails/?id=' + str(id) + '&page=1')

def admin_promotion_addmovie_page(request):
    context = preload()
    
    movie_list = [str(movie.id) for movie in DAO_Proxy.findMovieWithPromotion(request.GET['id'])]
    
    movies = DAO_Proxy.findMovieInSetByTitle_GenreId(DAO_Proxy.findMovieNotInList(movie_list),request.GET['title'],request.GET['genre_id'])
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(len(movies),current_page,ADMIN_MOVIE_PER_PAGE)
    
    context['totalpage'] = totalpage
    context['movies'] = movies[start:end]
    context['title'] = request.GET['title']
    context['promotion_id'] = request.GET['id']
    
    return render(request, 'admin-promotionaddmovie.html',context)

def admin_ajax_promotion_addmovie(request):
    
    if request.POST:
        DAO_Proxy.addMoviesToPromotion(request.POST['promotionid'],request.POST.getlist('movieid_list[]'))
    return HttpResponse(1)

def admin_promotion_removemovie_page(request):
    context = preload()
    
    movie_list = [str(movie.id) for movie in DAO_Proxy.findMovieWithPromotion(request.GET['id'])]
    
    movies = DAO_Proxy.findMovieInSetByTitle_GenreId(DAO_Proxy.findMovieInList(movie_list),request.GET['title'],request.GET['genre_id'])
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(len(movies),current_page,ADMIN_MOVIE_PER_PAGE)
    
    context['totalpage'] = totalpage
    context['movies'] = movies[start:end]
    context['title'] = request.GET['title']
    context['promotion_id'] = request.GET['id']
    
    return render(request, 'admin-promotionremovemovie.html',context)

def admin_ajax_promotion_removemovie(request):
    
    if request.POST:
        DAO_Proxy.removeMoviesFromPromotion(request.POST['promotionid'],request.POST.getlist('movieid_list[]'))
    return HttpResponse(1)

def admin_viewpromotionviewdetails(request):
    context = preload()
    
    promotion = DAO_Proxy.findPromotionById(request.GET['id'])[0] if DAO_Proxy.findPromotionById(request.GET['id']) else None
        
    movies = DAO_Proxy.findMovieWithPromotion(request.GET['id'])
    
    current_page = int(request.GET['page'])
    
    start,end,totalpage = pagemanager(len(movies),current_page,ADMIN_PROMOTION_MOVIE_PER_PAGE)
    
    context['totalpage'] = totalpage
    context['movies'] = movies[start:end]
    context['promotion'] = promotion
    
    return render(request, 'admin-promotiondetails.html',context)

def admin_updatepromotion(request):
    context = preload()

    if request.method == 'GET':
        if DAO_Proxy.findPromotionById(request.GET['id']):
            context['promotion'] = DAO_Proxy.findPromotionById(request.GET['id'])[0]
            return render(request, 'admin-promotionupdate.html',context)
        else:
            return redirect('/admin_findpromotion/?code=&begin=&end=&page=1')
    elif request.method == 'POST':
        DAO_Proxy.updatePromotionAt_Begin_End_Discount(request.POST['id'],request.POST['begin'],request.POST['end'],request.POST['discount'])
        return redirect('/admin_viewpromotionviewdetails/?id=' + request.POST['id'] + '&page=1')
    else:
        return render(request, 'error.html',context)
    
def admin_deletepromotion(request):
    context = preload()
    
    if request.method == 'GET':
        DAO_Proxy.deletePromotion(request.GET['id'])
        return redirect('/admin_findpromotion/?code=&begin=&end=&page=1')
    else:
        return render(request, 'error.html',context)

#Order
def admin_findorder(request):
    context = preload()
    
    if request.method == 'GET':
        
        orders = DAO_Proxy.findOrderByAccount_Status(request.GET['account'],request.GET['status'])
        
        current_page = int(request.GET['page'])
        start,end,totalpage = pagemanager(orders.count(),current_page,ADMIN_ORDER_PER_PAGE)
        orders = orders[start:end]
        
        context['totalpage'] = totalpage
        context['account'] = request.GET['account']
        context['status'] = request.GET['status']
        context['orders'] = orders
        
        return render(request, 'admin-orderlist.html',context)
    else:
        return render(request, 'error.html',context)
    
def admin_vieworderdetail(request):
    context = preload()
    
    if request.method == 'GET':
        if 'shipping' in request.GET:
            context['order'] = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
    
            return render(request, 'admin-viewordershipping.html',context)
        elif 'credit' in request.GET:
            context['order'] = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
            
            return render(request, 'admin-viewordercredit.html',context)
        else:
            autoupdateordersummary(request.GET['id'])
            order = DAO_Proxy.findOrderById(request.GET['id'])[0] if DAO_Proxy.findOrderById(request.GET['id']) else None
            items = DAO_Proxy.findItemByOrderId(request.GET['id'])
            
            context['order'] = order
            context['items'] = items
            context['subtotal'],context['tax'],context['total'] = autoupdateordersummary(order.id)
            return render(request, 'admin-vieworderdetail.html',context)
        
    else:
        return render(request, 'error.html',context)
    
def admin_shiporder(request):
    context = preload()
    
    if request.method == 'GET':
        DAO_Proxy.updateOrderStatus(request.GET['id'],2)
        
        return redirect('/admin_vieworderdetail/?id=' + str(request.GET['id']))
    else:
        return render(request, 'error.html',context)
    