from flask import Flask, jsonify, render_template, request
from openai import OpenAI
from config import Key

app = Flask(__name__)
client = OpenAI(api_key=Key)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/generateimages', methods=['POST'])
def generate():
        prompt = request.json.get('prompt')
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            return jsonify({'url': image_url})
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
        app.run(debug=True)