# Frontend Design Framework

Inspired by Anthropic's Frontend Design plugin - establish a design direction BEFORE coding.

## Design Process (Before Writing Code!)

### 1. Identify Context
- **Purpose:** What is this interface for? (dashboard, landing, app, marketing)
- **Audience:** Who's using it? (devs, consumers, enterprise, creative)
- **Brand:** What feeling should it evoke? (trust, playfulness, luxury, speed)

### 2. Choose Aesthetic Direction

Pick ONE primary direction. Don't try to blend too many.

#### Brutalist
- **Vibe:** Raw, bold, unapologetic
- **Typography:** System fonts, monospace, huge sizes
- **Colors:** Black, white, primary accent (red/yellow)
- **Layout:** Grid-breaking, asymmetric, overlapping
- **When:** Developer tools, portfolios, art projects

#### Maximalist
- **Vibe:** More is more, information-dense, energetic
- **Typography:** Multiple font families, varied sizes, decorative
- **Colors:** Bold, saturated, gradients everywhere
- **Layout:** Dense, overlapping sections, no white space
- **When:** Creative agencies, music apps, youth brands

#### Retro-Futuristic
- **Vibe:** Y2K meets cyberpunk
- **Typography:** Geometric sans, tech-inspired
- **Colors:** Neon accents on dark, holographic effects
- **Layout:** Card-based, floating elements, depth
- **When:** Crypto, gaming, AI products

#### Luxury
- **Vibe:** Premium, sophisticated, elegant
- **Typography:** Serif headlines, generous spacing
- **Colors:** Muted neutrals (beige, cream, charcoal), gold accents
- **Layout:** Spacious, centered, minimal
- **When:** Finance, real estate, high-end SaaS

#### Playful
- **Vibe:** Fun, approachable, friendly
- **Typography:** Rounded sans, varied weights
- **Colors:** Vibrant pastels, gradients
- **Layout:** Organic shapes, illustrations, bouncy animations
- **When:** Consumer apps, education, social

#### Neo-Brutalist (Modern Brutalism)
- **Vibe:** Brutalist but refined
- **Typography:** Bold sans-serif, tight spacing
- **Colors:** Black, white, one or two bright accents
- **Layout:** Heavy borders, shadows, layered cards
- **When:** Design tools, SaaS startups, agencies

#### Glassmorphism
- **Vibe:** Translucent, layered, modern
- **Typography:** Clean sans, medium weight
- **Colors:** Gradients, frosted overlays
- **Layout:** Overlapping panels, depth through blur
- **When:** Dashboards, modern apps, premium UI

### 3. Avoid Generic AI Patterns

**❌ DON'T:**
- System fonts everywhere (Arial, Helvetica, sans-serif)
- Purple gradients by default
- Cookie-cutter card layouts
- Generic "Explore More" buttons
- Predictable hero sections with centered text
- Rainbow gradients just because

**✅ DO:**
- Choose unexpected font pairings (e.g., serif + mono, display + grotesque)
- Use brand-aligned colors
- Break grids intentionally
- Write specific CTAs ("Start Building" > "Get Started")
- Asymmetric hero layouts
- Purposeful color choices

## Typography Principles

### Font Pairing Strategies

1. **Contrast:** Serif headline + Sans body (classic)
2. **Harmony:** Geometric sans + Humanist sans (modern)
3. **Display + Mono:** Bold display + Monospace code (developer tools)
4. **Variable Fonts:** Use font weights for hierarchy (100-900)

### Size Scale (Tailwind-inspired)
- Micro: 12px (captions, metadata)
- Small: 14px (body, UI text)
- Base: 16px (paragraphs)
- Large: 18-20px (large body, subtitles)
- XL: 24-32px (section headers)
- 2XL: 36-48px (page titles)
- Hero: 56-96px (landing hero)

### Unexpected Pairings (Examples)
- **Brutalist:** Space Mono + Inter
- **Luxury:** Playfair Display + Lato
- **Tech:** JetBrains Mono + Geist Sans
- **Playful:** Fredoka + DM Sans
- **Modern:** Clash Display + Inter

## Motion & Interaction

### Orchestrated Motion (Not Random)
- **Stagger animations:** Elements enter in sequence (0.05s delay)
- **Scroll-triggered:** Reveal content as user scrolls
- **Hover states:** Transform, scale, color shift (0.2s duration)
- **Exit animations:** Elements leave gracefully

### Animation Timing
- **Fast:** 150ms (micro-interactions, hovers)
- **Medium:** 300ms (modals, dropdowns)
- **Slow:** 500-800ms (page transitions, reveals)

### Easing Functions
- **ease-out:** For entrances (starts fast, ends slow)
- **ease-in:** For exits (starts slow, ends fast)
- **spring:** For playful, bouncy interactions
- **linear:** For loaders, progress bars

## Spatial Composition

