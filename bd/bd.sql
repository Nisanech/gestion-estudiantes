-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS estudiantes_andap
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Usar la base de datos creada
USE estudiantes_andap;

-- Crear tabla estudiante
CREATE TABLE estudiante (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL
);

-- Crear tabla programa
CREATE TABLE programa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_curso VARCHAR(100) NOT NULL
);

-- Crear tabla intermedia para relación muchos-a-muchos
CREATE TABLE estudiante_programa (
    estudiante_id INT,
    programa_id INT,
    PRIMARY KEY (estudiante_id, programa_id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiante(id),
    FOREIGN KEY (programa_id) REFERENCES programa(id)
);

------------------------------------------------------
-- INSERTAR REGISTROS (6 registros en total)
------------------------------------------------------

-- 3 estudiantes
INSERT INTO estudiante (id, nombre, edad) VALUES
(1, 'Juan Pérez', 20),
(2, 'María Gómez', 22),
(3, 'Carlos López', 19);

-- 3 programas
INSERT INTO programa (id, nombre_curso) VALUES
(1, 'Ingeniería de Sistemas'),
(2, 'Administración'),
(3, 'Diseño Gráfico');

-- Relación estudiante-programa (muchos a muchos)
-- 6 registros
INSERT INTO estudiante_programa (estudiante_id, programa_id) VALUES
(1, 1),  -- Juan → Ing. Sistemas
(1, 2),  -- Juan → Administración
(2, 1),  -- María → Ing. Sistemas
(2, 3),  -- María → Diseño Gráfico
(3, 2),  -- Carlos → Administración
(3, 3);  -- Carlos → Diseño Gráfico