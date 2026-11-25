# RAWNAK EVENTS — A Lifetime of Moments

V3: a cinematic, English-language editorial website with nine scroll-driven life chapters. The live site defaults to Story Mode when final footage is unavailable, rather than showing the low-poly blockout.

## Add cinematic footage

Upload silent H.264 MP4 files to `assets/films/`. The existing manifest lists the nine filenames. Start with `first-hello.mp4`; remaining chapters stay in Story Mode until their videos are available. The browser checks each file and seeks through the paused clip as visitors scroll. For smooth scrubbing encode with frequent keyframes, fast-start metadata, 24–30 fps and web-sized bitrate. No music or embedded text.

## Local preview

Run `python -m http.server 8000` from the repository root and open localhost:8000.

## Previous version

The original WebGL experience is retained at `archive/webgl-v2.html`. Its GLB model and camera files remain untouched. The current symbol is an interim floral mark, not the original production logo. Contact brief is copied locally; no booking is sent. Final video footage is not included yet.
