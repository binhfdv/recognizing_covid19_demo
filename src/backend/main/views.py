from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .ai import predict, get_metadata, detect_cough
import json

# Create your views here.
@csrf_exempt
def main(request):
    if request.method != "POST":
        return HttpResponse("NOT FOUND")
    metadata = get_metadata(request.POST)
    cough = detect_cough(request.FILES["audio_1"])

    if cough > 0.5:
        res = predict(request.FILES["audio"],metadata)
        response = {"prob": "Xác xuất dương tính là: "+str(res[0])}
    else:
        response = {"prob": "Không thể xác định âm thanh ho. Vui lòng thử lại. ("+str(cough)+")"}
    return HttpResponse(json.dumps(response), content_type="application/json")
