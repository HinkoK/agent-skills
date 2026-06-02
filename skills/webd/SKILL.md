---
name: webd
description: "Web design workflow for landing pages, SaaS frontends, conversion-oriented pages, and non-generic UI. Use when building or improving a website, landing page, SaaS UI, hero section, pricing page, conversion funnel, shadcn/ui interface, or when the user invokes /webd or @webd."
version: 1.0.0
author: HinkoK
license: MIT
platforms: [linux, macos, windows]
tags: [web-design, frontend, landing-pages, saas, conversion, shadcn, ui, ux]
---

# webd 🎨

Curated web design resources for building professional landing pages with shadcn/ui-based libraries.

## When to Use

- User asks for UI component libraries or design resources
- Building landing pages that need to look professional
- Looking for alternatives to "vibe coded" designs
- Need specific components (hero sections, pricing, testimonials)
- Want animation libraries or icon sets
- Creating distinctive, non-generic frontend interfaces
- Need design direction before starting to code

## Core Resources

- **[Design Framework](references/design-framework.md)** - Establish aesthetic direction BEFORE coding
- **[Conversion Patterns](references/conversion-patterns.md)** - Landing page optimization from Landing Pages Explained
- **[UI Libraries](references/ui-libraries.md)** - 17+ shadcn/ui-based component libraries

## Quick Categories

### For Marketing Pages
- **MVP Blocks** - Animated sections with Framer Motion
- **Magic UI** - 50+ animated components (used by Vercel/Stripe)
- **Luxe UI** - Premium testimonials, features, CTAs

### For Animations
- **Aceternity UI** - Crazy 3D effects
- **Motion Primitives** - Animation building blocks
- **Smooth UI** - Buttery hover effects

### For Clean/Minimal
- **Origin UI** - Consistent design language
- **Cult UI** - Minimal but powerful
- **Tailark** - Clean startup aesthetic

### For Unique Elements
- **Skipper UI** - Components you won't find elsewhere
- **Phosphor Icons** - 9000+ alternative to Lucide
- **PatternCraft** - Background patterns and textures

## Recommendations by Use Case

| Goal | Top Pick | Runner Up |
|------|----------|-----------|
| Launch fast | Bundui | MVP Blocks |
| Look premium | Luxe UI | Aceternity UI |
| SaaS dashboard | Cult UI | Origin UI |
| Stand out | Skipper UI | Kokonut UI |
| Heavy animations | Aceternity UI | Magic UI |

## Workflow

### Option 1: Component-First (Quick)
1. Identify the landing page goal (conversion, showcase, app)
2. Pick 1-2 primary libraries matching the aesthetic
3. Supplement with specific needs (icons from Phosphor, backgrounds from PatternCraft)
4. Keep it consistent - don't mix too many design languages

### Option 2: Design-First (Distinctive)
1. **Read [design-framework.md](references/design-framework.md)** for full process
2. Define context (purpose, audience, brand)
3. Choose aesthetic direction (brutalist, luxury, playful, etc.)
4. Establish typography, colors, motion strategy
5. Match UI libraries to aesthetic (see framework guide)
6. Code with intentional design choices (avoid generic patterns)

**Use Option 2 when:**
- The design needs to stand out from generic AI sites
- Building a brand identity through UI
- Client wants something distinctive
- You have time to think about design properly

### Option 3: Conversion-First (Marketing)
1. **Read [conversion-patterns.md](references/conversion-patterns.md)** for full patterns
2. Start with clarity: one clear value proposition
3. Show the product (demo, screenshot, video)
4. Build trust (social proof + transparency)
5. Remove friction (simple forms, clear pricing)
6. Optimize for speed (Core Web Vitals)
7. Test everything (headlines, CTAs, visuals)

**Use Option 3 when:**
- Conversion rate is the primary metric
- Building SaaS, course, or product landing pages
- Need to optimize existing page performance
- Marketing/growth-focused project

## Hermes usage rules

- Trigger on `/webd`, `@webd`, landing pages, SaaS frontend work, UI redesigns, conversion optimization, and requests to avoid generic AI/vibe-coded design.
- Default to **Design-First** when the user wants something distinctive.
- Default to **Conversion-First** when the user mentions sales, funnels, pricing, signup, launch, creator offers, or landing-page performance.
- Default to **Component-First** when the user wants a fast implementation or asks for UI libraries/components.
- Before coding, choose one clear aesthetic direction and 1-2 UI libraries; do not mix many visual systems.
- Use the linked references directly when needed:
  - `references/design-framework.md`
  - `references/conversion-patterns.md`
  - `references/ui-libraries.md`
