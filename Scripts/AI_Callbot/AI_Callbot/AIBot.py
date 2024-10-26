import os
import wave
import json
from vosk import Model, KaldiRecognizer

# Paths
MODEL_PATH = r"C:\Users\nyada\vosk_model\vosk-model-small-en-us-0.15"
AUDIO_FILE = r"c:\Users\nyada\Downloads\Recording (4).wav"

# Check if model path exists
if not os.path.exists(MODEL_PATH):
    raise Exception("Please download the model and unpack it to the correct folder.")

# Initialize the model
model = Model(MODEL_PATH)

# Open the audio file
wf = wave.open(AUDIO_FILE, "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() > 16000:
    raise Exception("Audio file must be WAV format mono PCM with a max sample rate of 16kHz.")

# Initialize the recognizer
rec = KaldiRecognizer(model, wf.getframerate())

# Process the audio and collect the final result
print("Processing audio...")
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print("Recognized Text:", json.loads(result)["text"])

# Extract final recognized text
final_result = rec.FinalResult()
recognized_text = json.loads(final_result).get("text", "")

# Check if recognized text exists
if not recognized_text:
    print("No text recognized.")
else:
    # Use the recognized text in a query
    query = f"Put your query here: {recognized_text}"
    print(query)


import requests

# Replace with your actual API key and external user ID
api_key = 'YXM2VzXWv46qgOrDWdWzafvcEFknlbwC'
external_user_id = 'nitin@354'

# Step 1: Create Chat Session
create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
create_session_headers = {
    'apikey': api_key
}
create_session_body = {
    "pluginIds": [],
    "externalUserId": external_user_id
}

# Make the request to create a chat session
create_session_response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
create_session_data = create_session_response.json()

# Extract the session ID from the response
session_id = create_session_data['data']['id']

# Step 2: Submit Query
submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
submit_query_headers = {
    'apikey': api_key
}
submit_query_body = {
    "endpointId": "predefined-openai-gpt4o",
    "query": f"patient query is: {result}, answer as a call bot for appointments in particular department ",
    "pluginIds": ["plugin-1712327325", "plugin-1713962163"],
    "responseMode": "sync"
}

# Make the request to submit a query
submit_query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
submit_query_data = submit_query_response.json()

# Print the response from the query submission
print(submit_query_data['data']['answer'])
