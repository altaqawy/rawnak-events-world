# RAWNAK EVENTS — Asset audit / V1 integration

## Files received
- `source/RAWNAK_EVENTS_master.blend` — editable Blender source.
- `assets/rawnak-events-world.glb` — web delivery model.
- Blender version visible in the user's workflow: 5.3.0.

## Confirmed GLB contents
- 9 island meshes / story locations.
- 1,570 glTF nodes and 1,503 mesh definitions.
- 35 materials.
- 0 embedded images and 0 textures.
- 1 glTF animation.
- 0 exported cameras.
- 15 named waterfall flow proxy objects.
- 56 Sakura tree proxy assemblies.
- 352 cloud-related nodes (includes cloud, island-cloud and transition-cloud assets).
- 9 chapter plaque / lettering pairs.

## Story chapters identified in the Blender source
1. THE FIRST HELLO
2. LITTLE WONDERS
3. DREAMS & ACHIEVEMENTS
4. TWO HEARTS
5. FOREVER BEGINS
6. THE ART OF GIVING
7. TOGETHER ALWAYS
8. EXTRAORDINARY GATHERINGS
9. THE TREE OF LIFE

## Important production findings
- The Blender source explicitly labels the scene as a geometry and camera blockout with no final production assets.
- Most botanical, cloud, water, glass and terrain materials are named as proxies.
- The GLB has no camera objects. The Blender source contains `CAM 01 | Life journey`, `CAM 02 | Overview` and `CAM 03 | Entrance portrait`.
- `RAWNAK_GlobalFog_V2` is a very large global fog volume. The web preview hides it and recreates atmospheric depth with lightweight browser effects.
- 1,500+ mesh definitions are too many to leave unoptimized for mobile. Before production, static meshes should be batched/merged by material, repeated assets instanced, and non-visible proxy geometry removed.
- This GLB is the RAWNAK EVENTS world only. It does not contain the Agency or Academy worlds.

## Web integration approach
- Keep the GLB as the visual source for the Events journey.
- Use scroll progress to drive a web camera path through the nine chapter islands.
- Use lightweight browser fog, cloud sprites, petal particles and animated waterfall materials for effects that should not be baked into the GLB.
- Export the original Blender camera path using `tools/export_camera_path.py`; copy the resulting `camera-path.json` into `assets/` to replace the empty fallback file.
- Keep this as a separate Events-world prototype until the current Rawnak Group website source/repository is provided and confirmed. Do not replace the live website with this preview.
