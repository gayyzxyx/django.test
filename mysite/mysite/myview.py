__author__ = 'yaoxin'
from django.http import HttpResponse,Http404
import datetime
def hello(request):
    return HttpResponse("""<div>this is a div</div><input type="button">""")
def curent_time(request):
    now = datetime.datetime.now()
    html="<html><body>it is now %s.</body></html>"%now
    return HttpResponse(html)
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