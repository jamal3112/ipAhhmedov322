from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'bid', views.BidViewSet)
router.register(r'street', views.StreetViewSet)
router.register(r'area', views.AreaViewSet)
router.register(r'clocationar', views.LocationViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest'))
]