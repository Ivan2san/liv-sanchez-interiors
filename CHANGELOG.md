# Studio v2: what changed and why

Folded in from the first real build (Terracotta, VOC08).

## New
- Stage 1b, concept development (`01b-concept/`): form study, hero materials board, massing/section sketch. The thinking an assessor marks for; the substance check made tangible.
- `05-assembly/DEPLOY-GUIDE.md`: the deploy reality (Netlify from a terminal, not Cowork; files inside the deploy root; production vs preview URL; kiosk presentation).
- Prompt library now has Nano Banana Pro image templates and a Google Gemini fallback for when Higgsfield credits run out.

## Changed
- Final HTML template now leads with a concept statement and an origin-to-render row, so the page tells the argument, not just shows the room. Storytelling is built in, not bolted on.
- Materials board is a hero composition (samples with depth and shadow), not a flat swatch grid.
- Brief stage now checks the deadline is real.

## Lessons that became rules
- Create the Cowork project with "Use an existing folder", never start-from-scratch, or it points at an empty folder.
- Cowork cannot write chat images to disk; save and drop them in yourself, into the deploy folder's drawings/.
- Netlify MCP needs the local CLI, so deploy via terminal or Claude Code, not Cowork.
- Keep drawings consistent across the set (a section showing a mezzanine must match the plan).
- Crop AI watermarks before shipping.
