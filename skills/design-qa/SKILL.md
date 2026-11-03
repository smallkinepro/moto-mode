---
name: design-qa
description: >-
  Visual QA of a web or app UI at desktop and phone widths: hierarchy, one
  primary action, type and spacing scale, contrast, cropping, states, and
  accessibility basics, with an annotated handoff. Use before UI goes to
  build or before a design is called ready.
license: MIT
metadata:
  phase: "5-verify"
  layer: L1
---
# Design QA

Check at 1440px and 390px wide. Take screenshots of both; attach them to the handoff.

## Checklist
1. **Hierarchy.** One clear primary action above the fold. Headings read as an outline.
2. **Type and spacing.** Sizes and gaps come from the design scale; no one-off values.
3. **Contrast.** Text meets WCAG AA (4.5:1 body, 3:1 large). Check text over images.
4. **Cropping.** Hero and card images don't clip faces, text, or key subjects at either width.
5. **States.** Hover, focus, disabled, loading, empty, and error states exist for interactive parts.
6. **Accessibility basics.** Visible focus ring, alt text on meaningful images, labels on inputs, tap targets at least 44px.
7. **Content.** No lorem ipsum or placeholder prices unless marked placeholder.
8. **Brand rules.** Any locked colors, logos, or banned motifs are respected.

## Handoff
List each section or component, what is final vs placeholder, and every failed item with a screenshot.

## Out of scope
Deploy and infrastructure (use `ship-verify`), game art.
