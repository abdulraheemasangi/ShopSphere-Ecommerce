from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('remove/<int:pk>',views.remove,name='remove'),
    path('details/<int:pk>',views.details,name='details'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('support/',views.support,name='support'),
    path('shipping/',views.shipping,name='shipping'),
    path('increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
]

