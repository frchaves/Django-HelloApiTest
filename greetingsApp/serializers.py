from rest_framework import serializers
from .models import Greetings


class GreetingsSerializer(serializers.ModelSerializer):
    number_greetings = serializers.IntegerField(read_only=True)

    class Meta:
        model = Greetings
        fields = ('name', 'number_greetings')
