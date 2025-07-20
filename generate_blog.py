import openai
from datetime import datetime
import os
import random

openai.api_key = os.getenv("OPENAI_API_KEY")

# List of blog topics (add or modify as you wish)
topics = [
    "How to prepare for an NDIS planning meeting",
    "NDIS and mental health: What you need to know",
    "Navigating NDIS plan reviews",
    "Technology supports for NDIS participants",
    "How to choose an NDIS provider",
    "NDIS supports for carers and families",
    "What is the difference between Core and Capacity Building funding?",
    "Assistive technology options under NDIS",
    "NDIS and early childhood supports",
    "Maximising your NDIS plan"
]

topic = random.choice(topics)

system_prompt = (
    "You are an expert NDIS support coordinator and copywriter for an NDIS provider's website. "
    "Write a professional, warm, participant-focused blog post (800-1000 words) on the following topic. "
    "Start with a real-sounding participant story (name, age, suburb), then cover practical information, tips, and relevant NDIS links. "
    "Format in markdown. Do not invent fake statistics. Use Australian English and include a gentle call-to-action to contact HD Heed for support at the end."
)

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Blog topic: {topic}"}
    ]
)
blog_content = response['choices'][0]['message']['content']

# Make a filename for the new blog post (e.g. "2025-07-21-how-to-prepare-for-an-ndis-planning-meeting.html")
today = datetime.now()
slug = topic.lower().replace(" ", "-").replace("?", "")
filename = f"{today.strftime('%Y-%m-%d')}-{slug}.html"

# Save the blog post as a new HTML file (simple wrapper)
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"<html><head><title>{topic}</title></head><body>\n")
    f.write(f"<h1>{topic}</h1>\n")
    f.write(blog_content.replace('\n', '<br>\n'))
    f.write("\n</body></html>")
