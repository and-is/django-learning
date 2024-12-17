from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data["title"] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    #     # serialization
    #     # model instance (model_data), turn to python dict
    #     # return JSON

    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})

