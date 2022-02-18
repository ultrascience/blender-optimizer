# Programa que busca archivos FBX y los importa .blend
import os
import bpy

"""Find all files with termination
    and returns it without termination
    :param path to directory
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
Funcion que importa los archivos y le aplica el modificador decimate
"""
def importFiles():        
    blenderFiles=findFiles('/home/aldo/modelos_raw')

    current_directory = os.getcwd()
    current_directory = os.path.join(current_directory, "modelosGLB")
    os.mkdir(current_directory)

    for file in blenderFiles:

        # Limpiamos los data blocks de blender
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.fbx(filepath=file)
        print("Importando archivo: "+file)

        # Agregamos el modificador decimal
        for object in bpy.data.objects:
            if object.type == "MESH" and not object.name.startswith("Camera") and not object.name.startswith("Cube") and not object.name.startswith("Lig"):
                
                print("Aplicamos el modificador decimate a: "+object.name)
                bpy.context.view_layer.objects.active = object
                bpy.ops.object.modifier_add(type='DECIMATE')

                bpy.context.object.modifiers["Decimate"].use_collapse_triangulate = True
                bpy.context.object.modifiers["Decimate"].ratio=0.1

                # Aplicamos el modificador al objeto
                bpy.ops.object.modifier_apply( modifier = 'Decimate' )

        nombre_archivo = os.path.basename(file)
        # path_file_blend = os.path.splitext(nombre_archivo)[0] + ".blend"

        path_file_glb = os.path.splitext(nombre_archivo)[0] + ".glb"
        path_directorio = os.path.join(current_directory,path_file_glb)

        # Guardamos el modelo reducido con el nombre del archivo fbx importado
        # bpy.ops.wm.save_as_mainfile(filepath=path_file_blend)    
        # Importamos el archivo a glb
        bpy.ops.export_scene.gltf(filepath = path_directorio, use_selection = False)

def main():
    importFiles()

if __name__ == '__main__':
    main()
