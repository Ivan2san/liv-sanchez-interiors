# Workflow

Follow these six stages in order for each project. Each stage tells you what to do and what to ask Cowork.

---

## Stage 1: Brief

**You:** Copy `00-brief/PROJECT-BRIEF.template.md` to a new file named after your project (for example `PROJECT-BRIEF-cafe-fitout.md`). Fill in what you can.

**Ask Cowork:** "Read my brief and my assets, then tell me back what you understand the design concept to be. Flag anything that is unclear."

**Done when:** Cowork can describe your concept correctly in its own words, and the deadline is real (check it, a generated brief can put today's date in).

---

## Stage 2: Assets

**You:** Drop everything you have into `01-assets/`. Floor plans, elevations, renders, mood boards, material samples, hand sketches, concept notes. Photos of physical models are fine too.

**Ask Cowork:** "Go through my assets and list the spaces and key design moments worth showing as 3D scenes."

**Done when:** You have a shortlist of spaces and moments to build scenes around.

---

## Stage 3: Narrative

**You:** Copy `02-narrative/EXHIBIT-NARRATIVE.template.md` to a new file for this project.

**Ask Cowork:** "Help me turn my shortlist into a scene-by-scene story arc. Suggest the order, the shot type for each scene, and what each scene should communicate. Fill in the narrative table."

**Before the scenes, do concept development (stage 1b, folder `01b-concept/`).** Produce a form study, a hero materials board, and a massing or section sketch. This is the thinking an assessor marks for and the antidote to a styled-but-empty exhibit. These lead the final page, above the drawings.

**Ground each scene in a design idea, not just a nice shot.** Open `REFERENCE-people-worth-knowing.md` and tie each scene to a principle: Ching for why a layout reads well, Zumthor or Marion Hall Best for light, Scarpa for where new work meets old fabric in a renovation. The reference is a compass; return to a name when a scene needs one.

**Ask Cowork:** "For each scene, what design idea is it actually demonstrating? Push me if a scene is only decorative."

**Done when:** You have an ordered scene list, each with a shot type (pan, exploded view, or walkthrough) and a one-line purpose, and each scene is making a design point, not just looking good. Aim for 4 to 7 scenes for a tight exhibit.

---

## Stage 4: Prompts

**You:** Open `03-prompts/PROMPT-LIBRARY.md`. Fill in the Style Lock block once for this project (lighting, materials, background, mood). This keeps every clip looking like one cohesive exhibit.

**Ask Cowork:** "Using the prompt library and my Style Lock, write a Higgsfield prompt for each scene in my narrative. Match the shot type."

**Done when:** Every scene has a finished prompt with the Style Lock baked in.

---

## Stage 5: Clips

**Ask Cowork:** "Generate scene 1 through the Higgsfield MCP. Use a 3 to 5 second clip." Review it together, then move on or re-roll.

**Rules of thumb:**
- Generate one scene at a time. Lock the prompt before you spend credits.
- Keep clips to 3 to 5 seconds. Longer clips drift and warp.
- Exploded views and full 360 pans need more re-rolls. Budget for failure.
- Save keepers into `04-clips/` with the scene number in the filename (for example `scene-02-explode.mp4`).

**Done when:** You have one clean clip per scene.

---

## Stage 6: Assembly

**Substance check before you assemble.** Read "The two traps" in `REFERENCE-people-worth-knowing.md`. Trap 1 is the stylist with hero shots and no buildable thinking behind them, and a slick AI render exhibit is exactly how you fall into it without noticing. Before assembling, ask yourself: for each scene, can I point to the plan, the section, the materials or the detail behind it? If a clip is pure vibe with nothing underneath, either add the design substance or cut it. The renders are how you show the thinking, not a replacement for it.

**Decide the format first:**

- **Slides** (default, simplest): Cowork drives the PowerPoint agent. Faster, you control it all.
  - **Ask Cowork:** "Assemble my clips into a slide deck, one scene per slide, in narrative order."

- **Web exhibit** (a shareable link that plays the videos): a hosted page, better for a portfolio. It is more setup, and remember a web page cannot become a working PDF (the videos freeze), so this is for sharing as a link, not as a document. Everything you need is in `05-assembly/`: `index.template.html` and `DEPLOY-CHECKLIST.md`. Follow the checklist. In short:
  - Copy the template to `index.html`, make a `clips/` folder, copy in your keeper clips renamed `scene-01.mp4` and so on.
  - **Ask Cowork:** "Fill in index.html from my narrative and my clips, one scene per section."
  - **Ask Cowork:** "Compress these clips for web, then deploy this folder to Netlify and give me the URL." (Needs the Netlify MCP connected; see the checklist.)

**Then, either path, ask Cowork:** "Draft speaker notes I can present from."

**Done when:** You have the final exhibit (deck or live link) plus speaker notes in `05-assembly/`, and you have rehearsed it once out loud.

---

## Quick troubleshooting

- **Clips look like different projects:** your Style Lock is not consistent. Re-check it is pasted into every prompt.
- **Furniture melts or warps mid-motion:** shorten the clip, slow the camera, or simplify the scene (single floor instead of whole house).
- **Parts fly out of frame in an exploded view:** add "generous margins, fully contained within the frame, slow controlled separation" and start more zoomed out.
- **Credits draining fast:** prefer 180 degree pans over 360, and single-floor cut-aways over full-house explodes.
