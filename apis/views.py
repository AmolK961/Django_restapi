# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import TestSerializer
from .models import TestModel

# create a viewset


class TestViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = TestModel.objects.all()

	# specify serializer to be used
	serializer_class = TestSerializer
