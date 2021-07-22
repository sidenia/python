from django.http import HttpResponse

def hello(request):
    return HttpResponse('Ola mundo')

def articles(request, year):
    return HttpResponse('O ano informado foi:' + str(year))