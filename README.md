# EON.AI Image Generator Using Flask, OpenAI DALL·E API, and Python

This project is an AI-powered image generator built using Flask, the OpenAI DALL·E API, and Python. With this tool, users can generate stunning, high-quality images based on simple text prompts. By leveraging OpenAI's advanced DALL·E model, this project makes it easy to create AI-generated images through a user-friendly web interface.

## Key Features:
- **Text-to-Image Generation:** Input any descriptive text prompt, and the AI will generate a corresponding image with remarkable creativity and detail.
- **Flask Web Application:** The project uses Flask to create a simple yet powerful web interface for easy interaction with the AI model.
- **Python-Powered Backend:** Python powers the backend, handling API requests, image processing, and user interactions.
- **OpenAI DALL·E Integration:** Utilizes OpenAI's DALL·E API to generate high-quality images from text prompts in seconds.

## How It Works:
1. **Set Up the Environment:** Install the required dependencies, including Flask and OpenAI's Python client library.
2. **API Key Configuration:** Secure your OpenAI API key and configure it within the Flask app to enable access to DALL·E's image generation service.
3. **Build the Flask App:** The app provides a simple web form where users can enter a text prompt. Once submitted, the app communicates with the OpenAI DALL·E API to generate an image.
4. **Display and Download:** The generated image is displayed directly in the browser, where users can view and download the image.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-image-generator.git
   cd ai-image-generator
2. Create and activate a virtual environment:
`python3 -m venv venv
source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
3. Install the required dependencies:
   `pip install -r requirements.txt`
4. Set your OpenAI API key as an environment variable:
   `export OPENAI_API_KEY='your-api-key-here'`
5. Run the Flask app:
   `flask run`

6. Enter a text prompt, and the app will generate and display the image based on your input.

Project Structure
app.py: The main Flask application that routes user inputs and handles interactions with the OpenAI DALL·E API.
templates/: Contains the HTML templates used by Flask for rendering the web interface.
static/: Holds static files like CSS, JavaScript, or images.


### Key Adjustments for README:
- Added proper Markdown formatting for code blocks, headers, and lists.
- Included step-by-step installation and setup instructions typical for README files.
- Included a "Project Structure" section to give an overview of the files and directories.
- Kept the description SEO-friendly while ensuring clarity for developers visiting your repo.

You can directly paste this into your `README.md` file, and it will render cleanly on GitHub.

