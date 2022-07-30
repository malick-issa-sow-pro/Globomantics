from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ProductsViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('products', views.all_products, name='all_product'),
    path('products/<int:id>', views.on_product, name='one_product'),
    path('category', views.all_category, name='all_category'),
    path('category/<int:id>',views.get_one_category,name='one_category'),
    # for api
    path('api/', include(router.urls))
]
