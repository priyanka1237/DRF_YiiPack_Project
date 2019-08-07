from django.shortcuts import render
from core1.models import User,PackageType
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import traceback
from django.contrib.auth.models import Permission
from django.views.decorators.csrf import csrf_exempt
from core1.serializers import *
from django.http import JsonResponse
import base64, random, pytz
from datetime import datetime, timedelta, tzinfo
from django.contrib.auth import get_user_model
User = get_user_model() 

errorMessage = "Something went wrong, Please try after sometime."
addSuccessMessage = "Successfully Added"
updateSuccessMessage = "Successfully Updated"
removeSuccessMessage = "Deleted Successfully"
sendSuccessMessage = "send message Successfully"


# api_view(['Post'])
# @csrf_exempt
# def AddAdmin(request):
#     try:
#         with transaction.atomic():
#             email=request.data['email']
#             first_name=request.data['first_name']
#             last_name=request.data['last_name']
#             password=request.data['password']
#             phone = request.data['phone']
#             city = request.data['city']
#             country = request.data['country']
#             zip = request.data['zip']
#             address = request.data['address']
#             user = User.objects.create(
#                                 email=email,
#                                 first_name=first_name,
#                                 last_name=last_name,
#                                 password=make_password(password),
#                                 phone=phone,
#                                 city=city,
#                                 country=country,
#                                 zip=zip,
#                                 address=address,
#                                 is_superuser=0,
#                                 is_staff=0,
#                                 is_active=1,
#                                 role=1
#                                 )
           
