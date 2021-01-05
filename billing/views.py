from django.shortcuts import render,redirect
from billing.models import Product,Purchase,Order,OrderLines
from billing.forms import ProductCreateForm,PurchaseCreateForm,OrderCreateForm,OrderlinesCreateForm
from django.views.generic import TemplateView
from django.db.models import Sum
from django.core.paginator import Paginator
from .filters import OrderFilter
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class CreateProduct(TemplateView):
    form_class=ProductCreateForm
    template_name = "billing/product_create.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=ProductCreateForm
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=ProductCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, self.context)
            # return render(request,"billing/product_list.html", self.context)
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

class ViewProduct(TemplateView):
    model=Product
    template_name = "billing/product_list.html"
    context={}

    def get(self, request, *args, **kwargs):
        products=self.model.objects.all()
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})

class HomePage(TemplateView):
    template_name = "billing/home_page.html"

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

class EditProduct(TemplateView):
    model=Product
    template_name = "billing/edit_product.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        products=self.get_object(kwargs.get("pk"))
        form=ProductCreateForm(instance=products)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        products = self.get_object(kwargs.get("pk"))
        form = ProductCreateForm(instance=products,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class DeleteProduct(TemplateView):
    model=Product

    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        products=self.get_object(kwargs.get("pk"))
        products.delete()
        return redirect("home")

class CreatePurchase(TemplateView):
    form_class=PurchaseCreateForm
    template_name = "billing/purchase_add.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=PurchaseCreateForm
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=PurchaseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class ViewPurchase(TemplateView):
    model=Purchase
    template_name = "billing/purchase_view.html"
    context={}

    def get_object(self):
        return self.model.objects.all()
    def get(self, request, *args, **kwargs):
        purchases=self.get_object()
        paginator = Paginator(purchases,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})

class EditPurchase(TemplateView):
    model=Purchase
    template_name = "billing/purchase_edit.html"
    context={}

    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        purchases=self.get_object(kwargs.get("pk"))
        form=PurchaseCreateForm(instance=purchases)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        purchases = self.get_object(kwargs.get("pk"))
        form = PurchaseCreateForm(instance=purchases,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class DeletePurchase(TemplateView):
    model=Purchase

    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        purchase=self.get_object(kwargs.get("pk"))
        purchase.delete()
        return redirect("home")

class OrderCreate(TemplateView):
    model=Order
    template_name = "billing/billing.html"
    context={}

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all().last()
        billnumber=int(orders.billnumber)
        billnumber+=1
        billnumber=str(billnumber)

        form=OrderCreateForm(initial={"billnumber":billnumber})
        self.context["form"]=form

        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            billnum=form.cleaned_data.get("billnumber")
            form.save()
            return redirect("orderlines",billno=billnum)
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

class OrderLinesView(TemplateView):
    model=OrderLines
    template_name = "billing/orderlines.html"
    context={}
    def get(self, request, *args, **kwargs):
        billnum=kwargs.get("billno")
        self.context["billnumber"] = billnum
        print(billnum)
        bill=Order.objects.get(billnumber=billnum)
        form=OrderlinesCreateForm(initial={"bill_number":bill})
        self.context["form"]=form
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form=OrderlinesCreateForm(request.POST)
        if form.is_valid():
            billnumb = kwargs.get("billno")
            product_name = form.cleaned_data.get("product_name")
            billnum=form.cleaned_data.get("bill_number")
            product_qy=form.cleaned_data.get("product_qty")
            # print(billnum,product_name,product_qy)
            getproductname=Product.objects.get(product_name=product_name)
            price = Purchase.objects.get(product__product_name=product_name)
            qtys=price.qty
            sellprices=price.selling_price
            amounts=product_qy*sellprices
            balanceqty=qtys-product_qy
            # print(balanceqty)
            price.qty=balanceqty
            price.save()
            self.context["price"] = price
            bill = Order.objects.get(billnumber=billnum)
            form = OrderlinesCreateForm(initial={"bill_number": bill})
            self.context["form"] = form
            val=OrderLines(bill_number=bill,product_name=getproductname,product_qty=product_qy,amount=amounts)
            val.save()
            sumofamount=OrderLines.objects.filter(bill_number=bill).aggregate(Sum('amount'))
            self.context["total"] = sumofamount
            # print(sumofamount)
            bill.bill_total=sumofamount
            print(bill.bill_total["amount__sum"])
            Order.objects.filter(billnumber=billnum).update(bill_total= bill.bill_total["amount__sum"])
            getorderlinesdatas=OrderLines.objects.filter(bill_number=bill)
            self.context["forms"]=getorderlinesdatas
            return render(request, self.template_name, self.context)
        else:
            self.context["form"] = form

            return render(request, self.template_name, self.context)

class BillGenerate(TemplateView):
    model = OrderLines
    template_name = "billing/bill_generate.html"
    context = {}
    def get_object(self,id):
        return self.model.objects.get(bill_number=id)

    def get(self, request, *args, **kwargs):
        billnum = kwargs.get("billno")
        print(billnum)
        bill = Order.objects.get(billnumber=billnum)
        self.context["getorder"] = bill
        getorderlinesdatas = OrderLines.objects.filter(bill_number__billnumber=billnum)
        self.context["getallitems"] = getorderlinesdatas
        return render(request, self.template_name, self.context)

class ViewBill(TemplateView):
    model=Order
    template_name = "billing/bill_total_views.html"
    context={}
    def get_object(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        getallbill=self.get_object()
        paginator = Paginator(getallbill, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,self.template_name, {'page_obj': page_obj})

class ViewBillItems(TemplateView):
    model=Order
    template_name = "billing/bill_view.html"
    context={}

    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        billnum=self.get_object(kwargs.get("billno"))
        self.context["billno"]=billnum

        billitems=OrderLines.objects.filter(bill_number=billnum)
        self.context["billitems"]=billitems

        return render(request, self.template_name, self.context)

class SearchOrder(TemplateView):
    model=Order
    template_name = "billing/bill_search.html"
    context={}

    def get_object(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        billnum=self.get_object()
        myfilter=OrderFilter(request.GET,queryset=billnum)
        billno=myfilter.qs
        self.context["billno"]=billno
        self.context["myfilter"]=myfilter
        return render(request,self.template_name,self.context)

class HomePageFinal(TemplateView):
    template_name = "billing/homepageview.html"

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

class UserLogin(TemplateView):
    template_name = "billing/login.html"
    # context={}
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        uname="admin"
        pwd="123"
        username=request.POST["username"]
        password=request.POST["password"]
        print(username,password)
        if uname==username and pwd==password:
            print("success")
            return redirect("page")
        else:
            print("invalid")
            return render(request,self.template_name)

class UserLogout(TemplateView):


    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")
