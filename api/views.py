from django.shortcuts import render
import cohere
#import openai
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dotenv import load_dotenv

load_dotenv()   #load API Keys from .env

from django.conf import settings

#openai.api_key = settings.OPEN_API_KEY  # read API key

# get the API key from .env file
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# initialize cohere API client
cohere_client = cohere.Client(COHERE_API_KEY)

# Create your views here.

def index(request):
    return render(request, 'index.html')    #serves the html file created

@csrf_exempt
def generate_text(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "").strip()

            # validate input

            # check if prompt is empty
            if not prompt:
                return JsonResponse({'error': 'Prompt is required'}, status=400)
            
            # check if prompt length is short
            if len(prompt) < 5:
                return JsonResponse({'error': 'Prompt must be atleast 5 character long'}, status=400)
            if len(prompt) > 100:
                return JsonResponse({'error': 'Prompt is too long. Limit is 100 characters'}, status=400)

            # Call cohere API
            response = cohere_client.generate(
                model = "command",    # or another model like gpt-4 if needed
                prompt = prompt,
                max_tokens=10000
            )
            
            generate_text = response.generations[0].text # extract generated text

            return JsonResponse({"response": generate_text}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"message": "Send a POST request"}, status=400)



