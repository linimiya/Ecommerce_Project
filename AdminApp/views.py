from django.shortcuts import render,redirect
from AdminApp.models import Catgory_DB,Product_DB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from datetime import datetime
from django.contrib import messages

def addcategoriespage(res):
    return render(res,'Addcategories.html')

def indexpage(res):
    today_date = datetime.now()
    count_cat=Catgory_DB.objects.count()
    count_prod = Product_DB.objects.count()
    return render(res,'index.html',{'today_date':today_date,'count_cat':count_cat,'count_prod':count_prod})

def save_Catgory_DB(request):
    if request.method=='POST':
        ab=request.POST.get('tcatname')
        ac=request.FILES['timage1']
        ad=request.FILES['timage2']
        ae=request.FILES['timage3']
        obj1=Catgory_DB(Category_Name=ab,Category_Image1=ac,Category_Image2=ad,Category_Image3=ae)
        obj1.save()
        messages.success(request,'Saved category')
        return redirect(addcategoriespage)
def displaycategoriespagefun(res):
    cat=Catgory_DB.objects.all()
    return render(res,'displaycategories.html',{'cat':cat})

def editcategoriespagefun(request,e_id):
    edobj=Catgory_DB.objects.get(id=e_id)
    return render(request,'editcategories.html',{'edobj':edobj})

def updateCategory_DB(request,u_id):
    if request.method=='POST':
        ua=request.POST.get('tcatname')
        try:
            img1=request.FILES['timage1']
            fs=FileSystemStorage()
            file1=fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1=Catgory_DB.objects.get(id=u_id). Category_Image1
        try:
            img2 = request.FILES['timage2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2=Catgory_DB.objects.get(id=u_id). Category_Image2
        try:
            img3 = request.FILES['timage2']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3=Catgory_DB.objects.get(id=u_id). Category_Image3
        Catgory_DB.objects.filter(id=u_id).update(Category_Name=ua,
                                                  Category_Image1=file1,
                                                  Category_Image2=file2,
                                                  Category_Image3=file3)
        return redirect(displaycategoriespagefun)


def delete_Catgory_DB(request, del_id):
    x=Catgory_DB.objects.filter(id=del_id)
    x.delete()
    return redirect(displaycategoriespagefun)

def add_Products_Page_fun(request):
    cat_P_id=Catgory_DB.objects.all()
    return render(request,'Add_Products.html',{'cat_P_id':cat_P_id})


def Save_Product_DB(request):
    if request.method=='POST':
        pz=request.POST.get('tCategory_Name')
        pa=request.POST.get('tprodname')
        pp=request.POST.get('tperprice')
        pb=request.FILES['tprodimg1']
        pc=request.FILES['tprodimg2']
        pd=request.FILES['tprodimg3']
        obj2 =Product_DB(Category_of_Product=pz,Product_Name=pa,Product_Image1=pb,Product_Image2=pc,Product_Image3=pd,Product_Price=pp)
        obj2.save()
        messages.success(request, 'Saved Product')
        return redirect(add_Products_Page_fun)

def Display_Productsfun(request):
    disobj=Product_DB.objects.all()

    return render(request,'Display_Products.html',{'disobj':disobj})


def Edit_Products(request,e_id):
    eobj=Product_DB.objects.get(id=e_id)
    cat1 = Catgory_DB.objects.all()
    return render(request,'Edit_Products.html',{'eobj':eobj,'cat1':cat1})

def update_Product_DB(request,Pu_id):
    if request.method=='POST':
        ua=request.POST.get('tCategory_Name')
        ub=request.POST.get('tprodname')
        try:
            pimg1=request.FILES['tprodimg1']
            fs=FileSystemStorage()
            file1=(pimg1.name,pimg1)
        except MultiValueDictKeyError:
            file1=Product_DB.objects.get(id=Pu_id).Product_Image1
        try:
            pimg2=request.FILES['tprodimg2']
            fs=FileSystemStorage()
            file2=(pimg2.name,pimg2)
        except MultiValueDictKeyError:
            file2=Product_DB.objects.get(id=Pu_id).Product_Image2
        try:
            pimg3=request.FILES['tprodimg3']
            fs=FileSystemStorage()
            file3=(pimg3.name,pimg3)
        except MultiValueDictKeyError:
            file3=Product_DB.objects.get(id=Pu_id).Product_Image3

    Product_DB.objects.filter(id=Pu_id).update(Category_of_Product=ua,Product_Name=ub,
                                               Product_Image1=file1,Product_Image2=file2,
                                               Product_Image3=file3)
    return redirect(Display_Productsfun)

def delete_products(request,del_id):
    x=Product_DB.objects.filter(id=del_id)
    x.delete()
    return redirect(Display_Productsfun)

def admin_loginfun(request):

    return render(request,'Adminlogin.html',)
# Create your views here.
def admin_login_Validation(request):
    if request.method=='POST':
        un=request.POST.get('username')
        pswd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                request.session['username'] = un
                request.session['password'] = pswd
                return redirect(indexpage)
            else:
                messages.error(request, 'password doenot match check ')
                return redirect(admin_loginfun)
        else:
            messages.error(request, 'User doesnot exist')
            return redirect(admin_loginfun)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request, 'logged out successfully ')
    return redirect(admin_loginfun)

def test1page(request):
    return render(request,'test1.html')