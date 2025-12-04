from models.usuario import Usuario


class LoginController:
    @staticmethod
    def login(correo, password):
        usuario = Usuario.autenticar(correo, password)

        if usuario is None:
            return None

        return usuario
