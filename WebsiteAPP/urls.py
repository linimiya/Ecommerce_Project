from django.urls import path
from WebsiteAPP import views

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('productspage/',views.productspage,name='productspage'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('Save_Contact_DB/',views.Save_Contact_DB,name='Save_Contact_DB'),
    path('display_contact_page/',views.display_contact_page,name='display_contact_page'),
    path('filtered_product_page/<Cat_name>',views.filtered_product_page,name='filtered_product_page'),
    path('Single_product_page/<int:prod_id>/',views.Single_product_page,name='Single_product_page'),
    path('signup_page/',views.signup_page,name='signup_page'),
    path('login_page/',views.login_page,name='login_page'),
    path('save_Signup_DB/',views.save_Signup_DB,name='save_Signup_DB'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('Save_Cart_DB/',views.Save_Cart_DB,name='Save_Cart_DB'),
    path('cart_page/',views.cart_page,name='cart_page'),
    path('check_outpage/',views.check_outpage,name='check_outpage'),
    path('Save_Order_DB/',views.Save_Order_DB,name='Save_Order_DB'),
    path('paymentpage/',views.paymentpage,name='paymentpage')



]