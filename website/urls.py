from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('works/', views.works, name='works'),
    path('materials/', views.materials, name='materials'),
    path('product/<int:pk>/', views.product, name='product'), # add product id
    path('reserve/<int:pk>/', views.reserve, name='reserve'), # add product id
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('add-product/', views.add_product, name='add-product'),
    path('update-product/<int:pk>/', views.update_product, name='update-product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete-product'),
    path('products-list/', views.products_list, name='products-list'),
    path('product-info/<int:pk>/', views.product_info, name='product-info'),

    path('add-video/', views.add_video, name='add-video'),
    path('delete-video/<int:pk>', views.delete_video, name='delete-video'),
    path('videos-list/', views.videos_list, name='videos-list'),
    path('update-showreel/', views.update_showreel, name='update-showreel'),

    path('reservations-list/', views.reservations_list, name='reservations-list'),
    path('reservation-details/<int:pk>/', views.reservation_details, name='reservation-details'),
    path('detele-reservation/<int:pk>/', views.delete_reservation, name='delete-reservation'),

    # path('send-message', views.send_message, name='send-message'),
    path('messages/', views.messages, name='messages'),
]