### Grid-Breaking Techniques
- **Overlap elements:** Cards slightly overlapping
- **Asymmetric layouts:** 60/40 splits instead of 50/50
- **Diagonal cuts:** Angled section dividers
- **Floating elements:** Icons/shapes outside grid
- **Offset grids:** Staggered card heights

### Depth Techniques
- **Layering:** Foreground, mid-ground, background
- **Shadows:** Soft (2-4px) for subtle, hard (8-16px) for drama
- **Gradients:** Depth through color fade (light → dark)
- **Blur:** Background blur for focus
- **3D transforms:** Subtle rotation/tilt on hover

## Visual Details

### Micro-Details That Matter
- **Border radius:** Consistent (8px, 12px, 16px) or sharp (0px)
- **Line heights:** 1.5-1.6 for body, 1.1-1.2 for headlines
- **Letter spacing:** Tight (-2%) for headlines, normal (0%) for body
- **Icon size:** Match text size (16px text = 16-20px icon)
- **Spacing scale:** 4px increments (4, 8, 12, 16, 24, 32, 48, 64)

### Texture & Patterns
- **Noise:** Subtle grain on backgrounds (3-5% opacity)
- **Gradients:** Mesh gradients, radial, conic
- **Grid overlays:** Dotted or line grids (subtle)
- **Shapes:** Blobs, geometric patterns, abstract forms

## Color Strategy

### Beyond Rainbow Gradients

1. **Monochrome + Accent:** Black/white + one vibrant color
2. **Analogous:** Adjacent colors on wheel (blue → purple)
3. **Complementary:** Opposite colors (blue + orange)
4. **Earth Tones:** Browns, greens, muted yellows (luxury, organic)
5. **Pastels:** Soft, desaturated colors (playful, approachable)
6. **Neons on Dark:** Bright accents on black (retro-futuristic)

### Gradient Types
- **Linear:** Top to bottom, diagonal
- **Radial:** Center outward (spotlight effect)
- **Conic:** Circular gradient (rainbow wheel)
- **Mesh:** Multiple color points (organic blends)

## Practical Workflow

### Step-by-Step
1. **Define context** (purpose, audience, brand)
2. **Pick aesthetic** (brutalist, luxury, playful, etc.)
3. **Choose fonts** (headline + body pairing)
4. **Set color palette** (2-3 main colors + neutrals)
5. **Design layout** (sketch asymmetric composition)
6. **Plan motion** (entrance animations, hovers)
7. **Add depth** (shadows, gradients, overlays)
8. **Refine details** (spacing, typography, micro-interactions)
9. **Code with purpose** (every choice intentional)

### Questions to Ask Before Coding
- What emotion should this evoke?
- What makes this interface memorable?
- What would a generic AI NOT do here?
- How can I break expectations tastefully?
- What's the ONE bold choice that defines this?

## Integration with webd Libraries

Match libraries to aesthetic:

| Aesthetic | Primary Library | Accent Library |
|-----------|----------------|----------------|
| Brutalist | Skipper UI | Phosphor Icons |
| Maximalist | Aceternity UI | PatternCraft |
| Retro-Futuristic | Magic UI | Motion Primitives |
| Luxury | Luxe UI | Origin UI |
| Playful | Kokonut UI | Animata |
| Neo-Brutalist | Cult UI | Smooth UI |
| Glassmorphism | Prism UI | MVP Blocks |

## Examples by Use Case

### SaaS Dashboard (Neo-Brutalist)
- **Fonts:** Inter Black (headline) + JetBrains Mono (data)
- **Colors:** Black, white, electric blue accent
- **Layout:** Dense grid, sharp corners, bold borders
- **Motion:** Minimal, fast (150ms), data-focused
- **Libraries:** Cult UI + Origin UI

### Crypto Landing (Retro-Futuristic)
- **Fonts:** Clash Display + Geist Sans
- **Colors:** Dark purple, neon green, holographic gradients
- **Layout:** Floating cards, 3D transforms, diagonal cuts
- **Motion:** Smooth, parallax, glow effects
- **Libraries:** Aceternity UI + Magic UI

### Creative Portfolio (Brutalist)
- **Fonts:** Space Mono + Arial (intentionally generic body)
- **Colors:** Black, white, red accent
- **Layout:** Broken grid, overlapping images, asymmetric
- **Motion:** Abrupt, no easing, fast transitions
- **Libraries:** Skipper UI + Phosphor Icons

### Finance App (Luxury)
- **Fonts:** Playfair Display + Inter
- **Colors:** Cream, charcoal, gold accents
- **Layout:** Spacious, centered, generous padding
- **Motion:** Slow, elegant, fade-ins
- **Libraries:** Luxe UI + Origin UI

## Final Notes

**Design is a conversation, not a formula.**

- Establish the vibe FIRST, then code
- Make bold choices, not safe ones
- Break patterns intentionally
- Every element should have a reason
- Generic = forgettable

If you're unsure, ask:
> "What would make this interface impossible to forget?"

Then do that.
