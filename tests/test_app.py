import pytest
from src.qafalda.app import QAfalda


class TestQAfalda:
    def setup_method(self):
        self.bot = QAfalda()

    def test_greeting(self):
        response = self.bot.respond("oi")
        assert "QA!" in response

    def test_goodbye(self):
        response = self.bot.respond("tchau")
        assert "QA!" in response

    def test_topic_list(self):
        response = self.bot.respond("temas")
        assert "Fundamentos" in response

    def test_knowledge_response(self):
        response = self.bot.respond("teste de software")
        assert "QA:" in response

    def test_fallback(self):
        response = self.bot.respond("Pergunta aleatória sem sentido")
        assert "QA" in response or "teste" in response