from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.def \

def landing(req):
    return HttpResponse("hello")



def landingpage2(req):
    return HttpResponse("<h1 style='color : red ;'>hello</h1>")

def text_response(req):

    return HttpResponse("this is text response",content_type="text/plain")



def html_response(req):
    HtML="<h1 style='color :red ;'> hello this html content </h1>"
    return HttpResponse(HtML,status=100,content_type="text/html")


def json_response(req):
    jsondat={'name' : 'jatin''age: 5'}
    jso=json.dumps(jsondat)
    return HttpResponse(jso,content_type="application/json")
