from .models import Plans, Oprators, History
from .serializers import PlanSerializer, OpratorsSerializer, HistorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StateList(APIView):

    def get(self, request):
        all_state = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh','Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                     'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                     'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal']
        return Response(all_state)
 

class OpratorsList(APIView):
    
    def get(self, request, format=None):
        AllOp = Oprators.objects.all()
        if self.request.query_params.get('state'):
            all_oprators = AllOp.filter(
                oprator_state=self.request.query_params.get('state'))
            serializer = OpratorsSerializer(all_oprators, many=True)
        return Response(serializer.data)
  
class PlanList(APIView):

    def get(self, request, format=None):
        AllPlans = Plans.objects.all()
        print('....')
        print(self.request.query_params.get('state'))
        print(self.request.query_params.get('operator'))
        print(self.request.query_params.get('plan_category'))
        print('....')

        AllPlans = AllPlans.filter(
            plan_oprator=self.request.query_params.get('operator'),
            plan_state=self.request.query_params.get('state'))
        
        if self.request.query_params.get('plan_price'):
            AllPlans = AllPlans.filter(plan_price=self.request.query_params.get('plan_price'))
            serializer = PlanSerializer(AllPlans, many=True)
        if self.request.query_params.get('plan_category'):
            AllPlans = AllPlans.filter(plan_category=self.request.query_params.get('plan_category'))
            serializer = PlanSerializer(AllPlans, many=True)
        if self.request.query_params.get('plan_validity'):
            AllPlans = AllPlans.filter(plan_validity=self.request.query_params.get('plan_validity'))
            serializer = PlanSerializer(AllPlans, many=True)
        else:
            serializer = PlanSerializer(AllPlans, many=True)
        return Response(serializer.data)


class HistoryList(APIView):

    def get(self, request, format=None):
        userHist = History.objects.all()
        serializer = HistorySerializer(userHist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        userHist = HistorySerializer(data=request.data)
        if userHist.is_valid():
            userHist.save()
            return Response(userHist.data, status=status.HTTP_200_OK)
        return Response(userHist.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoryDetail(APIView):
    
    def get_object(self, pk):
        try:
            return History.objects.get(pk=pk)
        except History.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userHist = self.get_object(pk)
        serializer = HistorySerializer(userHist)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userHist = self.get_object(pk)
        serializer = HistorySerializer(userHist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
