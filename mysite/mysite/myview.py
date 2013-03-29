# -*- coding:utf-8 -*-
__author__ = 'yaoxin'
from django.http import HttpResponse,Http404
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
def hello(request):
    return HttpResponse("""<div>this is a div</div><input type="button">""")
def curent_time(request):
    now = datetime.datetime.now()
    t = get_template('current_date.html')
    cur_date=t.render(Context({'current_date':now}))
    return HttpResponse(cur_date)
def main_page(request):
    return HttpResponse("this is the main page")
def houes_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="In %s hours,it will be %s."%(offset,dt)
    return HttpResponse(html)
def show_person(request):
    person_info={'current_date':datetime.datetime.now(),'name':'yaoxin','phone':'18697962711','this_is_new':False}
    context = Context({'person':person_info})
#    fp=open("absolute paths")  then Template(fp) to get template 这样可以的
    t=get_template('person.html')
    this_person = t.render(context)
    #可以用render_to_response来返回页面这样更简单
#    return HttpResponse(this_person)
    return render_to_response('person.html',{'person':person_info})
    #如果这里的变量名和模板中的变量名一样（如将上面的person_info改为person），则可以用locals()将变量的key和value自动映射上
#    return render_to_response('person.html',locals())
