from django.urls import path, include
from django.views.generic.base import TemplateView
# from romms import views

# urlpatterns = [
#     path('rooms/', TemplateView.as_view(template_name = "rooms/main.html"), name = 'room_main'),
#     path('rooms/list', views.RoomList.as_view(), name = 'room_list'),
#     path('rooms/create', views.RoomCreate.as_view(), name = 'room_create'),
#     path('rooms/<int:pk>', views.RoomDetail.as_view(), name = 'room_detail')
# ]