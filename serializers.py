from rest_framework import serializers
from .models import permission
class permissionserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=permission
		fields=('name','food','price','location')