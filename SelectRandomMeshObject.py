bl_info = {
    "name": "Select Random Mesh Object",
    "author": "BK7",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Select Random Mesh Object",
    "description": "Selects a random mesh object in the scene",
    "category": "Object",
}

import bpy
import random

# Define the operator class
class OBJECT_OT_random_mesh_selector(bpy.types.Operator):
    """Selects a random mesh object in the scene"""
    bl_idname = "object.random_mesh_selector"
    bl_label = "Select Random Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Switch to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        # Get a list of all the mesh objects in the scene
        mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']

        # Choose a random mesh object from the list
        random_obj = random.choice(mesh_objects)

        # Select and make active the random object
        random_obj.select_set(True)
        bpy.context.view_layer.objects.active = random_obj

        return {'FINISHED'}

# Define the panel class
class VIEW3D_PT_random_mesh_selector(bpy.types.Panel):
    """Creates a panel in the 3D View sidebar"""
    bl_label = "Select Random Mesh Object"
    bl_idname = "VIEW3D_PT_random_mesh_selector"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Select Random Mesh Object"

    def draw(self, context):
        layout = self.layout

        # Add a button that calls the operator
        layout.operator("object.random_mesh_selector")

# Register the classes
def register():
    bpy.utils.register_class(OBJECT_OT_random_mesh_selector)
    bpy.utils.register_class(VIEW3D_PT_random_mesh_selector)

# Unregister the classes
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_random_mesh_selector)
    bpy.utils.unregister_class(VIEW3D_PT_random_mesh_selector)

# Run the register function when the addon is enabled
if __name__ == "__main__":
    register()
