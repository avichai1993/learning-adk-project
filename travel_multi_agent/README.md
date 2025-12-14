# Travel Multi-Agent (ADK + A2A) using LiteLLM Proxy

This package exposes 3 specialized travel agents over A2A (each on its own port) and a main orchestrator agent that consumes them.

## Models

All agents default to `openai.gpt-5-chat` (matching the exact model ID from your LiteLLM Proxy).

Override (optional):

- `TRAVEL_MAIN_MODEL`
- `TRAVEL_FLIGHT_MODEL`
- `TRAVEL_HOTEL_MODEL`
- `TRAVEL_ITINERARY_MODEL`

## LiteLLM Proxy (required)

This project is intended to run against a LiteLLM Proxy.

Set these environment variables in the shell where you start the agents:

- Preferred:
  - `LITELLM_PROXY_BASE_URL` = your LiteLLM Proxy base URL (example: `http://localhost:4000/v1`)
  - `LITELLM_PROXY_API_KEY` = your LiteLLM Proxy key

- Also supported (OpenAI-compatible vars):
  - `OPENAI_API_BASE` = your LiteLLM Proxy base URL
  - `OPENAI_API_KEY` = your LiteLLM Proxy key

Do not set provider keys (like a real OpenAI key) on the agent processes if you want all traffic to go through the proxy.

## Run (4 processes)

Start each remote agent:

- `uvicorn travel_multi_agent.flight_agent.agent:flight_a2a_app --host localhost --port 8011`
- `uvicorn travel_multi_agent.hotel_agent.agent:hotel_a2a_app --host localhost --port 8012`
- `uvicorn travel_multi_agent.itinerary_agent.agent:itinerary_a2a_app --host localhost --port 8013`

Smoke test agent cards:

- `http://localhost:8011/.well-known/agent-card.json`
- `http://localhost:8012/.well-known/agent-card.json`
- `http://localhost:8013/.well-known/agent-card.json`

Then run the main agent UI:

- From the repo root (agents directory): `adk web .`

Select the `travel_multi_agent` app (it loads `travel_multi_agent/agent.py`, which exposes `root_agent`).
