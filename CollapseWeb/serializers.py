from rest_framework import routers, serializers, viewsets

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'version', 'filename', 'main_class', 'show_in_loader', 'working', 'internal', 'fabric', 'category', 'created_at', 'updated_at']

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FabricClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricClient
        fields = ['id', 'name', 'version', 'filename', 'show_in_loader', 'working', 'fabric', 'category', 'created_at', 'updated_at']

class FabricClientViewSet(viewsets.ModelViewSet):
    queryset = FabricClient.objects.all()
    serializer_class = FabricClientSerializer

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'body', 'type', 'post_at', 'hidden']

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ['id', 'file', 'client', 'config_path', 'server']

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

class AnalyticsCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsCounter
        fields = ['endpoint', 'count']

class AnalyticsCounterViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsCounter.objects.all()
    serializer_class = AnalyticsCounterSerializer

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'fabric_clients', FabricClientViewSet)
router.register(r'messages', MessagesViewSet)
router.register(r'configs', ConfigViewSet)
router.register(r'counter', AnalyticsCounterViewSet)