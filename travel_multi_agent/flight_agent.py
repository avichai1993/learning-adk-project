from __future__ import annotations

from google.adk.agents.llm_agent import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.lite_llm import LiteLlm

from .shared import settings


# def search_cheapest_flights(
#     origin: str,
#     destination: str,
#     start_date: str,
#     end_date: str,
#     passengers: int = 1,
# ) -> dict:
#     return {
#         "status": "success",
#         "origin": origin,
#         "destination": destination,
#         "start_date": start_date,
#         "end_date": end_date,
#         "passengers": passengers,
#         "results": [
#             {
#                 "airline": "MockAir",
#                 "price_usd": 199,
#                 "stops": 1,
#                 "depart": f"{start_date} 07:10",
#                 "arrive": f"{start_date} 12:35",
#                 "notes": "Budget option, basic economy.",
#             },
#             {
#                 "airline": "MockAir Direct",
#                 "price_usd": 249,
#                 "stops": 0,
#                 "depart": f"{start_date} 09:05",
#                 "arrive": f"{start_date} 11:25",
#                 "notes": "Slightly pricier, direct.",
#             },
#         ],
#     }


root_agent = Agent(
    name=settings.FLIGHT_AGENT_NAME,
    model=LiteLlm(model=settings.FLIGHT_MODEL, custom_llm_provider="openai"),
    description="Handles flight search logic and provides cheapest flight suggestions.",
    instruction=(
        "You are the Flight Agent. Your job is to propose the cheapest reasonable flight options. "
        "If required inputs are missing (origin, destination, dates, passengers), ask concise follow-up questions. "
        # "Use the tool search_cheapest_flights to fetch candidate options, then summarize them in a user-friendly way."
    ),
    # tools=[search_cheapest_flights],
)


a2a_app = to_a2a(root_agent, port=settings.FLIGHT_AGENT_PORT)
