from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	"""Serializes a name field for testing our APIView"""
	name = serializers.CharField(max_length=10)

class ConverterSerializer(serializers.Serializer):
	"""Serializes the input for our converter to receive from the frontend"""
	studio = serializers.CharField(max_length=100)
	directory = serializers.CharField(max_length=240)
	pathTest = serializers.FilePathField(path=None)



