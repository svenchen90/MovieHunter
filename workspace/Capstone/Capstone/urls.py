from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Capstone.views.home', name='home'),
    # url(r'^Capstone/', include('Capstone.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url
    (r'^$','shutter.views.home'),
    (r'^rating/$','shutter.views.ajax_rating'),
    
    (r'^toprating/$','shutter.views.toprating'),
    (r'^recommend/$','shutter.views.recommend'),
    
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    
    (r'^login/$','shutter.views.login_page'),
    (r'^logout/$', 'shutter.views.logout'),
    (r'^register/$','shutter.views.register_page'),
    (r'^search_movie/$','shutter.views.searchmovie'),
    (r'^movie_detail/$','shutter.views.moviedetail'),
    (r'^customer_home/$','shutter.views.customerhome'),
    (r'^view_profile/$','shutter.views.viewprofile'),
    
    (r'^ajax_modify_profile/$','shutter.views.ajax_modify_profile'),
    (r'^modify_profile_page/$','shutter.views.modify_profile_page'),
    
    (r'^ajax_password_modify/$','shutter.views.ajax_password_modify'),
    (r'^change_password_page/$','shutter.views.change_password_page'),
    (r'^view_shipping/$','shutter.views.viewshipping'),
    (r'^modify_shipping/$','shutter.views.modifyshipping_page'),
    (r'^view_credit/$','shutter.views.viewcredit'),
    (r'^modify_credit/$','shutter.views.modifycredit_page'),
    (r'^view_order_list/$','shutter.views.vieworderlist'),
    (r'^view_order_detail/$','shutter.views.vieworderdetail'),
    (r'^modify_order/$','shutter.views.modifyorder_page'),
    
    (r'^view_ordershipping/$','shutter.views.viewordershipping'),
    (r'^view_ordercredit/$','shutter.views.viewordercredit'),
    (r'^modifyordershipping_page/$','shutter.views.modifyordershipping_page'),
    (r'^modifyordercredit_page/$','shutter.views.modifyordercredit_page'),
    
    (r'^forgetpassword/$','shutter.views.forgetpassword'),
    
    (r'^ajax_checkout/$','shutter.views.ajax_checkout'),
    (r'^ajax_ordercredit_modify/$','shutter.views.ajax_ordercredit_modify'),
    (r'^ajax_ordershipping_modify/$','shutter.views.ajax_ordershipping_modify'),
    (r'^ajax_updateitempromotion/$','shutter.views.ajax_updateitempromotion'),
    (r'^ajax_check_deleteorder/$','shutter.views.ajax_check_deleteorder'),
    (r'^ajax_updateitemquantity/$','shutter.views.ajax_updateitemquantity'),
    (r'^ajax_additem/$','shutter.views.ajax_additem'),
    (r'^ajax_usercredit_modify/$','shutter.views.ajax_usercredit_modify'),
    (r'^ajax_usershipping_modify/$','shutter.views.ajax_usershipping_modify'),
    (r'^ajax_validate_account/$','shutter.views.ajax_validate_account'),
    (r'^ajax_register/$','shutter.views.ajax_register'),
    (r'^ajax_login/$','shutter.views.ajax_login'),
    
    #admin
    (r'^admin_login/$','shutter.views.admin_login_page'),
    (r'^admin_ajax_login/$','shutter.views.admin_ajax_login'),
    (r'^admin_logout/$','shutter.views.admin_logout'),
    (r'^admin_home/$','shutter.views.admin_home'),
    (r'^admin_findcustomer/$','shutter.views.admin_findcustomer'),
    (r'^admin_viewcustomer/$','shutter.views.admin_viewcustomer'),
    (r'^admin_ajax_modify_profile/$','shutter.views.admin_ajax_modify_profile'),
    (r'^admin_update_profile_page/$','shutter.views.admin_update_profile_page'),
    (r'^admin_findadmin/$','shutter.views.admin_findadmin'),
    (r'^admin_viewadmin/$','shutter.views.admin_viewadmin'),
    (r'^admin_update_adminprofile_page/$','shutter.views.admin_update_adminprofile_page'),
    (r'^admin_ajax_modify_adminprofile/$','shutter.views.admin_ajax_modify_adminprofile'),
    (r'^admin_updatepassword_page/$','shutter.views.admin_updatepassword_page'),
    (r'^admin_ajax_password_modify/$','shutter.views.admin_ajax_password_modify'),
    (r'^admin_addmovie_page/$','shutter.views.admin_addmovie_page'),
    (r'^admin_addmovie/$','shutter.views.admin_addmovie'),
    (r'^admin_findmovie/$','shutter.views.admin_findmovie'),
    (r'^admin_moviedetail/$','shutter.views.admin_moviedetail'),
    (r'^admin_updatemovie_page/$','shutter.views.admin_updatemovie_page'),
    (r'^admin_updatemovie/$','shutter.views.admin_updatemovie'),
    (r'^admin_findpromotion/$','shutter.views.admin_findpromotion'),
    (r'^admin_addpromotion_page/$','shutter.views.admin_addpromotion_page'),
    (r'^admin_ajax_code_isexisted/$','shutter.views.admin_ajax_code_isexisted'),
    (r'^admin_addpromotion/$','shutter.views.admin_addpromotion'),
    (r'^admin_promotion_addmovie_page/$','shutter.views.admin_promotion_addmovie_page'),
    (r'^admin_promotion_removemovie_page/$','shutter.views.admin_promotion_removemovie_page'),
    (r'^admin_ajax_promotion_addmovie/$','shutter.views.admin_ajax_promotion_addmovie'),
    (r'^admin_ajax_promotion_removemovie/$','shutter.views.admin_ajax_promotion_removemovie'),
    (r'^admin_viewpromotionviewdetails/$','shutter.views.admin_viewpromotionviewdetails'),
    (r'^admin_updatepromotion/$','shutter.views.admin_updatepromotion'),
    (r'^admin_deletepromotion/$','shutter.views.admin_deletepromotion'),
    (r'^admin_deletemovie/$','shutter.views.admin_deletemovie'),
    (r'^admin_deleteuser/$','shutter.views.admin_deleteuser'),
    (r'^admin_findorder/$','shutter.views.admin_findorder'),
    (r'^admin_vieworderdetail/$','shutter.views.admin_vieworderdetail'),
    (r'^admin_shiporder/$','shutter.views.admin_shiporder'),
    (r'^admin_addadmin/$','shutter.views.admin_addadmin')
    
)