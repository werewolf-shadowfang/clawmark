#!/usr/bin/env python3
"""
ClawMark Generator - A Python tool for creating Linktree-like websites
"""

import sys
import yaml
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from datetime import datetime


class ClawMarkGenerator:
    """Main class for generating ClawMark sites"""
    
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.config = None
        self.template_env = None
        
    def load_config(self):
        """Load configuration from YAML file"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            print(f"✓ Configuration loaded from {self.config_path}")
        except FileNotFoundError:
            print(f"❌ Configuration file '{self.config_path}' not found!")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"❌ Error parsing YAML configuration: {e}")
            sys.exit(1)
    
    def setup_template_environment(self):
        """Set up Jinja2 template environment"""
        templates_dir = Path("templates")
        if not templates_dir.exists():
            print("❌ Templates directory not found!")
            sys.exit(1)
            
        self.template_env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            autoescape=True
        )
        print("✓ Template environment initialized")
    
    def get_theme_path(self):
        """Get the path to the selected theme"""
        theme_name = self.config.get('site', {}).get('theme', 'default')
        theme_path = Path("themes") / theme_name
        
        if not theme_path.exists():
            print(f"❌ Theme '{theme_name}' not found in themes directory!")
            print(f"Available themes: {[d.name for d in Path('themes').iterdir() if d.is_dir()]}")
            sys.exit(1)
        
        return theme_path
    
    def load_theme_config(self, theme_path):
        """Load theme-specific configuration"""
        theme_config_path = theme_path / "theme.yaml"
        if theme_config_path.exists():
            with open(theme_config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {}
    
    def copy_theme_assets(self, theme_path, output_dir):
        """Copy CSS and other theme assets to output directory"""
        import shutil
        
        assets_dir = theme_path / "assets"
        if assets_dir.exists():
            output_assets_dir = output_dir / "assets"
            if output_assets_dir.exists():
                shutil.rmtree(output_assets_dir)
            shutil.copytree(assets_dir, output_assets_dir)
            print(f"✓ Theme assets copied to {output_assets_dir}")
    
    def copy_custom_assets(self, output_dir):
        """Copy custom assets from the assets/ directory to output/assets/"""
        import shutil
        
        assets_dir = Path("assets")
        if assets_dir.exists():
            output_assets_dir = output_dir / "assets"
            
            # If theme assets were already copied, we need to merge
            if output_assets_dir.exists():
                # Copy each subdirectory from custom assets
                for item in assets_dir.iterdir():
                    if item.is_dir():
                        dest_dir = output_assets_dir / item.name
                        if dest_dir.exists():
                            shutil.rmtree(dest_dir)
                        shutil.copytree(item, dest_dir)
                    else:
                        # Copy individual files
                        shutil.copy2(item, output_assets_dir / item.name)
            else:
                # No theme assets, just copy everything
                shutil.copytree(assets_dir, output_assets_dir)
            
            print(f"✓ Custom assets copied to {output_assets_dir}")
        else:
            print("ℹ No custom assets directory found")
    
    def generate_site(self):
        """Generate the complete LinkBio site"""
        if not self.config:
            print("❌ No configuration loaded!")
            return
        
        # Get theme information
        theme_path = self.get_theme_path()
        theme_config = self.load_theme_config(theme_path)
        theme_name = self.config.get('site', {}).get('theme', 'default')
        
        # Set up template loader for the specific theme
        theme_template_path = theme_path / "templates"
        if theme_template_path.exists():
            theme_env = Environment(
                loader=FileSystemLoader([str(theme_template_path), "templates"]),
                autoescape=True
            )
        else:
            theme_env = self.template_env
        
        try:
            # Load the main template
            template = theme_env.get_template("index.html")
        except TemplateNotFound:
            print(f"❌ Template 'index.html' not found for theme '{theme_name}'!")
            return
        
        # Prepare template context
        context = {
            'site': self.config.get('site', {}),
            'profile': self.config.get('profile', {}),
            'links': self.config.get('links', []),
            'social': self.config.get('social', {}),
            'advanced': self.config.get('advanced', {}),
            'theme': theme_config,
            'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Render the template
        html_content = template.render(**context)
        
        # Create output directory
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        # Write the HTML file
        output_file = output_dir / "index.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Copy theme assets
        self.copy_theme_assets(theme_path, output_dir)
        
        # Copy custom assets
        self.copy_custom_assets(output_dir)
        
        print(f"✅ Site generated successfully!")
        print(f"📁 Output location: {output_file.absolute()}")
        print(f"🎨 Theme used: {theme_name}")
    
    def run(self):
        """Main execution method"""
        print("🚀 ClawMark Generator Starting...")
        
        self.load_config()
        self.setup_template_environment()
        self.generate_site()
        
        print("\n✨ Generation complete! Open output/index.html in your browser.")


def main():
    """Entry point for the application"""
    parser = argparse.ArgumentParser(description="Generate a ClawMark site from configuration")
    parser.add_argument(
        "--config", 
        "-c", 
        default="config.yaml",
        help="Path to configuration file (default: config.yaml)"
    )
    
    args = parser.parse_args()
    
    generator = ClawMarkGenerator(config_path=args.config)
    generator.run()


if __name__ == "__main__":
    main()