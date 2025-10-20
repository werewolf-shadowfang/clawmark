# ClawMark Generator 🔗

A Python tool for generating beautiful, customizable Linktree-like websites with multiple theme options, animated backgrounds, and easy configuration.

## Features ✨

- **Multiple Themes**: Choose from Modern, Minimal, Gradient, and more
- **Animated Backgrounds**: Full Vanta.js integration with 15+ stunning effects
- **Easy Configuration**: Simple YAML-based configuration file
- **Responsive Design**: Works perfectly on all devices
- **Social Media Integration**: Built-in support for all major platforms with SVG icons
- **Custom Assets**: Support for images, CSS, JS, fonts, and other resources
- **Social Media Previews**: Generate custom Open Graph images for rich link previews
- **Custom Styling**: Override colors, fonts, and layout options
- **SEO Friendly**: Proper meta tags and Open Graph support
- **Analytics Ready**: Google Analytics integration
- **Fast Generation**: Creates static HTML files in seconds
- **Mobile Optimized**: Automatic fallbacks for mobile devices

## Quick Start 🚀

### 1. Installation

```bash
# Clone or download this repository
cd clawmark

# Install dependencies
pip install -r requirements.txt
```

### 2. Create Your Configuration

Copy the example config and customize it:

```bash
cp config.yaml config.myname.yaml
```

Edit `config.myname.yaml` with your information:

```yaml
site:
  title: "My ClawMark"
  description: "All my important links in one place"
  url: "https://yourdomain.com"  # Your deployed URL
  theme: "modern"  # Choose: modern, minimal, gradient
  og_image: "assets/images/og-preview.png"  # Social media preview image

profile:
  name: "Your Name"
  bio: "Your bio here"
  avatar: "assets/images/profile.jpg"  # Place your image in assets/images/

social:
  instagram: "yourhandle"
  x: "yourhandle"  # Twitter/X
  linkedin: "yourhandle"
  github: "yourhandle"
  # ... more social platforms

links:
  - title: "My Website"
    url: "https://yourwebsite.com"
    description: "Check out my website"
    icon: "🌐"
    featured: true
  # ... more links
```

### 3. Add Your Assets (Optional)

Place your custom files in the `assets/` directory:

```
assets/
├── images/          # Profile pictures, backgrounds, logos
│   └── profile.jpg
├── css/             # Custom CSS files
│   └── custom.css
├── js/              # Custom JavaScript
│   └── custom.js
├── fonts/           # Custom fonts
└── icons/           # Favicons and icons
    └── favicon.svg
```

All files in `assets/` will be automatically copied to `output/assets/` during generation.

### 4. Generate Social Media Preview Image

Create a custom Open Graph image for rich social media previews:

```bash
# Generate from your config
python create_og_image.py --config config.myname.yaml
```

This creates `assets/images/og-preview.png` which will be used when sharing your link on:
- Twitter/X
- Facebook
- LinkedIn
- Telegram
- Discord
- WhatsApp

**Customize the preview image** by adding to your config:

```yaml
advanced:
  og_image_config:
    title: "Your Name"
    subtitle: "Your Tagline"
    description: "What you do"
    cta: "View My Links"
    colors:
      bg_start: "#1e1b4b"
      bg_end: "#4f46e5"
      button: "#6366f1"
```

### 5. Generate Your Site

```bash
# Generate with custom config file
python clawmark_generator.py --config config.myname.yaml
```

The generator will:
1. Load your configuration
2. Apply your chosen theme
3. Copy all assets from `assets/` to `output/assets/`
4. Generate `output/index.html` with all your content
5. Include proper meta tags for social media previews

### 6. View Your Site

Open `output/index.html` in your browser or upload the `output/` folder to your web hosting.

## Usage Guide 📚

### ClawMark Generator

**Basic usage:**
```bash
python clawmark_generator.py --config config.yaml
```

**Options:**
- `--config` or `-c`: Specify config file (default: `config.yaml`)

**What it does:**
1. Reads your configuration from YAML
2. Loads the selected theme (modern, minimal, gradient)
3. Copies theme assets (CSS, etc.) to output
4. Copies your custom assets to output
5. Renders the HTML template with your content
6. Generates `output/index.html`

### Open Graph Image Generator

**Basic usage:**
```bash
python create_og_image.py --config config.yaml
```

**Options:**
- `--config` or `-c`: Specify config file (default: `config.connor.yaml`)

**What it does:**
1. Reads configuration and theme colors
2. Extracts title, bio, and branding
3. Generates a 1200x630 PNG image
4. Saves to `assets/images/og-preview.png`
5. Uses your theme colors or custom colors from config

