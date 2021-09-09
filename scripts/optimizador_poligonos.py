# Programa que busca archivos FBX y les aplica una reduccion de poligonos utilizando
# el modificador decimate
import os
import bpy


""" 
    Encuentra todos los archivos con la terminacion .fbx

    Parameters
    ----------
    path :  str 
        Ubicacion de la carpeta a examinar
    
    Returns
    ----------
    resultado : list
        Lista con la ubicacion con la terminacion dada
"""
def findFiles(path):
    resultado = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".fbx"):
                print(os.path.join(root,file))
                resultado.append(os.path.join(root,file))
    return resultado

"""
    Importa los archivos y le aplica el modificador decimate.

    Parameters
    ----------
    ubicacion_modelos : str
        Ubicacion de la carpeta con los modelos a procesar
    
    ubicacion_resultado: str
        Ubicacion de la carpeta con los modelos ya procesados

"""

def importFiles(ubicacion_modelos, ubicacion_resultado):        
    blenderFiles=findFiles('/home/aldo/modelos_raw')


    for file in blenderFiles:

        # Limpiamos los data blocks de blender
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importamos el modelo
        bpy.ops.import_scene.fbx(filepath=file)
        print("Importando archivo: "+file)

        # Agregamos el modificador decimal
        for object in bpy.data.objects:
            # Aplicamos el modificador decimate solo al modelos deseado
            if object.type == "MESH" and not object.name.startswith("Camera") and not object.name.startswith("Cube") and not object.name.startswith("Lig"):
                
                print("Aplicamos el modificador decimate a: "+object.name)
                bpy.context.view_layer.objects.active = object

                # Agregamos el modificador decimate al objecto seleccionado actualmente
                bpy.ops.object.modifier_add(type='DECIMATE')
                bpy.context.object.modifiers["Decimate"].use_collapse_triangulate = True

                # Reducimos la cantidad de poligonos en un 90%
                bpy.context.object.modifiers["Decimate"].ratio=0.1

                # Aplicamos el modificador al objeto
                bpy.ops.object.modifier_apply( modifier = 'Decimate' )

        nombre_archivo = os.path.basename(file)

        path_file_glb = os.path.splitext(nombre_archivo)[0] + ".glb"
        path_directorio = os.path.join(ubicacion_resultado, path_file_glb)

        # Guardamos el modelo reducido con el nombre del archivo fbx importado
        # bpy.ops.wm.save_as_mainfile(filepath=path_file_blend)    

        # Exportamos el modelo a glb
        bpy.ops.export_scene.gltf(filepath = path_directorio, use_selection = False)

def main():

    ubicacion_modelos_glb = os.getcwd()
    ubicacion_modelos_glb = os.path.join(ubicacion_modelos_glb, "modelos_glb")

    # Creamos la carpeta en donde colocaremos los modelos
    os.mkdir(ubicacion_modelos_glb)

    importFiles("home/aldo/modelos_raw",ubicacion_modelos_glb)

if __name__ == '__main__':
    main()
