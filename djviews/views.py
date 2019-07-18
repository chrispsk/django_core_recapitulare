from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    print(dir(request))
    print(request.build_absolute_uri()) # http://127.0.0.1:8000/as/
    print(request.is_ajax())
    print(request.method)
    print(request.get_full_path()) # /abc/

    return HttpResponse("Translate this ")

def response(request):
    response = HttpResponse(content_type='application/json')
    print(dir(response))
    print(response.status_code)
    response.write('{ "name":"John", "age":30, "car":null }')
    return response

def download(request):
    with open('djviews/fin.pdf', 'rb') as pdf:
    	response = HttpResponse(pdf.read())
    	response['content_type'] = 'application/pdf'
    	response['Content-Disposition'] = 'attachment;filename=file.pdf'
    return response

def laredirect(request):
    return HttpResponseRedirect('/response')
