from django.urls import path
# import the views here now
from . import views

urlpatterns = [
    path('', views.getRoutes), # getRoutes function will be executed at http//localhost/api
    path('factories/', views.getFactories), #getFactories function will be executed at http://localhost/api/factories
    path('factories/<int:factoryId>', views.getAFactory),
    path('factories/<int:factoryId>/<int:productId>', views.getAProduct)
]