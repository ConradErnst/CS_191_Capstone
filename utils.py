import openai
import pygame
import time
import requests
import openai
import os
from LipSyncAI import LS as ls

class LLM:
    def __init__(self):
        self.conversation_history = []

    def _initialize_therapist(self, input_text):
        return [
            {"role": "system", "content": "Assume the role of a therapist. Your task is to engage with the user as if you were conducting a therapy session. Provide a single response based on the user's prompt"},
            {"role": "user", "content": input_text}
        ]

    def text_in_text_out(self, input_text, emotion=None, max_tokens=100, temperature=0.05):

        openai.api_key = #will need generate  

        # Initialize conversation with therapist prompt if history is empty
        if not self.conversation_history:
            self.conversation_history.extend(self._initialize_therapist(input_text))
        else:
            
            # Append detected emotion and instruction to the prompt if emotion is provided 
            if emotion:
                # Construct the prompt including input_text and emotion information
                prompted_prompt = f"{input_text}\n\nEmotion: {emotion}\nGenerate a response based on the provided prompt while considering the accompanying emotion, ensuring that the tone of the response aligns with the conveyed emotion.\n\n"
                
            else:
                # Construct the prompt without emotion information
                prompted_prompt = f"{input_text}\n\nGenerate a response based on the provided prompt.\n\n"

            
            self.conversation_history.append({"role": "user", "content": prompted_prompt})

        # Construct prompt from conversation history
        prompt = "\n".join([msg['content'] for msg in self.conversation_history])

        
        # Send request to OpenAI API with prompt including emotion and instruction
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        # Extract AI's response
        ai_response = response.choices[0].text.strip()

        # Remove "Therapist:" prefix if present
        ai_response = ai_response.replace("Therapist:", "").strip()

        # Update conversation history
        self.conversation_history.append({"role": "system", "content": ai_response})

        return ai_response


def text_in_speech_out(input_text):

    url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"
    api_key = #will need to generate


    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "text": f"{input_text}"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Save the response content to a file
        with open("/Users/conradernst/Desktop/Undergrad/Spring_2024/CS_191/CS_191/speech.mp3", "wb") as f:
            f.write(response.content)
        print("audio file saved successfully.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    
    aux = #will need to generate
    pic = #will need to generate

    output = ls.LipS(pic = pic, aux = aux)
    face = output['output']['output_video']

    
    response = requests.get(face)
    
    #will need to generate
    with open("", "wb") as file:
        file.write(response.content)

    print("face file saved successfully")