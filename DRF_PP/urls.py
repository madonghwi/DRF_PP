from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from user.views import index

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
