from __future__ import annotations

from google.adk.agents.llm_agent import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.lite_llm import LiteLlm

from .shared import settings


# def search_cheapest_hotels(
#     destination: str,
#     check_in: str,
#     check_out: str,
#     guests: int = 1,
#     rooms: int = 1,
#     budget_per_night_usd: int | None = None,
# ) -> dict:
#     base = 85
#     if budget_per_night_usd is not None:
#         base = min(base, budget_per_night_usd)
#     return {
#         "status": "success",
#         "destination": destination,
#         "check_in": check_in,
#         "check_out": check_out,
#         "guests": guests,
#         "rooms": rooms,
#         "results": [
#             {
#                 "name": "Mock Inn Budget",
#                 "price_per_night_usd": base,
#                 "rating": 7.9,
#                 "distance_to_center_km": 2.4,
#                 "notes": "Basic rooms, good value.",
#             },
#             {
#                 "name": "Mock City Hotel",
#                 "price_per_night_usd": base + 25,
#                 "rating": 8.6,
#                 "distance_to_center_km": 0.9,
#                 "notes": "Central location, popular.",
#             },
#         ],
#     }


hotel_agent = Agent(
    name=settings.HOTEL_AGENT_NAME,
    model=LiteLlm(model=settings.HOTEL_MODEL, custom_llm_provider="openai"),
    description="Handles hotel search logic and provides cheapest hotel suggestions.",
    instruction=(
        "You are the Hotel Agent. Your job is to propose the cheapest reasonable hotel options. "
        "If required inputs are missing (destination, check-in, check-out, guests, rooms), ask concise follow-up questions. "
        "give the user a list of options and ask them to choose one. "
        "once the user choose a hotel, write a short description of the hotel. "
        # "Use the tool search_cheapest_hotels to fetch candidate options, then summarize them in a user-friendly way."
    ),
    # tools=[search_cheapest_hotels],
)


hotel_a2a_app = to_a2a(hotel_agent, port=settings.HOTEL_AGENT_PORT)
