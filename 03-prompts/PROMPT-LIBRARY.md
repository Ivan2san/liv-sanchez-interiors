# Prompt Library

Reusable Higgsfield prompt patterns for 3D design exhibits. Fill the Style Lock once per project, then paste it into every scene prompt so all your clips look like one cohesive piece.

---

## Style Lock (fill once per project)

Edit these for your project, then drop this exact block into every prompt below.

```
STYLE LOCK
Lighting: soft even studio lighting, subtle ambient occlusion, gentle contact shadows
Background: pure white seamless, no horizon line, #FFFFFF
Materials: [your materials, for example oak timber, matte ceramic, woven fabric, brushed metal]
Mood: [your three or four words]
Quality: photorealistic 3D render, architectural visualisation quality, 4K, cinematic
```

---

## Shot 1: Orbital pan

Best for showing a single space or a hero furniture piece. Reliable and clean.

```
Slow smooth orbital camera pan around [the space or object], rotating [180 / 360] degrees
on a single horizontal axis at constant speed. Centred composition, subject stays framed
throughout the rotation. Shallow depth of field, gentle bokeh on background elements.

[paste STYLE LOCK here]

No text, no people, no camera shake, no warping.
```

**Tips:** A 180 degree sweep is cleaner and cheaper than a full 360. If Higgsfield offers an Orbit motion preset, select it as well as writing the cue.

---

## Shot 2: Exploded view

Best for revealing interiors and showing how spaces fit together. Harder, needs more re-rolls.

```
Architectural exploded-view animation of [the building or room], layers separating slowly
and evenly in a controlled choreographed sequence. [Roof lifts, walls slide outward, floors
fan apart] to reveal the styled interior. Components stay evenly spaced and fully contained
within the frame at all times, generous margins around the structure, nothing leaves the canvas.
Slow steady motion, parts drift apart then settle. Centred, slight three-quarter angle.

[paste STYLE LOCK here]

No text, no people, no camera shake, no warping.
```

**Tips:** The word "explode" makes the model want speed and destruction, so always pair it with "slow, controlled, choreographed". A single-floor cut-away holds together far better than a whole multi-storey building. If Higgsfield offers start frame and end frame control, set the intact structure as the start and the separated layers as the end; that keeps it in bounds far better than text alone.

---

## Shot 3: Walkthrough

Best for giving a sense of moving through a space. Use sparingly; it drifts more than a pan.

```
Smooth cinematic walkthrough moving slowly forward through [the space], steady gliding camera
at eye level, gentle reveal of [the next area or feature]. Stable horizon, no sudden turns,
constant slow speed. Shallow depth of field.

[paste STYLE LOCK here]

No text, no people, no camera shake, no warping.
```

**Tips:** Keep the path simple and straight. Curves and turns are where walkthroughs warp. One reveal per clip.

---

## Negative cues (the "no" list)

These earn their place on white-background renders, where warping is the usual failure:

`no text, no people, no camera shake, no warping, no morphing, no flickering, no distortion`

---

## Higgsfield notes

- **Clip length:** keep every clip to 3 to 5 seconds. Longer clips drift and degrade.
- **Presets over words:** if a motion preset matches your shot (Orbit, Dolly), select it as well as writing the cue. The preset enforces the camera path far more reliably than text.
- **Start and end frames:** if available, use them for exploded views and any motion that needs to stay in bounds.
- **Credits:** every generation costs credits, including ones run through the MCP. Lock your prompt before generating. Re-rolls add up fast on explodes and 360s.
- **One motion at a time:** do not combine a camera orbit with an exploding scene in one clip. Two motions multiply the chance of warping. Get one clean first.