#             g = Group.objects.get(name='admin')
#             print(g)
#             g.user_set.add(user)
#             if user is not None:
#                 print(user.email)
#                 return Response({"message" : addSuccessMessage, "status" : "1"}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     except Exception as e:
#         print(traceback.format_exc())
#         # transaction.rollback()
#         return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def AddAdmin(request):
    try:
        with transaction.atomic():
            timeZone = request.META.get('HTTP_TIMEZONE')
            if timeZone is not None:
            # serializer.save()
                email = request.data['email']
                password = request.data['password']
                phone_no = request.data['phone']
                firstname = request.data['first_name']
                lastname = request.data['last_name']
                
                country = request.data['country']
                city = request.data['city']
                address = request.data['address']
                
                timeZone = pytz.timezone(request.META.get('HTTP_TIMEZONE'))
                nowTime = timezone.now().replace(microsecond=0)
                authuser = User.objects.create(username=email,
                                               email=email,
                                               first_name=firstname,
                                               last_name=lastname,
                                               password=make_password(password),
                                               country=country,
                                               city=city,
                                               address=address,
                                               phone=phone_no,
                                               is_superuser=0,
                                               is_staff=0,
                                               is_active=1,
                                               role=1,)
    #                                 date_joined=timezone.now())
                print(authuser.id, "id", type(authuser.id))
                g = Group.objects.get(name='admin')
                g.user_set.add(authuser)
                     
                # token = Token.objects.create(user=authuser)
                        
                userDetail = {
                                # 'token': token.key,
                                'id': authuser.id,
                                'firstname': authuser.first_name,
                                'lastname' : authuser.last_name,
                                'email': authuser.email,
                                'address':authuser.address,
                                'phone_no' :phone_no,
                                             
                            }
                    
                return Response({"status": "1", 'message': 'User has been successfully registered.', 'data': userDetail}, status=status.HTTP_200_OK)
            
            else:
                return Response({'status': "0", 'message': 'Timezone is missing!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    except Exception as e:
        print(traceback.format_exc())
        return Response({"message" : str(e), "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@csrf_exempt
def LoginAdmin(request):
    try:
        with transaction.atomic():
            email = request.data['email']
            password = request.data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                checkGroup = user.groups.filter(name='admin').exists()
                if checkGroup:
                    if user.is_active == 1:
                        
                        token = ''
                        try:
                            user_with_token = Token.objects.get(user=user)
                        except:
                            user_with_token = None
                        if user_with_token is None:
                            token1 = Token.objects.create(user=user)
                            token = token1.key
                        else:
                            Token.objects.get(user=user).delete()
                            token1 = Token.objects.create(user=user)
                            token = token1.key
                        return Response({"status" : "1", "token" : token}, status=status.HTTP_200_OK)
                        
                    else:
                        return Response({"message" : "Your account has been blocked", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({"message" : "Email or Password incorrect", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"message" : "Email or Password incorrect", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(traceback.format_exc())
        # transaction.rollback()
        return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


# @api_view(['POST'])
# def AppLogin(request):
#     try:
#         with transaction.atomic():
            
#             login_status = request.data['login_status']
#             #userTimeZone = request.data['user_time_zone']
#             phone = request.data['phone']
#             email = request.data['email']	
#             firstname = request.data['first_name']
#             lastname = request.data['last_name']
#             socialId = request.data['socialId']
#             image = request.data['image']
#             country = request.data['country']
#             city = request.data['city']
#             address = request.data['address']
#             if(login_status != ""):
                
#                 if(login_status == 'g_login_type_status_email'):  # 1 for phone number
#                     if(email != ""):
#                         try:
#                             existedUser = User.objects.get(email=email)
#                         except:
#                             existedUser = None
                        
#                         if existedUser is not None:
#                             authUser = authenticate(username=email, password=phone)
#                             if authUser is not None:
#                                 checkGroup = authUser.groups.filter(name='User').exists()
#                                 if checkGroup:
                    
#                                     token = ''
#                                     try:
#                                         user_with_token = Token.objects.get(user=authUser)
#                                     except:
#                                         user_with_token = None
#                                     if user_with_token is None:
#                                         token1 = Token.objects.create(user=authUser)
#                                         token = token1.key
#                                     else:
#                                         Token.objects.get(user=authUser).delete()
#                                         token1 = Token.objects.create(user=authUser)
#                                         token = token1.key
                                    
#                                     userDetail = {
#                                         'token':token,
#                                         'first_name':existedUser.first_name,
#                                         'email':existedUser.email, 
#                                         'phone':existedUser.phone, 
#                                         'image':existedUser.image
#                                         }
#                                     return Response({"status" : "1", 'message':'User already exists.', 'data':userDetail}, status=status.HTTP_200_OK)
#                                 else:
#                                     return Response({"message" : "Username or password incorrect", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
#                             else:
                                
#                                 return Response({"message" : "This email is linked with another account.", "status" : "0"}, status=status.HTTP_200_OK)
#                         else:
#                             authUser = User.objects.create_user(username=email,
#                                                email=email,
#                                                first_name=firstname,
#                                                last_name=lastname,
#                                                password=make_password(phone),
#                                                country=country,
#                                                city=city,
#                                                address=address,
#                                                phone=phone,
#                                                login_status=login_status,
#                                                socialId=socialId,
#                                                image=image,
#                                                is_superuser=0,
#                                                is_staff=0,
#                                                is_active=1,
#                                                role=2,)
#                             print(authUser)
#                             g = Group.objects.get(name='User')
#                             g.user_set.add(authUser)
#                             token = Token.objects.create(user=authUser)    
                            
#                             userDetail = {
#                                 'token':token.key, 
#                                 'first_name':authUser.first_name, 
#                                 'email':authUser.email, 
#                                 'phone':authUser.phone, 
#                                 'image':authUser.image
#                                 }
#                             return Response({"status": "1", 'message': 'User has been successfully registered.', 'data': userDetail}, status=status.HTTP_200_OK)
#                     else:
#                         return Response({'success':0, 'status':0, 'message':'Phone Number is Missing.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)                    
#                 else:            
#                     return Response({"status" : "1", 'message':'User has been successfully registered.'}, status=status.HTTP_200_OK)
#             elif(login_status == 'g_login_type_status_facebook'):
#                 pass  # 2 for facebook and email
#     except Exception as e:
#         print(traceback.format_exc())
#         return Response({"status" : "0", 'message':errorMessage}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def AppLogin(request):
    try:
        with transaction.atomic():
            
            login_status = request.data['login_status']
            #userTimeZone = request.data['user_time_zone']
            phone = request.data['phone']
            firstname = request.data['fullName']
            lastname = ''
            email = request.data['email']	
            password = request.data['password']
            age = request.data['date_of_birth']
            socialId = request.data['socialId']
            image = request.data['image']

            if phone is None or phone == "Null" or phone == "null":
                phone = ""
            if email is None or email == "Null" or email == "null":
                email = ""
            if firstname is None or firstname == "Null" or firstname == "null":
                firstname = ""
            else:
                n = firstname.rfind(' ')
                if n != -1:
                    lastname = firstname[n+1:]
                    firstname = firstname[:n]
                else:
                    lastname = ""

            if socialId is None or socialId == "Null" or socialId == "null":
                socialId = ""
            if age is None or age == "Null" or age == "null":
                age = ""
            nowTime = datetime.now()

            if(login_status != ""):
                
                if(login_status == 'g_login_type_status_email'):  # 1 for email
                    if(email != ""):
                        try:
                            existedUser = User.objects.get(email=email)
                        except Exception as e:
                            existedUser = None
                        
                        if existedUser is not None:
                            authUser = authenticate(username=email, password=password)
                            print(authUser)
                            if authUser is not None:
                    
                                token = ''
                                try:
                                    user_with_token = Token.objects.get(user=authUser)
                                except:
                                    user_with_token = None
                                if user_with_token is None:
                                    token1 = Token.objects.create(user=authUser)
                                    token = token1.key
                                else:
                                    Token.objects.get(user=authUser).delete()
                                    token1 = Token.objects.create(user=authUser)
                                    token = token1.key
                                    
                                    
                                return Response({"status" : "1", "token" : token}, status=status.HTTP_200_OK)
                                
                            else:
                                
                                return Response({"message" : "This email is already used", "status" : "0"}, status=status.HTTP_200_OK)
                        else:
                            authUser = User.objects.create(username=email,
                                               email=email,
                                               first_name=firstname,
                                               last_name='',
                                               password=make_password(password),
                                               phone=phone,
                                               login_status=login_status,
                                               date_of_birth=age,
                                               socialId=socialId,
                                               image=image,
                                               is_superuser=0,
                                               is_staff=0,
                                               is_active=1
                                               )
                        
                            
                            
                            token = Token.objects.create(user=authUser)    
                            
                            userDetail = {
                                'token':token.key, 
                                'fullname':authUser.first_name, 
                                'email':authUser.email, 
                                'phone':authUser.phone, 
                                'image':authUser.image
                                }
                            return Response({"status": "1", 'message': 'User has been successfully registered.', 'data': userDetail}, status=status.HTTP_200_OK)
                    else:
                        return Response({'success':0, 'status':0, 'message':'email is Missing.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)                    
                
            
                elif(login_status == 'g_login_type_status_facebook'or login_status=='g_login_type_status_google'):  # 2 for facebook 
                    if socialId != "":
                            try:
                                existedUser = User.objects.get(socialId=socialId)
                                print(existedUser)
                            except:
                                existedUser = None
                            if existedUser is not None:
                                    authUser = authenticate(username=socialId, password=socialId)
                                    token = ''
                                    try:
                                        user_with_token = Token.objects.get(user=authUser)
                                    except:
                                        user_with_token = None
                                    if user_with_token is None:
                                        token1 = Token.objects.create(user=authUser)
                                        token = token1.key
                                    else:
                                        Token.objects.get(user=authUser).delete()
                                        token1 = Token.objects.create(user=authUser)
                                        token = token1.key 
                                    User.objects.filter(id = existedUser.id).update(first_name=firstname, last_name=lastname)
                                    userDetail = {
                                            'token':token,
                                            'first_name':existedUser.first_name,
                                            'email':existedUser.email, 
                                            'phone':existedUser.phone, 
                                            'image':existedUser.image
                                            }
                                    return Response({"status" : "1", 'message':'User already exists.', 'data':userDetail}, status=status.HTTP_200_OK)
                                        
                            else:
                                if(request.data['image'] is not None and request.data['image'] != ""):
                                    imageName = 'ka_' + request.data['fullname'].partition(' ')[0] + '_' + nowTime.strftime("%S%H%M%f") + '.jpg'
                                    try:
                                        format, tempString = request.data['image'].split(';base64,')
                                    except:
                                        tempString = ""
                                    if tempString == "":
                                        tempString = request.data['image']
                                    image_64_decode = base64.decodestring(tempString) 
                                    fh = default_storage.open("profilepic/" + imageName, 'w')  # create a writable image and write the decoding result
                                    fh.write(image_64_decode)
                                    fh.close()
                                    profilepicUrl = settings.MEDIA_URL + "profilepic/" + imageName
                                else:
                                    profilePicUrl = ''
                                try:
                                    existedPhone = User.objects.get(phone=phone)
                                except:
                                    existedPhone = None
                                if existedPhone is not None:
                                    phoneNumber = ''
                                else:
                                    phoneNumber = phone
                                emailId = email
                                authUser = User.objects.create(username=socialId,
                                            email='',
                                            first_name='',
                                            last_name='',
                                            password=make_password(socialId),
                                            socialId=socialId,
                                            login_status=login_status,
                                            is_superuser=0,
                                               is_staff=0,
                                               is_active=1
                                )
                                token = Token.objects.create(user=authUser)
                                userDetail = {
                                    'token':token.key, 
                                    'first_name':authUser.first_name, 
                                    'email':authUser.email, 
                                    'phone':authUser.phone, 
                                    'image':authUser.image
                                    }
                                return Response({"status": "1", 'message': 'User has been successfully registered.', 'data': userDetail}, status=status.HTTP_200_OK)
                                                
                    else:            
                        return Response({'status':"0", 'message':'Email is Missing.'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({'status':"0", 'message':'Invalid Login type.'}, status=status.HTTP_401_UNAUTHORIZED)    
            else:
                 return Response({'status':"0", 'message':'please provide all details.'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(traceback.format_exc())
        return Response({"status" : "0", 'message':errorMessage}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)








@api_view(['GET'])
def getUserList(request):
    try:
        with transaction.atomic():
            API_key = request.META.get('HTTP_AUTHORIZATION')
        if API_key is not None:
            try:
                token1 = Token.objects.get(key=API_key)
                user = token1.user
                checkUser = user.groups.filter(name='User').exists()
                print(checkUser)
            except:
                return Response({'message' : "Session expired! Please login again","status":"0"},status=status.HTTP_401_UNAUTHORIZED)
                
            if checkUser is not None:
                user1 = User.objects.get(id=user.id)
                print(user1)
                userdetail = {
                    "first_name":user1.first_name,
                    "last_name":user1.last_name,
                    "phone" : user1.phone,
                    "email" : user1.email,
                    "address" : user1.address
                    }
                return Response({"status": "1", 'message': 'Get successfully.', 'data':userdetail}, status=status.HTTP_200_OK)

            else:
                return Response({"message": errorMessage, "status": "0"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": errorMessage, "status": "0"}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        #print(e)
        print(traceback.format_exc())

        return Response({"message": errorMessage, "status": "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def EditUserProfile(request):
    try:
        with transaction.atomic():
            API_key = request.META.get('HTTP_AUTHORIZATION')
            if API_key is not None:
                try:
                    token1 = Token.objects.get(key=API_key)
                    user = token1.user
                    checkGroup = user.groups.filter(name='User').exists()
                    print(checkGroup)
                except:
                    return Response({"message": "Session expired!! please login again", "status": "0"},status=status.HTTP_401_UNAUTHORIZED)
                if checkGroup:
                    userr = User.objects.get(id=user.id) 
                    print(userr)
                    firstname = request.data['firstname']
                    lastname = request.data['lastname']
                    age = request.data['age']
                    country = request.data['country']
                    city = request.data['city']
                    update1 = User.objects.filter(id=userr.id).update(first_name=firstname, last_name=lastname, date_of_birth=age, country=country, city=city)
                    
                    if update1:
                        user1 = User.objects.get(id=userr.id)
                        data = {
                            "firstname":user1.first_name,
                            "email":user1.email,
                        
                            }
                        
                        return Response({"status": "1", 'message': 'Updated successfully.', 'data':data }, status=status.HTTP_200_OK)
                    else:
                        return Response({"message": errorMessage, "status": "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response({"message": errorMessage, "status": "0"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"message": errorMessage, "status": "0"}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        print(traceback.format_exc())
        return Response({"message" : str(e), "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def addPackageType(request):
    try:
        with transaction.atomic():
            API_key = request.META.get('HTTP_AUTHORIZATION')
            if API_key is not None:
                try:
                    token1 = Token.objects.get(key=API_key)
                    user = token1.user
                    checkGroup = user.groups.filter(name='admin').exists()
                    print(checkGroup)
                except:
                    return Response({"message" : "Session Expired!! Please Login Again", "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
                if checkGroup:
                    permissions = Permission.objects.filter(user=user)
                    if user.has_perm('core1.add_packagetype'):
                        name = request.data["name"]
                        authuser = PackageType.objects.create(
                                                            name=name,
                                             )
                        if authuser is not None:
                            print(authuser)
                            return Response({"message" : addSuccessMessage, "status" : "1"}, status=status.HTTP_201_CREATED)
                        else:
                            return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    else:
                        return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"message" : errorMessage, "status" : "0"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(traceback.format_exc())
        return Response({"message" : str(e), "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
