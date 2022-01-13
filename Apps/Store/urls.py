
from django.urls import path
from . import views


urlpatterns = [
     path('', views.store, name='store'),
     path('categoria_p/<int:cat_prod_id>/', views.productos_filtrados, name="prod_filt")
]
