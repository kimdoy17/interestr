# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

users = {
    'apptoken' : 888888,
    'paul': {
        'interests' : ['science', 'music', 'math']
    },
    'rob': {
        'interests': ['coding', 'drugs']
    },
    'simmerd' : {
        'interests' : ['kenya', 'bioinformatics', 'medieval womans poetry']
    },
    'minham' : {
        'interests' : ['hockey', 'india', 'bananas']
    }
}
# Create your views here.
@api_view(["POST"])
def RetrieveUserData(data):
    try:
        interests = None
        data=json.loads(data.body.decode('utf-8'))
        apptoken=data["apptoken"]
        user=data["userid"]
        if apptoken == "888888":
            # if user == "paul":
            interests = users[user]["interests"]
        return JsonResponse(user + "'s interests are " + str(interests),safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
