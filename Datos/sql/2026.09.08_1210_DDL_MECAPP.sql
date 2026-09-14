create database mecapp;
use mecapp;

create table tipos_direccion(
    id_tipo_direccion integer auto_increment,
    tipo_direccion varchar(25) not null,
    detalle varchar(20) null,
    habilitado tinyint not null default 1,
constraint pk_tipos_direccion primary key (id_tipo_direccion)
);

create table comunas(
    id_comuna integer auto_increment,
    codigo_comuna varchar(5) not null unique,
    nombre_comuna varchar(30) not null,
    constraint pk_comunas primary key (id_comuna)
);

create table direcciones(
    id_direccion integer auto_increment,
    comuna integer not null,
    calle varchar(50) not null,
    numero varchar(5) null,
    departamento varchar(5) null,
    tipo_direccion integer null,
    constraint pk_direcciones primary key (id_direccion),
    constraint fk_direcciones_comunas foreign key (comuna) references comunas(id_comuna),
    constraint fk_direcciones_tipos_direccion foreign key (tipo_direccion) references tipos_direccion(id_tipo_direccion)      
)