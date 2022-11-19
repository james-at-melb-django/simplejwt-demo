from rest_framework.response import Response
from rest_framework.views import APIView


class MessageView(APIView):
    def get(self, request):
        print(str(request.META))
        return Response(dict(message="Hello World"))
