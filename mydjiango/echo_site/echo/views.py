# _*_ coding:utf-8 _*__
from django.shortcuts import render, redirect
from .models import Node
from forms import NodeForm, LineForm, Device
# Create your views here.
def lists(request):
    # 从 node 节点获得所有数据
    data = Node.objects.all()
    #建立context字典，将值传递到相应页面
    context = {
                'data': data,
    }
    #跳转到相应页面，并将值传递过去
    return render(request,'lists.html',context)

def add(request):
    #获取来自NodeForm的表单数据
    form = NodeForm(request.POST or None)
    #判断form是否有效
    if form.is_valid():
        #创建实例，需要做些数据处理，暂不做保存
        instance = form.save(commit=False)
        #将登录用户作为登记人
        instance.node_signer = request.user
        #保存该实例
        instance.save()
        #跳转至列表页面
        return redirect('/lists/')

    #创建context来集中处理需要传递到页面的数据
    context = {
                 'form': form,
             }
    #如果没有有效提交，则仍留在原来页面
    return render(request, 'add.html',  context)
