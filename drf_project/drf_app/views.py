from rest_framework import viewsets
from .serializers import PhoneNumberSerializer, SpamNumberSerializer


from .models import PhoneNumber, SpamNumber


class PhoneNumberViewSet(viewsets.ModelViewSet):
      queryset = PhoneNumber.objects.all()
      serializer_class = PhoneNumberSerializer
      
class SpamNumberViewSet(viewsets.ModelViewSet):
      queryset = SpamNumber.objects.all()
      serializer_class = SpamNumberSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

    def get_queryset(self):
        queryset = self.queryset
        query = self.request.query_params.get('q')
        if query:
            queryset = queryset.filter(number__icontains=query)
        return queryset
