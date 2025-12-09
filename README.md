# 🎓 Sistema de Gestión de Estudiantes y Test Vocacional

Aplicación de escritorio desarrollada en **Python** con **Tkinter** para la gestión integral de estudiantes, programas académicos y orientación vocacional mediante inteligencia artificial. El sistema incluye un test vocacional basado en lógica difusa que recomienda programas académicos según las respuestas del estudiante.

![Aplicación](/img/inicio-sesion.png)
![Aplicación](/img/admin-panel-est.png)
![Aplicación](/img/admin-panel-prog.png)
![Aplicación](/img/est-panel-test.png)
![Aplicación](/img/est-panel-result.png)

## Tabla de Contenido

* [Características Principales](#-características-principales)
* [Tecnologías](#-tecnologías)
* [Requisitos Previos](#-requisitos-previos)
* [Instalación](#-instalación)
* [Configuración de Base de Datos](#-configuración-de-base-de-datos)
* [Uso](#-uso)
* [Estructura del Proyecto](#-estructura-del-proyecto)
* [Arquitectura](#-arquitectura)
* [Funcionalidades Detalladas](#-funcionalidades-detalladas)
* [Sistema de Recomendaciones IA](#-sistema-de-recomendaciones-ia)
* [Desarrollado Por](#-desarrollado-por)

## Características Principales

### Sistema de Autenticación
- Login con roles diferenciados (Admin/Estudiante).
- Redirección automática según rol del usuario.

### Panel de Administración
- Gestión completa de estudiantes.
- Gestión de programas académicos.
- Visualización de datos en tablas.

### Panel de Estudiante
- Test vocacional con 50 preguntas categorizadas.
- Visualización de resultados con recomendaciones personalizadas.
- Sistema de puntuación basado en lógica difusa.
- Carga dinámica de resultados.
- Ranking de programas por afinidad.

### Test Vocacional
- 10 categorías de evaluación vocacional.
- 50 preguntas con escala Likert (5 opciones).
- Valores difusos (0.0 - 1.0) para análisis preciso.
- Cálculo de afinidad por categoría.
- Recomendaciones automáticas de programas.

## Tecnologías

| Tecnología             | Versión            | Uso                       |
|------------------------|--------------------|---------------------------|
| Python                 | 3.12               | Lenguaje principal        |
| MySQL                  | 8.0+               | Base de datos relacional  |
| Tkinter                | Incluido en Python | Interfaz gráfica (GUI)    |
| mysql-connector-python | 9.5.0              | Conector MySQL            |
| NumPy                  | 2.3.5              | Cálculos de lógica difusa |

## Requisitos Previos

Antes de iniciar el proyecto, asegúrate de tener instalado:

- [Python 3.12](https://www.python.org/downloads/)
- [MySQL Server 8.0+](https://dev.mysql.com/downloads/installer/) o [XAMPP](https://www.apachefriends.org/es/index.html)

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Nisanech/gestion-estudiantes.git
    cd gestion-estudiantes
    ```

2. **Crear entorno virtual:**

    ```bash
    python -m venv venv
    ```
   
3. **Activar entorno virtual:**

    **Windows:**
    ```bash
    venv\Scripts\activate
    ```
    
    **Linux/Mac:**
    ```bash
    source venv/bin/activate
    ```
   
4. **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuración de Base de Datos

1. **Ejecutar el script SQL:**
   
   Ejecuta el archivo `bd/bd.sql` en tu servidor MySQL para crear la base de datos y todas las tablas necesarias.

   ![Diagrama Entidad Relación](/img/Diagrama-entidad-relacion.png)

2. **Configurar credenciales:**
   
   Edita el archivo `bd/conexion.py` con tus credenciales de MySQL:

   ```python
   def __init__(self):
       self.host = 'localhost'      # Cambiar si es necesario
       self.user = 'root'           # Tu usuario de MySQL
       self.password = 'root'       # Tu contraseña de MySQL
       self.database = 'estudiantes_andap'
       self.connection = None
       self._initialized = True
   ```

3. **Usuarios por defecto:**

   | Correo                    | Contraseña | Rol        |
   |---------------------------|------------|------------|
   | admin@correo.com          | admin123   | admin      |
   | estudiante1@correo.com    | est123     | estudiante |

## Uso

### Ejecutar la aplicación

```bash
python main.py
```

### Flujo de Usuario - Administrador

1. **Login** con credenciales de administrador
2. **Gestión de Estudiantes:**
   - Crear nuevos estudiantes con datos personales
   - Asignar credenciales de acceso
   - Visualizar lista completa de estudiantes
3. **Gestión de Programas:**
   - Crear programas académicos
   - Visualizar lista de programas

### Flujo de Usuario - Estudiante

1. **Login** con credenciales de estudiante
2. **Visualizar datos personales** en el dashboard
3. **Realizar Test Vocacional:**
   - Responder 50 preguntas categorizadas
   - Usar escala de 5 puntos (Totalmente en desacuerdo → Totalmente de acuerdo)
   - Enviar respuestas para procesamiento
4. **Ver Resultados:**
   - Programa recomendado con mayor afinidad
   - Ranking completo de programas con porcentajes
   - Actualización dinámica al hacer clic en la pestaña

## 📁 Estructura del Proyecto

```text
gestion-estudiantes/
│
├── main.py                              # Punto de entrada de la aplicación
│
├── bd/
│   ├── bd.sql                          # Script de creación de BD y datos
│   ├── conexion.py                     # Gestión de conexión MySQL
│   └── gestion-estudiantes-entidad-relacion.mwb  # Modelo ER
│
├── controllers/                         # Lógica de negocio
│   ├── estudiante_controller.py        # Controlador de estudiantes
│   ├── programa_controller.py          # Controlador de programas
│   ├── usuario_controller.py           # Controlador de usuarios
│   ├── login_controller.py             # Controlador de autenticación
│   ├── test_vocacional_controller.py   # Controlador del test
│   └── ia_controller.py                # Controlador de IA y recomendaciones
│
├── models/                              # Modelos de datos (ORM manual)
│   ├── estudiante.py                   # Modelo Estudiante
│   ├── programa.py                     # Modelo Programa
│   ├── usuario.py                      # Modelo Usuario
│   ├── estudiante_programa.py          # Relación M:N
│   ├── test_vocacional.py              # Modelo Test
│   ├── respuesta_estudiante.py         # Modelo Respuestas
│   └── ia.py                           # Modelo IA (afinidades y recomendaciones)
│
├── ui/                                  # Interfaz gráfica
│   ├── components/                     # Componentes reutilizables
│   │   ├── styles.py                   # Estilos globales
│   │   ├── form_builder.py            # Constructor de formularios
│   │   ├── table_builder.py           # Constructor de tablas
│   │   └── header_builder.py          # Constructor de encabezados
│   │
│   ├── helpers/                        # Utilidades UI
│   │   ├── ui_helpers.py              # Helpers generales
│   │   └── form_fields.py             # Definiciones de campos
│   │
│   └── views/                          # Vistas principales
│       ├── login_view.py              # Vista de login
│       ├── admin_view.py              # Panel administrador
│       └── estudiante_view.py         # Panel estudiante
│
├── requirements.txt                     # Dependencias del proyecto
└── README.md                           # Este archivo
```

## Arquitectura

El proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)**.

### Modelos (Models)
- Representan las entidades de la base de datos
- Contienen métodos para operaciones CRUD
- Gestionan la lógica de acceso a datos

### Vistas (Views)
- Interfaces gráficas construidas con Tkinter
- Componentes reutilizables para consistencia visual

### Controladores (Controllers)
- Intermediarios entre modelos y vistas
- Contienen la lógica de negocio
- Validan datos antes de persistirlos

## Funcionalidades Detalladas

### Gestión de Estudiantes

| Funcionalidad      | Descripción                                    | Método                                            |
|--------------------|------------------------------------------------|---------------------------------------------------|
| Crear estudiante   | Registra estudiante con usuario asociado       | `EstudianteController.crear_estudiante_usuario()` |
| Listar estudiantes | Obtiene todos los estudiantes con sus datos    | `EstudianteController.listar_estudiantes()`       |
| Obtener datos      | Recupera información completa de un estudiante | `EstudianteController.datos_estudiante()`         |
| Buscar por usuario | Encuentra estudiante por ID de usuario         | `Estudiante.buscar_por_usuario_id()`              |

### Gestión de Programas

| Funcionalidad    | Descripción                       | Método                                  |
|------------------|-----------------------------------|-----------------------------------------|
| Crear programa   | Registra nuevo programa académico | `ProgramaController.crear_programa()`   |
| Listar programas | Obtiene todos los programas       | `ProgramaController.listar_programas()` |
| Obtener por ID   | Recupera programa específico      | `Programa.listar()`                     |

### Test Vocacional

| Funcionalidad       | Descripción                                        | Método                                                   |
|---------------------|----------------------------------------------------|----------------------------------------------------------|
| Listar preguntas    | Obtiene preguntas organizadas por categoría        | `TestVocacionalController.listar_preguntas_categorias()` |
| Guardar respuestas  | Almacena respuestas del estudiante                 | `TestVocacionalController.guardar_respuestas()`          |
| Validar completitud | Verifica que todas las preguntas estén respondidas | Validación en `EstudianteView.enviar_test()`             |

### Sistema de Autenticación

| Funcionalidad    | Descripción                             | Método                           |
|------------------|-----------------------------------------|----------------------------------|
| Login            | Autentica usuario y retorna rol         | `LoginController.autenticar()`   |
| Validar usuario  | Verifica credenciales en BD             | `Usuario.validar_usuario()`      |
| Cerrar sesión    | Cierra ventana actual y vuelve al login | `UIHelpers.cerrar_sesion()`      |

## 🤖 Sistema de Recomendaciones IA

### Categorías del Test Vocacional

1. **Ciencias Exactas y Matemáticas** - STEM, ingeniería, ciencias puras
2. **Tecnología y Programación** - Desarrollo software, sistemas digitales
3. **Ciencias de la Salud** - Medicina, enfermería, bienestar
4. **Ciencias Sociales y Humanas** - Comportamiento humano, cultura
5. **Negocios y Administración** - Gestión empresarial, finanzas
6. **Artes y Diseño** - Creatividad, diseño visual
7. **Comunicación y Lenguaje** - Expresión verbal, medios
8. **Ciencias Naturales y Ambiente** - Biología, ecología
9. **Educación y Pedagogía** - Enseñanza, formación
10. **Derecho y Justicia** - Leyes, sistema judicial

### Algoritmo de Recomendación

1. **Recopilación de Respuestas:**
   - 50 preguntas con valores difusos (0.0 - 1.0)
   - 5 preguntas por categoría
   - Escala Likert de 5 puntos

2. **Cálculo de Afinidad por Categoría:**
   ```python
   afinidad_categoria = promedio(valores_fuzzy_respuestas)
   ```

3. **Mapeo Programa-Categorías:**
   - Cada programa está asociado a 1-2 categorías relevantes
   - Ejemplo: Ingeniería de Software → [Ciencias Exactas, Tecnología]

4. **Puntuación de Programas:**
   ```python
   puntaje_programa = promedio(afinidades_categorias_relevantes)
   ```

5. **Ranking Final:**
   - Programas ordenados por puntaje descendente
   - Visualización en formato porcentual
   - Actualización dinámica en la interfaz

### Visualización de Resultados

**Columna 1 - Programa Principal:**
- Programa con mayor afinidad
- Puntaje en formato porcentaje

**Columna 2 - Otros Programas:**
- Lista ordenada de programas restantes
- Cards individuales con nombre y porcentaje

## 👥 Desarrollado Por

- **Nicolas Santiago Naranjo**
- **Jose Alexander Ferreira**

**Programa:** Inteligencia Artificial - Explorador G148P  
**Institución:** Talento Tech  
**Año:** 2025

---

## Licencia

Este proyecto fue desarrollado con fines educativos como parte del programa de Inteligencia Artificial de Talento Tech.