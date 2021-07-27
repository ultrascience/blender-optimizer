# Programa que convierte todos los archivos .blend a .glb para su uso en jsx

import bpy
import os

# Funcion que recibe como parametro la ruta en donde se colocaran los modelos exportados
def exportar_objetos(rutaDirectorio):
     
    rutaDirectorio = os.path.abspath(rutaDirectorio)

    joinObjects()

    # Obtenemos todos los objetos de tipo MESH
    lista_objetos = [e for e in bpy.data.objects if e.type == 'MESH' and e.name.startswith('tex')]


    # Recorremos la lista de los objetos
    for objecto3D in lista_objetos:

        nameExtension = os.path.basename(bpy.data.filepath)
        nameFile = os.path.splitext(nameExtension)[0]

        # Seleccionamos el objeto
        bpy.context.scene.objects[objecto3D.name].select_set(True)
        
        # Creamos los directorios
        directorioResultado = os.path.join(rutaDirectorio, nameFile)
        os.mkdir(directorioResultado)
        
        # Asignamos el nombre del archivo
        directorioResultado = os.path.join(directorioResultado, nameFile+'.glb')

        # Aquí es donde exportamos la escena a GLB.        
        bpy.ops.export_scene.gltf(
            filepath=directorioResultado,
            export_format='GLB'
        )
        

def joinObjects():
    
    # Deseleccionamos todos
    bpy.ops.object.select_all(action='DESELECT')
    lista_objetos = [e for e in bpy.data.objects if e.type == 'MESH' and e.name.startswith('tex')]
    nombreObjetoActivo = lista_objetos[0].name

    for obj in bpy.context.scene.objects:
        obj.select_set(True)

    bpy.context.view_layer.objects.active = bpy.data.objects[nombreObjetoActivo] 

    bpy.ops.object.join()

    # Deseleccionamos todos
    bpy.ops.object.select_all(action='DESELECT')

        
exportar_objetos('archivosGLB')
