from rest_framework import serializers
from .models import userData, workSpace, column, card


class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ['id', 'username', 'email', 'password', 'imgURL', 'workSpaceMemberOrder', 'workSpaceOwnerOrder', 'workSpaceRequest']

class userLogin:
    class Meta:
        model = userData
        fields = ['username', 'password']

class workSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = workSpace
        fields = ['id', 'create_at', 'name', 'members', 'owner', 'icon_unified', 'request']
class columnSerializer(serializers.ModelSerializer):
    class Meta:
        model = column
        fields = ['id', 'cards', 'columnIndex', 'title', 'workSpaceID']
class cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = card
        fields = ['id', 'assignID', 'cardIndex', 'columnID', 'content', 'dueDate', 'task']