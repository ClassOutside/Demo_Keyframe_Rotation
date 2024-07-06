import bpy

class RotationKeyframeOperator(bpy.types.Operator):
    """Set rotation keyframes for the selected object"""
    bl_idname = "object.rotation_keyframe_operator"
    bl_label = "Rotation Keyframe Operator"
    
    frame: bpy.props.IntProperty(name="Frame")

    def execute(self, context):
        # Get the currently selected object
        obj = bpy.context.object

        # Set the initial rotation keyframe at frame 0
        obj.rotation_euler = (0, 0, 0)
        obj.keyframe_insert(data_path="rotation_euler", frame=0)

        # Set another rotation keyframe 360 degrees on Z axis at the passed frame
        obj.rotation_euler = (0, 0, 3.14159 * 2)  # 360 degrees in radians
        obj.keyframe_insert(data_path="rotation_euler", frame=self.frame)

        return {'FINISHED'}
