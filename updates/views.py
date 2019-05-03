import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
from django.views.generic import View

def update_model_detail_view(request):
    '''
    URI -- for REST API
    GET -- Retrieve
    '''
    data = {
        "count":100,
        "content": "Some good thing"
    }
    #jason_data = json.dumps(data)
    #return HttpResponse(jason_data, content_type='application/jason')
    return JsonResponse(data)


class JsonCBV(View):

        def get(self, request, *args, **kwargs):
            data = {
                "count":100,
                "content": "Some  thing"
            }
            jason_data = json.dumps(data)
            return HttpResponse(jason_data, content_type='application/jason')

class SerializedDetailView(View):
        def get(self, request, *args, **kwargs):
            obj = Update.objects.get(id=1)
            data = {
                "user":data.user.username,
                "content": obj.content
            }
            jason_data = json.dumps(data)
            return HttpResponse(jason_data, content_type='application/jason')

class SerializedListView(View):
        def get(self, request, *args, **kwargs):
            qs = Update.objects.all()
            #data = serialize("json", qs, fields=('user', 'content'))
            data = Update.objects.all().serialize()
            return HttpResponse(data, content_type='application/jason')