**Requirements:**
```bash
pip install Pillow
```

## Configuration Examples 🔧

### Basic Configuration

```yaml
site:
  title: "John Doe"
  theme: "modern"

profile:
  name: "John Doe"
  bio: "Full Stack Developer"
  avatar: "assets/images/profile.jpg"

links:
  - title: "Portfolio"
    url: "https://johndoe.com"
    featured: true
```

### Advanced Configuration with Vanta.js

```yaml
advanced:
  vanta:
    enabled: true
    effect: "net"  # waves, birds, net, cells, etc.
    settings:
      color: "#4f46e5"
      backgroundColor: "#1e1b4b"
  
  theme_options:
    button_style: "gradient_border"
    primary_color: "#6366f1"
    secondary_color: "#8b5cf6"
```

### Full Configuration with Custom Assets

```yaml
site:
  title: "Jane Smith"
  url: "https://janesmith.dev"
  favicon: "assets/icons/favicon.svg"
  custom_css: "assets/css/custom.css"
  custom_js: "assets/js/custom.js"
  og_image: "assets/images/og-preview.png"

profile:
  name: "Jane Smith"
  avatar: "assets/images/profile.jpg"
  
advanced:
  og_image_config:
    title: "Jane Smith"
    subtitle: "Product Designer"
    cta: "See My Work"
```

## Available Themes 🎨

### Modern
- Clean, professional design
- Gradient backgrounds
- Smooth animations
- Glass morphism effects

### Minimal
- Black and white aesthetic
- Clean typography
- Fast loading
- Print-friendly

### Gradient
- Vibrant gradients
- Floating animations
- Colorful design
- Dynamic backgrounds

## Configuration Guide 📖

### Site Settings

```yaml
site:
  title: "My ClawMark"                    # Page title
  description: "All my links"            # Meta description
  theme: "modern"                        # Theme selection
  favicon: "path/to/favicon.ico"         # Optional favicon
  custom_css: "path/to/custom.css"       # Optional custom CSS
  analytics:
    google_analytics: "GA-XXXXXXXXX"    # Optional Google Analytics
```

### Profile Information

```yaml
profile:
  name: "Your Name"                      # Your display name
  bio: "Your bio text"                   # Short description
  avatar: "https://example.com/img.jpg"  # Profile picture URL
  location: "Your City, Country"         # Optional location
```

### Social Media Links

```yaml
social:
  instagram: "username"       # Just the username
  x: "username"               # Just the username (formerly Twitter)
  linkedin: "username"        # Just the username
  github: "username"          # Just the username
  youtube: "channel"          # Channel name
  tiktok: "username"          # Just the username
  facebook: "username"        # Just the username
  discord: "invite-code"      # Discord invite
  email: "you@example.com"    # Email address
```

### Main Links

```yaml
links:
  - title: "Link Title"              # Display text
    url: "https://example.com"       # Destination URL
    description: "Optional desc"     # Subtitle text
    icon: "🌐"                      # Emoji or CSS class
    featured: true                   # Makes link stand out
```

### Advanced Customization

```yaml
advanced:
  custom_head: "<script>...</script>"    # Custom HTML head content
  custom_footer: "<p>Footer text</p>"    # Custom footer content
  
  theme_options:
    primary_color: "#6366f1"             # Override theme colors
    secondary_color: "#8b5cf6"
    background_color: "#ffffff"
    text_color: "#1f2937"
    primary_font: "Inter, sans-serif"    # Custom font
    max_width: "400px"                   # Container width
    button_style: "gradient_border"      # Button design style
    animation: true                      # Enable/disable animations
    
  # Vanta.js Animated Backgrounds
  vanta:
    enabled: true                        # Enable/disable Vanta.js
    effect: "waves"                      # Background effect type
    mobile_fallback: true                # Use static bg on mobile
    
    settings:
      color: "#4f46e5"                   # Primary color
      color2: "#7c3aed"                  # Secondary color
      backgroundColor: "#1e1b4b"         # Background color
      waveHeight: 20                     # Effect-specific settings
      waveSpeed: 0.5
      zoom: 1
      
    performance:
      lowPerformanceMode: false          # Reduce quality for performance
      fps: 60                           # Target frames per second
      
    mobile_background:
      type: "gradient"                   # Mobile fallback type
      gradient: "linear-gradient(...)"   # Gradient definition
```

## Vanta.js Animated Backgrounds 🌊

ClawMark now supports stunning animated backgrounds powered by Vanta.js! Choose from 15+ different effects to make your link page truly stand out.

