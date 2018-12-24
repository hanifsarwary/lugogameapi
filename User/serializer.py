from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'coins_count', 'ticket1_count', 'ticket2_count', 'ticket3_count', 'game_won',
                  'game_played']


class UpdateCoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['coins_count']


class UpdateTicketOne(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['ticket1_count']


class UpdateTicketTwo(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['ticket2_count']


class UpdateTicketThree(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['ticket3_count']


class UpdateTicketFour(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['ticket4_count']


class UpdateTicketFive(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['ticket5_count']


class UpdateTicketSix(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['ticket6_count']


class UpdateGameWon(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['game_won']


class UpdateGamePlayed(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['game_played']


class UserAuthSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        print(validated_data)
        return CustomUser.objects.create(**validated_data)

    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'profile_pic')


class TransactionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)


    class Meta:
        model = Transaction
        fields = '__all__'


