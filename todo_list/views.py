import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from todo_list.models import ToDo


@csrf_exempt
def create_todo(request):
    body = json.loads(request.body)
    print(body)
    name = body['name']
    todo = ToDo(name=name)
    todo.save()

    return HttpResponse('', status=201)


def index(request):
    return None
