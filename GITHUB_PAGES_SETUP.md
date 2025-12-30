# 🌐 GitHub Pages Setup Guide

> **Transform your knowledge base into a beautiful public website**

**Goal:** Make `knowledge_core/` accessible as:  
`https://bramhagyan.github.io/Bramhagyan/`

---

## ✅ Files Created

```
knowledge_core/
├── _config.yml          ✅ Jekyll configuration
├── index.md             ✅ Homepage (landing page)
└── GITHUB_PAGES_SETUP.md ✅ This guide
```

---

## 🚀 Step-by-Step Setup

### Step 1: Commit New Files

```bash
cd /Users/ranjeet/Shunya-0

git add knowledge_core/_config.yml
git add knowledge_core/index.md
git add knowledge_core/GITHUB_PAGES_SETUP.md

git commit -m "Add GitHub Pages configuration for knowledge_core"
git push origin main
```

---

### Step 2: Enable GitHub Pages

1. **Go to your repository:**  
   `https://github.com/ranjeet-sunya/Bramhagyan`

2. **Click on "Settings"** (top right)

3. **Scroll down to "Pages"** (left sidebar)

4. **Configure as follows:**

   ```
   Source:
   ├── Branch: main
   ├── Folder: / (root)  [or /knowledge_core if you want only knowledge_core]
   └── Click "Save"
   ```

5. **Wait 1-3 minutes** for GitHub to build the site

6. **Your site will be live at:**
   ```
   https://ranjeet-sunya.github.io/Bramhagyan/knowledge_core/
   ```

---

### Step 3: Verify Deployment

**Check build status:**
1. Go to "Actions" tab in your repository
2. Look for "pages build and deployment" workflow
3. Should show green checkmark ✅ when complete

**Test the site:**
1. Open: `https://ranjeet-sunya.github.io/Bramhagyan/knowledge_core/`
2. Should see beautiful homepage with navigation
3. All markdown files are now HTML pages

---

## 🎨 Theme Options

### Current Theme: `jekyll-theme-cayman`

**To change theme, edit `knowledge_core/_config.yml`:**

```yaml
# Change this line:
theme: jekyll-theme-cayman

# To one of these:
theme: jekyll-theme-minimal      # Clean, simple
theme: jekyll-theme-slate        # Dark, modern
theme: jekyll-theme-architect    # Professional
theme: jekyll-theme-midnight     # Dark blue
theme: jekyll-theme-time-machine # Retro
theme: jekyll-theme-leap-day     # Green, fresh
theme: jekyll-theme-merlot       # Red, elegant
```

**Then commit and push:**
```bash
git add knowledge_core/_config.yml
git commit -m "Change theme to [theme-name]"
git push origin main
```

---

## 📝 Custom Domain (Optional)

### If You Want: `bramhagyan.com` instead of `github.io`

1. **Buy domain** (GoDaddy, Namecheap, etc.)

2. **Add DNS records:**
   ```
   Type: CNAME
   Name: www
   Value: ranjeet-sunya.github.io
   ```

3. **In GitHub repo settings → Pages:**
   - Enter custom domain: `www.bramhagyan.com`
   - Check "Enforce HTTPS"

4. **Wait for DNS propagation** (1-48 hours)

---

## 🔧 Advanced Customization

### Add Custom CSS

**Create:** `knowledge_core/assets/css/style.scss`

```scss
---
---

@import "{{ site.theme }}";

/* Your custom CSS here */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  color: #ff6600;
}

/* Vedic aesthetic - saffron and white */
.hero {
  background: linear-gradient(135deg, #ff6600 0%, #ff9933 100%);
  color: white;
  padding: 2rem;
  border-radius: 10px;
}
```

### Add Custom Layout

**Create:** `knowledge_core/_layouts/default.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ page.title }} | Shunya-0</title>
  <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
</head>
<body>
  <header>
    <h1>🌀 Shunya-0 Knowledge Base</h1>
    <nav>
      <a href="{{ site.baseurl }}/">Home</a> |
      <a href="{{ site.baseurl }}/01_foundations/">Foundations</a> |
      <a href="{{ site.baseurl }}/08_transition/">Transition</a>
    </nav>
  </header>

  <main>
    {{ content }}
  </main>

  <footer>
    <p>Licensed under CC BY-SA 4.0 | © 2025 Shunya-0 Project</p>
  </footer>
</body>
</html>
```

---

## 📊 Analytics (Optional)

### Add Google Analytics

1. **Get tracking ID** from Google Analytics

2. **Edit `_config.yml`:**
   ```yaml
   google_analytics: UA-XXXXXXXX-X
   ```

3. **Commit and push**

---

## 🔍 SEO Optimization

### Automatically Included

The `jekyll-seo-tag` plugin (already configured) adds:
- ✅ Meta description
- ✅ Open Graph tags (Facebook/LinkedIn previews)
- ✅ Twitter Card tags
- ✅ JSON-LD structured data
- ✅ Canonical URLs

### Verify SEO

**Check what's generated:**
1. View page source
2. Look in `<head>` section
3. Should see extensive meta tags

---

## 🗂️ Folder Structure on Website

