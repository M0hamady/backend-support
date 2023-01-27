from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.admin import User

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, viewsets, status
from rest_framework.authtoken.models import Token

from project.models import Project
from project.serializers import ProjectSerializers
from .serializers import UserSerializers, RegisterSerializer, User_Serualizer, ChangeImagwSerializer, UserSerializersMin
from .models import User as User_inf
from django.shortcuts import get_object_or_404


@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def main_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        # print(1)
        serializer = User_Serualizer(users, many=True)
        # print(serializer.data)
        return Response(serializer.data)
@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def users(request):
    if request.method == 'GET':
        users =User_inf.objects.all()
        # print(1)
        serializer=  UserSerializers(users,many=True)
        # print(serializer.data)
        return Response(serializer.data)
    elif request.method == "POST":
        list_of_search = [k for k, v in request.data.items()]
        name = ''
        ip = ''
        info = ''
        phone= ''
        location = ''
        is_visitor= False
        is_client= False
        is_eng= False
        is_designer= False
        is_manager = False
        if 'ip' in list_of_search :
            ip = request.data['ip']
        if 'name'in list_of_search :
            name = request.data['name']
        if 'info' in list_of_search :
            info = request.data['info']
        if 'phone' in  list_of_search :
            phone = request.data['phone']
        if 'location' in list_of_search  :
            location = request.data['location']
        if 'is_visitor' in list_of_search :
            is_visitor = request.data['is_visitor']
        if 'is_client' in list_of_search:
            is_client = request.data['is_client']
        if 'is_eng' in list_of_search :
            is_eng = request.data['is_eng']
        if 'is_designer' in list_of_search :
            is_designer = request.data['is_designer']
        if 'is_manager' in list_of_search:
            is_manager = request.data['is_manager']

        user= User_inf.objects.create(
            name=name,
            ip=ip,
            info=info,
            phone=phone,
            location=location,
            is_visitor=is_visitor,
            is_client=is_client,
            is_eng=is_eng,
            is_designer = is_designer,
            is_manager=is_manager
        )
        # if user.is_valid():
        user.save()
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['PUT'])
def is_admin(request):
    '''
    firs get th token
    then check in user get user then check if admin
    '''
    if request.method == 'PUT':
        list_of_search = [k for k, v in request.data.items()]
        # print(list_of_search)
        if 'token' in list_of_search:
            # print(request.data['token'])
            # print(1)
            try:
                user_id =  Token.objects.get(key =request.data['token'] )
                # print(user_id)
                if user_id:
                    user = User.objects.get(auth_token=user_id)
                    user_inf = User_inf.objects.get(user=user)
                    print(user_inf,'is login')
                    if user_inf.is_manager :
                        # print('admin')
                        return Response({'is_admin': True})
            except:pass

        print(list_of_search)
        return Response({'is_admin':False})

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def user(request):
    if request.method == 'PUT':
        list_of_search = [k for k, v in request.data.items()]
        # print(list_of_search,request.data)
        if 'token' in list_of_search:
            try:
                try:
                    # print(str(request.data['token']).split(' ')[1],1111111111111)
                    user_id =  Token.objects.get(key =str(request.data['token']).split(' ')[1])
                    # print(6)
                except:
                    try:
                        print(request.data['token'],959595595)
                        user_id =  Token.objects.get(key =request.data['token'])
                        print(user_id, 000000000000)
                    except: return Response({'message':"auth failed token value err 1"})
                if user_id:
                    user = User.objects.get(auth_token=user_id)
                    print(user)
                    user_inf = User_inf.objects.get(user=user)
                    print(user_inf)
                    try:
                        serialize = UserSerializers(user_inf , context={'request': request})
                        return Response(serialize.data )
                    except Exception as e:return Response({'message':f"serializer err {e}"})
                     #serialize.data
            except : return Response({'message':"auth failed token value err"})
        else:return Response({'messsage':'no token in body'})

class UserView(viewsets.ModelViewSet):
    queryset = User_inf.objects.all()
    serializer_class =UserSerializers

    def retrieve(self, request, pk=None):
        queryset = User_inf.objects.all()
        user = User_inf.objects.get(user=User.objects.get(auth_token = pk))
        serializer = UserSerializers(user, context={'request': request})
        return Response(serializer.data)

@api_view(["GET", "PUT"])
def ProfileView(request):
    try:
        item = User_inf.objects.get(uuid=request.data['uuid'])
    except User_inf.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = UserSerializersMin(item,  context={'request': request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializersMin(item, data=request.data, partial=True,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)