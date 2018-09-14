from chatterbot import ChatBot


class Brain:
    def __init__(self, chatbot_name):
        self.chatbot = ChatBot(
            chatbot_name,
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )
        # Train based on the english corpus
        self.chatbot.train("chatterbot.corpus.english")

    def custom_train(self, data):
        """
            train your bot with custom data
            :prams data: list of messages and responses
            data = [
                "Hello",
                "Hi there!",
                "How are you doing?",
                "I'm doing great.",
                "That is good to hear",
                "Thank you.",
                "Your welcome."
            ]
        """
        self.chatbot.train(data)

    def get_reponse(self, meesage):
        # Get a response to an input statement
        response = self.chatbot.get_response(meesage)
        return response
