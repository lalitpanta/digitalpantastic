
import json
import threading
import os
from dotenv import load_dotenv
from openai import OpenAI
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env file!")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

# Global variables for business info
business_info = {}
business_context = "You are a helpful AI assistant."

def load_business_context():
    """Load business information and create context"""
    global business_info, business_context
    try:
        with open("aboutbusiness.json", "r", encoding="utf-8") as f:
            business_info = json.load(f)
            json_string = json.dumps(business_info, indent=2)
        
        business_context = f"""You are Lalit Pant's AI Assistant on his portfolio website.
Below is the comprehensive information about Lalit Pant, including his projects, skills, education, and FAQ.

<business_info>
{json_string}
</business_info>

RULES - BE CONCISE & SWEET:
1. Base your answers strictly on the provided <business_info> JSON.
2. If the user asks a question that is in the "faq_bot_questions", try to use the exact or similar answer provided there.
3. ALWAYS respond in 1-2 sentences MAXIMUM unless explicitly asked for a list or detailed explanation.
4. Be super brief, direct, and helpful.
5. Be warm and friendly but not chatty.
6. Answer only what's asked - no extra fluff.
7. If outside scope, politely say you don't know and redirect them to contact Lalit directly at pantlaalit@gmail.com.
8. NO lengthy explanations - straight to the point."""
        print(f"\n✓ Business loaded: {business_info.get('full_name', 'N/A')} ({business_info.get('professional_title', 'N/A')})")
        print("=" * 60)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        business_context = "You are a helpful AI assistant."
        print(f"\n⚠ No business info found. Edit aboutbusiness.json with your business details.")

class BusinessFileHandler(FileSystemEventHandler):
    """Watch for changes to aboutbusiness.json"""
    def on_modified(self, event):
        if event.src_path.endswith('aboutbusiness.json'):
            print("\n📝 Detected changes to aboutbusiness.json - reloading...")
            load_business_context()

# Load business context on startup
load_business_context()

# Start file watcher in background thread
def start_file_watcher():
    observer = Observer()
    observer.schedule(BusinessFileHandler(), path='.', recursive=False)
    observer.start()

watcher_thread = threading.Thread(target=start_file_watcher, daemon=True)
watcher_thread.start()

# Load existing chat history
try:
    with open("chat_history.json", "r") as f:
        conversation = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    conversation = []

# Show greeting if no conversation history
if not conversation:
    print("\n💻 Lalit Pant AI Assistant")
    print("=" * 60)
    print("Hey! I am Lalit Pant, how can I help you?\n")

while True:
    user = input("You: ")

    conversation.append({
        "role": "user",
        "content": user
    })

    response = client.chat.completions.create(
        model="anthropic/claude-3-haiku",
        messages=[{"role": "system", "content": business_context}] + conversation
    )

    reply = response.choices[0].message.content

    print("Agent:", reply)

    conversation.append({
        "role": "assistant",
        "content": reply
    })

    # Save chat history to JSON
    with open("chat_history.json", "w") as f:
        json.dump(conversation, f, indent=2)

