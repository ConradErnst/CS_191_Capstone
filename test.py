import requests

# Define the API endpoint
url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"

# Set your Deepgram API key
api_key = #will need to generate

# Define the headers
headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
}

# Define the payload
payload = {
    "text": f"{input_text}"
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a file
    with open("your_output_file.mp3", "wb") as f:
        f.write(response.content)
    print("File saved successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")
