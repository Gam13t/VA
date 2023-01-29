from dotenv import load_dotenv


class TestConfig:
    def test_load_dotenv_method(self):
        status = load_dotenv()
        assert status == True
