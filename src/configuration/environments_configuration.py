import os
from io import StringIO
from dotenv import dotenv_values, load_dotenv


class Environments():
    """
        Classe responável por retornar e criar variáveis de ambientes
        escenciais para o funcionamento do sistema.
    """
    def __init__(self, env_value, env_key):
        self.environment = dotenv_values(".env")
        self.env_value = env_value
        self.env_key = env_key

    def insert_new_environment_value(self):
        """
            Método responsável por gerar novas variáveis de ambiente para o
            sistema.
            É necessário passar os valores da chave e conteúdo da variável na
            classe Environment() [self.env_value, self.env_key]
        """
        config = StringIO(f"{self.env_key}={self.env_value}")

        load_dotenv(stream=config)

        return os.getenv(self.env_key)

    def return_environment_value(self, env_value):
        """"""
        load_dotenv()

        return os.getenv(env_value)