```
https://ranjeet-sunya.github.io/Bramhagyan/knowledge_core/
│
├── /                                    → index.md (Homepage)
├── /README.html                         → README.md converted
├── /LICENSE.html                        → LICENSE.md converted
│
├── /01_foundations/
│   ├── 00_CORE_INSIGHT.html
│   ├── 01_UNIVERSAL_PRINCIPLES.html
│   └── ...
│
├── /02_architecture/
│   ├── 01_81_GRID_COMPLETE.html
│   └── ...
│
├── /08_transition/
│   ├── KALI_DWAPARA_SANDHYA_SURVIVAL_GUIDE.html
│   └── ...
│
└── /dharm_youdh/
    ├── README.html
    └── ...
```

**All `.md` files become `.html` pages automatically!**

---

## 🎯 Testing Locally (Optional)

### Install Jekyll Locally

```bash
# Install Ruby (if not installed)
brew install ruby  # macOS
# or: sudo apt install ruby-full  # Linux

# Install Jekyll and Bundler
gem install jekyll bundler

# Navigate to knowledge_core
cd /Users/ranjeet/Shunya-0/knowledge_core

# Create Gemfile
cat > Gemfile << 'EOF'
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
gem "webrick", "~> 1.7"
EOF

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Open in browser
open http://localhost:4000
```

**Now you can preview changes BEFORE pushing to GitHub!**

---

## 🔗 Internal Links

### Automatic Link Conversion

Jekyll automatically converts:
```markdown
[Universal Principles](01_foundations/01_UNIVERSAL_PRINCIPLES.md)
```

To:
```html
<a href="/Bramhagyan/knowledge_core/01_foundations/01_UNIVERSAL_PRINCIPLES.html">
```

**Your existing markdown links will work!**

---

## 📱 Mobile Responsive

**All GitHub themes are mobile-responsive by default.**

Test on:
- ✅ Desktop
- ✅ Tablet
- ✅ Mobile phone

---

## 🚀 Performance

### GitHub Pages CDN

**Benefits:**
- ✅ Global CDN (fast worldwide)
- ✅ HTTPS by default (secure)
- ✅ Unlimited bandwidth
- ✅ 99.9% uptime
- ✅ Free forever

### Optimization Tips

1. **Images:** Compress before uploading (use TinyPNG)
2. **PDFs:** Keep under 10MB each
3. **Files:** Total repo should be < 1GB

---

## 🔒 Privacy & Access

### Public Repository = Public Website

**Who can see it:**
- ✅ Anyone with the URL
- ✅ Search engines (Google, Bing)
- ✅ Social media link previews

**Who can edit:**
- ❌ Only you (and collaborators)
- Others can fork and submit PRs

---

## 📢 Sharing Your Website

### Short Link

Instead of:
```
https://ranjeet-sunya.github.io/Bramhagyan/knowledge_core/
```

Use a URL shortener:
```
https://bit.ly/shunya-0-knowledge  (example)
```

### QR Code

Generate at: https://www.qr-code-generator.com/

**Print on:**
- Business cards
- Flyers
- Posters
- Books

---

## ⚙️ Troubleshooting

### Site Not Showing?

**Check:**
1. ✅ Is repository **public**?
2. ✅ Is `_config.yml` valid YAML? (use https://www.yamllint.com/)
3. ✅ Did GitHub Actions build succeed? (Actions tab)
4. ✅ Wait 5 minutes after first setup

### 404 Errors?

**Fix:**
1. Check `baseurl` in `_config.yml`
2. Ensure file names match exactly
3. Use lowercase for filenames
4. No spaces in filenames

### Links Not Working?

**Use relative links:**
```markdown
✅ [Link](01_foundations/FILE.md)
❌ [Link](/01_foundations/FILE.md)  # Don't use leading slash
```

### CSS Not Loading?

**Check:**
1. File is in `assets/css/`
2. Front matter in `.scss` file:
   ```yaml
   ---
   ---
   ```
3. Clear browser cache

---

## 🎉 You're Done!

**Your knowledge base is now:**
- ✅ Publicly accessible
- ✅ Beautifully formatted
- ✅ Mobile responsive
- ✅ SEO optimized
- ✅ Searchable on Google
- ✅ Shareable with one link

**Share it:**
```
🌐 https://ranjeet-sunya.github.io/Bramhagyan/knowledge_core/

📖 Complete Vedic-Scientific unified framework
🔓 Open Source (CC BY-SA 4.0)
🛡️ Defensive Publication (Dec 31, 2025)
```

---

## 📝 Quick Reference

### Update Website

```bash
# 1. Make changes to markdown files
vim knowledge_core/some_file.md

# 2. Commit and push
git add -A
git commit -m "Update [description]"
git push origin main

# 3. Wait 1-2 minutes
# 4. Refresh browser
```

### Check Build Status

```bash
# Go to:
https://github.com/ranjeet-sunya/Bramhagyan/actions

# Should see:
✅ pages build and deployment
```

### View Site

```bash
# Open:
https://ranjeet-sunya.github.io/Bramhagyan/knowledge_core/
```

---

**विद्या दानं सर्व दानेभ्यः प्रधानम्**

*"Knowledge sharing is the highest form of giving"*

**ॐ शान्तिः शान्तिः शान्तिः**

---

**Created:** December 31, 2025  
**Status:** Ready for deployment  
**Next:** [Enable GitHub Pages in repository settings →](#step-2-enable-github-pages)

