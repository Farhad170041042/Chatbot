# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from datetime import date
import datetime
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionSearchInformation(Action):

     def name(self) -> Text:
         return "action_search_information"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'days':
                 now = datetime.datetime.now()
                 message = now.strftime("%A")
             if e['entity'] == 'news':
                 message = "https://www.bbc.com/news/world"
             if e['entity'] == 'month':
                 tod = date.today()
                 message = tod.strftime("%B %d, %Y")

         dispatcher.utter_message(text="It is " + message)

         return []


class ActionSearchMood(Action):

    def name(self) -> Text:
        return "action_search_mood"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'sarcasm':
                message = " Here is something you need to hear - Two guys stole a calendar. They got six months each."
            if e['entity'] == 'happy':
                message = "You are always happy"
            if e['entity'] == 'sad':
                message = "Don't be sad"
            if e['entity'] == 'great':
                message = "Awesome, carry on!"
        dispatcher.utter_message(text= message)

        return []