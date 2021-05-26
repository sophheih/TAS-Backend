from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from data_api.serializer import DataSerializer
from TASBackend.models import data
from mongoengine.errors import ValidationError

@api_view(["GET"])
def get_member(request, member_id, timestamp):
    member_filter = {'member_id': member_id, 'timestamp': timestamp} 
    
    try: 
        curMember = data.objects(__raw__ = member_filter)
    except data.DoesNotExist:
        return JsonResponse(
            {'message': 'Member is not in database.'},
            status = status.status.HTTP_400_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'Member does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )
    serializer = DataSerializer(curMember)
    return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )

@api_view(["POST"])
def add_member(request):
    input = JSONParser().parse(request)
    nutritionDict = input.get("Data")
    member_id = input.get("Member_id")
    timestamp = input.get("Timestamp")

    if member_id is None:
        msg = {'message': 'body parameter "Member_id" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if timestamp is None:
        msg = {'message': 'body parameter "Timestamp" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if nutritionDict is None:
        msg = {'message': 'body parameter "Data" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)

    member_filter = {'member_id': member_id, 'timestamp': timestamp} 

    try: 
        curMember = data.objects.gets(__raw__ = member_filter)
        for item in curMember.Data.keys():
            curMember.Data[item] += nutritionDict[item]

        serializer = DataSerializer(data = { 
            'Member_id': member_id,
            'Timestamp': timestamp,
            'Data': curMember.Data, 
            
        }) 

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    except data.DoesNotExist:
        serializer = DataSerializer(data = { 
            'Member_id': member_id,
            'Timestamp': timestamp,
            'Data': nutritionDict, 
            
        }) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

