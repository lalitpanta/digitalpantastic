# 🤖 AI Chatbot Agent

An intelligent chatbot that learns your business info and responds accordingly. Features automatic chat history saving and real-time business context updates.

## ✨ Features

- 💬 Smart conversational AI
- 📱 Beautiful web interface
- 💾 Auto-saves chat history to JSON
- 🔄 Real-time business context updates
- 🚀 Easy deployment to Render
- ⚡ File watching for instant updates

## 📦 All Files Included

```
✅ server.py              - Flask web server
✅ agent.py               - CLI chatbot
✅ aboutbusiness.json     - Business info
✅ chat_history.json      - Chat storage
✅ requirements.txt       - Dependencies
✅ Procfile              - Render config
✅ .gitignore            - Git config
✅ RENDER_DEPLOYMENT.md  - Deployment guide
```

## 🚀 Quick Start

### Local (No hosting needed)

**Web UI:**
```bash
pip install -r requirements.txt
python server.py
# Open http://localhost:5000
```

**CLI:**
```bash
python agent.py
```

### Cloud (Render - Free)

See **RENDER_DEPLOYMENT.md** for full instructions

## 🎯 What's Included

| File | Purpose |
|------|---------|
| `server.py` | Web chatbot interface (Flask) |
| `agent.py` | Terminal chatbot |
| `aboutbusiness.json` | Your business details |
| `chat_history.json` | Saved conversations |
| `requirements.txt` | Python packages needed |
| `Procfile` | Render deployment config |
| `.gitignore` | Git ignore patterns |

## 📝 Usage

1. Edit `aboutbusiness.json` with your business details
2. Run `python server.py` (web) or `python agent.py` (CLI)
3. Chat with the AI - it knows your business!
4. All conversations auto-save to `chat_history.json`

## 🔄 Auto-Updates

Edit `aboutbusiness.json` and the chatbot automatically:
- Detects changes
- Reloads business context
- Applies to next message
- No restart needed!

## 📋 Requirements

- Python 3.7+
- pip package manager
- OpenRouter API key (free to get)

## 🌐 Deployment

**Free Hosting Options:**
1. **Render** (Recommended) - See RENDER_DEPLOYMENT.md
2. Railway
3. Replit
4. PythonAnywhere
5. Vercel (Serverless)

## 🔑 API Key

Uses OpenRouter API (Claude 3 Haiku). Get free credits at https://openrouter.ai

## 📖 Business Info Format

```json
{
  "business_name": "Your Business",
  "ceo": "CEO Name",
  "industry": "Your Industry",
  "description": "What you do",
  "services": ["Service 1", "Service 2"],
  "mission": "Your mission",
  "target_audience": "Who you serve",
  "contact": "email@example.com",
  "additional_info": "Extra details"
}
```

## 🎨 Web UI Features

- 💬 Real-time chat
- 📱 Mobile responsive
- ✨ Typing indicators
- 🎯 Message history
- 🗑️ Clear chat button
- 🎨 Beautiful gradient design

## ⚙️ Configuration

### Change Model
Edit `server.py` or `agent.py`:
```python
model="anthropic/claude-3-haiku"  # Change to other models
```

### Change Port (Local)
```python
app.run(port=8000)  # Change from 5000
```

### Response Length
Edit business context in `server.py`/`agent.py` to adjust response style

## 🐛 Troubleshooting

**Chatbot doesn't know my business?**
- Edit `aboutbusiness.json`
- Save the file
- Restart the application

**Chat history not saving?**
- Check file permissions
- Ensure `chat_history.json` exists

**Port 5000 already in use?**
- Change port in `server.py`
- Or kill the process using it

## 🤝 Support

- Check file formats (valid JSON)
- Review API key limits
- Check internet connection
- Verify Python 3.7+

## 📄 License

Free to use and modify!

---

**Ready to deploy?** → See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

**Questions?** Check the guides or edit the files directly!

🚀 **Happy Chatting!**
