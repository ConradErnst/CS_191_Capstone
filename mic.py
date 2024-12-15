import sounddevice as sd
import numpy as np
import keyboard
import threading
import queue
import wavio

# Parameters
sample_rate = 44100  # audio sample rate
output_file = "output.wav"
buffer_size = int(sample_rate * 0.1)  # buffer size for audio recording (0.1 seconds)

# Global variables
audio_data_queue = queue.Queue()
recording = False

# Function to record audio in a separate thread
def record_audio():
    global recording
    print("Press and hold the space bar to start recording. Release to stop.")
    with sd.InputStream(callback=callback, channels=1, dtype=np.int16):
        keyboard.wait("space", suppress=True, trigger_on_release=True)
        recording = True
        while recording:
            pass
    print("Recording stopped.")

# Callback function for audio recording
def callback(indata, frames, time, status):
    if status:
        print(f"Error in audio callback: {status}")
    audio_data_queue.put(np.copy(indata))

# Save audio data to a WAV file
def save_audio(filename, audio_data, sample_rate):
    print(f"Saving audio to {filename}...")
    wavio.write(filename, audio_data, sample_rate, sampwidth=3)
    print("Audio saved.")

if __name__ == "__main__":
    # Start the recording thread
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

    # Wait for the space bar to be pressed again to stop recording
    keyboard.wait("space", suppress=True, trigger_on_release=True)

    # Stop recording
    recording = False
    recording_thread.join()
 
    # Retrieve and save recorded audio
    audio_data = []
    while True:
        try:
            audio_frame = audio_data_queue.get_nowait()
            audio_data.append(audio_frame)
        except queue.Empty:
            break

    if audio_data:
        audio_data = np.concatenate(audio_data, axis=0)
        save_audio(output_file, audio_data, sample_rate)
    else:
        print("No audio data recorded.")
