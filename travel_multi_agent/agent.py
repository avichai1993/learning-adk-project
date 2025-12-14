from __future__ import annotations

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.models.lite_llm import LiteLlm

from .shared import settings


def add_trip_to_calendar(
    title: str,
    start_date: str,
    end_date: str,
    reminder_days_before: int = 7,
) -> dict:
    return {
        "status": "success",
        "event": {
            "title": title,
            "start_date": start_date,
            "end_date": end_date,
            "reminder_days_before": reminder_days_before,
        },
        "message": "Mock calendar event created. In a real integration, this would call Google Calendar API.",
    }


flight_agent = RemoteA2aAgent(
    name=settings.FLIGHT_AGENT_NAME,
    description="Remote agent that suggests cheapest flights.",
    agent_card=(
        f"http://{settings.HOST}:{settings.FLIGHT_AGENT_PORT}{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

hotel_agent = RemoteA2aAgent(
    name=settings.HOTEL_AGENT_NAME,
    description="Remote agent that suggests cheapest hotels.",
    agent_card=(
        f"http://{settings.HOST}:{settings.HOTEL_AGENT_PORT}{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

itinerary_agent = RemoteA2aAgent(
    name=settings.ITINERARY_AGENT_NAME,
    description="Remote agent that builds day-by-day itineraries.",
    agent_card=(
        f"http://{settings.HOST}:{settings.ITINERARY_AGENT_PORT}{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)


root_agent = Agent(
    name="main_travel_agent",
    model=LiteLlm(model=settings.MAIN_MODEL, custom_llm_provider="openai"),
    description="Orchestrates travel planning by delegating to specialized remote agents.",
    instruction=(
        "You are the Main Travel Agent (orchestrator). You coordinate trip planning based on user-provided dates and destination.\n\n"
        "You must first ensure you have: destination, start date, end date. If the user wants flights, also collect origin airport/city and number of passengers.\n\n"
        "Ask the user what they want help with (any subset is allowed):\n"
        "1) Cheapest flight suggestions\n"
        "2) Cheapest hotel suggestions\n"
        "3) Day-by-day itinerary\n\n"
        "Routing rules:\n"
        "- For flights: delegate to flight_agent.\n"
        "- For hotels: delegate to hotel_agent.\n"
        "- For itinerary: delegate to itinerary_agent.\n\n"
        "After presenting results, ask the user if they want to add the trip to their calendar. If yes, use add_trip_to_calendar.\n\n"
        "When combining results from multiple agents, present them in sections with clear headings."
    ),
    sub_agents=[flight_agent, hotel_agent, itinerary_agent],
    tools=[add_trip_to_calendar],
)
