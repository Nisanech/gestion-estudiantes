CREATE DATABASE IF NOT EXISTS estudiantes_andap CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE estudiantes_andap;

-- TABLAS GENERALES --
CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    correo VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'estudiante') NOT NULL
);


CREATE TABLE estudiante (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INT,
    genero ENUM('M','F','Otro'),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE programa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_programa VARCHAR(150) NOT NULL,
    descripcion TEXT
);

CREATE TABLE estudiante_programa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    estudiante_id INT NOT NULL,
    programa_id INT NOT NULL,
    tipo ENUM('recomendado','interesado','inscrito'),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (estudiante_id) REFERENCES estudiante(id),
    FOREIGN KEY (programa_id) REFERENCES programa(id)
);

-- TEST VOCACIONAL --

-- Categorias del test --
CREATE TABLE categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE pregunta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    categoria_id INT NOT NULL,
    texto_pregunta TEXT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);

CREATE TABLE opcion_respuesta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pregunta_id INT NOT NULL,
    texto_opcion VARCHAR(200) NOT NULL,
    valor_fuzzy DECIMAL(4,3) NOT NULL,   -- 0.000–1.000
    FOREIGN KEY (pregunta_id) REFERENCES pregunta(id)
);

CREATE TABLE respuesta_estudiante (
    id INT PRIMARY KEY AUTO_INCREMENT,
    estudiante_id INT NOT NULL,
    pregunta_id INT NOT NULL,
    opcion_id INT NOT NULL,
    valor_fuzzy DECIMAL(4,3) NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES estudiante(id),
    FOREIGN KEY (pregunta_id) REFERENCES pregunta(id),
    FOREIGN KEY (opcion_id) REFERENCES opcion_respuesta(id)
);

CREATE TABLE afinidad_difusa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    estudiante_id INT NOT NULL,
    categoria_id INT NOT NULL,
    nivel_fuzzy DECIMAL(4,3) NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES estudiante(id),
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);

CREATE TABLE recomendacion_programa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    estudiante_id INT NOT NULL,
    programa_id INT NOT NULL,
    puntaje DECIMAL(4,3) NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES estudiante(id),
    FOREIGN KEY (programa_id) REFERENCES programa(id)
);

-- INSERTAR DATOS --

INSERT INTO usuario (correo, password, rol) VALUES
('admin@correo.com', 'admin123', 'admin'),
('estudiante1@correo.com', 'est123', 'estudiante'),
('estudiante2@correo.com', 'est456', 'estudiante');

INSERT INTO estudiante (usuario_id, nombre, apellido, edad, genero) VALUES
(2, 'Carlos', 'Ramírez', 19, 'M'),
(3, 'Laura', 'González', 21, 'F');

INSERT INTO programa (nombre_programa, descripcion) VALUES
('Ingeniería de Software', 'Formación en desarrollo de software, programación, análisis y diseño de sistemas.'),
('Contabilidad y Finanzas', 'Formación en principios contables, gestión financiera y análisis de estados financieros.'),
('Diseño Gráfico', 'Programa centrado en creatividad, diseño digital, ilustración y herramientas visuales.'),
('Administración de Empresas', 'Formación en dirección, gestión, mercadeo y procesos administrativos.'),
('Sistemas de Información', 'Programa orientado al manejo de datos, infraestructura tecnológica y soporte TI.'),
('Marketing Digital', 'Formación en estrategias digitales, redes sociales, publicidad online y analítica web.');


INSERT INTO categoria (nombre, descripcion) VALUES
('CIENCIAS EXACTAS Y MATEMÁTICAS', 'Mide la afinidad con áreas STEM, ingeniería y ciencias puras'),
('TECNOLOGÍA Y PROGRAMACIÓN', 'Evalúa interés en desarrollo de software, sistemas y tecnologías digitales'),
('CIENCIAS DE LA SALUD', 'Mide vocación por medicina, enfermería y áreas relacionadas con bienestar'),
('CIENCIAS SOCIALES Y HUMANAS', 'Evalúa interés en comportamiento humano, sociedad y cultura'),
('NEGOCIOS Y ADMINISTRACIÓN', 'Mide afinidad con gestión empresarial, finanzas y emprendimiento'),
('ARTES Y DISEÑO', 'Mide habilidades comunicativas, escritura y expresión verbal'),
('COMUNICACIÓN Y LENGUAJE', 'Mide la afinidad con áreas STEM, ingeniería y ciencias puras'),
('CIENCIAS NATURALES Y AMBIENTE', 'Evalúa interés por biología, ecología y medio ambiente'),
('EDUCACIÓN Y PEDAGOGÍA', 'Mide vocación por la enseñanza y formación de otros'),
('DERECHO Y JUSTICIA', 'Evalúa interés por leyes, sistema judicial y argumentación');

