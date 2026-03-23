# Production Workflow: *How the Human Brain Works*

## A) Concise Production Plan

1. **Lock style before page generation**
   - Use one **global style prompt** + one **anti-drift negative prompt** for every page.
   - Keep camera language, palette, rendering cues, and finish constraints constant.

2. **Prepare page package**
   - For each page, define: learning objective, scene description, age-friendly metaphor, text overlay zone, and composition notes.
   - Keep a consistent trim/safe-area strategy for print.

3. **Generate in controlled batches**
   - Start with 5-page pilot batch.
   - Produce 2–4 candidates per page.

4. **Run watercolor QA rubric**
   - Score each candidate using a strict style checklist.
   - Reject any page with vector/flat/glossy drift.

5. **Repair drift immediately**
   - Rewrite prompt using stronger material cues (paper grain, pigment bleed, soft edge control, wash layering) and stronger exclusions.
   - Regenerate only failed pages.

6. **Approve and normalize final pages**
   - Ensure tonal/palette continuity across spread sequence.
   - Verify text legibility zones and whitespace consistency.

7. **Assemble print-ready PDF**
   - Export each approved page to final dimensions.
   - Place pages in order with bleed/safe margins.
   - Output PDF/X-ready print file + screen preview PDF.

---

## B) Reusable Global Style Prompt

Use this block at the top of **every** page prompt:

> **Global style anchor:**
> Soft hand-painted watercolor children’s storybook illustration, traditional picture-book warmth, visible cold-press watercolor paper texture, gentle pigment variation, translucent layered washes, subtle watercolor blooms/backruns, soft feathered edges, organic brush irregularities, delicate granulation, calm poetic educational tone, child-friendly and emotionally warm, elegant composition with generous breathing room, balanced storytelling detail and simplicity, consistent character design and color harmony across the full book, print-illustration quality.

---

## C) Reusable Negative Prompt / Anti-Drift Prompt

Append this block to **every** page prompt:

> **Anti-drift constraints (must avoid):**
> No vector art, no flat infographic style, no geometric icon style, no crisp hard-line cel shading, no glossy 3D render, no plastic or toy-like characters, no posterized gradients, no stock illustration look, no photoreal collage, no metallic shine, no neon UI overlays, no sterile white-background explainer graphic, no hyper-saturated digital airbrush finish, no comic ink outlines dominating watercolor, no sharp-edged clipping-mask look, no text baked into image unless explicitly requested.

> **Material enforcement:**
> Preserve visible watercolor paper grain and analog paint behavior in all regions (foreground, midground, background); keep edges soft-to-lost where appropriate; maintain natural pigment pooling and wash transitions.

---

## D) Page Prompt Template

Copy/paste and fill per page:

```text
[GLOBAL STYLE ANCHOR — paste section B verbatim]

Book: “How the Human Brain Works”
Page: [##]
Learning focus: [single concept for this page]
Narrative beat: [what happens in this scene]
Audience level: general audience, child-friendly explanation

Scene description:
- Setting: [where]
- Characters: [who, recurring design notes]
- Action: [what they are doing]
- Brain concept visual metaphor: [e.g., neuron forest, memory library, message bridges]

Composition:
- Orientation: [portrait/landscape]
- Framing: [wide / medium / close]
- Focal point: [primary visual subject]
- Reserved text area: [top/bottom/left/right + approx. % whitespace]
- Keep generous whitespace and uncluttered reading flow.

Color direction:
- Primary palette: [soft warm palette]
- Accent palette: [limited accent tones]
- Lighting mood: [gentle morning / cozy interior / twilight calm]

Watercolor execution cues:
- Visible cold-press paper texture
- Layered translucent washes
- Soft feathered edges and occasional lost edges
- Subtle blooms/backruns and pigment granulation
- Hand-painted irregular brush behavior

Output intent:
- Storybook illustration, print-ready clarity, no embedded typography (unless specified).

[ANTI-DRIFT CONSTRAINTS — paste section C verbatim]
```

---

## E) QA Rubric: Reject Pages That Are Not Watercolor Enough

Score each criterion **0/1/2** (0 = fail, 1 = mixed, 2 = strong). Pass threshold: **16/20 minimum** with no hard-fail triggers.

1. **Paper texture visibility** (cold-press grain clearly present)
2. **Wash behavior** (layered translucent watercolor, not flat fills)
3. **Edge quality** (mostly soft/organic edges, limited hard edges)
4. **Pigment variation** (natural pooling/granulation, non-uniform color)
5. **Analog feel** (hand-painted imperfections, not algorithmically clean)
6. **Style consistency** with prior approved pages
7. **Warm picture-book tone** (gentle, inviting, child-friendly)
8. **Composition & whitespace** (clear focal point + readable text zone)
9. **Concept clarity** (brain idea understandable through metaphor)
10. **Print suitability** (no artifacts, no muddy over-detail)

