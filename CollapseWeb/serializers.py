from collections import Counter
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from .models import Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'version', 'link', 'created_at', 'updated_at']

class BaseClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientViewSet(BaseClientViewSet):
    pass

class InfoViewSet(viewsets.ViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def list(self, request):
        versions_counter = Counter(self.queryset.values_list('version', flat=True))
        
        data = {
            'count': self.queryset.count(),
            'versions': dict(versions_counter),
        }

        return Response(data)

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'info', InfoViewSet, basename='info')