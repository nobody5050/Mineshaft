# Contribution rules
- Using git is preferred over GitHub web/Gitlab WebIDE.
- Describe what you changed in the commits: no stupid commits like "Update README.md"
# Structure information
One of the core ideas of Mineshaft, is the replaceable modules.
You can replace any piece of the Mineshaft modules with your own.Think of Mineshaft as a puzzle where you can replace pieces with different ones.
The "puzzle" is split into these directories:
- `core` is core components and classes
- `render` is the rendering engine. The rendering engine manages how does the game get displayed. it also manages shading.
- `gen` is the world generation engine.
- `assets` are the assets like music, sounds, textures, and other stuff.
