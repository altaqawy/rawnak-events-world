# RAWNAK EVENTS — A Lifetime of Moments

A standalone interactive 3D website prototype for RAWNAK Events, using a nine-chapter floating-island world, Three.js, and scroll-driven camera navigation.

## Project layout

- `index.html` — English-language interactive website.
- `assets/rawnak-events-world.glb` — Blender world export.
- `assets/camera-path.json` — optional sampled camera path.
- `tools/export_camera_path.py` — Blender camera export utility.
- `source/RAWNAK_EVENTS_master.blend` — editable source scene (optional; keep private if desired).

## Local preview

After uploading the project files, run `python -m http.server 8000` from the repository root and open `http://localhost:8000`. Internet access is needed for Three.js CDN dependencies.

## Status

Repository initialized. The website and binary assets must be uploaded before the preview can run. The scene is a geometric prototype, not a final production asset pack. Live WebGL performance has not been validated.
