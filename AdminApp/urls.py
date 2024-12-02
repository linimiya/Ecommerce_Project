from django.urls import path
from AdminApp import views

urlpatterns = [
    path('addcategoriespage/',views.addcategoriespage,name='addcategoriespage'),
    path('indexpage/',views.indexpage,name='indexpage'),
    path('save_Catgory_DB/',views.save_Catgory_DB,name='save_Catgory_DB'),
    path('displaycategoriespagefun/',views.displaycategoriespagefun,name='displaycategoriespagefun'),
    path('editcategoriespagefun/<int:e_id>/',views.editcategoriespagefun,name='editcategoriespagefun'),
    path('updateCategory_DB/<int:u_id>/',views.updateCategory_DB,name='updateCategory_DB'),
    path('add_Products_Page_fun/',views.add_Products_Page_fun,name='add_Products_Page_fun'),
    path('Save_Product_DB/',views.Save_Product_DB,name='Save_Product_DB'),
    path('Display_Productsfun/',views.Display_Productsfun,name='Display_Productsfun'),
    path('Edit_Products/<int:e_id>/',views.Edit_Products,name='Edit_Products'),
    path('update_Product_DB/<int:Pu_id>/',views.update_Product_DB,name='update_Product_DB'),
    path('delete_products/<int:del_id>/',views.delete_products,name='delete_products'),
    path('delete_Catgory_DB/<int:del_id>/',views.delete_Catgory_DB,name='delete_Catgory_DB'),
    path('admin_loginfun/',views.admin_loginfun,name='admin_loginfun'),
    path('admin_login_Validation/',views.admin_login_Validation,name='admin_login_Validation'),
    path('Admin_logout/',views.Admin_logout,name='Admin_logout'),
    path('test1page/',views.test1page,name='test1page')

]

