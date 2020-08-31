import json

from loafer.message_translators import AbstractMessageTranslator


class GoatMessagesTranslator(AbstractMessageTranslator):

    def translate(self, message):
        return {'content': json.loads(message["Body"]), 'metadata': {}}