import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from config import (
    OMNIROUTE_API_KEY,
    OMNIROUTE_BASE_URL,
    OMNIROUTE_MODEL
)

load_dotenv()


class AIProvider:

    TASK_PROVIDER_MAP = {
        "summary": "omniroute",
        "quiz": "omniroute",
        "question_answering": "omniroute",
        "reflection": "omniroute",
    }

    def __init__(self):

        self.omniroute_api_key = OMNIROUTE_API_KEY
        self.omniroute_base_url = OMNIROUTE_BASE_URL
        self.omniroute_model = OMNIROUTE_MODEL

    def _omniroute(self):

        if not self.omniroute_api_key:
            raise ValueError("OmniRoute API key not found.")
        if not self.omniroute_base_url:
            raise ValueError("OmniRoute base URL not found.")
        if not self.omniroute_model:
            raise ValueError("OmniRoute model not found.")

        return ChatOpenAI(
            api_key=self.omniroute_api_key,
            base_url=self.omniroute_base_url,
            model=self.omniroute_model,
            temperature=0.3,
        )

    def get_llm(self, provider="auto", task=None):
        """Return an LLM, using task routing only for provider='auto'."""

        provider = provider.lower()

        if provider in ("groq", "openrouter", "auto", "omniroute"):
            return self._omniroute()

        raise ValueError(
            "Provider must be: auto, groq, openrouter or omniroute."
        )

    def _try_provider(self, provider):
        """Try one provider for automatic routing and return None on failure."""
        if provider in ("groq", "openrouter", "omniroute", "auto") and self.omniroute_api_key:
            try:
                return self._omniroute()
            except Exception as e:
                print(f"OmniRoute failed: {e}")

        return None

    def available_providers(self):

        providers = []

        if self.omniroute_api_key:
            providers.append("OmniRoute")

        return providers

    def health_check(self):
        """Minimal provider health check."""
        try:
            llm = self._omniroute()
            llm.invoke("Test")
            return True
        except Exception as e:
            print(f"Health check failed: {e}")
            return False
