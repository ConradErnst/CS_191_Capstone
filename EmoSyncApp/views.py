from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .EmotionDetection.emotions import EmotionDetector
from utils import text_in_speech_out, LLM
from PIL import Image
import threading
import io
import base64
import cv2
import numpy as np

last_detected_emotion = None
emotion_lock = threading.Lock()  # Lock for thread safety

# Create an instance of the EmotionDetector class
emotion_detector = EmotionDetector()

def home(request):
    if request.method == 'GET':
        return render(request, 'home/second_page.html')

@csrf_exempt
def chatbot_endpoint(request):
    if request.method == 'POST':
        user_input = json.loads(request.body.decode('utf-8'))['user_input']
    
        # Lock to ensure thread safety
        with emotion_lock:
            emotion = last_detected_emotion
        
        # Create an instance of the LLM class
        llm_instance = LLM()
        
        # Call the text_in_text_out method on the instance
        model_output = llm_instance.text_in_text_out(input_text=user_input, emotion=emotion)
    
        text_in_speech_out(model_output)
         # Start a new thread to call text_in_speech_out function
        # thread = threading.Thread(target=text_in_speech_out, args=(model_output,))
        # thread.start()

        # Return the model output as JsonResponse
        response_data = {'response': model_output}
        response = JsonResponse(response_data)
        
        return response

@csrf_exempt
def handle_frame(request):

    global last_detected_emotion

    if request.method == 'POST':
        base64_frame = request.POST.get('frame')
        _, encoded_frame = base64_frame.split(',', 1)
            # Decode the base64 data into bytes
        frame_bytes = base64.b64decode(encoded_frame)
            # Convert bytes to numpy array
        image_array = np.frombuffer(frame_bytes, np.uint8)
            # Decode the numpy array as an image using OpenCV
        frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # Call the detect_emotion method with the frame
        processed_frame, emotions = emotion_detector.detect_emotion(frame)
        
        print(emotions)
        with emotion_lock:
            last_detected_emotion = emotions[0] if emotions else None

        # Convert processed frame to base64
        _, encoded_frame = cv2.imencode('.jpg', processed_frame)
        base64_processed_frame = base64.b64encode(encoded_frame).decode('utf-8')

        return JsonResponse({'processed_frame': base64_processed_frame, 'emotions': emotions})
        
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
