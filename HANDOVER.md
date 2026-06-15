# Handover: 3D Exhibit Studio, ready for Olivia's real project

## What this is
A reusable Cowork studio that turns an interior design project into a web exhibit: brief, concept development, narrative, prompts, clips, assembly, deploy. Built and proven end to end on a throwaway test (Terracotta, a laneway cafe-bar for VOC08). Package is at v2.

## State
- Scaffold v2 lives at `/home/ivan/projects/3d-exhibit-studio/` (canonical). Folders: 00-brief, 01-assets, 01b-concept, 02-narrative, 03-prompts, 04-clips, 05-assembly. Plus README, WORKFLOW, REFERENCE-people-worth-knowing, CHANGELOG.
- Cowork project "3D Exhibit Studio" exists but was created start-from-scratch, so it points at an empty Documents folder. Recreate it with "Use an existing folder" pointed at the canonical path above. Instructions block is set; memory on.
- Connectors: Higgsfield MCP connects fine (custom connector, mcp.higgsfield.ai/mcp, account auth). Netlify does NOT deploy from Cowork; deploy from a terminal.

## The Terracotta build was a test
It used placeholder test footage and an invented concept. Do not reuse it. Olivia's real submission starts fresh: her own brief, her own concept, her own clips.

## Next session: run Olivia's real project
1. Confirm her actual VOC08 brief (or whichever unit) and a real deadline. Fill 00-brief from the template.
2. Run the workflow from stage 1, all stages, do not skip brief or narrative; that is the point of using the studio.
3. Stage 1b concept development is mandatory: form study, hero materials board, section sketch. This is what the assessor marks for.
4. Generate stills and clips from 03-prompts/PROMPT-LIBRARY.md. Higgsfield credits may be out; Google Gemini is the fallback for stills, same prompts.
5. Assemble with 05-assembly/index.template.html (leads with concept statement, then origin-to-render row, then scenes). Deploy per 05-assembly/DEPLOY-GUIDE.md.

## Rules learned the hard way
- Cowork cannot write chat images to disk. Save generated images yourself and drop them into the deploy folder's `drawings/`.
- Files must sit inside the deploy root (the folder with index.html). Anything one level up does not ship.
- Deploy via terminal: `cd` into the project folder, `netlify deploy --prod`. Share the production URL ([site].netlify.app), not the hashed preview URL.
- Keep drawings consistent (a section showing a mezzanine must match the plan).
- Crop AI watermarks before shipping.
- Present fullscreen: Mac uses Control+Command+F or `open -a "Google Chrome" --args --kiosk "[url]"`. F11 is Windows only.

## Open judgement calls
- This is Olivia's coursework. Keep the design decisions hers; check the school's AI policy so the exhibit is defensible as her work.
- Watch credit and time budget before a real deadline; generation plus re-rolls take hours.
