from typing import Text, List, Dict, Any

from rasa.shared.core.constants import ACTION_DEFAULT_FALLBACK_NAME
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class UtterBotChallenges(Action):
    def name(self) -> Text:
        return "utter_bot_challenges"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Implement the logic for the bot's response
        response = "I can help you with information about various challenges. Please ask me a specific question."
        dispatcher.utter_message(text=response)

        return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return ACTION_DEFAULT_FALLBACK_NAME

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="my_custom_fallback_template")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]

