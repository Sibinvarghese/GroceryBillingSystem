from django.shortcuts import render,redirect
from billing.models import Product,Purchase,Order,OrderLines
from billing.forms import ProductCreateForm,PurchaseCreateForm,OrderCreateForm,OrderlinesCreateForm
from django.views.generic import TemplateView
from django.db.models import Sum
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
        self.context["form"]=products
        return render(request, self.template_name, self.context)

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
        self.context["form"]=purchases
        return render(request,self.template_name,self.context)

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
        form=OrderCreateForm
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
            price = Purchase.objects.get(product=product_name)
            qtys=price.qty
            sellprices=price.selling_price
            amounts=product_qy*sellprices

            # print(qtys, sellprices)
            # print(amounts)
            balanceqty=qtys-product_qy
            # print(balanceqty)
            price.qty=balanceqty
            price.save()

            self.context["price"] = price
            bill = Order.objects.get(billnumber=billnum)


            form = OrderlinesCreateForm(initial={"bill_number": bill})

            self.context["form"] = form
            val=OrderLines(bill_number=bill,product_name=product_name,product_qty=product_qy,amount=amounts)
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

class View_Bill(TemplateView):
    model=OrderLines
    template_name = "billing/bill_view.html"
    context={}

    def get_object(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        billsnumber = self.get_object()
        self.context["forms"] = billsnumber
        return render(request,self.template_name,self.context)

class View_ToatlBill(TemplateView):
    model=Order
    template_name = "billing/bill_total_views.html"
    context={}
    def get_object(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        allval=self.get_object()
        self.context["forms"]=allval
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            billnum = form.cleaned_data.get("billnumber")
            return redirect("viewbilldetails", billno=billnum)
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)
class View_BillDetails(TemplateView):
    model=Order
    template_name = "billing/bill_view.html"
    context={}
    def get_object(self,billnum):
        return self.model.objects.filter(billnumber=billnum)

    def get(self, request, *args, **kwargs):
        billnum = self.get_object(kwargs.get("billnumber"))
        # print(billnum)
        getorderlinesdatas = billnum
        self.context["forms"] = getorderlinesdatas


        # self.context["forms"] = getorderlinesdatas
        return render(request, self.template_name, self.context)


