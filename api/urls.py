from django.urls import path
from .views import BotUserListCreateAPIView, FeedbackListCreateAPIView

urlpatterns = [
    path('users/', BotUserListCreateAPIView.as_view(), name='users'),
    path('feedbacks/', FeedbackListCreateAPIView.as_view(), name='feedbacks'),
]
