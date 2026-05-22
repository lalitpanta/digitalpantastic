# Environment Variables Guide

## Local Development

### 1. Create `.env` file
Copy `.env.example` and rename to `.env`:
```bash
cp .env.example .env
```

### 2. Add Your API Key
Edit `.env` and add your OpenRouter API key:
```
OPENROUTER_API_KEY=sk-or-v1-your-actual-api-key
```

Get free API key: https://openrouter.ai

### 3. Run Locally
```bash
python server.py
# or
python agent.py
```

---

## Render Deployment

### ⚠️ IMPORTANT: Never Commit `.env` to GitHub!

The `.gitignore` file already excludes `.env`, so your API key stays private.

### Steps to Set Environment on Render:

1. **Go to Render Dashboard**
2. **Select Your Web Service** (ai-chatbot)
3. **Go to "Environment"** tab
4. **Add Environment Variable:**
   - **Key**: `OPENROUTER_API_KEY`
   - **Value**: `sk-or-v1-your-api-key` (your actual key)

5. **Click "Save"**
6. **Service auto-redeploys** with new environment

---

## Security Best Practices ✅

✅ **Do:**
- Store sensitive keys in `.env` file
- Add `.env` to `.gitignore`
- Use environment variables in Render
- Rotate API keys regularly

❌ **Don't:**
- Commit `.env` file to GitHub
- Hardcode API keys in source files
- Share `.env` files
- Use same key everywhere

---

## Troubleshooting

### Error: "OPENROUTER_API_KEY not found in .env file!"
- Create `.env` file (copy `.env.example`)
- Add your API key
- Restart the app

### Works locally but not on Render
- Verify environment variable in Render dashboard
- Check variable name is exactly: `OPENROUTER_API_KEY`
- Redeploy or restart the service

### How to get OpenRouter API Key
1. Go to https://openrouter.ai
2. Sign up
3. Go to Settings → Keys
4. Create new API key
5. Copy and paste into `.env` or Render dashboard

---

## File Structure

```
AI-Agent/
├── .env                 ← Local API key (NOT in Git) ⚠️
├── .env.example         ← Template (shows format)
├── .gitignore           ← Excludes .env
├── server.py            ← Uses os.getenv()
├── agent.py             ← Uses os.getenv()
└── requirements.txt     ← Includes python-dotenv
```

---

## Verify Setup

### Test Locally
```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('OPENROUTER_API_KEY'))"
```

Should print your API key if setup correctly.

### Test on Render
- Check logs in Render dashboard
- Should show: "✅ Business context loaded!"
- Should NOT show: "❌ OPENROUTER_API_KEY not found"

---

**Your API key is now secure!** 🔒
