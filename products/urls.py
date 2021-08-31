from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views import View
from django.urls import include
from . import views



urlpatterns =[
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name='checkout'),
    path('update-item/', views.updateItem, name='update-item'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)