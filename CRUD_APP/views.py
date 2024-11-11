from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,render
from .forms import OrderForm, Order
import json
from django.core.serializers import serialize
# Create your views here.
def addOrder_view(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_urls')
    template_name = 'CRUD_APP/add.html'
    context = {'form':form}
    return render(request,template_name,context)

def show_view(request):
    obj = Order.objects.all()
    template_name = 'CRUD_APP/show.html'
    context = {'data':obj}
    return render(request,template_name,context)


def get_via_id(request):
    ids=request.GET.get('id')
    print(ids)
    res = Order.objects.filter(id=ids)
    json_data = serialize('json', res)
    return JsonResponse({"response": json_data})

def get_via_name(request):
    names=request.GET.get('name')
    print(names)
    res = Order.objects.filter(ename=names)
    json_data =serialize('json',res)
    return JsonResponse({"response": json_data})

def get_via_gmail(request):
    gmail=request.GET.get('email')
    res = Order.objects.filter()


def delete_view(request, pk):
    obj = Order.objects.filter(eid=pk)
    if request.method == 'POST':
        for i in obj:
            i.delete()
        return redirect('show_urls')
    template_name = 'CRUD_APP/del_confirm.html'
    context = {'data': obj }
    return render(request, template_name, context)



def update_view(request, upk):
    print(upk)
    obj = Order.objects.get(eid=upk)
    form = OrderForm(instance = obj)
    if request.method == 'POST':
        form = OrderForm(data=request.POST , instance = obj)
        if form.is_valid():
            form.save()
            return redirect('show_urls')
    template_name = 'CRUD_APP/add.html'
    context = {'form': form}
    return render(request,template_name,context)