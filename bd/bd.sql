CREATE DATABASE IF NOT EXISTS estudiantes_andap CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE estudiantes_andap;


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


INSERT INTO estudiante (id, nombre, edad) VALUES
(1, 'Juan Perez', 20),
(2, 'Carlos Reina', 48),
(3, 'Juanita Torres', 16),
(4, 'Maria DB', 30);

INSERT INTO programa (id, nombre_programa) VALUES
(1, 'Ingeniería de Sistemas'),
(2, 'Administración'),
(3, 'Diseño Gráfico');

INSERT INTO estudiante_programa (estudiante_id, programa_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 3),
(4, 2),
(4, 3);