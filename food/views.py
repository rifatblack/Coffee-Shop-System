from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import generics, permissions
from .forms import OrderForm
from .models import OrderInstance, BusinessObject
from .serializers import OrderSerializer
from .permissions import IsBaristaOnly

@login_required
@permission_required('food.can_order', raise_exception=True)
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            coffee_order = form.cleaned_data['coffee_order']
       
            customer_order = OrderInstance(name=name, email=email, coffee_order=coffee_order)
            customer_order.save()
            
         
            request.session['pp_order'] = True

         
            dict_order = model_to_dict(customer_order)
            request.session['order_data'] = dict_order
            return redirect('food:success')
    else:
        form = OrderForm()
    return render(request, "food/order.html", { 'form':form })

def homepage(request):
    return render(request, "food/homepage.html")

@login_required
@permission_required('food.can_serve', raise_exception=True)
def prepare(request):
    if request.method == 'POST':
        obj = BusinessObject.objects.first()
        obj.business_status = request.POST['business_status']
        obj.save()
        business_status = obj.business_status
    else:
        business_status = BusinessObject.objects.first().business_status
    orders = OrderInstance.objects.all()
    return render(request, "food/prepare.html", { 'orders':orders, 'business_status':business_status })

@login_required
def success(request):
    if 'pp_order' in request.session:
        del request.session['pp_order'] 
        return render(request, "food/orderSuccess.html", { 'order_data': request.session['order_data'] })
    else:
        return HttpResponseBadRequest('<h1>HTTP Error 400: You need to place an order!</h1>')

def business(request):
    business_status = BusinessObject.objects.first().business_status
    return render(request, 'food/business.html', { 'business_status':business_status })

class OrderList(generics.ListCreateAPIView):
    queryset = OrderInstance.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderInstance.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsBaristaOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)