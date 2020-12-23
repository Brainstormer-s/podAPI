from rest_framework import serializers

class YourSerializer(serializers.Serializer):
        img = serializers.CharField()
        link = serializers.CharField()
        title = serializers.CharField()
        types = serializers.CharField()