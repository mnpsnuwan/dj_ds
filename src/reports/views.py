from django.shortcuts import render
from django.shortcuts import HttpResponse
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report

# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def create_report_view(request):
    if is_ajax(request=request):
        name = request.POST.get('name')
        remarks = request.POST.get('remarks')
        image = request.POST.get('image')

        img = get_report_image(image)

        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name, remarks=remarks, image=img, author=author)
        return JsonResponse({'msg':'sent'})
    return JsonResponse({})

