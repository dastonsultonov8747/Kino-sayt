from django.urls import path
from . import views
from .views import KinoListApi, KinoDetailApi, MultfilmListApi, MultfilmDetailApi, SerialListApi, SerialDetailApi, \
    SerialItemApi, SerialItemDetailApi, AnimeItemApi, AnimeDetailApi

urlpatterns = [
    path('', views.Index, name='index'),
    path('kinolar/', views.Kinolar_views, name='kinolar'),
    path('multfilimlar/', views.Multfilimlar_views, name='multfilimlar'),
    path('seriallar/', views.Seriallar_views, name='seriallar'),
    path('animelar/', views.Animelar_views, name='animelar'),

    path('api/kinolar/', KinoListApi.as_view(), name='kino-list'),
    path('api/kinolar/<int:pk>/', KinoDetailApi.as_view(), name='kino-detail'),

    path('api/multfilmlar/', MultfilmListApi.as_view(), name='multfilm-list'),
    path('api/multfilmlar/<int:pk>/', MultfilmDetailApi.as_view(), name='multfilm-detail'),

    path('api/seriallar/', SerialListApi.as_view(), name='serial-list'),
    path('api/seriallar/<int:pk>/', SerialDetailApi.as_view(), name='serial-detail'),

    path('api/serial_item/', SerialItemApi.as_view(), name='serial_item-list'),
    path('api/serial_item/<int:pk>/', SerialItemDetailApi.as_view(), name='serial_item-detail'),

    path('api/animelar', AnimeItemApi.as_view(), name='anime-list'),
    path('api/animelar/<int:pk>/', AnimeDetailApi.as_view(), name='anime-detail'),

    path('api/anime_item/', AnimeItemApi.as_view(), name='anime_item-list'),
    path('api/anime_item/<int:pk>/', AnimeDetailApi.as_view(), name='anime_item-detail'),

]
