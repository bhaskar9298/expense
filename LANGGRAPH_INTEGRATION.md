# LangGraph Integration Setup Guide

## Overview
The expense tracker now uses `client1.py` logic (LangGraph + MCP) instead of direct Gemini.js parsing.

**New Flow:**
Frontend (Gemini.js parses NL) → FastAPI → LangGraph Service → MCP Server → MongoDB

## Changes Made

### 1. Created `client/langgraph_service.py`
- Implements LangGraph workflow with MCP adapter
- Maintains compatibility with existing frontend (still accepts tool + args)
- Adds user_id injection automatically

### 2. Updated `fastapi_auth/main.py`
- Imports `langgraph_service.py`
- `/mcp/execute` now uses LangGraph instead of direct HTTP calls
- Maintains same API contract (no frontend changes needed)

### 3. Frontend remains unchanged
- `gemini.js` still parses natural language
- Dashboard.jsx works as before
- No breaking changes to UI/UX

## Setup Steps

### 1. Ensure dependencies are installed
```bash
# In project root
uv sync
```

### 2. Verify .env configuration
```env
# Required variables
GEMINI_API_KEY=your_gemini_key
MONGODB_URI=your_mongo_uri
JWT_SECRET_KEY=your_secret
MCP_SERVER_URL=https://optimistic-brown-antelope.fastmcp.app/mcp
```

### 3. Test the integration
```bash
# Run test script
python test_langgraph_integration.py
```

Expected output:
```
Test 1: List expenses
✓ Success: [...]

Test 2: Summarize expenses  
✓ Success: [...]

Test 3: Add expense
✓ Success: {"status": "success", ...}
```

### 4. Start the services

**Terminal 1 - FastAPI (Port 8001):**
```bash
cd fastapi_auth
uvicorn main:app --reload --port 8001
```

**Terminal 2 - Frontend (Port 5173):**
```bash
cd frontend
npm run dev
```

### 5. Test in browser
1. Navigate to http://localhost:5173
2. Login/Signup
3. Try commands:
   - "Add coffee expense of $5 today"
   - "Show my expenses this month"
   - "Summarize my spending"

## Architecture

```
User Input
    ↓
Gemini.js (NL → tool + args)
    ↓
Dashboard.jsx (sends to API)
    ↓
FastAPI /mcp/execute
    ↓
LangGraph Service
    ├─ Initializes MCP Client
    ├─ Builds tool graph
    ├─ Injects user_id
    └─ Executes tool via MCP
    ↓
MCP Server (FastMCP)
    ↓
MongoDB
```

## Key Benefits

1. **Agentic behavior**: LangGraph can chain multiple tool calls
2. **Better error handling**: Tools validated before execution  
3. **Extensibility**: Easy to add new tools/workflows
4. **Maintained compatibility**: No frontend changes needed

## Troubleshooting

### Error: "Module not found: langgraph_service"
```bash
# Verify client directory in PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/client"
```

### Error: "MCP connection failed"
- Check MCP_SERVER_URL in .env
- Verify server is accessible: `curl https://optimistic-brown-antelope.fastmcp.app/mcp`

### Error: "Tool not found"
- Restart FastAPI to reinitialize MCP client
- Check MCP server logs

## Next Steps

To fully utilize LangGraph capabilities:

1. **Remove Gemini.js** (optional): Frontend can send raw text, let LangGraph parse
2. **Add multi-step workflows**: Chain tools (e.g., "add expense then show summary")
3. **Add memory**: Store conversation context for follow-up questions
4. **Custom agents**: Create specialized agents for budgeting, analytics, etc.

## Rollback (if needed)

If issues occur, revert FastAPI changes:
```bash
git checkout fastapi_auth/main.py
```

Frontend will continue working with old direct MCP calls.
