from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView, ListCreateAPIView
from .serializer import *
# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from django.core import serializers


class UpdateCoins(UpdateAPIView):
    serializer_class = UpdateCoinSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateTicketOneView(UpdateAPIView):
    serializer_class = UpdateTicketOne
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateTicketTwoView(UpdateAPIView):
    serializer_class = UpdateTicketTwo
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateTicketFourView(UpdateAPIView):
    serializer_class = UpdateTicketFour
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateTicketThreeView(UpdateAPIView):
    serializer_class = UpdateTicketThree
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateTicketFiveView(UpdateAPIView):
    serializer_class = UpdateTicketFive
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()

class UpdateTicketSixView(UpdateAPIView):
    serializer_class = UpdateTicketSix
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateGameWonView(UpdateAPIView):
    serializer_class = UpdateGameWon
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateGamePlayedView(UpdateAPIView):
    serializer_class = UpdateGamePlayed
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class UpdateUserView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'
    queryset = CustomUser.objects.all()


class GetUserData(APIView):

    def get(self,request,username):
        data = \
            serializers.serialize(format="json",
                                     queryset=CustomUser.objects.filter(username=username).only('username','coins_count','ticket1_count','ticket2_count','ticket3_count','game_won','game_played'))
        return Response(data)


class SignUp(ListCreateAPIView):
    serializer_class = UserAuthSerializer

    def get_queryset(self):
        return CustomUser.objects.all()


class CreateTransactionView(CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


