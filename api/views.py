from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api import serializers

import lxml.etree as etree
import csv
import os


class HelloApiView(APIView):
	"""TEST API VIEW"""

	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		"""Returns a list of APIView featurs"""

		apiview_list = [
			'item 1',
			'item 2',
			'item 3',
			'item 4'
		]

		return Response({'msg': 'PANDA BOOGIE', 'a_list': apiview_list})

	def post(self, request):
		serializer = self.serializer_hello_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			msg = f'Hello, {name}'
			return Response({'msg': msg})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

class ConverterApiView(APIView):
	"""XML Converter APIView"""

	serializer_class = serializers.ConverterSerializer

	def get(self, request, format=None):
		return Response('GET not allowed.')

	def post(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			studio = serializer.validated_data.get('studio')
			directory = serializer.validated_data.get('directory')
			test = serializer.validated_data.get('pathTest')

			# msg = f'Entered studio: {studio}; and directory: {directory}'
			msg = test
			return Response({'msg': msg})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

		# if serializer.is_valid():
		# 	studio = serializer.validated_data.get('studio')
		# 	directory = serializer.validated_data.get('directory')
		# 	# directory = 'C:\\Box\\EST & Streampix\\Metadata By Month\\2020\\7. July\\TV\\Disney\\30 For 30'
		# 	# print('\tDIRECTORY --> ' + directory)
		# 	test = serializer.validated_data.get('pathTest')
		# 	list_data = []
		# 	for filename in os.listdir(directory):
		# 		list_data.append(filename)
		# 		# if filename.endswith(".xml"):
		# 		# 	# file = os.path.join(directory, filename)
		# 		# 	if studio.lower() == "a&e":
		#   #               # ae_dict = create_ae_data_dict(file)
		# 		# 		list_data.append(studio)
		# 		# 	elif studio.lower() == "disney":
		#   #               # disney_dict = create_disney_data_dict(file)
		# 		# 		list_data.append(studio)
		# 		# 	elif studio.lower() == 'discovery':
		#   #               # discovery_dict = create_discovery_data_dict(file)
		# 		# 		list_data.append(studio)
		# 		# 	else:
		# 		# 		print("- '" + studio + "' is not set up to convert XMLs to CSV at this time.")
		# 		# 		break
		# 	return Response({'msg': directory, 'file': list_data})
		# else:
		# 	return Response(
		# 		serializer.errors,
		# 		status=status.HTTP_400_BAD_REQUEST
		# 	)