from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework import status, viewsets
from rest_framework.response import Response

from api_messages.serializers import MessageSerializer
from api_messages.models import Message


class SingleViewMessages(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, *args, **kwargs):
        page = kwargs['page'] + 1
        paginator = Paginator(self.queryset, 10)
        try:
            list_of_something = paginator.get_page(page)
        except PageNotAnInteger:
            list_of_something = paginator.get_page(1)
        except EmptyPage:
            list_of_something = paginator.get_page(paginator.num_pages)
        serializer = self.serializer_class(list_of_something, many=True)
        return Response(serializer.data)

    def get_object(self, *args, **kwargs):
        try:
            obj = Message.objects.get(pk=kwargs['pk'])
            serializer = self.serializer_class(obj)
        except Exception as e:
            raise Exception(e)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
