#from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # instance = Product.objects.all().order_by("?").first()
    
    # if model_data:
    #     data['id'] = model_data.id
    #     data["title"] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    #     # serialization
    #     # model instance (model_data), turn to python dict
    #     # return JSON

    # if instance:
    #     #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
    return Response({"invalid": "not good data"}, status=400)