### Hard-fail triggers (automatic reject)
- Any vector/infographic appearance.
- Glossy 3D/plastic character rendering.
- Posterized or overly crisp digital shading.
- Missing watercolor paper texture.
- Inconsistent character/style model versus approved pages.

### Drift repair protocol
When a page fails:
1. Increase material language weight: “visible paper grain in all planes,” “translucent wash layering,” “soft feathered edges.”
2. Strengthen exclusions: explicitly repeat “no vector, no flat infographic, no glossy 3D.”
3. Simplify scene complexity if rendering turns graphic.
4. Regenerate 2–4 variants and re-score.

---

## F) Five Test Page Prompts (Pilot Batch)

## Test Page 1 — “The Brain as the Captain of the Body”

```text
Soft hand-painted watercolor children’s storybook illustration, traditional picture-book warmth, visible cold-press watercolor paper texture, gentle pigment variation, translucent layered washes, subtle watercolor blooms/backruns, soft feathered edges, organic brush irregularities, delicate granulation, calm poetic educational tone, child-friendly and emotionally warm, elegant composition with generous breathing room, balanced storytelling detail and simplicity, consistent character design and color harmony across the full book, print-illustration quality.

Book: “How the Human Brain Works”
Page: 1
Learning focus: The brain is the body’s control center.
Narrative beat: A curious child imagines the brain as a kind captain guiding the body-ship.
Audience level: general audience, child-friendly explanation

Scene description:
- Setting: Cozy bedroom transforming into a dreamy sea voyage scene.
- Characters: One child protagonist, a friendly anthropomorphic brain captain (gentle expression, non-cartoonish exaggeration).
- Action: The captain-brain stands near a ship wheel while subtle lines of motion connect to hands, feet, eyes, and heart symbols.
- Brain concept visual metaphor: Brain as ship captain sending guidance to the body crew.

Composition:
- Orientation: Landscape
- Framing: Medium-wide
- Focal point: Brain captain and child at ship wheel
- Reserved text area: top-right 25% soft sky wash, low detail
- Keep generous whitespace and uncluttered reading flow.

Color direction:
- Primary palette: warm peach, soft coral, dusty blue, cream
- Accent palette: muted teal and golden ochre
- Lighting mood: Gentle morning glow

Watercolor execution cues:
- Visible cold-press paper texture across entire page
- Layered translucent sky and sea washes
- Soft feathered edges around characters
- Subtle blooms near cloud and ocean wash transitions
- Hand-painted irregular brush behavior on clothing and ship wood

Output intent:
- Storybook illustration, print-ready clarity, no embedded typography.

Anti-drift constraints (must avoid): No vector art, no flat infographic style, no geometric icon style, no crisp hard-line cel shading, no glossy 3D render, no plastic or toy-like characters, no posterized gradients, no stock illustration look, no photoreal collage, no metallic shine, no neon UI overlays, no sterile white-background explainer graphic, no hyper-saturated digital airbrush finish, no comic ink outlines dominating watercolor, no sharp-edged clipping-mask look, no text baked into image.
Material enforcement: Preserve visible watercolor paper grain and analog paint behavior in all regions (foreground, midground, background); keep edges soft-to-lost where appropriate; maintain natural pigment pooling and wash transitions.
```

## Test Page 2 — “Neurons: Tiny Messengers”

