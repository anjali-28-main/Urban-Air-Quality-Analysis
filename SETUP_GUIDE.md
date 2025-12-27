# Quick Setup Guide

## Prerequisites
- Python 3.8 or higher installed on your system
- pip package manager
- Jupyter Notebook

## Installation Steps

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Urban-Air-Quality-Analysis
```

### 2. Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook
```

### 5. Open the Analysis Notebook
- Navigate to `notebooks/urban_air_quality_analysis.ipynb`
- Run all cells sequentially to perform the complete analysis

## Project Structure
```
Urban-Air-Quality-Analysis/
├── README.md                    # Main project documentation
├── SETUP_GUIDE.md              # This file
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── data/
│   ├── air_quality_data.csv    # Main dataset (10,950+ records)
│   └── generate_dataset.py     # Dataset generation script
├── notebooks/
│   └── urban_air_quality_analysis.ipynb  # Main analysis notebook
└── visualizations/             # Generated plots and charts
    └── (created when notebook is run)
```

## Dataset Information
- **Records**: 10,950 daily measurements
- **Time Period**: January 2022 - December 2024 (3 years)
- **Cities**: 10 major Indian cities (Delhi, Mumbai, Kolkata, Chennai, Bangalore, Hyderabad, Ahmedabad, Pune, Jaipur, Lucknow)
- **Pollutants**: PM2.5, PM10, NO2, SO2, CO, O3
- **Metrics**: Air Quality Index (AQI)

## Running the Analysis

### Option 1: Run All Cells
- Open the notebook and click "Cell" → "Run All"
- Wait for all cells to execute (takes 2-5 minutes)
- All visualizations will be automatically saved to `visualizations/` folder

### Option 2: Run Step by Step
- Execute cells one by one to understand each analysis phase
- Review outputs and visualizations as you progress

## Analysis Phases Included

1. **Data Loading**: Import and initial exploration
2. **Data Cleaning**: Handle missing values and outliers
3. **Exploratory Data Analysis**: Statistical summaries and distributions
4. **Temporal Analysis**: Trends over time, seasonal patterns
5. **City & State Comparison**: Geographic analysis
6. **Correlation Analysis**: Relationships between pollutants
7. **AQI Categorization**: Air quality classification
8. **Insights & Recommendations**: Data-driven conclusions

## Visualizations Generated

The notebook creates 10+ high-quality visualizations:
- Pollutant distribution histograms
- City-wise comparison charts
- Monthly and yearly trend lines
- Seasonal analysis plots
- Correlation heatmaps
- AQI category distributions
- State-wise comparisons
- And more...

## Troubleshooting

### Issue: Module not found
**Solution**: Make sure you've installed all requirements
```bash
pip install -r requirements.txt
```

### Issue: Jupyter Notebook won't start
**Solution**: Install Jupyter explicitly
```bash
pip install jupyter notebook
```

### Issue: Plots not showing
**Solution**: Make sure you have matplotlib backend configured
```python
%matplotlib inline
```

### Issue: Virtual environment not activating
**Solution**: Use the full path to the activation script
```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source ./venv/bin/activate
```

## Next Steps

After running the analysis:
1. Review the generated visualizations in `visualizations/` folder
2. Check the analysis summary in `data/analysis_summary.csv`
3. Modify the notebook to explore specific aspects
4. Add your own analysis cells
5. Export results for presentations or reports

## Support

For issues or questions:
- Check the main README.md
- Review the notebook comments
- Open an issue in the repository

## Data Attribution

This project uses synthetic data based on real-world air quality patterns in Indian cities. The data is generated for educational and research purposes.

---

Happy Analyzing!
