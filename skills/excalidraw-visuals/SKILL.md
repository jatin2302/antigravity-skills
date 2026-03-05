---
name: excalidraw-visuals
description: Use when someone asks for a hand-drawn visual, PNG image, rendered diagram, visual explanation, or says "excalidraw image" or "excalidraw visual". This generates PNG images, not editable files.
---

# Excalidraw Visuals Skill

Generate hand-drawn Excalidraw-style PNG diagrams using AI. Describe the concept, and the agent builds a structured prompt with a locked style to ensure consistency.

## Prerequisites

1.  **API Key**: Sign up at [kie.ai](https://kie.ai) and add `KIE_AI_API_KEY` to your `.env`.
2.  **Node.js**: Version 18+ required.
3.  **Assets**: Ensure the style reference image exists at `resources/excalidraw-style-reference.png`.

## Style Specification (LOCKED)

This exact text is prepended to EVERY prompt to ensure a consistent, premium hand-drawn look.

```text
Excalidraw-style hand-drawn diagram on a clean white background. All text uses neat, consistent architect-style handwriting -- legible, slightly rounded letters with medium stroke weight. Letter sizes are uniform within each label. Titles are bold and larger. Body labels are smaller but equally neat. This is NOT sloppy handwriting -- it looks like a designer wrote it carefully with a thick marker.

Shapes are rounded rectangles with a 2-3px dark gray (#495057) hand-drawn outline and soft pastel fills. Lines and arrows are slightly wobbly and hand-drawn, not ruler-straight. Arrowheads are simple triangles. Nothing is pixel-perfect -- everything has a natural, sketched feel with visible stroke texture.

Color palette: soft blue (#a5d8ff), warm yellow (#ffec99), soft green (#b2f2bb), coral (#ffa8a8), light purple (#d0bfff). All text is dark charcoal (#343a40). All lines and arrows are dark gray (#495057). Background is always clean white.

People are simple stick figures with round heads, no facial features. AI agents/robots have a round head with two dot eyes and a small antenna. Documents have a folded corner. Gears represent automation. All icons are simple line drawings, not detailed or cartoonish.

Layout is clean and spacious with generous whitespace. Visual hierarchy is clear -- title is largest, labels are short (max 3 words each). The overall feel is educational, friendly, and slightly more polished than basic Excalidraw -- colored fills, intentional spacing, consistent sizing, and meaningful color coding elevate it.

Do NOT include: realistic photos, gradients, drop shadows, 3D effects, corporate clip art, stock imagery, dark backgrounds, heavy borders.
```

## Layout Templates

| Template | Best For |
| :--- | :--- |
| **Left-to-Right Flow** | Processes, sequences, transformations |
| **Hub and Spoke** | Capabilities, features around a central concept |
| **Top-to-Bottom Hierarchy** | Levels, layers, progressive depth |
| **Side-by-Side Comparison** | Before/after, old vs new, option A vs B |
| **Numbered Steps List** | Frameworks, checklists, ordered instructions |
| **Cycle / Loop** | Feedback loops, iterative processes |

## Execution Protocol

### 1. Plan the Text (Minimize)
*   **Titles**: Max 5 words.
*   **Labels**: Max 3 words (prefer 1-2).
*   **Annotations**: Max 4 words.
*   **Total**: Target < 30 words (Max 50).
*   **Spelling**: Flag words > 8 chars. Use abbreviations (API, DB, UI).

### 2. Build the Prompt
```text
[STYLE PREFIX]
STYLE REFERENCE: Match the visual style of the reference image exactly -- same font, same shapes, same colors, same level of polish.

Diagram concept: [TITLE]
Layout: [TEMPLATE NAME]
Elements: [List with colors & labels]
Connections: [Directional arrows]
```

### 3. Generate
Call the script with the style reference:
```bash
node scripts/generate-visual.js "<PROMPT>" "outputs/[filename].png" "16:9" --input "resources/excalidraw-style-reference.png"
```

## File Structure

| Asset | Path |
| :--- | :--- |
| Instructions | `SKILL.md` |
| Style Reference | `resources/excalidraw-style-reference.png` |
| Generation Script | `scripts/generate-visual.js` |
