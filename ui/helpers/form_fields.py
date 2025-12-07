class FormFields:
    @staticmethod
    def estudiante_fields():
        return {
            "titulo": "Crear Nuevo Estudiante",
            "secciones": [
                {
                    "titulo": "Datos de Usuario",
                    "campos": [
                        {
                            "nombre": "correo",
                            "etiqueta": "Correo Electrónico:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "password",
                            "etiqueta": "Contraseña:",
                            "tipo": "password"
                        },
                        {
                            "nombre": "rol",
                            "etiqueta": "Rol:",
                            "tipo": "readonly",
                            "default": "estudiante"
                        }
                    ]
                },
                {
                    "titulo": "Datos del Estudiante",
                    "campos": [
                        {
                            "nombre": "nombre",
                            "etiqueta": "Nombre:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "apellido",
                            "etiqueta": "Apellido:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "edad",
                            "etiqueta": "Edad:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "genero",
                            "etiqueta": "Género:",
                            "tipo": "combobox",
                            "opciones": ["F", "M", "Otro"],
                            "default": "F"
                        }
                    ]
                }
            ]
        }

    @staticmethod
    def programa_fields():
        return {
            "titulo": "Crear Nuevo Programa",
            "secciones": [
                {
                    "titulo": "Datos del Programa",
                    "campos": [
                        {
                            "nombre": "nombre_programa",
                            "etiqueta": "Nombre del Programa:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "descripcion",
                            "etiqueta": "Descripción del programa:",
                            "tipo": "entry"
                        }
                    ]
                }
            ]
        }
