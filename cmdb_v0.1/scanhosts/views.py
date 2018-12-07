from django.shortcuts import render

# Create your views here.
from .models import UserIpInfo, BrowseInfo
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
import json

def user_info(request:HttpRequest):
    try:
        header_infos = request.META
        user_agent = header_infos['HTTP_USER_AGENT']
        user_ip = header_infos['REMOTE_ADDR']

        data = {}
        user_obj = UserIpInfo.objects.filter(ip=user_ip)
        if user_obj:
            data['exist'] = True
            res = UserIpInfo.objects.filter(ip=user_ip).get()
        else:
            data['exist'] = False
            # user = UserIpInfo()
            # browse = BrowseInfo()
            # user.ip = user_ip
            # user.save()
            res = UserIpInfo.objects.create(ip=user_ip)
        user_id = res.id

        BrowseInfo.objects.create(userip_id=user_id, useragent=user_agent)
        data['ip'] = user_ip
        return JsonResponse(data)
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(e)

def get_info(request:HttpRequest):
    try:
        header_infos = request.META
        user_ip = header_infos['REMOTE_ADDR']
        data = {}
        query = UserIpInfo.objects.filter(ip=user_ip)
        result =[]
        if not query:
            data['res'] = False
        else:
            user_obj = query.get()
            data['res'] = True
            result = [ i.useragent for i in BrowseInfo.objects.filter(userip_id=user_obj.id)]
        data['result'] = result
        return JsonResponse(data)
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(e)