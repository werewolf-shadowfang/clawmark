#!/usr/bin/env python3
"""
Create a PNG version of the Open Graph preview image
Reads configuration from config.yaml or a custom config file
"""
import argparse
import yaml
import os

try:
    from PIL import Image, ImageDraw, ImageFont
    
    def load_config(config_path):
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"❌ Config file not found: {config_path}")
            return None
        except yaml.YAMLError as e:
            print(f"❌ Error parsing YAML: {e}")
            return None
    
    def get_og_config(config):
        """Extract Open Graph image configuration from config"""
        # Default values
        og_config = {
            'title': config.get('profile', {}).get('name', 'Your Name'),
            'subtitle': config.get('profile', {}).get('bio', 'Your Bio')[:50],  # First 50 chars
            'description': '',
            'cta': 'View All Links',
            'colors': {
                'bg_start': '#1e1b4b',
                'bg_end': '#4f46e5',
                'text': '#ffffff',
                'subtitle': '#c7d2fe',
                'description': '#a5b4fc',
                'button': '#6366f1',
                'accent1': '#6366f1',
                'accent2': '#8b5cf6'
            },
            'width': 1200,
            'height': 630,
            'output': 'assets/images/og-preview.png'
        }
        
        # Override with custom OG settings if provided
        advanced = config.get('advanced', {})
        og_custom = advanced.get('og_image_config', {})
        
        # Allow customization of text
        if 'title' in og_custom:
            og_config['title'] = og_custom['title']
        elif config.get('site', {}).get('title'):
            og_config['title'] = config['site']['title']
            
        if 'subtitle' in og_custom:
            og_config['subtitle'] = og_custom['subtitle']
            
        if 'description' in og_custom:
            og_config['description'] = og_custom['description']
        elif config.get('profile', {}).get('bio'):
            bio = config['profile']['bio']
            # Use second sentence or continuation of bio for description
            if len(bio) > 60:
                og_config['description'] = bio[50:120]
                
        if 'cta' in og_custom:
            og_config['cta'] = og_custom['cta']
            
        # Allow color customization
        if 'colors' in og_custom:
            og_config['colors'].update(og_custom['colors'])
        elif 'theme_options' in advanced:
            theme = advanced['theme_options']
            if 'primary_color' in theme:
                og_config['colors']['button'] = theme['primary_color']
                og_config['colors']['accent1'] = theme['primary_color']
            if 'secondary_color' in theme:
                og_config['colors']['accent2'] = theme['secondary_color']
                
        # Allow dimension customization
        if 'width' in og_custom:
            og_config['width'] = og_custom['width']
        if 'height' in og_custom:
            og_config['height'] = og_custom['height']
        if 'output' in og_custom:
            og_config['output'] = og_custom['output']
            
        return og_config
    
    def create_og_image(config_path='config.yaml'):
        """Create Open Graph preview image from config"""
        # Load configuration
        config = load_config(config_path)
        if not config:
            return False
            
        og_config = get_og_config(config)
        
        # Create image
        width = og_config['width']
        height = og_config['height']
        colors = og_config['colors']
        
        img = Image.new('RGB', (width, height), color=colors['bg_start'])
        draw = ImageDraw.Draw(img)
        
        # Try to use system fonts, fallback to default
        try:
            title_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 60)
            subtitle_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 32)
            desc_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
            cta_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 28)
        except:
            try:
                # Try alternative font paths
                title_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 60)
                subtitle_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 32)
                desc_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 24)
                cta_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
            except:
                print("⚠️  Using default font - install TrueType fonts for better results")
                title_font = ImageFont.load_default()
                subtitle_font = ImageFont.load_default()
                desc_font = ImageFont.load_default()
                cta_font = ImageFont.load_default()
        
        # Draw gradient background
        for y in range(height):
            # Parse hex colors and interpolate
            r1, g1, b1 = int(colors['bg_start'][1:3], 16), int(colors['bg_start'][3:5], 16), int(colors['bg_start'][5:7], 16)
            r2, g2, b2 = int(colors['bg_end'][1:3], 16), int(colors['bg_end'][3:5], 16), int(colors['bg_end'][5:7], 16)
            
            r = int(r1 + (r2 - r1) * y / height)
            g = int(g1 + (g2 - g1) * y / height)
            b = int(b1 + (b2 - b1) * y / height)
            color = f'#{r:02x}{g:02x}{b:02x}'
            draw.line([(0, y), (width, y)], fill=color)
        
        # Add decorative elements
        draw.ellipse([50, 50, 150, 150], fill=colors['accent1'])
        draw.ellipse([width-150, height-150, width-50, height-50], fill=colors['accent2'])
        
        # Prepare text
        title = og_config['title']
        subtitle = og_config['subtitle']
        description = og_config['description']
        cta = og_config['cta']
        
        # Calculate text positions (centered)
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (width - title_width) // 2
        
        # Draw title
        draw.text((title_x, 180), title, fill=colors['text'], font=title_font)
        
        # Draw subtitle if present
        if subtitle:
            subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
            subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
            subtitle_x = (width - subtitle_width) // 2
            draw.text((subtitle_x, 260), subtitle, fill=colors['subtitle'], font=subtitle_font)
        
        # Draw description if present
        if description:
            desc_bbox = draw.textbbox((0, 0), description, font=desc_font)
            desc_width = desc_bbox[2] - desc_bbox[0]
            desc_x = (width - desc_width) // 2
            draw.text((desc_x, 320), description, fill=colors['description'], font=desc_font)
        
        # Draw CTA button
        button_width, button_height = 300, 60
        button_x = (width - button_width) // 2
        button_y = 400
        draw.rounded_rectangle([button_x, button_y, button_x + button_width, button_y + button_height], 
                              radius=30, fill=colors['button'])
        
        cta_bbox = draw.textbbox((0, 0), cta, font=cta_font)
        cta_width = cta_bbox[2] - cta_bbox[0]
        cta_x = (width - cta_width) // 2
        draw.text((cta_x, button_y + 16), cta, fill=colors['text'], font=cta_font)
        
        # Add subtle pattern/decoration
        for i in range(3):
            y_offset = 50 + i * 30
            draw.line([(width-200, y_offset), (width-200+40, y_offset+30)], 
                     fill=colors['accent2'], width=4)
        
        # Save image
        output_path = og_config['output']
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, 'PNG', quality=95)
        
        print(f"✅ Created Open Graph image: {output_path}")
        print(f"   Title: {title}")
        print(f"   Subtitle: {subtitle}")
        if description:
            print(f"   Description: {description}")
        print(f"   Dimensions: {width}x{height}")
        return True
    
    def main():
        """Main entry point"""
        parser = argparse.ArgumentParser(
            description='Create Open Graph preview image from ClawMark config'
        )
        parser.add_argument(
            '--config', '-c',
            default='config.connor.yaml',
            help='Path to configuration file (default: config.connor.yaml)'
        )
        
        args = parser.parse_args()
        
        print("🎨 ClawMark Open Graph Image Generator")
        print(f"📄 Using config: {args.config}\n")
        
        if create_og_image(args.config):
            print("\n✨ Done! Your Open Graph image is ready.")
        else:
            print("\n❌ Failed to create Open Graph image.")
            exit(1)
    
    if __name__ == "__main__":
        main()
    
except ImportError:
    print("❌ PIL (Pillow) not available. Please install with: pip install Pillow")
    print("ℹ️  As a workaround, you can:")
    print("   1. Use an online SVG to PNG converter")
    print("   2. Create a 1200x630 PNG image manually")
    print("   3. Use any existing PNG/JPG image you have")
    exit(1)
    
except Exception as e:
    print(f"❌ Error creating PNG: {e}")
    print("ℹ️  You can create a PNG manually or use an online converter")
    exit(1)