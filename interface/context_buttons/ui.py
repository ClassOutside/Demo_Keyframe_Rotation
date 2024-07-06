import bpy
from ..popup.rotation_details import RotationPopup

class ConfigureRotationMenu(bpy.types.Menu):
    bl_label = "Rotation Configuration Menu"
    bl_idname = "OBJECT_MT_rotation_configuration"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        layout.operator(RotationPopup.bl_idname, text="Configure Rotation")

def menu_func(self, context):
    self.layout.separator()
    self.layout.menu(ConfigureRotationMenu.bl_idname)

def register():
    bpy.utils.register_class(ConfigureRotationMenu)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)

def unregister():
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)
    bpy.utils.unregister_class(ConfigureRotationMenu)
