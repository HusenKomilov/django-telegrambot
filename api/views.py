from rest_framework.generics import ListCreateAPIView
from .models import BotUser, Feedback
from .serializers import BotUserSerializers, FeedbackSerializers


class BotUserListCreateAPIView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers
