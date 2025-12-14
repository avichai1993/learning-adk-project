import os


def env_str(name: str, default: str) -> str:
    value = os.getenv(name)
    return value if value is not None and value != "" else default


DEFAULT_MODEL = "openai.gpt-5-chat"

MAIN_MODEL = env_str("TRAVEL_MAIN_MODEL", DEFAULT_MODEL)
FLIGHT_MODEL = env_str("TRAVEL_FLIGHT_MODEL", DEFAULT_MODEL)
HOTEL_MODEL = env_str("TRAVEL_HOTEL_MODEL", DEFAULT_MODEL)
ITINERARY_MODEL = env_str("TRAVEL_ITINERARY_MODEL", DEFAULT_MODEL)

LITELLM_PROXY_BASE_URL = env_str("LITELLM_PROXY_BASE_URL", "")
LITELLM_PROXY_API_KEY = env_str("LITELLM_PROXY_API_KEY", "")


def _set_openai_env_for_litellm_proxy() -> None:
    base_url = LITELLM_PROXY_BASE_URL
    if base_url.endswith("/v1/chat/completions"):
        base_url = base_url[: -len("/chat/completions")]
    if base_url.endswith("/v1/chat/completions/"):
        base_url = base_url[: -len("/chat/completions/")]

    if base_url:
        os.environ["OPENAI_API_BASE"] = base_url
    if LITELLM_PROXY_API_KEY:
        os.environ["OPENAI_API_KEY"] = LITELLM_PROXY_API_KEY


_set_openai_env_for_litellm_proxy()

FLIGHT_AGENT_PORT = int(env_str("TRAVEL_FLIGHT_AGENT_PORT", "8011"))
HOTEL_AGENT_PORT = int(env_str("TRAVEL_HOTEL_AGENT_PORT", "8012"))
ITINERARY_AGENT_PORT = int(env_str("TRAVEL_ITINERARY_AGENT_PORT", "8013"))

FLIGHT_AGENT_NAME = env_str("TRAVEL_FLIGHT_AGENT_NAME", "flight_agent")
HOTEL_AGENT_NAME = env_str("TRAVEL_HOTEL_AGENT_NAME", "hotel_agent")
ITINERARY_AGENT_NAME = env_str("TRAVEL_ITINERARY_AGENT_NAME", "itinerary_agent")

HOST = env_str("TRAVEL_AGENT_HOST", "localhost")
