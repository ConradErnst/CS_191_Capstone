function changeProfileImage() {
    document.getElementById('profileImage').src = '{% static "img/profile_hover.png" %}';
}

function restoreProfileImage() {
    document.getElementById('profileImage').src = '{% static "img/profile.png" %}';
}

let isRecording = false;
let recognition = new webkitSpeechRecognition(); // Using webkitSpeechRecognition for Chrome

recognition.continuous = true;
recognition.interimResults = true;

recognition.onresult = function(event) {
    let result = event.results[event.results.length - 1];
    let text = result[0].transcript;
    document.getElementById('user-input').value = text;
};

function toggleRecording() {
    var image = document.getElementById('buttonImage');
    
    if (!isRecording) {
        recognition.start();
        isRecording = true;
        document.getElementById('recordButton').style.backgroundColor = '#d2d2d2';
        // Change image source to the clicked state
        image.src = "{% static 'img/mic_clicked.png' %}";
    } else {
        recognition.stop();
        isRecording = false;
        document.getElementById('recordButton').style.backgroundColor = ''; // Restore default color
        // Change image source back to the default state
        image.src = "{% static 'img/mic.png' %}";

    }
}

function sendMessage() {
    var userMessage = document.getElementById('user-input').value;

    // Append user's outgoing message
    var chatbox = document.getElementById('chatbox');
    var outgoingMessage = document.createElement('li');
    outgoingMessage.className = 'chat outgoing'; // Add 'outgoing' class for outgoing messages
    outgoingMessage.innerHTML = '<p>' + userMessage + '</p>';
    chatbox.appendChild(outgoingMessage);

    // Send user message to the chatbot endpoint using AJAX
    fetch('/chatbot_endpoint/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // Include Django CSRF token
        },
        body: JSON.stringify({'user_input': userMessage}),
    })
    .then(response => response.json())
    .then(data => {
        // Append incoming message from the chatbot
        var incomingMessage = document.createElement('li');
        incomingMessage.className = 'chat incoming'; // Add 'incoming' class for incoming messages
        incomingMessage.innerHTML = '<p>' + data.response + '</p>';
        chatbox.appendChild(incomingMessage);

        // Scroll to the bottom of the chatbox to show the latest messages
        chatbox.scrollTop = chatbox.scrollHeight;

        // Update the video after chat update is complete
        updateVideo();
    })
    .catch(error => console.error('Error:', error));

    // Clear the input field
    document.getElementById('user-input').value = '';
}

// Function to update the video
function updateVideo() {
    console.log("before video");
    document.getElementById('video').load(); // Load the new video
    console.log("updated video");
}





// Function to set up the camera stream and send frames to the backend
function setupCamera() {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            // Save the stream to a global variable for later use
            window.cameraStream = stream;
            // Continuously send frames to the backend for processing
            setInterval(sendFrameToBackend, 1000); // Capture a frame every second
        })
        .catch(function (err) {
            console.error('Error accessing camera:', err);
        });
}

// Function to send a frame to the backend
function sendFrameToBackend() {
    // Capture a frame from the camera stream
    const videoTrack = window.cameraStream.getVideoTracks()[0];

    const imageCapture = new ImageCapture(videoTrack);

    imageCapture.grabFrame()
        .then(function (frame) {
            // Convert the frame to base64 or any other format you need
            const base64Frame = frameToBase64(frame);
            // Extract base64 data from the frame
            // Send frame data to the backend
            $.ajax({
                url: '/handle_frame',
                method: 'POST',
                data: { frame: base64Frame },
                success: function (response) {
                    console.log('Frame sent successfully:', response);
                    updateProcessedFrame(response.processed_frame);
                },
                error: function (error) {
                    console.error('Error sending frame:', error);
                }
            });
        })
        .catch(function (err) {
            console.error('Error capturing frame:', err);
        });
}

// Function to convert a frame to base64 (you can customize this)
function frameToBase64(frame) {
    // Implement your logic to convert the frame to base64
    // For example, you can use a canvas to draw the frame and then get its data URL
    const canvas = document.createElement('canvas');
    canvas.width = frame.width;
    canvas.height = frame.height;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(frame, 0, 0, frame.width, frame.height);
    return canvas.toDataURL('image/jpeg'); // Change format if needed
}

// Call the setupCamera function when the DOM is ready
document.addEventListener('DOMContentLoaded', setupCamera);

function updateProcessedFrame(processedFrameData) {
    // Get the <img> element by its id
    var imgElement = document.getElementById('processed-frame');
    // Set the src attribute of the <img> element with the base64-encoded processed frame data
    imgElement.src = 'data:image/jpeg;base64,' + processedFrameData;
}
