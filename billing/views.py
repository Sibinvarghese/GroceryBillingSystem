from django.shortcuts import render,redirect
from billing.models import Product,Purchase
from billing.forms import ProductCreateForm,PurchaseCreateForm
from django.views.generic import TemplateView
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