```text
Soft hand-painted watercolor children’s storybook illustration, traditional picture-book warmth, visible cold-press watercolor paper texture, gentle pigment variation, translucent layered washes, subtle watercolor blooms/backruns, soft feathered edges, organic brush irregularities, delicate granulation, calm poetic educational tone, child-friendly and emotionally warm, elegant composition with generous breathing room, balanced storytelling detail and simplicity, consistent character design and color harmony across the full book, print-illustration quality.

Book: “How the Human Brain Works”
Page: 2
Learning focus: Neurons send messages through the brain and body.
Narrative beat: The child explores a glowing forest of neuron trees passing spark-like messages.
Audience level: general audience, child-friendly explanation

Scene description:
- Setting: Dreamy “neuron forest” with branching tree-like forms.
- Characters: Child protagonist observing with wonder.
- Action: Soft glowing signals hop from branch to branch like fireflies.
- Brain concept visual metaphor: Neurons as trees linked by light pathways.

Composition:
- Orientation: Landscape
- Framing: Wide
- Focal point: Arc of glowing signal moving between two prominent neuron trees
- Reserved text area: bottom-left 20% pale wash, minimal detail
- Keep generous whitespace and uncluttered reading flow.

Color direction:
- Primary palette: lavender gray, soft indigo, warm cream
- Accent palette: tiny amber glow points
- Lighting mood: Evening calm, magical but subtle

Watercolor execution cues:
- Visible cold-press texture, especially in background washes
- Layered translucent purples and blues
- Soft edges on trees; selective sharper accents only at focal glow
- Subtle blooms around glow halos, never neon
- Hand-painted irregular branching marks

Output intent:
- Storybook illustration, print-ready clarity, no embedded typography.

Anti-drift constraints (must avoid): No vector art, no flat infographic style, no geometric icon style, no crisp hard-line cel shading, no glossy 3D render, no plastic or toy-like characters, no posterized gradients, no stock illustration look, no photoreal collage, no metallic shine, no neon UI overlays, no sterile white-background explainer graphic, no hyper-saturated digital airbrush finish, no comic ink outlines dominating watercolor, no sharp-edged clipping-mask look, no text baked into image.
Material enforcement: Preserve visible watercolor paper grain and analog paint behavior in all regions (foreground, midground, background); keep edges soft-to-lost where appropriate; maintain natural pigment pooling and wash transitions.
```

## Test Page 3 — “Senses Bring News to the Brain”

```text
Soft hand-painted watercolor children’s storybook illustration, traditional picture-book warmth, visible cold-press watercolor paper texture, gentle pigment variation, translucent layered washes, subtle watercolor blooms/backruns, soft feathered edges, organic brush irregularities, delicate granulation, calm poetic educational tone, child-friendly and emotionally warm, elegant composition with generous breathing room, balanced storytelling detail and simplicity, consistent character design and color harmony across the full book, print-illustration quality.

Book: “How the Human Brain Works”
Page: 3
Learning focus: Eyes, ears, nose, tongue, and skin send information to the brain.
Narrative beat: The child receives “mail” from five sensory helpers.
Audience level: general audience, child-friendly explanation

Scene description:
- Setting: Whimsical town-square scene with five gentle sensory characters delivering envelopes.
- Characters: Child protagonist + five sensory messengers (subtle symbolic styling).
- Action: Messengers pass pastel envelopes toward a central brain-shaped mailbox.
- Brain concept visual metaphor: Senses as couriers sending updates.

Composition:
- Orientation: Landscape
- Framing: Medium-wide
- Focal point: Brain-shaped mailbox with incoming envelopes
- Reserved text area: upper-left 25% pale sky wash
- Keep generous whitespace and uncluttered reading flow.

Color direction:
- Primary palette: blush pink, warm beige, soft sky blue
- Accent palette: muted mint and apricot
- Lighting mood: Bright but gentle midday

Watercolor execution cues:
- Clear paper grain visible in open sky and ground
- Layered washes with slight value variation in each color family
- Soft, hand-painted contours with minimal hard outlining
- Occasional blooms in mailbox shadow and sky transitions
- Brushstroke irregularity visible on architecture and clothing

Output intent:
- Storybook illustration, print-ready clarity, no embedded typography.

Anti-drift constraints (must avoid): No vector art, no flat infographic style, no geometric icon style, no crisp hard-line cel shading, no glossy 3D render, no plastic or toy-like characters, no posterized gradients, no stock illustration look, no photoreal collage, no metallic shine, no neon UI overlays, no sterile white-background explainer graphic, no hyper-saturated digital airbrush finish, no comic ink outlines dominating watercolor, no sharp-edged clipping-mask look, no text baked into image.
Material enforcement: Preserve visible watercolor paper grain and analog paint behavior in all regions (foreground, midground, background); keep edges soft-to-lost where appropriate; maintain natural pigment pooling and wash transitions.
```

## Test Page 4 — “Memory Library”

