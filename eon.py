from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))


def generate_image(prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
prompt = "A futuristic city with flying cars"
image_url = generate_image(prompt)
if image_url:
    print(f"Image generated: {image_url}")
else:
    print("Failed to generate image")
