# 🆓 Free Deployment Guide - Render

## Total Cost: $0/month forever

---

## Part 1: Deploy Backend on Render

### Step 1: Sign Up
1. Go to [render.com](https://render.com)
2. Sign up with GitHub

### Step 2: Create FastAPI Service
1. Click **New +** → **Web Service**
2. Connect your GitHub repo
3. Configure:

**Settings:**
- Name: `expense-tracker-api`
- Root Directory: `fastapi_auth`
- Runtime: `Python 3`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Instance Type: **Free**

**Environment Variables:**
```
MONGODB_URI=mongodb+srv://tammanabhaskar7_db_user:Bhaskar7@cluster1...
JWT_SECRET_KEY=84a99ddf2b64133cd732acf4b6137016c855a80dfd6d47e384765cd89ffe9e48
GEMINI_API_KEY=AIzaSyC...
MCP_SERVER_URL=https://smiling-amaranth-frog.fastmcp.app/mcp
```

4. Click **Create Web Service**
5. Wait 5-10 minutes
6. Copy URL: `https://expense-tracker-api.onrender.com`

---

## Part 2A: Deploy Frontend on Vercel (Recommended)

### Why Vercel?
- ✅ No sleep (instant load)
- ✅ Better performance
- ✅ Automatic HTTPS

**Steps:**
1. Go to [vercel.com](https://vercel.com/signup)
2. Import GitHub repo
3. Root Directory: `frontend`
4. Add env vars:
   - `VITE_GEMINI_API_KEY`: Your key
   - `VITE_API_URL`: `https://expense-tracker-api.onrender.com`
5. Deploy

---

## Part 2B: Deploy Frontend on Render (Alternative)

### If you prefer all-in-one platform:

1. Click **New +** → **Static Site**
2. Connect repo
3. Configure:
   - Name: `expense-tracker-frontend`
   - Root Directory: `frontend`
   - Build: `npm install && npm run build`
   - Publish: `dist`
4. Add env vars (same as Vercel)
5. Deploy

---

## Part 3: Update CORS

In `fastapi_auth/main.py`, update:

```python
allow_origins=[
    "http://localhost:5173",
    "https://expense-tracker-frontend.onrender.com",  # If using Render
    "https://*.vercel.app",  # If using Vercel
    "https://*.onrender.com"
],
```

Push to GitHub - Render auto-deploys.

---

## ⚠️ Important: Free Tier Notes

### Render Free Tier
- **Backend sleeps after 15min** of inactivity
- First request after sleep: ~30 second delay
- Subsequent requests: instant

### Keep Alive (Optional)
Use [cron-job.org](https://cron-job.org) to ping your API every 14 minutes:
- URL: `https://expense-tracker-api.onrender.com/health`
- Schedule: Every 14 minutes

---

## 📊 Cost Comparison

| Platform | Frontend | Backend | Sleep? | Total |
|----------|----------|---------|--------|-------|
| Vercel + Render | Free | Free | Yes (backend) | $0 |
| Render only | Free | Free | Yes (backend) | $0 |
| Vercel + Railway | Free | $5/mo | No | $5 |

**Recommendation:** Vercel (frontend) + Render (backend) = Best free option

---

## 🐛 Troubleshooting Free Tier

### "App is starting up"
- Normal on first request after sleep
- Wait 30 seconds and retry

### "Out of hours"
- Render free tier: 750 hours/month
- Running 24/7 = 720 hours (within limit)
- Multiple apps share the 750 hours

---

## 🎉 You're Done!

Frontend: Instant load (Vercel) or small delay (Render)
Backend: 30s first load, then instant
Database: Always available (MongoDB Atlas free)
MCP Server: Always available (FastMCP)

**Total monthly cost: $0**
