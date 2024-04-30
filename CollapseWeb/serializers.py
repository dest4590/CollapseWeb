from rest_framework import serializers, viewsets, routers
from .models import Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'version', 'link', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            self.fields['created_at'].read_only = False
            self.fields['updated_at'].read_only = False
        else:
            self.fields.pop('created_at', None)
            self.fields.pop('updated_at', None)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