### Available Effects

- **waves** - Smooth ocean-like wave animations
- **birds** - Animated flocking birds  
- **gradient** - Flowing color gradients
- **net** - Interconnected network nodes
- **dots** - Animated dot patterns
- **topology** - 3D topographic surfaces
- **clouds** - Floating cloud formations
- **fog** - Atmospheric fog effects
- **rings** - Expanding ring patterns
- **cells** - Cellular organism-like movement
- **globe** - 3D rotating globe
- **trunk** - Tree-like branching structures
- **halo** - Glowing halo effects
- **noise** - Dynamic noise patterns

### Basic Configuration

```yaml
advanced:
  vanta:
    enabled: true           # Turn on/off animated backgrounds
    effect: "waves"         # Choose your preferred effect
    mobile_fallback: true   # Use static background on mobile
    
    settings:
      color: "#4f46e5"      # Primary animation color
      backgroundColor: "#1e1b4b"  # Base background color
```

### Advanced Configuration Examples

#### Waves Effect
```yaml
vanta:
  enabled: true
  effect: "waves"
  settings:
    color: "#4f46e5"
    color2: "#7c3aed"
    backgroundColor: "#1e1b4b"
    waveHeight: 20          # Wave amplitude (10-40)
    waveSpeed: 0.5          # Animation speed (0.1-2.0)
    zoom: 1                 # Zoom level (0.5-2.0)
```

#### Birds Effect
```yaml
vanta:
  enabled: true
  effect: "birds"
  settings:
    color1: "#ff6b6b"
    color2: "#4ecdc4"
    backgroundColor: "#667eea"
    quantity: 4             # Number of birds (1-10)
    birdSize: 1.5          # Size multiplier (0.5-3.0)
    wingSpan: 40           # Wing span (20-80)
    speedLimit: 5          # Max speed (1-10)
```

#### Net Effect
```yaml
vanta:
  enabled: true
  effect: "net"
  settings:
    color: "#6366f1"
    backgroundColor: "#0f172a"
    points: 10             # Connection points (5-15)
    maxDistance: 20        # Max connection distance (10-30)
    spacing: 16            # Point spacing (10-25)
    showDots: true         # Show connection points
```

### Mobile Optimization

Vanta.js effects can be performance-intensive on mobile devices. ClawMark automatically detects mobile devices and provides fallback options:

```yaml
vanta:
  mobile_fallback: true    # Enable mobile fallbacks
  mobile_background:
    type: "gradient"       # Options: color, gradient, image
    color: "#1e1b4b"      # Solid color fallback
    gradient: "linear-gradient(135deg, #1e1b4b, #4f46e5)"
    image: "url-to-image" # Background image URL
```

### Performance Settings

Fine-tune performance for different devices:

```yaml
vanta:
  performance:
    lowPerformanceMode: false  # Reduce quality for better performance
    fps: 60                   # Target FPS (30-60)
```

### Theme Integration

Each theme includes recommended Vanta.js settings that complement the theme's design:

- **Modern Theme**: Waves, Net, Topology effects with blue/purple colors
- **Gradient Theme**: Gradients, Birds, Rings effects with vibrant colors  
- **Minimal Theme**: Dots, Topology, Net effects with subtle monochrome colors

See `example-vanta-config.yaml` for complete configuration examples with all available effects.

### Button Styles 🎨

Choose from multiple button styles to match your design and ensure optimal visibility:

#### Available Styles

- **rounded** - Classic rounded buttons with subtle styling
- **square** - Sharp, minimalist square buttons
- **pill** - Fully rounded pill-shaped buttons
- **gradient_border** - Static gradient borders with high-visibility background
- **solid** - High-contrast solid gradient buttons (best for dark animated backgrounds)
- **glass** - Glassmorphism effect with backdrop blur
- **neon** - Glowing neon-style buttons

#### Configuration

```yaml
advanced:
  theme_options:
    button_style: "solid"    # Choose your preferred style
```

#### Visibility Recommendations

**For Vanta.js Animated Backgrounds:**
- ✅ **solid** - Best choice for maximum visibility and contrast
- ✅ **gradient_border** - Good choice with animated border effects
- ⚠️ **glass** - May be hard to see on busy backgrounds
- ⚠️ **neon** - Works well with dark, minimal effects like dots or topology

**For Static Backgrounds:**
- ✅ **rounded**, **square**, **pill** - Clean, professional look
- ✅ **gradient_border** - Adds visual interest
- ✅ **glass** - Beautiful glassmorphism effect

