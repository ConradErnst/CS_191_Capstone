from django.urls import path
from .views import home, handle_frame, chatbot_endpoint, text_in_speech_out

urlpatterns = [
    path('', home, name='home'),
    path('chatbot_endpoint/', chatbot_endpoint), 
    path('handle_frame', handle_frame, name='handle_frame'),
    path('text_in_speech_out/', text_in_speech_out, name='text_in_speech_out'),
    # ... other paths
]

