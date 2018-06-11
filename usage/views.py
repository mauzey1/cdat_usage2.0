from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from usage.models import *

@csrf_exempt
def add(request):
    print('connected')

    if request.method != "POST":
        print('!POST')
        return HttpResponseBadRequest("POST Only")

    try:
        platform = request.POST["platform"]
        platform_version = request.POST["platform_version"]
        hashed_hostname = request.POST["hashed_hostname"]
        source = request.POST["source"]
        cdat_info_version = request.POST["cdat_info_version"]
        source_version = request.POST["source_version"]
        action = request.POST["action"]
        sleep = request.POST["sleep"]
        pid = request.POST["pid"]
        #login = request.POST["login"]
        login = 'remove me'
        hashed_username = request.POST["hashed_username"]
        gmtime = request.POST["gmtime"]

        ip =  request.META.get('REMOTE_ADDR', '0.0.0.0')
        domain = request.META.get('REMOTE_HOST', 'Unknown')
        print('done with request')
    except Exception as e:
        print('failed in request')
        print(e)


    try:
        entry = Entry()
        entry.platform = platform
        entry.platform_version = platform_version
        entry.hashed_hostname = hashed_hostname
        entry.source = source
        entry.cdat_info_version = cdat_info_version
        entry.source_version = source_version
        entry.action = action
        entry.sleep = sleep
        entry.pid = pid
        entry.login = login
        entry.hashed_username = hashed_username
        entry.gmtime = gmtime
        entry.ip = ip
        entry.domain = domain
        entry.save()
        print('done with save')
    except Exception as e:
        print('failed in save')
        print(e)

    return HttpResponse()
