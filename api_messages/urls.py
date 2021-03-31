from django.urls import path
from api_messages import views

app_name = 'api_messages'

urlpatterns = [
    path('list/<int:page>/', views.SingleViewMessages.as_view({'get': 'list'}), name='list_page'),
    path('single/<int:pk>/', views.SingleViewMessages.as_view({'get': 'get_object'}), name='message_detail'),
    path('single/', views.SingleViewMessages.as_view({'post': 'create'}), name='message_create')
]
