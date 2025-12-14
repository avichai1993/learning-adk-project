from __future__ import annotations

from google.adk.agents.llm_agent import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.lite_llm import LiteLlm

from .shared import settings


# def build_day_by_day_itinerary(
#     destination: str,
#     start_date: str,
#     end_date: str,
#     interests: str | None = None,
#     pace: str | None = None,
#     budget: str | None = None,
# ) -> dict:
#     return {
#         "status": "success",
#         "destination": destination,
#         "start_date": start_date,
#         "end_date": end_date,
#         "interests": interests,
#         "pace": pace,
#         "budget": budget,
#         "skeleton": [
#             {"day": 1, "morning": "Arrive + check-in", "afternoon": "City orientation walk", "evening": "Local dinner"},
#             {"day": 2, "morning": "Top attraction", "afternoon": "Museum / neighborhood", "evening": "Scenic viewpoint"},
#             {"day": 3, "morning": "Day trip / nature", "afternoon": "Café + shopping", "evening": "Relax"},
#         ],
#     }


root_agent = Agent(
    name=settings.ITINERARY_AGENT_NAME,
    model=LiteLlm(model=settings.ITINERARY_MODEL, custom_llm_provider="openai"),
    description="Builds a day-by-day itinerary tailored to destination, dates, and preferences.",
    instruction=(
        "You are the Itinerary Agent. Build a clear day-by-day plan for the trip. "
        "If required inputs are missing (destination, dates), ask concise follow-up questions. "
        # "Use the tool build_day_by_day_itinerary to get a rough skeleton, then expand it into a detailed itinerary. "
        "Include practical tips (transit, time allocations, reservations) and keep it realistic for the given dates."
    ),
    # tools=[build_day_by_day_itinerary],
)


a2a_app = to_a2a(root_agent, port=settings.ITINERARY_AGENT_PORT)
