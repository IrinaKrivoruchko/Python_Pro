"""
URL configuration for test_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from catalog.views import CategoryViews, TagViews, GoodsViews
from potter.views import IngredientsViews, ElixirsViews, HousesViews, SpellsViews

Router = routers.DefaultRouter()

Router.register('category', CategoryViews)
Router.register('goods', GoodsViews)

Router.register('ingredients', IngredientsViews)
Router.register('elixirs', ElixirsViews)
Router.register('houses', HousesViews)
Router.register('spells', SpellsViews)

schema_view = get_schema_view(
   openapi.Info(
      title="Catalog API",
      default_version='v3',
      description="Catalog API"
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

schema_view_potter = get_schema_view(
   openapi.Info(
      title="Potter API",
      default_version='v3',
      description="Potter API"
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls)),
    path('api/tags', TagViews.as_view({'get': 'list'})),
    path('api-auth/', include('rest_framework.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),

    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('doc', schema_view_potter.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view_potter.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