### Tips for Best Results

1. **Choose colors that complement your theme** - Use your theme's color palette
2. **Test on mobile devices** - Always enable mobile fallbacks
3. **Consider your audience** - Some effects work better for creative vs. professional profiles
4. **Monitor performance** - Use browser dev tools to check frame rates
5. **Less is more** - Subtle animations often work better than intense effects
6. **Button visibility** - Use `solid` or `gradient_border` styles with animated backgrounds

## Button Styles 🎨

ClawMark offers multiple button design styles to match your aesthetic preferences. You can configure the button style in your `advanced.theme_options.button_style` setting.

### Available Button Styles

#### Gradient Border (`gradient_border`)
Beautiful animated gradient borders with glow effects, just like modern design systems. Features:
- Animated rotating gradient borders
- Subtle glow effects on hover
- Glass-like transparency
- Perfect for animated backgrounds

```yaml
advanced:
  theme_options:
    button_style: "gradient_border"
```

#### Glass (`glass`)
Modern glass morphism effects with blur and transparency:
- Frosted glass appearance
- Backdrop blur effects
- Subtle transparency
- Clean and modern look

#### Neon (`neon`)
Striking neon-style buttons with glowing borders:
- Colorful glowing effects
- Dark background with bright accents
- Pulsing animations on hover
- Great for creative profiles

#### Rounded (`rounded`) - Default
Clean, professional rounded buttons:
- Subtle shadows and borders
- Smooth hover animations
- Works with all themes
- Excellent readability

#### Square (`square`)
Sharp, professional square buttons:
- Clean geometric design
- Minimal styling
- Business-focused appearance
- High contrast

#### Pill (`pill`)
Fully rounded pill-shaped buttons:
- Maximum border radius
- Friendly, approachable design
- Smooth curved edges
- Modern aesthetic

### Theme Integration

Each theme has optimized button styles:

- **Modern Theme**: All styles work beautifully, `gradient_border` and `glass` are excellent with Vanta.js
- **Gradient Theme**: `gradient_border` and `glass` complement the vibrant design
- **Minimal Theme**: `glass` and `rounded` maintain the clean aesthetic

### Custom Colors

Button styles automatically adapt to your theme colors:
- Gradient borders use your primary/secondary colors
- Neon effects use your primary color for glows
- All styles respect your theme's color palette

See `example-button-styles.yaml` for complete configuration examples.
```

## File Structure 📁

```
clawmark/
├── clawmark_generator.py     # Main Python script
├── requirements.txt          # Python dependencies
├── config.yaml              # Your configuration file
├── templates/               # Base HTML templates
│   └── index.html
├── themes/                  # Available themes
│   ├── modern/
│   │   ├── assets/
│   │   │   └── style.css
│   │   └── theme.yaml
│   ├── minimal/
│   │   ├── assets/
│   │   │   └── style.css
│   │   └── theme.yaml
│   └── gradient/
│       ├── assets/
│       │   └── style.css
│       └── theme.yaml
└── output/                  # Generated site files
    ├── index.html
    └── assets/
        └── style.css
```

## Creating Custom Themes 🛠️

1. Create a new folder in `themes/` directory:
   ```
   themes/mytheme/
   ├── assets/
   │   └── style.css
   └── theme.yaml
   ```

2. Create `theme.yaml` with theme metadata:
   ```yaml
   name: "My Theme"
   description: "Custom theme description"
   version: "1.0.0"
   
   colors:
     primary: "#your-color"
     # ... more colors
   
   features:
     - "Feature 1"
     - "Feature 2"
   ```

3. Style your theme in `assets/style.css`

4. Set `theme: "mytheme"` in your config.yaml

## Deployment 🌐

### Static Hosting
Upload the contents of the `output/` folder to any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- Firebase Hosting
- AWS S3

### Custom Domain
Most hosting services allow you to use a custom domain for your ClawMark site.

**Important for Social Media Previews:**
After deploying, update your `site.url` in config.yaml to your actual domain, then regenerate:

```yaml
site:
  url: "https://yourdomain.com"  # Your actual deployed URL
