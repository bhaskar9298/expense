# ✅ Free Render Deployment Checklist

## Step 1: Push to GitHub (5 min)
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/expense-tracker.git
git push -u origin main
```

## Step 2: Deploy Backend on Render (10 min)

1. Sign up: [render.com](https://render.com) with GitHub
2. **New +** → **Web Service**
3. Select your repo
4. Settings:
   - Name: `expense-tracker-api`
   - Root: `fastapi_auth`
   - Runtime: `Python 3`
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Free** plan
5. Environment Variables (click "Add"):
   ```
   MONGODB_URI = mongodb+srv://tammanabhaskar7_db_user:Bhaskar7@cluster1.t5ic1yp.mongodb.net/?appName=Cluster1
   JWT_SECRET_KEY = 84a99ddf2b64133cd732acf4b6137016c855a80dfd6d47e384765cd89ffe9e48
   GEMINI_API_KEY = AIzaSyCMYkeDx7kWYZUi7DvF0Y1ewUK_4K26c2w
   MCP_SERVER_URL = https://smiling-amaranth-frog.fastmcp.app/mcp
   ```
6. Click **Create Web Service**
7. Wait 5-10 min, copy URL

## Step 3: Deploy Frontend on Vercel (5 min)

1. Sign up: [vercel.com/signup](https://vercel.com/signup) with GitHub
2. **New Project** → Import your repo
3. Settings:
   - Root: `frontend`
   - Framework: Vite (auto-detected)
4. Environment Variables:
   ```
   VITE_GEMINI_API_KEY = AIzaSyCMYkeDx7kWYZUi7DvF0Y1ewUK_4K26c2w
   VITE_API_URL = https://expense-tracker-api.onrender.com
   ```
   (Use your Render URL from Step 2)
5. Click **Deploy**
6. Wait 2-3 min

## Step 4: Update CORS (2 min)

Edit `fastapi_auth/main.py`:
```python
allow_origins=[
    "http://localhost:5173",
    "https://your-app.vercel.app",  # Add your Vercel URL
    "https://*.vercel.app",
],
```

Push:
```bash
git add .
git commit -m "Update CORS"
git push
```

Render auto-deploys in 5 min.

## Step 5: Test! 🎉

Visit your Vercel URL, sign up, add expense.

**Note:** First request to backend takes 30s (free tier sleep). Then instant.

---

## 💰 Monthly Cost: $0
