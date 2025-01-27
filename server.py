from flask import Flask, jsonify, request
from mcp.server.fastmcp import FastMCP
import requests

# Initialize MCP server
mcp = FastMCP("MyAppMCP")

API_BASE_URL = "http://localhost:8001"  # Assuming the Flask app is running locally


@mcp.tool()
def summarize_video(video_id: str) -> dict:
    """
    Initiates video summarization by calling the /summarize endpoint.
    """
    try:
        payload = {"video_id": video_id}
        response = requests.post(f"{API_BASE_URL}/summarize", json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def get_summary(summary_id: str) -> dict:
    """
    Retrieves video summary details by calling /summarize/<summary_id>.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/summarize/{summary_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def create_chat(summary_id: str, message: str, chat_history: list = []) -> dict:
    """
    Creates a new chat session via /chat endpoint.
    """
    try:
        payload = {
            "summary_id": summary_id,
            "message": message,
            "chat_history": chat_history
        }
        response = requests.post(f"{API_BASE_URL}/chat", json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def get_chat(chat_id: str) -> dict:
    """
    Retrieves chat details from /chat/<chat_id>.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/chat/{chat_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    mcp.run(transport='stdio')
