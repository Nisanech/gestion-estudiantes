# 🎓 Registro de Estudiantes

Aplicación de escritorio desarrollada en **Python** para la gestión de estudiantes y programas académicos. Esta aplicación permite registrar estudiantes, asignar programas y realizar consultas a través de una interfaz gráfica (GUI) desarrollada con **Tkinter**.

![Aplicación](/img/app.png)

## Tabla de Contenido

* [Características](#características)
* [Tecnologías](#tecnologías)
* [Requisitos Previos](#requisitos-previos)
* [Instalación](#instalación)
* [Configuración de Base de Datos](#configuración-de-base-de-datos)
* [Uso](#uso)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Funcionalidades](#funcionalidades)
* [Desarrollado Por](#desarrollado-por)

## Características

- Registro de nuevos estudiantes.
- Asignación múltiple de programas académicos a estudiantes.
- Selección de estudiantes existentes.
- Visualización de datos en tabla principal (`TreeView`).
- Filtro por edad (mayores de 18 años). 
- Filtro por programa académico. 
- Interfaz gráfica (GUI) con `Tkinter`.

## Tecnologías

| Tecnología             | Versión            | Uso                |
|------------------------|--------------------|--------------------|
| Python                 | 3.12               | Lenguaje principal |
| MySQL                  | 8.0+               | Base de datos      |
| Tkinter                | Incluido en Python | Interfaz gráfica   |
| mysql-connector-python | 9.1.0+             | Conector MySQL     |

## Requisitos Previos

Antes de iniciar el proyecto, asegúrate de tener instalado:

- [Python 3.12](https://www.python.org/downloads/)
- [MySQL Server 8.0+](https://dev.mysql.com/downloads/installer/) o [Xampp](https://www.apachefriends.org/es/index.html)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Nisanech/gestion-estudiantes.git
    ```

    ```bash
    cd gestion-estudiantes
    ```

2. Crear entorno virtual

    ```bash
    python -m venv venv
    ```
   
3. Activar entorno virtual

    ```bash
    venv\Scripts\activate
    ```
   
4. Instalar dependencias

    ```bash
   pip install mysql-connector-python
    ```
   
## Configuración de Base de Datos

1. Ejecuta el archivo `bd/db.sql` para crear la base de datos y las tablas necesarias.

    ![Diagrama Entidad Relacion](/img/diagrama-entidad-relacion.png)

2. Edita el archivo `database/conexion.py` y agrega las credenciales según tu configuración:

    ```python
    def __init__(self):
      self.host = 'localhost'      # Cambiar si es necesario
      self.user = 'root'           # Tu usuario de MySQL
      self.password = 'root'       # Tu contraseña de MySQL
      self.database = 'estudiantes_andap'
      self.connection = None
      self._initialized = True
    ```
   
## Uso

Ejecutar la aplicación.

```bash
python main.py
```

### Interfaz principal

La aplicación se divide en tres secciones:

1. Formulario de Registro

    - Tipo "Nuevo": Registra un nuevo estudiante ingresando nombre y edad 
    - Tipo "Existente": Selecciona un estudiante ya registrado 
    - Selecciona un programa académico para asignar 
    - Presiona "Guardar" para registrar

2. Tabla de Estudiantes

    - Visualiza todos los estudiantes registrados
    - Muestra: ID, Nombre, Edad y Programas asignados
    - Actualización automática después de cada operación

3. Panel de Filtros

    - "Mayores de 18": Muestra solo estudiantes con edad > 18
    - "Filtrar por programa": Muestra estudiantes de un programa específico
    - "Todos": Restaura la vista completa

## Estructura del Proyecto

```text
    gestion-estudiantes/
    │
    ├── main.py                          # Punto de entrada de la aplicación
    │
    ├── database/
    │   └── conexion.py                  # Gestión de conexión MySQL
    │
    ├── models/
    │   ├── estudiante.py                # Modelo y operaciones de Estudiante
    │   ├── programa.py                  # Modelo y operaciones de Programa
    │   └── estudiante_programa.py      # Gestión de relación M:N
    │
    ├── ui/
    │   └── interfaz.py                  # Interfaz gráfica (Tkinter)
    │   
    ├── README.md                        # Este archivo
```

## Funcionalidades

### Gestión de Estudiantes

| Funcionalidad  | Descripción                      | Método                           |
|----------------|----------------------------------|----------------------------------|
| Crear          | Registra un nuevo estudiante     | `Estudiante.crear()`             |
| Listar todos   | Obtiene todos los estudiantes    | `Estudiante.listar()`            |
| Listar mayores | Filtra estudiantes > 18 años     | `Estudiante.listar_mayores_18()` |
| Buscar por ID  | Obtiene un estudiante específico | `Estudiante.listar_por_id(id)`   |

### Gestión de Programas

| Funcionalidad | Descripción                 | Método              |
|---------------|-----------------------------|---------------------|
| Listar        | Obtiene todos los programas | `Programa.listar()` |

### Relación Estudiante-Programa

| Funcionalidad        | Descripción                      | Método                                                 |
|----------------------|----------------------------------|--------------------------------------------------------|
| Asignar              | Inscribe estudiante en programa  | `EstudiantePrograma.asignar()`                         |
| Obtener programas    | Lista programas de un estudiante | `EstudiantePrograma.obtener_programas_de_estudiante()` |
| Filtrar por programa | Lista estudiantes de un programa | `EstudiantePrograma.filtrar_por_programa()`            |

## Desarrollado Por

- Nicolas Santiago Naranjo
- Jose Alexander Ferreira

**Inteligencia artificial - Explorador G148P**