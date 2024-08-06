from rest_framework import routers, serializers, viewsets
from .models import ClientLoader, Message, Config

class ClientLoaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientLoader
        fields = ['id', 'name', 'version', 'category', 'filename', 'main_class', 'show_in_loader', 'working', 'internal', 'created_at', 'updated_at']

class BaseClientViewSet(viewsets.ModelViewSet):
    queryset = ClientLoader.objects.all()
    serializer_class = ClientLoaderSerializer

class ClientViewSet(BaseClientViewSet):
    pass

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'body', 'type', 'post_at', 'hidden']

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = ['id', 'file', 'client', 'config_path', 'server']

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessagesViewSet)
router.register(r'configs', ConfigViewSet)