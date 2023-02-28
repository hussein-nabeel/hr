from django.http import JsonResponse
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#get all the drinks 
#serialize them 
#return json
@api_view(['GET','POST'])
def category_list(request, format=None):

 if request.method == 'GET':
    categorys= Category.objects.all()     #get all the drinks 
    serializer = CategorySerializer(categorys, many=True) 
    return Response(serializer.data)                              #return JsonResponse({'drinks':serializer.data})

 if request.method == 'POST':
    serializer = CategorySerializer(data=request.data) 
    if serializer.is_valid() :
        serializer.save ()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view (['GET','PUT','DELETE'])
def category_detail(request,id ,format=None):
    try:
      category =Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
         serializer = CategorySerializer(category, data=request.data)
         if serializer.is_valid():
            serializer.save ()
            return Response (serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      