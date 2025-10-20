# Assets Directory

This directory contains all your custom assets that will be copied to the `output/assets/` folder during site generation.

## Directory Structure

- **`images/`** - Profile pictures, backgrounds, icons, logos, etc.
- **`css/`** - Custom CSS files for additional styling
- **`js/`** - JavaScript files for custom functionality
- **`fonts/`** - Custom font files (woff, woff2, ttf, etc.)
- **`icons/`** - Favicon files and custom icons

## Usage in Config

Reference assets in your `config.yaml` files using relative paths:

```yaml
profile:
  avatar: "assets/images/profile.jpg"

site:
  favicon: "assets/icons/favicon.ico"
  custom_css: "assets/css/custom.css"

advanced:
  vanta:
    mobile_background:
      image: "assets/images/background.jpg"
```

## Supported File Types

- **Images**: JPG, PNG, GIF, SVG, WebP
- **CSS**: CSS files
- **JavaScript**: JS files
- **Fonts**: WOFF, WOFF2, TTF, OTF
- **Icons**: ICO, PNG, SVG

All files in this directory will be automatically copied to `output/assets/` during generation.