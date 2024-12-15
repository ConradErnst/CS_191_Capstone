import os
import requests
import json

class LS:
    def __init__(self, pic, aux):
        self.pic = pic
        self.aux = aux
 
    def LipS(pic, aux):
        files = [
            ("input_face", open(pic, "rb")),
            ("input_audio", open(aux, "rb")),
        ]

        payload = {
            "face_padding_top": 1,
            "face_padding_bottom": 5,
            "face_padding_left": 1,
            "face_padding_right": 1,
        }

        response = requests.post(
            "https://api.gooey.ai/v2/Lipsync/form/",
            headers={
                "Authorization": "",
            },    
            files=files,
            data={"json": json.dumps(payload)},
        )
        assert response.ok, response.content

        result = response.json()
        return(result)
