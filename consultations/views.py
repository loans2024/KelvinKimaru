# consultations/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Consultation
from .serializers import ConsultationSerializer

class ConsultationListCreateView(generics.ListCreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            # Return the validation errors with 400
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Otherwise, proceed as normal
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

