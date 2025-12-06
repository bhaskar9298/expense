"""
Test script for LangGraph integration
Run: python test_langgraph_integration.py
"""
import asyncio
import sys
from pathlib import Path

# Add client to path
sys.path.append(str(Path(__file__).parent / 'client'))
from langgraph_service import process_tool_call

async def test_integration():
    print("Testing LangGraph MCP Integration...\n")
    
    # Test 1: List expenses
    print("Test 1: List expenses")
    try:
        result = await process_tool_call(
            "list_expenses",
            {
                "start_date": "2025-12-01",
                "end_date": "2025-12-31"
            },
            "69340c8c3a58dfab5e887dd2"
        )
        print(f"✓ Success: {result}\n")
    except Exception as e:
        print(f"✗ Failed: {e}\n")
    
    # Test 2: Summarize
    print("Test 2: Summarize expenses")
    try:
        result = await process_tool_call(
            "summarize",
            {
                "start_date": "2025-12-01",
                "end_date": "2025-12-31"
            },
            "69340c8c3a58dfab5e887dd2"
        )
        print(f"✓ Success: {result}\n")
    except Exception as e:
        print(f"✗ Failed: {e}\n")
    
    # Test 3: Add expense
    print("Test 3: Add expense")
    try:
        result = await process_tool_call(
            "add_expense",
            {
                "date": "2025-12-06",
                "amount": 15.0,
                "category": "Food",
                "note": "Test lunch"
            },
            "69340c8c3a58dfab5e887dd2"
        )
        print(f"✓ Success: {result}\n")
    except Exception as e:
        print(f"✗ Failed: {e}\n")

if __name__ == '__main__':
    asyncio.run(test_integration())
