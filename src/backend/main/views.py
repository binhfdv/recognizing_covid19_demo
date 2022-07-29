from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .ai import predict, get_metadata, detect_cough, convert_webm_to_wav
import os
import json

# Create your views here.
@csrf_exempt
def main(request):
    if request.method != "POST":
        return HttpResponse("NOT FOUND")

    metadata = get_metadata(request.POST)
    input_file = request.FILES["audio"]
    audio_1 = request.FILES["audio_1"]

    try:
        print(audio_1)
        print(type(audio_1))
        cough = detect_cough(audio_1)
    except:
        url_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"weights/recorded/")
        url_save = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"weights/input_file/")
        convert_webm_to_wav(str(request.FILES["audio_1"]),url_path,url_save)
        input_file = os.path.join(url_save, 'soundwebm.wav')
        print(input_file)
        print(type(input_file))
        cough = detect_cough(input_file)

    if cough > 0.5:
        print(input_file)
        print(type(input_file))
        res = predict(input_file,metadata)
        response = {"prob": "Xác xuất dương tính là: "+str(res[0])}
    else:
        response = {"prob": "Không thể xác định âm thanh ho. Vui lòng thử lại"}

    return HttpResponse(json.dumps(response), content_type="application/json")
