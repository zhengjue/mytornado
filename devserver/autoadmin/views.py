# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.shortcuts import render_to_response
import os,sys,time
from django.http import HttpResponse
from autoadmin.models import ModuleList
from autoadmin.models import ServerList
from autoadmin.models import ServerAppCateg
from autoadmin.models import ServerFunCateg
from django.conf import settings
from django.utils.log import logging
from public.public import *
# Create your views here.

'''
=main index page
=主页
'''
def index(request):
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/main.html',res_template_dist)

"""
=Add module page
=添加模块
"""
def module_add(request):
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/module_add.html',res_template_dist)


'''
=Return server IP list
=返回服务器列表方法
'''
def server_list(request):
    ip = ""
    ip_hostname = ""
    if not 'app_categId' in request.GET:
        app_categId = ""
    else:
        # 获取用户选择的应用分类ID
        app_categId = request.GET["app_categId"]
    # ServerList为server_list表模型对象，实现过滤获取的应用分类ID相匹配的主机列表
    ServerListObj = ServerList.objects.filter(server_app_id = app_categId)
    for host in ServerListObj:
        ip+=', '+host.server_lip
        ip_hostname+=', '+host.server_lip+'*'+host.server_name
    server_list_string = ip[1:]+"|"+ip_hostname[1:]
    # 输出格式：192.168.1.10，192.168.1.20|192.168.1.10*sn2012-07-010，\
    # 192.168.1.20*sn2013-08-020，其中“|”分隔符前部分为IP地址，作为HTML <option>
    # 下拉框显示项，
    # 分隔符后部分为<option>的value，以“*”号作为分隔符，目的是为后端提供主机名及IP两种
    # 目标地址支持
    return HttpResponse(server_list_string)

'''
=Return module list
=返回功能模块列表方法
'''
def module_list(request):
    module_id = '-1'
    module_name = u'请选择功能模块...'
    # ModuleList为module_list表模型对象，实现读取所有模块列表，以模块id做排序
    ModuleObj = ModuleList.objects.order_by('id')
    for m in ModuleObj:
        module_id+=', '+str(m.id)
        module_name +=', '+m.module_name
    module_list_string = module_name+"|"+module_id
    # 输出格式：“请选择功能模块...，查看系统日志，查看最新登录，查看系统版本|-1，1001，
    # 1002，1003”
    # 其中“|”号分隔模块名称与模块ID，Web前端获取数据后通过JavaScript做拆分与组装
    return HttpResponse(module_list_string)

"""
 =Return module info
"""
def module_info(request):
    if not 'Module_Id' in request.GET:
        Module_Id=""
    else:
        Module_Id=request.GET['Module_Id']
    ModuleObj = ModuleList.objects.get(id=Module_Id)
    module_info_string=str(ModuleObj.id)+"@@"+ModuleObj.module_name+"@@"+ModuleObj.module_caption+"@@"+ModuleObj.module_extend
    return HttpResponse(module_info_string)


'''
=Return server function categ
=返回功能分类列表方法
'''
def server_fun_categ(request):
    categ_id='-1'
    categ_name=u"<-请选择功能类别->"
    ServerFunObj=ServerFunCateg.objects.order_by('id')
    for fun in ServerFunObj:
        categ_id +=", "+str(fun.id)
        categ_name+=", "+fun.server_categ_name
    fun_categ_string=categ_name+"|"+categ_id
    return HttpResponse(fun_categ_string)


"""
=Return server app categ
=返回功能运用列表方法
"""
def server_app_categ(request):
    categ_id='-1'
    categ_name=u"<-请选择应用类别->"
    if not 'fun_categId' in request.GET:
        fun_categId=""
    else:
        fun_categId=request.GET['fun_categId']
    ServerAppObj = ServerAppCateg.objects.filter(server_categ_id=fun_categId)
    for e in ServerAppObj:
        categ_id+=","+str(e.id)
        categ_name+=","+e.app_categ_name
    app_categ_string=categ_name+"|"+categ_id
    return HttpResponse(app_categ_string)

'''
=Run module
=运行模块的方法
'''
def module_run(request):
    import rpyc # 导入远程通信模块
    from cPickle import loads
    put_string="" # 前端选取的配置主机，需要配置的功能模块ID号

    # 前端选取的功能模块的ID
    if not 'ModuleID' in request.GET:
        Module_Id=""
    else:
        Module_Id=request.GET['ModuleID']
        put_string+=Module_Id+"@@"

    # 前端选取的主机
    if not 'hosts' in request.GET:
         Hosts=""
    else:
        Hosts=request.GET['hosts']
        put_string+=Hosts+"@@"

    # 有的模块所需要的系统参数1
    if not 'sys_param_1' in request.GET:
        Sys_param_1=""
    else:
        Sys_param_1=request.GET['sys_param_1']
        put_string+=Sys_param_1+"@@"

    # 有的模块所需要的系统参数2
    if not 'sys_param_2' in request.GET:
        Sys_param_2=""
    else:
        Sys_param_2=request.GET['sys_param_2']
        put_string+=Sys_param_2+"@@"

    # 连接rpyc 服务器
    try:
        print settings.RPYC_SET
        conn=rpyc.connect(settings.RPYC_SET['HOST'], settings.RPYC_SET['PORT'])
        conn.root.login(settings.RPYC_SET['USER'], settings.RPYC_SET['KEY'])
    except Exception,e:
        logging.error('connect rpyc server ERROR:'+str(e))
        return HttpResponse('connect rpyc server ERROR:'+str(e))

    # 加密要发送到rpyc服务器的配置字符串
    put_string=tencode(put_string, settings.SECRET_KEY)
    result=conn.root.Runcommands(put_string)
    # 解密从RPYC服务器获得的执行结果
    Opresult=tdecode(result,settings.SECRET_KEY)

    return HttpResponse(Opresult)

"""
=添加新的模块
"""
def module_add_post(request):
    if request.method=="GET":
        # 由于不是很重要的数据,所有使用get方法提交，先做一个检测
        # 也就是没用form提交，只是一般get加了一些参数
        if request.GET.get("module_name" ""):
            return HttpResponse("模块名称不能为空！")
        #检查表单-监控URL
        if not request.GET.get('module_caption', ''):
            return HttpResponse("模块功能描述不能为空！")

        module_name=request.GET['module_name']
        module_caption=request.GET['module_caption']
        module_extend=request.GET['module_extend'] 

        moduleobj = ModuleList(module_name=module_name, \
            module_caption=module_caption, \
            module_extend=module_extend)
        try:
            moduleobj.save()
            #lastId = moduleobj.objects.order_by('-pk')[0]
            lastId = ModuleList.objects.latest('id')
        except Exception,e:
            return HttpResponse("入库失败，请与管理员联系！"+str(e))

        InfoList="祝贺你，模块前端添加成功，模块ID为："+str(lastId.pk)+"，下一步请在服务器端编写模块逻辑！"
        return HttpResponse(InfoList)
    else:
        return HttpResponse("非法提交！")
