# Programa que convierte todos los archivos .blend a .glb para su uso en jsx

import bpy
import os

# Funcion que recibe como parametro la ruta en donde se colocaran los modelos exportados
def exportar_objetos(rutaDirectorio):
     
    rutaDirectorio = os.rutaDirectorio.abspath(rutaDirectorio)

    # Obtenemos todos los objetos de tipo MESH
    lista_objetos = [e for e in bpy.data.objects if e.type == 'MESH']
    
    # Deseleccionamos todos
    bpy.ops.object.select_all(action='DESELECT')


    # Selecionamos un objeto activo para realizar la fusion
    bpy.context.scene.objects.active = bpy.data.objects["texturedMesh"]


    bpy.ops.object.join()

    # Recorremos la lista de los objetos
    for objecto3D in lista_objetos:
        
        # Seleccionamos el objeto
        bpy.context.scene.objects[objecto3D.name].select_set(True)
        
        # Creamos los directorios
        directorioResultado = os.rutaDirectorio.join(rutaDirectorio, objecto3D.name)
        os.mkdir(directorioResultado)
        
        # Asignamos el nombre del archivo
        directorioResultado = os.rutaDirectorio.join(directorioResultado, objecto3D.name+'.glb')

        # Aquí es donde exportamos la escena a GLB.        
        bpy.ops.export_scene.gltf(
            filepath=directorioResultado,
            export_format='GLB'
        )
        

        
exportar_objetos('archivosGLB')
