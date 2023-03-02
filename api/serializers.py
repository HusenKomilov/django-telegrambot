from .models import BotUser, Feedback
from rest_framework.serializers import ModelSerializer


class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('name', 'username', 'user_id', 'created_ad')


class FeedbackSerializers(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('user_id', 'created_ad', 'body')