```

Then regenerate and redeploy:
```bash
python clawmark_generator.py --config config.yaml
```

## Troubleshooting 🔧

### Common Issues

#### Site Generation Issues

**Theme not found**
- Check theme name spelling in `config.yaml`
- Ensure theme folder exists in `themes/` directory
- Available themes: `modern`, `minimal`, `gradient`

**Missing dependencies**
```bash
pip install -r requirements.txt
```

**YAML parsing errors**
- Check YAML syntax with proper indentation (use spaces, not tabs)
- Ensure all strings with special characters are quoted
- Validate your YAML: https://www.yamllint.com/

**Config file not found**
```bash
# Make sure you specify the correct path
python clawmark_generator.py --config config.myname.yaml
```

#### Asset Issues

**Images not loading**
- For local images, place them in `assets/images/` and use: `assets/images/filename.jpg`
- For external images, use full URLs: `https://...`
- Check image URLs are accessible
- Verify assets are copied to `output/assets/`

**Custom CSS/JS not applying**
- Ensure files are in `assets/css/` or `assets/js/`
- Reference them in config: `custom_css: "assets/css/custom.css"`
- Check browser console for errors

**Assets not copied to output**
- Ensure `assets/` folder exists
- Check folder structure matches expected layout
- Run generator with proper config file

#### Social Media Preview Issues

**Twitter/X not showing image**
- Image must be PNG or JPG (not SVG)
- Use absolute URL: `https://yourdomain.com/assets/images/og-preview.png`
- Image dimensions should be 1200x630
- Clear Twitter cache: https://cards-dev.twitter.com/validator
- Ensure `site.url` is set in config

**Generate Open Graph image fails**
```bash
# Install Pillow
pip install Pillow

# Run with correct config
python create_og_image.py --config config.myname.yaml
```

**Social preview not updating**
- Clear social platform cache using their validation tools
- Change filename to force refresh
- Wait 24-48 hours for cache expiration
- Ensure absolute URLs are used in meta tags

#### Vanta.js Background Issues

**Background not showing**
- Check `advanced.vanta.enabled: true` in config
- Verify effect name is correct (lowercase)
- Check browser console for JavaScript errors
- Ensure internet connection (Vanta.js loads from CDN)

**Poor performance**
- Enable mobile fallback: `mobile_fallback: true`
- Reduce FPS: `fps: 30`
- Enable low performance mode in config
- Use simpler effects like `gradient` or `fog`

**Mobile fallback not working**
- Ensure `mobile_fallback: true` in config
- Set fallback style in `mobile_background` section
- Clear browser cache and reload

#### Command Not Working

**Python command not found**
```bash
# Try python3 instead
python3 clawmark_generator.py --config config.yaml
```

**Permission denied**
```bash
# Make scripts executable
chmod +x clawmark_generator.py
chmod +x create_og_image.py
```

**Wrong config file used**
```bash
# Always specify your config explicitly
python clawmark_generator.py --config config.myname.yaml
```

### Getting Help

If you're still having issues:
1. Check the `docs/` folder for detailed documentation
2. Review example configs in the repository
3. Open an issue on GitHub with:
   - Your config file (remove sensitive info)
   - Error messages
   - Steps to reproduce
   - Your environment (OS, Python version)

## Project Structure 📁

```
clawmark/
├── clawmark_generator.py      # Main site generator
├── create_og_image.py          # OG image generator
├── config.yaml                 # Default configuration
├── config.connor.yaml          # Example custom config
├── example-config.yaml         # Full example config
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
│
├── assets/                     # Your custom assets
│   ├── images/                 # Images, logos, photos
│   ├── css/                    # Custom CSS
│   ├── js/                     # Custom JavaScript
│   ├── fonts/                  # Custom fonts
│   └── icons/                  # Favicons, icons
│
├── templates/                  # HTML templates
│   └── index.html             # Main template
│
├── themes/                     # Available themes
│   ├── modern/
│   ├── minimal/
│   └── gradient/
│
├── docs/                       # Documentation
│   ├── og-image-generator.md  # OG image docs
│   └── example-vanta-config.yaml
│
└── output/                     # Generated site (not in git)
    ├── index.html
    └── assets/
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
3. Add your theme or feature
4. Test thoroughly
5. Submit a pull request

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Support 💬

If you need help or have questions:
- Check the troubleshooting section above
- Review the configuration examples
- Read the documentation in `docs/`
- Open an issue on GitHub

## Changelog 📝

### Recent Updates

- ✅ Added configurable Open Graph image generator
- ✅ Implemented custom assets system (images, CSS, JS, fonts)
- ✅ Enhanced social media preview support with proper meta tags
- ✅ Added SVG social media icons for professional appearance
- ✅ Improved button styles with gradient borders and glass effects
- ✅ Full Vanta.js integration with 15+ animated backgrounds
- ✅ Mobile optimization with automatic fallbacks
- ✅ Theme color integration for Open Graph images

---

**Made with ❤️ and 🐺 by the Connor Shadowfang Goodwolf**