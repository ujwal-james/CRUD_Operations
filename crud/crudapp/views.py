from django.shortcuts import render, redirect, get_object_or_404
from . models import Crud

def home(request):
    ans=Crud.objects.all()
    if request.method=='POST':
        slno=request.POST.get('sl_no','')
        Itemname=request.POST.get('item_name','')
        desc=request.POST.get('desc','')
        task=Crud(slno=slno,Item_name=Itemname,Description=desc)
        task.save()
    return render(request,'index.html',{'item':ans})

def delete(request,taskid):
    dlt=Crud.objects.get(id=taskid)
    if request.method=='POST':
        dlt.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    upt=get_object_or_404(Crud,id=id)
    if request.method=='POST':
        upt.slno=request.POST.get('sl_no')
        upt.Item_name=request.POST.get('item_name')
        upt.Description=request.POST.get('desc')
        upt.save()
        return redirect('/')
    return render(request,'update.html',{'upt':upt})






