import os

from django.shortcuts import render



def index(request):
    build_object = {
        "VERSION": os.getenv('VERSION'),
        # "CIRCLE_BUILD_URL": os.getenv('CIRCLE_BUILD_URL'),
        # "CIRCLE_SHA1": os.getenv('CIRCLE_SHA1'),
        # "CIRCLE_USERNAME": os.getenv('CIRCLE_USERNAME'),
        # "CIRCLE_BUILD_NUM": os.getenv('CIRCLE_BUILD_NUM')
    }

    return render(request, 'demo/index.html', build_object)

