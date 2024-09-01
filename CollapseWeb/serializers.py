from rest_framework import routers, serializers, viewsets

from .models import *


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'version', 'filename', 'main_class', 'show_in_loader', 'working', 'internal', 'created_at', 'updated_at']

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FabricClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FabricClient
        fields = ['id', 'name', 'version', 'filename', 'show_in_loader', 'working', 'hidden', 'created_at', 'updated_at']

class FabricClientViewSet(viewsets.ModelViewSet):
    queryset = FabricClient.objects.all()
    serializer_class = FabricClientSerializer

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
router.register(r'fabric_clients', FabricClientViewSet)
router.register(r'messages', MessagesViewSet)
router.register(r'configs', ConfigViewSet)