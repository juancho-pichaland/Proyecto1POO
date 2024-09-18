from models import Receta

def obtener_recetas():
    session = get_session()
    recetas = session.query(Receta).all()
    return recetas

def agregar_receta(nombre, descripcion, ingredientes, instrucciones):
    session = get_session()
    receta = Receta(nombre=nombre, descripcion=descripcion, ingredientes=ingredientes, instrucciones=instrucciones)
    session.add(receta)
    session.commit()
    
from models import Planificacion

def obtener_planificaciones():
    session = get_session()
    planificaciones = session.query(Planificacion).all()
    return planificaciones

def agregar_planificacion(usuario_id, receta_id, fecha):
    session = get_session()
    planificacion = Planificacion(usuario_id=usuario_id, receta_id=receta_id, fecha=fecha)
    session.add(planificacion)
    session.commit()
from models import ListaCompras

def obtener_listas_compras():
    session = get_session()
    listas_compras = session.query(ListaCompras).all()
    return listas_compras

def agregar_lista_compras(usuario_id, receta_id, ingredientes):
    session = get_session()
    lista_compras = ListaCompras(usuario_id=usuario_id, receta_id=receta_id, ingredientes=ingredientes)
    session.add(lista_compras)
    session.commit()
from models import Inventario

def obtener_inventarios():
    session = get_session()
    inventarios = session.query(Inventario).all()
    return inventarios

def agregar_inventario(usuario_id, ingredientes):
    session = get_session()
    inventario = Inventario(usuario_id=usuario_id, ingredientes=ingredientes)
    session.add(inventario)
    session.commit()
