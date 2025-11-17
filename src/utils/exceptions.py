class ExcecaoAmostraInvalida(Exception):
    def __init__(self, msg):
        super().__init__(f"[ERRO] Amostra inválida: {msg}")
