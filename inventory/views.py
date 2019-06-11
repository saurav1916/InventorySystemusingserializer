from .serializers import baseserializers
from .models import inven
from rest_framework .response import Response
from rest_framework .views import APIView
# Create your views here.
class see(APIView):
    def get(self,request):
        if 'id' in request.GET:
            items=inven.objects.all().filter(id=request.GET['id']).values()
        else:
            items=inven.objects.all()
            obj=baseserializers(items,many=True)
            return Response({"ITEMS":obj.data})
        
        return Response({"ITEMS":items})


    def post(self,request):
        obj=baseserializers(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({"Message":"Data Recorded"})
        else:
            return Response({"Message":obj.errors})
        #inven.objects.create(**request.data)    
        

    def put(self,request):
        id=request.data('id')
        items=request.data
        items.pop('id') 
        inven.objects.all().filter(id=id).update(**request.data)  
        return Response({"Message":"Record Updated"}) 