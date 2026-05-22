# AI Chatbot Agent - Render Deployment Guide

## 📋 All Requirements

### Files Created ✅
- `requirements.txt` - Python dependencies
- `Procfile` - Process file for Render
- `.gitignore` - Git ignore file
- `server.py` - Flask web server
- `agent.py` - CLI chatbot
- `aboutbusiness.json` - Business info
- `chat_history.json` - Chat storage

### Python Dependencies
```
flask==3.0.0
openai==1.3.0
watchdog==3.0.0
```

---

## 🚀 Step-by-Step Deployment on Render

### Step 1: Push Code to GitHub
```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial AI Chatbot Agent"

# Push to GitHub
git push origin main
```

### Step 2: Create Render Account
1. Go to https://render.com
2. Click "Sign up" 
3. Sign up with GitHub (recommended)

### Step 3: Deploy Web Service
1. Click **"New +"** button
2. Select **"Web Service"**
3. Connect your GitHub repository
4. Fill in the form:
   - **Name**: `ai-chatbot` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Plan**: Free

### Step 4: Set Environment Variables (if needed)
1. Go to **Environment** tab
2. Add if using environment variables:
   ```
   PORT = 5000
   ```

### Step 5: Deploy
1. Click **"Create Web Service"**
2. Wait for deployment (2-3 minutes)
3. You'll get a URL like: `https://your-app-name.onrender.com`

---

## ✅ Testing

- Open your deployed URL in browser
- Start chatting!
- Chat history saves automatically to `chat_history.json`
- Edit `aboutbusiness.json` and changes reload automatically

---

## 📝 File Structure

```
AI-Agent/
├── server.py              # Web server (Flask)
├── agent.py               # CLI chatbot
├── aboutbusiness.json     # Business info
├── chat_history.json      # Chat storage
├── requirements.txt       # Python packages
├── Procfile              # Render config
├── .gitignore            # Git ignore
└── README.md             # This file
```

---

## 🔑 Important Notes

1. **API Key**: Your OpenRouter API key is in `server.py` - keep it secret!
   - Consider moving to `.env` file in production

2. **File Watchers**: Render may have limitations with file watching
   - Chat history still saves automatically
   - Business info updates on server restart

3. **Free Tier Limits**:
   - 750 hours/month (24/7 free service)
   - Auto-spins down after 15 mins of inactivity

4. **Custom Domain** (optional):
   - Add your own domain in Render dashboard

---

## 🛠️ Troubleshooting

**Issue**: Deployment fails
- Check `requirements.txt` format
- Verify GitHub repo is public

**Issue**: Chat not saving
- Check file permissions
- Restart the service

**Issue**: Business info not updating
- Restart Render service
- Check `aboutbusiness.json` format (must be valid JSON)

---

## 📚 Additional Resources

- Render Docs: https://render.com/docs
- Flask Docs: https://flask.palletsprojects.com
- OpenAI Docs: https://platform.openai.com/docs

---

## 🎉 You're All Set!

Your AI Chatbot is now live on Render! 🚀

Visit your deployment URL and start chatting with your AI agent that knows your business!
