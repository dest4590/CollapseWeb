from rest_framework import serializers, viewsets, routers
from .models import Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'version', 'link']

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)