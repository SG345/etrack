from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Log, UDevice, BlockedEvents
from api.serializers import LogSerializer, BlockedEventsSerializer

@api_view(['POST'])
def adduser(request):
	if request.method == 'POST':
		results = []
		try:
			if UDevice.objects.filter(UID=request.data['UserDevice']).exists():
				results.append({'Failed': 'UserDevice is already mapped to a user'})
				return HttpResponse(results,content_type='application/json')
			Mapper = UDevice(UID = request.data['UserDevice'], UserName = request.data['UserName'])
			Mapper.save()
			results.append({'Success': 'Username/Device mapped successfully'})
		except:
			results.append({'Operation Failed': 'Database not accessible/invalid data input'})
			pass
		
		return HttpResponse(results,content_type='application/json')


def checkblockedlist(ename):
	answer = 0 #0 indicates the event is not blocked
	if BlockedEvents.objects.filter(EventName=ename).exists():
		a = BlockedEvents(EventName = ename)
		a.Counter += 1
		a.save()
		answer = 1 #update and return true - that the event is blocked
		return answer
	else:
		return answer #return false

@api_view(['POST'])
def event_post(request):
	if request.method == 'POST':

		results = []
		f = checkblockedlist(request.data[('EventName')])
		if f == 0:
			serializer = LogSerializer(data=request.data)

			if serializer.is_valid():
				if UDevice.objects.filter(UID=request.data['UserDevice']).exists():
					serializer.save()
					results.append({'Success': 'Event recorded'})
					return Response(results, content_type='application/json')
				else:
					results.append({'Error': 'UserDevice does not exist in the system'})
					return Response(results,content_type='application/json')
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
				results.append({'Error': 'Event was blocked as per existing rules'})
				return HttpResponse(results,content_type='application/json')

	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def event_detail(request, UserDevice):
	if request.method == 'GET':
		if Log.objects.filter(UserDevice=UserDevice).exists():
			data = Log.objects.filter(UserDevice=UserDevice)

			results = []
			uname = ''
			try:
				temp = UDevice.objects.filter(UID=UserDevice)
				uname = temp[0].UserName

			except:
				uname = 'Username not mapped'
				pass

			for entry in data:
				results.append({'UserName': uname,'EventName': entry.EventName, 'EventLabel': entry.EventLabel, 'EventAction':entry.EventAction, 'EventTime':entry.EventTime.strftime("%Y-%m-%d %H:%M")})
#			response = serializers.serialize("json", results)
			return HttpResponse(results, content_type='application/json')
	results = []
	results.append({'Error': 'User Device Data Not Found'})
	return HttpResponse(results,content_type='application/json')


@api_view(['POST'])
def block_event_add(request):
	if request.method == 'POST':
		results = []
		try:
			if BlockedEvents.objects.filter(EventName=request.data['EventName']).exists():
				results.append({'Error': 'EventName is already blocked'})
				return HttpResponse(results, content_type='application/json')
			E = BlockedEvents(EventName=request.data['EventName'], Counter=0)
			E.save()
			results.append({'Success': 'Event has been succesfully blocked'})
			return HttpResponse(results,content_type='application/json')
		except:
			results.append({'Error': 'Invalid input data'})
			return HttpResponse(results, content_type='application/json')


@api_view(['POST'])
def block_event_delete(request):
	if request.method == 'POST':
		results = []
		try:
			if BlockedEvents.objects.filter(EventName=request.data['EventName']).exists():
				E = BlockedEvents.objects.filter(EventName=request.data['EventName'])
				E.delete()
				results.append({'Success': 'Event has been removed from Block List'})
				return HttpResponse(results, content_type='application/json')
			else:
				results.append({'Error': 'Event was already deleted / Event not found in BlockedEvents List'})
				return HttpResponse(results,content_type='application/json')
		except:
			results.append({'Error': 'Invalid input data'})
			return HttpResponse(results, content_type='application/json')






