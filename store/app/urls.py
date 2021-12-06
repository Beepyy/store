from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.catalogs,name="cat"),
    path('search/',views.search,name="search"),
    path('catalogs/',views.catalogs,name="cat"),
    path('catalogs/<str:c_str>/',views.goods,name="goods"),
    path('good/<int:g_id>/',views.goods_descr,name="goods_descr"),
    path('profile/',views.profile,name="profile"),
    path('basket/',views.basket,name="basket"),
    path('basket_change/<int:g_id>/',views.basket_change,name="basket_change"),
    path('bought/',views.bought,name="bought"), 
    #path('buying/',views.buying,name="buying"),транзакция с таймером в 60 минут
    #Купивший может писать комменты
    
    
]