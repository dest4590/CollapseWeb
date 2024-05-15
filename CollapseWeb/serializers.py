from rest_framework import routers, serializers, viewsets
from .models import ClientLoader

class ClientLoaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientLoader
        fields = ['id', 'name', 'version', 'category', 'filename', 'main_class', 'show_in_loader', 'working', 'internal', 'created_at', 'updated_at']

class BaseClientViewSet(viewsets.ModelViewSet):
    queryset = ClientLoader.objects.all()
    serializer_class = ClientLoaderSerializer

class ClientViewSet(BaseClientViewSet):
    pass

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)