# ClawMark Quick Start Guide

Get your link page up and running in 5 minutes!

## 🚀 Installation (1 minute)

```bash
cd clawmark
pip install -r requirements.txt
```

## ⚙️ Configuration (2 minutes)

Create your config file:

```bash
cp config.yaml config.myname.yaml
```

Edit the essential fields in `config.myname.yaml`:

```yaml
site:
  title: "Your Name"
  url: "https://yourdomain.com"

profile:
  name: "Your Name"
  bio: "What you do"
  avatar: "assets/images/profile.jpg"

social:
  instagram: "yourhandle"
  x: "yourhandle"
  linkedin: "yourhandle"

links:
  - title: "My Website"
    url: "https://yoursite.com"
    featured: true
```

## 🖼️ Add Your Image (30 seconds)

Place your profile photo in `assets/images/profile.jpg`

## 🎨 Generate Preview Image (30 seconds)

```bash
python create_og_image.py --config config.myname.yaml
```

## 🔨 Generate Site (30 seconds)

```bash
python clawmark_generator.py --config config.myname.yaml
```

## ✅ View Result

Open `output/index.html` in your browser!

## 📤 Deploy

Upload the entire `output/` folder to:
- GitHub Pages
- Netlify
- Vercel
- Any web host

---

**That's it!** Your link page is ready. 

For more customization options, see [README.md](README.md).
