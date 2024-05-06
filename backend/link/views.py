from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LinkSerializer
from rest_framework import status


class LinkAPIView(APIView):
    
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid:
            link, status_code = serializer.create(
                validated_data=serializer.validated_data
            )
            return Response(LinkSerializer(link).data, status=status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
