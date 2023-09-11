from rest_framework.decorators import api_view
from rest_framework.response import Response
from chat.models import Message
# from chat.models import Users
from .serializers import ItemSerializer


@api_view(['GET'])
def getUser(request):
    Msg = Message.objects.all()
    serializer = ItemSerializer(Message, many=True)
    return Response(serializer.data)
