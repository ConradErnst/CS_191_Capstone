
[View the Project Poster](./CS_191_Poster+(1).pdf.pdf)

# Virtual Therapist Capstone Project

Welcome to the repository for our Computer Science Capstone project! This project aimed to create a **virtual therapist application** that mimics the experience of a Zoom therapy session. Despite minimal funding, we successfully built a functional prototype, though the visual model is still a work in progress.

## Features

- **Real-Time Virtual Therapy**: Simulates a live therapy session with dynamic, LLM-generated responses.
- **Emotion Detection**: Integrates basic emotion recognition to personalize interactions.
- **Extensibility**: The foundation for expanding the app into a mobile version.

## Prerequisites

- Python 3.9
- Conda
- API keys

## Installation and Setup

### 1. Create Conda Environment

```bash
conda create --name virtual_therapist python=3.9
conda activate virtual_therapist
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

- Obtain necessary API keys (e.g., OpenAI, etc.)

### 4. Run Development Server

```bash
python manage.py runserver
```

- Open the development server link provided in the terminal to access the application

## Project Development Paths

From the start of the semster we wanted to explore three key development strategies: 

1. **Hand-Building Models**
   - Custom LLM trained for a therapy use case
   - Manually developed an emotion detection model

2. **Using Open Source & APIs**
   - Incorporated various open-source tools and APIs for faster development

3. **Mobile App Extension**
   - Preliminary work started on a mobile app version (currently incomplete)

## Project Status

This repository represents the initial prototype of our virtual therapist application. While some features remain basic due to resource constraints, it provides a solid foundation for future development.

## Contributions

We welcome contributions! Feel free to:
- Fork the repository
- Submit pull requests
- Provide feedback
- Expand on our vision of accessible, virtual mental health support

## Disclaimer

The project is a student capstone project and should be viewed as an experimental prototype. It is not a replacement for professional mental health services.

## License

[Add your license information here]
