# Free Hosting Options for Telegram Monitor

## 1. Render.com (Recommended) - FREE
**Pros:** Simple, reliable, good free tier
**Free tier:** 750 hours/month

### Setup:
1. Create account at render.com
2. Connect your GitHub repository
3. Create new "Web Service"
4. Use these settings:
   - Build Command: `pip install telethon`
   - Start Command: `python main.py`
5. Add environment variables:
   - `TELEGRAM_API_ID`: Your API ID
   - `TELEGRAM_API_HASH`: Your API hash
   - `TELEGRAM_PHONE`: Your phone number
   - `TARGET_CHANNEL`: Sport_433et
   - `COMMENT_MESSAGES`: hey this is me

## 2. Railway.app - FREE
**Pros:** Easy deployment, good performance
**Free tier:** $5 credit monthly

### Setup:
1. Sign up at railway.app
2. Create new project from GitHub
3. Add environment variables in dashboard
4. Deploy automatically

## 3. Heroku - FREE (with limitations)
**Pros:** Popular, well-documented
**Free tier:** Limited hours

### Setup:
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set environment variables:
   ```bash
   heroku config:set TELEGRAM_API_ID=your_id
   heroku config:set TELEGRAM_API_HASH=your_hash
   heroku config:set TELEGRAM_PHONE=your_phone
   ```
4. Deploy: `git push heroku main`

## 4. PythonAnywhere - FREE
**Pros:** Python-focused, persistent storage
**Free tier:** Limited CPU seconds

### Setup:
1. Create account at pythonanywhere.com
2. Upload files via web interface
3. Create scheduled task or always-on task
4. Install telethon: `pip3.10 install --user telethon`

## 5. Koyeb - FREE
**Pros:** Modern platform, good free tier
**Free tier:** 512MB RAM, 2.5M seconds/month

### Setup:
1. Sign up at koyeb.com
2. Connect GitHub repository
3. Set build command: `pip install telethon`
4. Set run command: `python main.py`
5. Add environment variables

## IMPORTANT: Generate Session String First

Before deploying, you MUST generate a session string:

1. **Run locally:** `python generate_session.py`
2. **Enter your credentials** when prompted
3. **Copy the session string** it outputs
4. **Use this string** as `TELEGRAM_SESSION` environment variable

## Environment Variables Needed:
For all platforms, you'll need these environment variables:
- `TELEGRAM_API_ID`: Your Telegram API ID
- `TELEGRAM_API_HASH`: Your Telegram API Hash  
- `TELEGRAM_SESSION`: Your session string (from generate_session.py)
- `TARGET_CHANNEL`: Sport_433et
- `COMMENT_MESSAGES`: hey this is me

**Note:** `TELEGRAM_PHONE` is not needed when using session string

## Files to Upload:
- `main.py`
- `config.py`
- `telegram_monitor.py`
- `rate_limiter.py`
- `render.yaml` (for Render)
- `railway.json` (for Railway)
- `Procfile` (for Heroku)
- `runtime.txt` (for Heroku)

## Recommended: Render.com
Render is the easiest and most reliable for this type of application:
1. Push code to GitHub
2. Connect GitHub to Render
3. Add environment variables
4. Deploy!

The monitor will run 24/7 and automatically comment on new posts.