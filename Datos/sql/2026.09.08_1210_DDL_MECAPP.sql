CREATE DATABASE mecapp;

USE mecapp;

CREATE TABLE tipos_direccion(
    id_tipo_direccion INTEGER AUTO_INCREMENT,
    tipo_direccion VARCHAR(25) NOT NULL,
    detalle VARCHAR(50) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1

    CONSTRAINT pk_tipo_direccion PRIMARY KEY (id_tipos_direccion)
);

CREATE TABLE comunas(
    id_comuna INTEGER AUTO_INCREMENT,
    codigo_comuna VARCHAR(5) NOT NULL,
    nombre_comuna VARCHAR(30) NOT NULL,

    CONSTRAINT pk_comunas PRIMARY KEY (id_comunas)
);    

CREATE TABLE direcciones(
    id_direccion INTEGER AUTO_INCREMENT,
    comuna INTEGER NOT NULL,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(5) NULL,
    departamento VARCHAR(5) NULL,
    tipo_direccion INTEGER NULL,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direccion),
    CONSTRAINT pf_direcciones_comunas FOREING KEY (comuna) REFERENCES comunas(id_comuna),
    CONSTRAINT fk_direcciones_tipos_direccion FOREING KEY (tipo_direccion) references tipo_direccion(id_tipo_direccion)
);


CREATE TABLE talleres(
    id_taller INTEGER AUTO_INCREMENT,
    nombre_taller VARCHAR(50) NOT NULL,
    direccion INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
)   COMMENT = 'informacion talleres mecanicos';

CREATE TABLE tipos_mecanico(
    id_tipos_mecanico INTEGER AUTO_INCREMENT,
    tipo_mecanico VARCHAR(25) NOT NULL,
    detalle VARCHAR(50) NULL,
    habilitado  TINYINT NOT NULL DEFAULT 1,

);

CREATE TABLE mecanico(
    rut INTEGER NOT NULL UNIQUE,
    digito_verificador char(1) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(250) NULL,
    telefono VARCHAR(15) NULL,
    fecha_nacimiento DATE NOT NULL,
    fecha_contrato DATE NOT NULL,
    salario DECIMAL NULL,
    direccion INTEGER NULL,
    tipo_mecanico INTEGER NULL,
    
    CONSTRAINT pk_mecanicos PRIMARY KEY (rut),
    CONSTRAINT fk_mecanicos_direcciones FOREING KEY (direccion) REFERENCES direcciones(id_direccion)
    CONSTRAINT fk_mecanicos_tiposmecanico foreing KEY (tipo_mecanico) REFERENCES tipos_mecanico(id_tipos_mecanico)
);

CREATE TABLE talleres_mecanicos(
    id_taller_mecanico INTEGER AUTO_INCREMENT,
    mecanico INTEGER NOT NULL,
    taller INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_talleres_mecanicos PRIMARY KEY (id_taller_mecanico),
    CONSTRAINT fk_talleresmecanicos_taller foreing KEY (taller) REFERENCES talleres(id_taller),
    CONSTRAINT fk_talleresmecanico_ mecanico FOREING KEY (mecanico) REFERENCES mecanicos(rut)
);

CREATE TABLE parametros(
    id_parametro INTEGER AUTO_INCREMENT,
    tipo_parametro VARCHAR(30) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,

    CONSTRAINT pf_parametros PRIMARY KEY (id_parametro)
) COMMENT = 'informacion parametrica usada dentro de la aplicacion, combustible, tipo de vehiculo, etc'

ALTER TABLE parametros ADD habilitado TINYINT NOT NULL DEFAULT 1;





INSERT INTO parametros(tipo_parametro, descripcion) VALUES
('COMBUSTIBLE', '93 octanos')
('COMBUSTIBLE', '95 octanos')
('COMBUSTIBLE', '97 octanos')
('COMBUSTIBLE', 'Diesel')
('COMBUSTIBLE', 'parafina')
('COMBUSTIBLE', 'alcohol')
('COMBUSTIBLE', 'Bio-diesel')
('COMBUSTIBLE', 'electricidad')
('COMBUSTIBLE', 'gas licuado')
('tipo de vehiculo', 'City car')
('tipo de vehiculo', 'hatshback')
('tipo de vehiculo', 'Csedan')
('tipo de vehiculo', 'SUV')
('tipo de vehiculo', 'Crossover')
('tipo de vehiculo', 'camioneta')
('tipo de vehiculo', 'Van')
('tipo de vehiculo', 'transporte de pasajeros')
('tipo de vehiculo', 'transporte de cargas')