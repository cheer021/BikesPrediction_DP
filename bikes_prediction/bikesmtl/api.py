# from rest_framework import generics, permissions

# from .models import Station, StationDataNow
# from .serializers import StationSerializer, StationDataNowSerializer

# class StationList(generics.ListCreateAPIView):
#     model = Station
#     serializer_class = StationSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]

# class StationDataNowList(generics.ListCreateAPIView):
#     model = StationDataNow
#     serializer_class = StationDataNowSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]

# class StationDataList(generics.ListAPIView):
#     model = StationDataNow
#     serializer_class = StationDataNowSerializer

#     def get_queryset(self):
#         queryset = super(StationDataList, self).get_queryset()
#         return queryset.filter(station=self.kwargs.get('station'))
#  ]

from djangular.views.crud import NgCRUDView

class MyCRUDView(NgCRUDView):
    model = BikesMtl