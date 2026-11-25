import bpy
import json
import math
import os
from mathutils import Matrix

scene = bpy.context.scene
camera = bpy.data.objects.get("CAM 01 | Life journey")
if camera is None or camera.type != "CAMERA":
    raise RuntimeError("Life journey camera not found")
old_frame = scene.frame_current
start_frame, end_frame = scene.frame_start, scene.frame_end
frames = sorted(set(start_frame + round((end_frame-start_frame)*i/119) for i in range(120)))
basis = Matrix.Rotation(-math.pi/2, 4, 'X')
samples = []
try:
    for frame in frames:
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        matrix = basis @ camera.matrix_world
        loc, quat = matrix.translation, matrix.to_quaternion()
        samples.append({"frame": frame, "position": list(loc), "quaternion": [quat.x,quat.y,quat.z,quat.w], "lens": float(camera.data.lens), "fov": float(camera.data.angle_y)})
finally:
    scene.frame_set(old_frame)
payload = {"coordinateSystem":"glTF Y-up","camera":camera.name,"fps":scene.render.fps/scene.render.fps_base,"frameStart":start_frame,"frameEnd":end_frame,"samples":samples}
path = os.path.join(bpy.path.abspath("//"),"camera-path.json")
with open(path,"w",encoding="utf-8") as f:
    json.dump(payload,f,indent=2)
print("Camera path exported:",path)
