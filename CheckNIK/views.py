from CheckNIK.serialization import Serializationclass
from CheckNIK.models import Dukcapilmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

@api_view(['GET'])
def list(request):
    if request.method=='GET':
        print(request.GET.get('nik'))
        results=Dukcapilmodel.objects.all()
        serialize=Serializationclass(results,many=True)
        return Response(serialize.data)

# Nomor 2   
@api_view(['GET'])
def check(request):
    if request.method=='GET':
        data = request.GET.get('nik')
        results=Dukcapilmodel.objects.filter(nik=data)
        serialize=Serializationclass(results,many=True)
        return Response(serialize.data)

# Nomor 3
@api_view(['POST'])
def post(request):
    if request.method == 'POST': 
        dukcapil_data = JSONParser().parse(request)
        dukcapil_serializer = Serializationclass(data=dukcapil_data) 
        if dukcapil_serializer.is_valid(): 
            dukcapil_serializer.save() 
            return JsonResponse(dukcapil_serializer.data) 
        return JsonResponse(dukcapil_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
