# Programa que busca archivos FBX y los importa .blend
import os
import bpy

"""Find all files with termination .glb in the current directory
    and returns it without termination
    :param path to directory
"""
def findFiles(path):
    resultado = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".dae"):
                print(os.path.join(root,file))
                resultado.append(os.path.join(root,file))
    return resultado

"""
Funcion que importa los archivos y le aplica el modificador decimate
"""
def importFiles(ruta):
    blenderFiles=findFiles(ruta)

    current_directory = os.getcwd()
    current_directory = os.path.join(current_directory, "modelosGLB")
    os.mkdir(current_directory)

    for file in blenderFiles:

        # Limpiamos los data blocks de blender
        bpy.ops.wm.read_factory_settings(use_empty=True)
        # bpy.ops.import_scene.gltf(filepath=file)
        bpy.ops.wm.collada_import(filepath=file)
        print("Importando archivo: "+file)

        # Agregamos el modificador decimal
        for object in bpy.data.objects:
            if object.type == "MESH":
                # if number of faces is less than 1000
                number_of_faces = len(object.data.polygons)
                ratio = 0.93

                if number_of_faces > 15:

                    if number_of_faces > 50000:
                        ratio = 0.1
                    
                        print("Aplicamos el modificador decimate a: "+object.name)
                        bpy.context.view_layer.objects.active = object
                        bpy.ops.object.modifier_add(type='DECIMATE')

                        bpy.context.object.modifiers["Decimate"].decimate_type = 'COLLAPSE'
                        bpy.context.object.modifiers["Decimate"].ratio = ratio
                        bpy.context.object.modifiers["Decimate"].use_collapse_triangulate = True
                        bpy.context.object.modifiers["Decimate"].use_symmetry = True


                        # Aplicamos el modificador al objeto
                        bpy.ops.object.modifier_apply( modifier = 'Decimate' )

                        # apply shade smooth
                        bpy.ops.object.shade_smooth()
            else:
                # Borra todos los objetos que no son de tipo MESH
                bpy.data.objects.remove(object, do_unlink=True)


        # Set origin to 3D cursor
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        # Select all object
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.join()

        factor_scale = ( 19 // bpy.data.objects[0].dimensions[0])
        # Scale object  
        bpy.ops.transform.resize(value=(factor_scale, factor_scale, factor_scale))

        bpy.ops.file.find_missing_files(find_all=True)
        nombre_archivo = os.path.basename(file)
        # path_file_blend = os.path.splitext(nombre_archivo)[0] + ".blend"

        path_file_glb = os.path.splitext(nombre_archivo)[0] + ".glb"
        path_directorio = os.path.join(current_directory,path_file_glb)

        # Guardamos el modelo reducido con el nombre del archivo fbx importado
        # bpy.ops.wm.save_as_mainfile(filepath=path_file_blend)    
        # Importamos el archivo a glb
        bpy.ops.export_scene.gltf(filepath = path_directorio, use_selection = False)

def main():
    cwd = os.getcwd()
    importFiles(cwd)

if __name__ == '__main__':
    main()
