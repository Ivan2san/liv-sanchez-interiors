# 3D Exhibit Studio

A workspace for turning a design project into a dynamic 3D video exhibit, using Cowork to plan and Higgsfield to generate the clips.

## What this is

You drop a design project in here (floor plans, renders, mood boards, your concept notes). Cowork reads it, helps you shape it into a scene-by-scene story, writes the Higgsfield prompts for each scene, generates the clips, and assembles the final presentation. You stay the designer; the tools just visualise and assemble.

## How to use it with Cowork

1. Open this whole folder as a project in Cowork.
2. Tell Cowork: "Read the README and WORKFLOW, then walk me through stage 1 for my new project."
3. Work through the six stages in order. Cowork uses the templates and the prompt library in here as it goes.

Connect the Higgsfield MCP in your Cowork settings first (authenticate with your Higgsfield account, no API keys needed). That lets Cowork generate clips without you leaving the workflow.

## The six stages

1. **Brief** (`00-brief/`) - capture what the project is and what each scene should say.
2. **Assets** (`01-assets/`) - drop your plans, renders, mood boards, notes.
3. **Narrative** (`02-narrative/`) - shape the scene-by-scene story arc.
4. **Prompts** (`03-prompts/`) - the reusable Higgsfield prompt patterns; Cowork fills these per scene.
5. **Clips** (`04-clips/`) - generated videos land here; keep the good ones, re-roll the rest.
6. **Assembly** (`05-assembly/`) - the final deck or web exhibit, plus speaker notes.

## Folder map

```
3d-exhibit-studio/
  README.md                          you are here
  WORKFLOW.md                        step-by-step you follow for each project
  REFERENCE-people-worth-knowing.md  the designers and studios worth knowing
  00-brief/                          PROJECT-BRIEF template, one copy per project
  01-assets/                         your source material goes here
  02-narrative/                      EXHIBIT-NARRATIVE template, your scene plan
  03-prompts/                        PROMPT-LIBRARY, the reusable Higgsfield patterns
  04-clips/                          generated videos
  05-assembly/                       final presentation and speaker notes
```

## One rule worth keeping

The design concepts are yours. Higgsfield is a visualisation tool, not the designer. Keep authoring the story and the design decisions yourself, and check your course's AI policy so the exhibit is clearly your work. A slick render with no plan, section or detail behind it is just styling; `REFERENCE-people-worth-knowing.md` calls that the first trap. The renders are how you show your thinking, not a substitute for it.
