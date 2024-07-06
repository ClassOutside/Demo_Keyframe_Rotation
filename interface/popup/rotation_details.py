import bpy
from ...services.rotationOperators import RotationKeyframeOperator

class RotationPopup(bpy.types.Operator):
    bl_idname = "object.rotation_popup"
    bl_label = "Rotation Popup Operator"

    frame_duration: bpy.props.IntProperty(name="Frame Duration")

    def execute(self, context):
        print("Frame Duration:", self.frame_duration)
        
        bpy.ops.object.rotation_keyframe_operator(frame=self.frame_duration)
        
        return {'FINISHED'}

    def invoke(self, context, event):
        print("Here")
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "frame_duration")

def register():
    bpy.utils.register_class(RotationPopup)

def unregister():
    bpy.utils.unregister_class(RotationPopup)
