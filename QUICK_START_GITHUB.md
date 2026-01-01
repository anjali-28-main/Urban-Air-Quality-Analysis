# Quick Start: Publishing to GitHub

## Prerequisites
- GitHub account (create at https://github.com)
- Git installed on your computer

## Steps (5 minutes)

### 1. Create GitHub Repository
- Go to https://github.com/new
- Name: `Urban-Air-Quality-Analysis`
- Set to **Public**
- Don't initialize with README
- Click "Create repository"

### 2. Push Your Code
In your project folder, run:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/Urban-Air-Quality-Analysis.git
git branch -M main
git push -u origin main
```

### 3. Update README
- Replace `yourusername` with your actual GitHub username in README.md
- Run:
```bash
git add README.md
git commit -m "Update README with GitHub username"
git push
```

### 4. View Online
Your notebook is now live at:
- **Read-only view**: https://nbviewer.org/github/YOUR_USERNAME/Urban-Air-Quality-Analysis/blob/main/notebooks/urban_air_quality_analysis.ipynb
- **Interactive**: https://mybinder.org/v2/gh/YOUR_USERNAME/Urban-Air-Quality-Analysis/main?filepath=notebooks/urban_air_quality_analysis.ipynb

Replace `YOUR_USERNAME` with your GitHub username.

## That's it!

For detailed instructions, see PUBLISHING_GUIDE.md
