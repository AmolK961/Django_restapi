from django.urls  import path , include
from rest_framework import routers



from .views import  *

router = routers.DefaultRouter()


# define the router path  and viewset   to be used 
router.register(r'test', TestViewSet)


# specify url path for  rest_framework

urlpatterns = [
    
    
    path('',include(router.urls)),
    path('api-auth',include('rest_framework.urls'))
         
]


