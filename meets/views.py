from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Meet as Meeting
from .serializers import MeetingSerializers


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def meeting(request):

    if request.method == "GET":
        try:
            users = Meeting.objects.get(user=request.user)
            serializer = MeetingSerializers(users,many=False)
        except Exception as e:
            return Response({'messge': f'does not exust create a meeting'})
        return Response(serializer.data)
    elif request.method == "POST":
        serialize = MeetingSerializers(data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
@api_view(['PUT'])
@permission_classes((AllowAny,))
def meeting_Update(request,id):
    if request.method == 'PUT':
        list_of_search = [k for k, v in request.data.items()]
        if 'succeded' in list_of_search :
            meet = Meeting.objects.get(id=id)
            if meet.is_success == True and request.data['succeded'] == 'False':
                print('false success')
                meet.is_success ="False"
                meet.save()
            elif meet.is_success == False and request.data['succeded']  :
                print('true success')
                meet.is_success =True
                meet.save()
            print(meet,'succc')
            return Response({'done':True})
        elif 'is_accepted' in list_of_search :
            meet = Meeting.objects.get(id=id)
            print(request.data['is_accepted'], 5555555, meet.is_accepted)
            if meet.is_accepted == True and request.data['is_accepted'] == 'False':
                print('false accepted')
                meet.is_accepted =False
                meet.save()
            elif meet.is_accepted == False and request.data['is_accepted'] =='True':
                print('true is_accepted')
                meet.is_accepted =True
                meet.save()
            print(meet,'acc')
            return Response({'done':True})
        else:return Response({'done':False})


@api_view(['GET','post'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_exact_meating(request,id):
    if request.method == 'GET':
        meet = Meeting.objects.get(id=id)
        serializer = MeetingSerializers(meet,many=False)
        return Response(serializer.data)

