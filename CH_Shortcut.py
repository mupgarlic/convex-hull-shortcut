import bpy

bl_info = {
    "name": "Convex Hull Shortcut",
    "author": "mupgarlic - Bunny Ash",
    "version": (1, 0),
    "blender" : (4, 0, 2),
    "description": "Press RIGHT SHIFT to instantly apply Convex Hull!",
    "category": "Development",
}


class OBJECT_OT_CustomOp(bpy.types.Operator):
    """Apply Convex Hull"""
    bl_idname = "object.simple_operator"
    bl_label = "Convex Hull Operator"

    def execute(self, context):
        
        #Convex Hull script (you can replace this with any script to shortcut anything)
        bpy.ops.mesh.convex_hull()
        
        return {'FINISHED'}


addon_keymaps = []

def register():
    bpy.utils.register_class(OBJECT_OT_CustomOp)
    
    #Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new(
            OBJECT_OT_CustomOp.bl_idname, type='RIGHT_SHIFT', value='PRESS'
            )
        addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_CustomOp)
    
    #Remove the hotkey
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()