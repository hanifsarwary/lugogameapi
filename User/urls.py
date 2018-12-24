
from django.urls import path, include
from .views import *
urlpatterns = [
    path('updatecoins/<str:username>',UpdateCoins.as_view()),
    path('updategamewon/<str:username>',UpdateGameWonView.as_view()),
    path('updategameplayed/<str:username>',UpdateGamePlayedView.as_view()),
    path('updateticketone/<str:username>',UpdateTicketOneView.as_view()),
    path('updatetickettwo/<str:username>',UpdateTicketTwoView.as_view()),
    path('updateticketthree/<str:username>',UpdateTicketThreeView.as_view()),
    path('updateticketfour/<str:username>', UpdateTicketFourView.as_view()),
    path('updateticketfive/<str:username>', UpdateTicketFiveView.as_view()),
    path('updateticketsix/<str:username>', UpdateTicketSixView.as_view()),
    path('getuser/<str:username>',GetUserData.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('signup',SignUp.as_view()),
    # path('auth/registration', include('rest_auth.registration.urls')),
    path('api/newTransaction',CreateTransactionView.as_view())

]
