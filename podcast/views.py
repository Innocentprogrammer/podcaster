from django.shortcuts import render, redirect, get_object_or_404
from features.models import Podcast
from features.forms import PodcastForm
from collections import defaultdict
from django.contrib.auth.decorators import login_required

# Basic Views
def landing(request):
    podcasts = Podcast.objects.all()
    grouped_podcasts = defaultdict(list)
    for podcast in podcasts:
        grouped_podcasts[podcast.category].append(podcast)
    return render(request, 'index1.html', {'grouped_podcasts': dict(grouped_podcasts)})

def most(request):
    return render(request, "most.html")

def upload(request):
    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/upload')
    else:
        form = PodcastForm()
    return render(request, 'upload.html', {'form': form})

def podcast_detail(request, id):
    podcast = get_object_or_404(Podcast, id=id)
    return render(request, 'most.html', {'podcast': podcast})

@login_required
def delete_podcast(request, podcast_id):
    podcast = get_object_or_404(Podcast, id=podcast_id)
    podcast.delete()
    return redirect('landing')


# === Chatbot Views ===
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-pro-exp-03-25",
    generation_config={
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    },
)
chat_session = model.start_chat(history=[])

# Predefined Q&A
ALLOWED_QA = {
    "what is podcaster": "Podcaster is a platform that allows users to upload, manage, and distribute podcasts.",
    "what is podcast": "A podcast is a digital audio program that you can listen to on your phone, computer, or other devices. It's similar to a radio show, but it’s available on-demand, meaning you can listen to it anytime you want.",
    "how to upload a podcast": "Go to the Upload section, fill in the relevant details, and click submit. Your podcast will be uploaded successfully.",
    # Add more QAs as needed
}

def recommend_podcasts(category):
    category = category.lower()
    podcasts = Podcast.objects.filter(category__icontains=category)
    if podcasts.exists():
        return [podcast.title for podcast in podcasts]
    return ["Sorry, no podcasts found in this category."]

# ✅ Function to fetch all unique podcast categories
def get_all_categories():
    categories = Podcast.objects.values_list('category', flat=True).distinct()
    return list(set([cat.strip() for cat in categories if cat]))  # Remove duplicates and strip whitespace
@csrf_exempt
@require_POST
def chatbot_view(request):
    try:
        data = json.loads(request.body)
        user_message = data.get("message", "").strip().lower()

        # Greetings
        if user_message in ['hi', 'hello', 'hey']:
            return JsonResponse({"reply": "Hello! How can I assist you today?"})

        # Static QA
        if user_message in ALLOWED_QA:
            return JsonResponse({"reply": ALLOWED_QA[user_message]})

        # List all podcast categories
        if ("what" in user_message or 'list' in user_message or "recommend" in user_message) and "category" in user_message and "podcast" in user_message:
            categories = get_all_categories()
            if categories:
                return JsonResponse({
                    "reply": f"The available podcast categories are: {', '.join(categories)}"
                })
            else:
                return JsonResponse({"reply": "No podcast categories found yet."})

        # ✅ Predefined categories to detect
        predefined_categories = ["most popular", "news", "crime", "comedy", "sports", "study"]

        for category in predefined_categories:
            if category in user_message:
                podcasts = recommend_podcasts(category)
                return JsonResponse({
                    "reply": f"Here are some podcasts in the '{category.title()}' category: {', '.join(podcasts)}"
                })

        # Fallback
        return JsonResponse({"reply": "Sorry! I can't help you with that."})

    except Exception as e:
        return JsonResponse({"reply": f"Oops! Something went wrong: {str(e)}"}, status=500)
