# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import TestModel

# Create a model serializer
class TestSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = TestModel
		fields = ('title', 'description')
