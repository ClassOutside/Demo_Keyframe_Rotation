from .module_loader import refresh
refresh()

bl_info = {
    "name": "Auto Rotation Add-on",
    "blender": (4, 1, 1),
    "category": "Object",
}

import bpy
from .services.rotationOperators import *
from .interface.context_buttons.ui import *
from .interface.popup.rotation_details import *

classes = [
    RotationKeyframeOperator,
    RotationPopup,
    ConfigureRotationMenu,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_object_context_menu.append(ConfigureRotationMenu.draw)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    bpy.types.VIEW3D_MT_object_context_menu.remove(ConfigureRotationMenu.draw)


if __name__ == "__main__":
    register()
