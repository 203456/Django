from rest_framework import routers, serializers, viewsets
# Importación de modelos
from loadImageComponente.models import imgField
class imgSerializer(serializers.ModelSerializer):
    class Meta:
        model = imgField
        fields = [ 'id', 'name_img', 'url_img', 'format_img']