INSERT INTO pregunta (categoria_id, texto_pregunta) VALUES
(1, 'Me gusta resolver problemas utilizando números y fórmulas matemáticas'),
(1, 'Disfruto entender cómo funcionan las cosas desde un punto de vista técnico'),
(1, 'Me siento cómodo trabajando con ecuaciones y cálculos complejos'),
(1, 'Me interesa descubrir patrones y relaciones lógicas en los datos'),
(1, 'Prefiero soluciones basadas en evidencia científica y métodos cuantitativos'),

(2, 'Me atrae la idea de crear aplicaciones, software o sitios web'),
(2, 'Disfruto aprender nuevos lenguajes de programación o herramientas tecnológicas'),
(2, 'Me interesa entender cómo funcionan los sistemas informáticos y redes'),
(2, 'Me gusta automatizar procesos y resolver problemas mediante código'),
(2, 'Paso tiempo explorando nuevas tecnologías y tendencias digitales'),

(3, 'Me motiva la idea de ayudar a las personas a mejorar su salud'),
(3, 'Me interesa comprender el funcionamiento del cuerpo humano y sus enfermedades'),
(3, 'Tengo paciencia y empatía para tratar con personas en situaciones difíciles'),
(3, 'Me siento cómodo en entornos hospitalarios o clínicos'),
(3, 'Me gustaría participar en investigación médica o práctica clínica'),

(4, 'Me fascina entender el comportamiento humano y las dinámicas sociales'),
(4, 'Disfruto analizar problemas sociales y proponer soluciones'),
(4, 'Me interesa la historia, la política y los movimientos culturales'),
(4, 'Me gusta investigar sobre diferentes culturas y formas de pensamiento'),
(4, 'Considero importante trabajar por el bienestar social y la justicia'),

(5, 'Me interesa cómo funcionan las empresas y cómo se toman decisiones estratégicas'),
(5, 'Me atrae la idea de crear o dirigir mi propio negocio'),
(5, 'Disfruto analizar datos financieros y tendencias del mercado'),
(5, 'Me siento cómodo liderando equipos y coordinando proyectos'),
(5, 'Me motiva alcanzar metas comerciales y mejorar resultados organizacionales'),

(6, 'Me gusta expresarme a través de la creación artística (dibujo, música, diseño, etc.)'),
(6, 'Tengo facilidad para visualizar conceptos y representarlos gráficamente'),
(6, 'Disfruto proyectos que requieren creatividad e innovación estética'),
(6, 'Me interesa la teoría del color, composición y elementos visuales'),
(6, 'Valoro la originalidad y la expresión personal en mi trabajo'),

(7, 'Me siento cómodo hablando en público y expresando mis ideas'),
(7, 'Disfruto escribir textos, artículos o historias'),
(7, 'Me interesa aprender idiomas y entender diferentes formas de comunicación'),
(7, 'Me gusta trabajar con medios de comunicación (radio, TV, redes sociales)'),
(7, 'Tengo facilidad para persuadir y transmitir mensajes de forma efectiva'),

(8, 'Me preocupa el estado del medio ambiente y la conservación de recursos'),
(8, 'Me fascina estudiar seres vivos, ecosistemas y procesos naturales'),
(8, 'Disfruto realizar trabajo de campo y experimentos en laboratorio'),
(8, 'Me interesa la investigación en áreas como biología, química o geología'),
(8, 'Me gustaría contribuir a soluciones ambientales y sostenibilidad'),

(9, 'Me gusta explicar conceptos y ayudar a otros a aprender'),
(9, 'Tengo paciencia para trabajar con diferentes tipos de estudiantes'),
(9, 'Me motiva la idea de contribuir a la formación de nuevas generaciones'),
(9, 'Disfruto planificar actividades educativas y metodologías de enseñanza'),
(9, 'Me interesa la psicología del aprendizaje y el desarrollo educativo'),

(10, 'Me interesa conocer las leyes y cómo se aplican en la sociedad'),
(10, 'Disfruto debatir y argumentar desde diferentes perspectivas legales'),
(10, 'Me motiva defender derechos y buscar justicia'),
(10, 'Me siento cómodo analizando casos legales y normativas'),
(10, 'Me gustaría trabajar en el sistema judicial o en asesoría legal');


-- Crear para cada ID pregunta (1-50) --
INSERT INTO opcion_respuesta (pregunta_id, texto_opcion, valor_fuzzy) VALUES
(50, 'Totalmente en desacuerdo', 0.0),
(50, 'En desacuerdo', 0.25),
(50, 'Neutral', 0.5),
(50, 'De acuerdo', 0.75),
(50, 'Totalmente de acuerdo', 1.0);

