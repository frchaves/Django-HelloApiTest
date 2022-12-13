from rest_framework import viewsets
from rest_framework.response import Response

from .models import Greetings
from .serializers import GreetingsSerializer


# Create your views here.
class GreetingsViewSet(viewsets.ModelViewSet):
    """
      List: Shows all given names and how often they were greeted

      Create: Creates a new greeting with the given name and returns an hello
      """
    queryset = Greetings.objects.all()
    serializer_class = GreetingsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        greetings_name = serializer.validated_data['name']

        greetings_queryset = Greetings.objects.filter(
            name=greetings_name)

        if greetings_queryset.exists():
            existing_greetings = greetings_queryset[0]
            existing_greetings.number_greetings += 1
            existing_greetings.save()
        else:
            serializer.save(name=greetings_name, number_greetings=1)

        response_message = f'Hello,{greetings_name}'
        return Response({response_message})
