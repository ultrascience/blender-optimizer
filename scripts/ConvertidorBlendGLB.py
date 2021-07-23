# Programa que convierte todos los archivos .blend a .glb para su uso en jsx

import bpy
import os

# Funcion que recibe como parametro la ruta en donde se colocaran los modelos exportados
def exportar_objetos(path):
     
    path = os.path.abspath(path)

    lista_objetos = bpy.context.scene.objects

    # Recorremos la lista de los objetos
    for o in lista_objetos:
        
        # Seleccionamos el objeto
        bpy.context.scene.objects[o.name].select_set(True)
        
        # Creamos los directorios
        outpath = os.path.join(path, o.name)
        os.mkdir(outpath)
        
        # Asignamos el nombre del archivo
        outpath = os.path.join(outpath, o.name+'.glb')

        # Aquí es donde exportamos la escena a GLB.        
        bpy.ops.export_scene.gltf(
            filepath=outpath,
            export_format='GLB'
        )
        

        
exportar_objetos('modelos')
