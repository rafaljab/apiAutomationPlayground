from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from shop.views import ProductList, ProductDetail


urlpatterns = [
    path("products/", ProductList.as_view()),
    path("products/<int:pk>/", ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
