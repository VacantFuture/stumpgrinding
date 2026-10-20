# TF Stump Grinding

Professional stump grinding website built with Astro, Svelte, and Tailwind CSS v4.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🛠 Tech Stack

- **Framework**: [Astro](https://astro.build/) v7.2
- **UI Components**: [Svelte](https://svelte.dev/) v5
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **Icons**: [astro-iconset](https://github.com/astro-authors/astro-iconset) (Material Symbols, MDI)
- **Fonts**: Work Sans (headings), Roboto (body) - via Google Fonts

## 📁 Project Structure

```
src/
├── components/
│   ├── About.astro          # About section
│   ├── Contact.astro        # Contact section with phone CTA
│   ├── Footer.astro         # Footer with business info & schema
│   ├── Hero.astro           # Hero section with background image
│   ├── NavBar.astro         # Navigation with mobile menu
│   └── Testimonials.astro   # Customer reviews
├── images/
│   └── Tfstump-main-background-v2.jpg  # Hero background
├── layouts/
│   └── BaseLayout.astro     # Base layout with SEO & GA
├── pages/
│   └── index.astro          # Home page
└── styles/
    └── global.css           # Design system & Tailwind config
```

## 🎨 Design System

### Brand Colors

- **Primary Navy**: `#2B4C5E` → `var(--color-accent-500)`
- **Accent Yellow**: `#F59E0B` → `var(--color-accent-secondary-500)`
- **Neutrals**: Warm gray scale (50-950)

### Typography

- **Wordmark/Headings**: Work Sans (400-900)
- **Body**: Roboto (300-500)

### Type Scale (Major Third - 1.25 ratio)

- `text-xs`: 12px
- `text-sm`: 14px
- `text-base`: 16px
- `text-lg`: 20px
- `text-xl`: 25px
- `text-2xl`: 31px
- `text-3xl`: 39px
- `text-4xl`: 49px
- `text-5xl`: 61px
- `text-6xl`: 76px

## 📊 SEO & Analytics

### Google Analytics

Tracking ID: `G-RDHHXBVYXW`

Analytics is configured in `src/layouts/BaseLayout.astro` with gtag.js.

### Schema.org Markup

The site includes comprehensive LocalBusiness schema markup:

- Business name, phone, location
- Service area (St. Lawrence County, NY)
- Services offered (Stump Grinding, Tree Removal, Full Service Clean Up)
- Aggregate rating (5.0/5 from 3 reviews)
- Opening hours

Schema is injected as JSON-LD in the Footer component.

## 📱 Sections

1. **Header/Nav** - Fixed navigation with brand logo and mobile menu
2. **Hero** - Full-screen hero with background image, navy overlay, phone CTA
3. **Pricing** - Pricing explanation, free estimates, Full Service Clean Up details
4. **About** - Service area and company description
5. **Testimonials** - 3 customer reviews with Google Reviews link
6. **Contact** - Click-to-call phone button
7. **Footer** - Business info, hours, quick links, social media

## ♿ Accessibility

- Skip-to-content link for keyboard navigation
- ARIA labels on all interactive elements
- Focus trap in mobile menu
- Semantic HTML structure
- Color contrast meets WCAG AA standards
- Screen reader-only utilities available

## 🌐 Deployment

### Build Output

Production build creates optimized static files in `dist/`:

- Pre-rendered HTML
- Optimized images (WebP, AVIF)
- Minified CSS/JS
- Favicon files

### Hosting

Can be deployed to any static hosting platform:

- Netlify
- Vercel
- Cloudflare Pages
- GitHub Pages
- AWS S3 + CloudFront

## 📞 Business Information

- **Phone**: (315) 212-6847
- **Location**: Potsdam, NY
- **Service Area**: St. Lawrence County, Northern New York
- **Hours**: Mon-Fri 8AM-6PM, Sat 9AM-2PM, Sun Closed

## 🔗 Links

- [Google Reviews](https://g.page/tf-stump-grinding/review)
- [Material Symbols](https://fonts.google.com/icons)
- [MDI Icons](https://pictogrammers.com/library/mdi/)

## 📝 Notes

- No contact form - uses click-to-call only (simpler, no backend needed)
- No street address - serves entire county
- All colors use CSS variables for easy theming
- Mobile-first responsive design