```text
Soft hand-painted watercolor children’s storybook illustration, traditional picture-book warmth, visible cold-press watercolor paper texture, gentle pigment variation, translucent layered washes, subtle watercolor blooms/backruns, soft feathered edges, organic brush irregularities, delicate granulation, calm poetic educational tone, child-friendly and emotionally warm, elegant composition with generous breathing room, balanced storytelling detail and simplicity, consistent character design and color harmony across the full book, print-illustration quality.

Book: “How the Human Brain Works”
Page: 4
Learning focus: The brain stores and organizes memories.
Narrative beat: The child walks through a cozy memory library of floating picture-books.
Audience level: general audience, child-friendly explanation

Scene description:
- Setting: Warm circular library interior with gently curving shelves.
- Characters: Child protagonist and a kind librarian-brain guide.
- Action: Small illustrated memory-books glow softly as they are shelved.
- Brain concept visual metaphor: Memories as books in a living library.

Composition:
- Orientation: Landscape
- Framing: Medium interior shot
- Focal point: Child and librarian-brain placing a memory-book on shelf
- Reserved text area: bottom-right 22% light floor wash
- Keep generous whitespace and uncluttered reading flow.

Color direction:
- Primary palette: warm sienna, rose beige, cream, muted blue-gray
- Accent palette: soft gold highlights on memory-books
- Lighting mood: Cozy indoor lamplight

Watercolor execution cues:
- Visible textured paper in wall and floor washes
- Layered warm washes for depth, no flat fills
- Soft, diffuse edges on shelves and books
- Subtle blooms around lamp glow and shelf corners
- Handmade brush irregularity in circular architecture

Output intent:
- Storybook illustration, print-ready clarity, no embedded typography.

Anti-drift constraints (must avoid): No vector art, no flat infographic style, no geometric icon style, no crisp hard-line cel shading, no glossy 3D render, no plastic or toy-like characters, no posterized gradients, no stock illustration look, no photoreal collage, no metallic shine, no neon UI overlays, no sterile white-background explainer graphic, no hyper-saturated digital airbrush finish, no comic ink outlines dominating watercolor, no sharp-edged clipping-mask look, no text baked into image.
Material enforcement: Preserve visible watercolor paper grain and analog paint behavior in all regions (foreground, midground, background); keep edges soft-to-lost where appropriate; maintain natural pigment pooling and wash transitions.
```

## Test Page 5 — “Practice Makes Pathways Stronger”

```text
Soft hand-painted watercolor children’s storybook illustration, traditional picture-book warmth, visible cold-press watercolor paper texture, gentle pigment variation, translucent layered washes, subtle watercolor blooms/backruns, soft feathered edges, organic brush irregularities, delicate granulation, calm poetic educational tone, child-friendly and emotionally warm, elegant composition with generous breathing room, balanced storytelling detail and simplicity, consistent character design and color harmony across the full book, print-illustration quality.

Book: “How the Human Brain Works”
Page: 5
Learning focus: Repetition strengthens brain pathways (learning and habit).
Narrative beat: The child practices tying shoes while glowing path-bridges become brighter and steadier.
Audience level: general audience, child-friendly explanation

Scene description:
- Setting: Home doorway and garden path transitioning into a symbolic bridge network.
- Characters: Child protagonist, supportive caregiver in background.
- Action: Each practice attempt adds another soft painted layer to a bridge path.
- Brain concept visual metaphor: Repeated practice reinforcing bridges between islands.

Composition:
- Orientation: Landscape
- Framing: Medium shot with foreground action
- Focal point: Child’s hands and strengthening painted bridge motif
- Reserved text area: top-left 20% soft sky gradient wash
- Keep generous whitespace and uncluttered reading flow.

Color direction:
- Primary palette: soft teal, peach, warm gray, cream
- Accent palette: gentle golden bridge highlights
- Lighting mood: Late-afternoon calm

Watercolor execution cues:
- Strong visible cold-press paper texture in sky and path
- Multi-layer translucent washes to show “strengthening” effect
- Soft feathered edges, minimal hard lines
- Controlled blooms in bridge glow transitions
- Hand-painted stroke variance in repeated path marks

Output intent:
- Storybook illustration, print-ready clarity, no embedded typography.

Anti-drift constraints (must avoid): No vector art, no flat infographic style, no geometric icon style, no crisp hard-line cel shading, no glossy 3D render, no plastic or toy-like characters, no posterized gradients, no stock illustration look, no photoreal collage, no metallic shine, no neon UI overlays, no sterile white-background explainer graphic, no hyper-saturated digital airbrush finish, no comic ink outlines dominating watercolor, no sharp-edged clipping-mask look, no text baked into image.
Material enforcement: Preserve visible watercolor paper grain and analog paint behavior in all regions (foreground, midground, background); keep edges soft-to-lost where appropriate; maintain natural pigment pooling and wash transitions.
```

---

## PDF Assembly Blueprint (for after full-page approval)

1. Create final page images at uniform trim size (e.g., 8.5x11 in or 10x8 in), 300 DPI, consistent color profile.
2. Keep inside-safe text margins consistent across pages.
3. Sequence files with zero-padded names (`page_01` ... `page_N`).
4. Assemble into print-ready PDF (with bleed if required by printer).
5. Export additional lightweight review PDF for digital proofing.
