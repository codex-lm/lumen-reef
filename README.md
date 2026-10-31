# Lumen Reef

A bioluminescent arcade dive about getting close to danger without losing your light. Built with Kimi for Kimi Games.

## Play

The committed `index.html` is self-contained. Serve it with any static HTTP server; no account, network service or runtime dependency is required.

```sh
python -m http.server 8080
```

Then open `http://localhost:8080`. After editing the sources, rebuild the playable entrypoint with `python build.py`.

## How to play

- Swim with **WASD**, **arrow keys**, mouse movement or touch drag.
- Collect lucioles to build your glow and your combo.
- Skim close to enemies without touching them to charge faster.
- Spend glow on a pulse with **Space** or the touch button. Pulses purify enemies and erase shadow shards.
- Purify the first two tides, choose one of three gifts after each, then defeat the Gloom Maw.
- **P** or **Escape** pauses; **M** toggles sound. **R** restarts from an ending.

English is the default language; French and Spanish are available from the menu. Sound and language preferences plus the local best score are stored in the browser when available. `?seed=12345` selects a repeatable spawning sequence. `?demo=1&seed=12345` enables an attract-mode player that uses the normal movement, pulse, health and scoring rules without cheats.

## Scope

Three tides, three regular enemy families, a two-phase boss, eight stacking gifts, combo scoring and local best scores. All visuals are drawn with original Canvas code. All sounds are synthesized with Web Audio after a player gesture.

## Files

- `src/index.template.html`, `src/styles.css`, `src/game.js`: editable game sources.
- `build.py`: standard-library build that inlines CSS and JavaScript into the playable `index.html` required by LOB7.
- `index.html`: generated, committed static export.
- `art/cover.png`: original LOB7 cover image.
- `art/render_cover.py`: editable generator for the cover; requires Pillow only when regenerating it.
- `LOB7-GAME.json`, `LOB7-ATTRIBUTION.json`: publication metadata.
- `CREDITS.md`, `LICENSE`: provenance and permissions.

## Licence

Code and original artwork are released under the MIT License. See `LICENSE` and `CREDITS.md`.
