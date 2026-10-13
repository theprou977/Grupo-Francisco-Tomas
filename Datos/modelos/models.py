��from peewee import DateField,IntegerField,AutoField,CharField,SQL,Model
from auxiliares import defecto
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Autores(BaseModel):
    fecha_defuncion = DateField(null=True)
    fecha_nacimiento = DateField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_autor = AutoField()
    nombre = CharField(max_length=100, null=True)
    pais = IntegerField(index=True, null=True)
    pseudonimo = CharField(max_length=25, null=True)

    class Meta:
        table_name = 'autores'

class Bibliotecarios(BaseModel):
    contrasena = CharField(max_length=60)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_bibliotecario = AutoField()
    tipo_usuario = IntegerField(index=True)
    usuario = IntegerField(index=True)

    class Meta:
        table_name = 'bibliotecarios'

class Bibliotecas(BaseModel):
    correo = CharField(null=True)
    direccion = IntegerField(index=True, null=True)
    id_biblioteca = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=15, null=True)
    web = CharField(null=True)

    class Meta:
        table_name = 'bibliotecas'

class Comunas(BaseModel):
    codigo_comuna = CharField(max_length=5)
    comuna = CharField(max_length=50)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_comuna = AutoField()

    class Meta:
        table_name = 'comunas'

class Direcciones(BaseModel):
    calle = CharField(max_length=50)
    comuna = IntegerField(index=True, null=True)
    departamento = CharField(max_length=5, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_direccion = AutoField()
    numero = CharField(max_length=5, null=True)
    parametro = IntegerField(index=True)

    class Meta:
        table_name = 'direcciones'

class DireccionesUsuarios(BaseModel):
    direccion = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_direccion_usuario = AutoField()
    usuario = IntegerField(index=True)

    class Meta:
        table_name = 'direcciones_usuarios'

class Editoriales(BaseModel):
    correo = CharField(null=True)
    direccion = IntegerField(index=True, null=True)
    editorial = CharField(max_length=100)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_editorial = AutoField()
    pais = IntegerField(index=True)
    telefono = CharField(max_length=15, null=True)

    class Meta:
        table_name = 'editoriales'

class Estados(BaseModel):
    descripcion = CharField(max_length=100, null=True)
    estado = CharField(max_length=20)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_estado = AutoField()

    class Meta:
        table_name = 'estados'

class Inventarios(BaseModel):
    estado = IntegerField(index=True)
    id_inventario = AutoField()
    libro = IntegerField(index=True)
    ubicacion = IntegerField(index=True)

    class Meta:
        table_name = 'inventarios'

class Lectores(BaseModel):
    categoria = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_lector = AutoField()
    usuario = IntegerField(index=True)

    class Meta:
        table_name = 'lectores'

class Libros(BaseModel):
    autor = IntegerField(index=True)
    biblioteca = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_libro = AutoField()
    paginas = IntegerField(null=True)
    publicacion = IntegerField(index=True)
    subgenero = IntegerField(index=True)
    titulo = CharField(max_length=100, null=True)

    class Meta:
        table_name = 'libros'

class Parametros(BaseModel):
    codigo = CharField(max_length=20)
    descripcion = CharField(max_length=100, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_parametro = AutoField()
    parametro = CharField(max_length=50)

    class Meta:
        table_name = 'parametros'

class Prestamos(BaseModel):
    fecha_devolucion = DateTimeField()
    fecha_prestamo = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fecha_retorno = DateTimeField(null=True)
    id_prestamo = AutoField()
    lector = IntegerField(index=True)
    libro = IntegerField(index=True)

    class Meta:
        table_name = 'prestamos'

class Publicaciones(BaseModel):
    editorial = IntegerField(index=True, null=True)
    fecha_publicacion = DateField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_publicacion = AutoField()
    idioma = IntegerField(index=True, null=True)
    isbn = CharField(max_length=17)
    publicacion = CharField(max_length=25, null=True)

    class Meta:
        table_name = 'publicaciones'

class TiposDireccion(BaseModel):
    descripcion = CharField(max_length=100, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_tipo_direccion = AutoField()
    tipo_direccion = CharField(max_length=20)

    class Meta:
        table_name = 'tipos_direccion'

class Ubicaciones(BaseModel):
    detalles = CharField(max_length=100, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_ubicacion = AutoField()
    ubicacion = CharField(max_length=20)

    class Meta:
        table_name = 'ubicaciones'

class Usuarios(BaseModel):
    apellido = CharField(max_length=25)
    correo = CharField()
    fecha_incorporacion = DateField()
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField()
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_usuario = AutoField()
    nombre = CharField(max_length=25)
    pais = IntegerField(index=True, null=True)
    rut = CharField(max_length=11, null=True, unique=True)

    class Meta:
        table_name = 'usuarios'

