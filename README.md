# 🚀 Autodesk APAC Customer Analytics
## Strategic Data Analysis & Business Intelligence Methodology

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg)](https://pandas.pydata.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-SQL%20Analytics-orange.svg)](https://duckdb.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboards-yellow.svg)](https://powerbi.microsoft.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red.svg)](https://jupyter.org/)

---

## 📊 Project Overview

**Business Challenge:** Analyze usage behaviors of APAC customers to identify baselines, trends, and risk/expansion signals across different customer segments and regions.

**Data Scope:** 955,033 customer usage records across 4 months (May-August 2024) covering 253,079 unique accounts in 6 APAC regions.

**Approach:** Comprehensive 12-step analytical methodology transforming raw usage data into actionable business intelligence through systematic analysis, data optimization, and executive-ready visualization.

---

## 🎯 Key Business Findings

### 📈 **APAC Performance Baselines Established**
- **Assignment Rate:** 92.9% average (100% median) - Excellent onboarding
- **Utilization Rate:** 74.0% average (100% median) - Strong product adoption

### 🏢 **Enterprise Performance Crisis Discovered**
- **Critical Finding:** 500+ seat customers perform 40 points worse than single-seat customers
- **Performance Inversion:** 1 seat (98.3% assignment) vs 500+ seats (58.5% assignment)
- **Business Impact:** Largest revenue customers have worst product adoption

### ⏰ **Customer Lifecycle Opportunity Identified**
- **Surprising Pattern:** First-quarter customers outperform 3+ year veterans by 14 points
- **New Customer Peak:** 94.4% assignment, 88.9% utilization in first quarter
- **Veteran Decline:** Drop to 74.9% utilization after 3+ years

### 🌏 **Regional Performance Disparities**
- **Top Performer:** ANZ - 97.2% assignment, 79.4% utilization
- **Bottom Performer:** Greater China - 82.8% assignment, 57.6% utilization
- **Critical Gap:** 21.8 percentage point utilization difference requiring immediate intervention

### ⚠️ **Predictive Risk & Expansion Signals**
- **Churn Threshold:** <60% utilization strongly correlates with customer churn
- **Expansion Indicator:** >80% utilization correlates with account growth
- **Early Warning:** Usage patterns provide 22-point predictive separation

---

## 🔬 Analytical Methodology

### **Phase 1: Data Foundation (Steps 1-6)**

#### **Step 1: Initial Data Assessment** 
**Purpose:** Establish data quality and scope understanding
**Key Validation:** 
- Verified 955K usage records + 242K account dimensions
- Confirmed zero missing values and duplicates
- Identified 6 APAC regions and 4-month coverage

#### **Step 2: Customer Tenure Analysis**
**Purpose:** Understand customer lifecycle distribution
**Key Insight:** 47.1% veteran customers (3+ years) indicating strong retention foundation

#### **Step 3: Performance Category Analysis** 
**Purpose:** Assess business health through revenue performance
**Key Metrics:** 2.6x growth ratio (Expansion vs Contraction), 1.6% churn rate

#### **Step 4: Usage Data Structure & Validation**
**Purpose:** Validate metric calculations and regional coverage
**Critical Discovery:** Metrics in decimal format (0-1) requiring business interpretation

#### **Step 5: Metric Format Standardization**
**Purpose:** Convert technical metrics to business-readable percentages
**Transformation:** Multiplied rates by 100 for stakeholder communication

#### **Step 6: Outlier Investigation & Data Cleaning**
**Purpose:** Handle utilization rates >100% for meaningful analysis
**Business Rule:** Capped utilization at 100% (affected 2.69% of records)

### **Phase 2: Baseline Establishment (Step 7)**

#### **Step 7: APAC Baseline Metrics Calculation**
**Purpose:** Establish performance benchmarks for stakeholder reference
**Methodology:** Comprehensive statistical analysis (mean, median, quartiles)
**Result:** 92.9% assignment, 74.0% utilization baselines established

### **Phase 3: Customer Segmentation Analysis (Steps 8-10)**

#### **Step 8: Customer Size Band Creation**
**Purpose:** Implement stakeholder-specified segmentation strategy
**Framework:** 8 size bands from "1 Seat" to "500+ Seats"
**Finding:** 85.4% small business market (1-5 seats) with 0.7% enterprise

#### **Step 9: Size Band Performance Analysis** ⚠️ **CRITICAL DISCOVERY**
**Purpose:** Analyze performance by customer size
**Shocking Result:** Complete performance inversion - largest customers worst performers
**Business Impact:** Enterprise customer success crisis identified

#### **Step 10: Customer Tenure Performance Analysis** ⚠️ **UNEXPECTED PATTERN**
**Purpose:** Track performance across customer lifecycle
**Surprising Finding:** New customers outperform veterans significantly
**Opportunity:** Clear veteran re-engagement program need identified

### **Phase 4: Regional Analysis (Step 11)**

#### **Step 11: APAC Regional Performance Comparison** ⚠️ **MAJOR GAPS**
**Purpose:** Comparative analysis across 6 APAC regions
**Critical Finding:** 21.8-point utilization gap between best/worst regions
**Strategic Priority:** Greater China intervention required immediately

### **Phase 5: Risk & Opportunity Analysis (Step 12)**

#### **Step 12: Performance Category Usage Patterns**
**Purpose:** Link usage behavior to business performance
**Predictive Discovery:** Clear thresholds for churn risk and expansion opportunity
**Early Warning System:** <60% utilization = churn risk, >80% = expansion ready

---

## 🏗️ Data Architecture & Optimization Strategy

### **Stakeholder-Segmented Dataset Design**

After completing comprehensive analysis, I designed a **7-dataset architecture** that transforms complex findings into purpose-built, stakeholder-optimized data products:

#### **1. Master Fact Table: `autodesk_master_usage_data.csv`**
*955,033 records | Complete dimensional model*

**Why Created:** Stakeholders need drill-down capability from insights to account details
**Optimization Decisions:**
- Performance flags: `HighPerformer`, `AtRisk`, `ExpansionCandidate` for instant filtering
- Calculated fields: Pre-computed `UnusedSeats`, `UnassignedSeats` avoid runtime calculations
- Date intelligence: Split Month into Year/MonthNum for proper hierarchy
- Business-friendly naming: PascalCase, no underscores for Power BI best practices

#### **2. Executive Summary: `autodesk_regional_summary.csv`**
*6 regions | Pre-aggregated for C-level dashboards*

**Why Created:** 21.8-point regional gap requires executive attention
**Strategic Fields:**
- Performance rankings: `AssignmentRateRank`, `UtilizationRateRank`
- Market context: `MarketShareBySeats` vs performance correlation
- Risk indicators: `AtRiskRate` by region for intervention prioritization

#### **3. Segmentation Insights: `autodesk_sizeband_analysis.csv`**
*8 size bands | Enterprise crisis focus*

**Why Created:** Counterintuitive finding - largest customers show worst performance
**Analytical Enhancements:**
- Revenue vs performance: `RevenueContribution` vs `AvgUtilizationRate` reveals ROI crisis
- Complexity indicator: `PerformanceGap` highlights enterprise deployment challenges
- Sorting logic: `SizeBandOrder` ensures proper visualization progression

#### **4. Lifecycle Intelligence: `autodesk_tenure_analysis.csv`**
*9 tenure segments | Customer journey optimization*

**Why Created:** New customers outperform veterans by 14 points
**Journey Mapping Fields:**
- Lifecycle classification: `LifecycleStage` groups quarters into business phases
- Trajectory analysis: `TenureOrder` enables chronological visualization
- Intervention targeting: Veteran customer re-engagement opportunity quantified

#### **5. Strategic Decision Support: `autodesk_risk_opportunity_matrix.csv`**
*5 performance categories | Predictive customer success*

**Why Created:** Usage patterns correlate with revenue performance
**Predictive Analytics Fields:**
- Business signal classification: Growth vs Risk categories
- Early warning system: AtRiskRate establishes intervention thresholds
- Resource allocation: `PriorityOrder` guides customer success focus

#### **6. Time-Series Analysis: `autodesk_monthly_trends.csv`**
*24 month-region combinations | Trend identification*

**Why Created:** Track improvement against established baselines
**Trend Analytics:**
- Efficiency tracking: `UtilizationEfficiency` shows regional trajectories
- Risk monitoring: `AtRiskRate` trending identifies deteriorating regions
- Seasonal patterns: Month-over-month analysis capability

#### **7. Executive KPI Tracking: `autodesk_overall_monthly_trends.csv`**
*4 months | C-level performance monitoring*

**Why Created:** Board-level reporting requires simple APAC narrative
**Executive Metrics:**
- Change indicators: `AssignmentRateChange`, `UtilizationRateChange`
- Baseline comparison: Track against 92.9%/74.0% benchmarks
- Performance velocity: Month-over-month acceleration patterns

---

## 🛠️ Technical Implementation

### **Core Technology Stack**
- **Python + Pandas:** Data analysis, transformation, and statistical calculations
- **DuckDB:** SQL optimization for large dataset performance 
- **Power BI:** Executive dashboards and interactive visualization
- **Jupyter Notebook:** Reproducible analysis workflow and documentation

### **Performance Optimizations**
- **Pre-aggregated summaries** eliminate dashboard loading delays
- **Calculated business logic** embedded at dataset level, not visual level
- **Proper relationships** via AccountID, Region keys for seamless joins
- **Data type optimization** for memory efficiency and query performance

### **Data Quality Assurance**
- **Zero missing values** across all datasets validated
- **No duplicates** confirmed through systematic checking
- **Business rule validation** applied (utilization rate capping)
- **Format standardization** for stakeholder accessibility

---

## 📁 Repository Structure

```
autodesk-apac-customer-analytics/
├── data/
│   ├── processed_datasets.zip              # All 7 optimized datasets
│   └── original_datasets.zip               # Raw data files
├── powerbi/
│   └── Autodesk Presentation.pbix          # Executive dashboard
├── database/
│   ├── create_database.py                  # DuckDB optimization script
│   └── analytics_database.zip              # SQL-queryable database
├── Autodesk_Practice.ipynb                 # Complete 12-step analysis
└── README.md                               # This documentation
```

---

## 🚀 Strategic Recommendations

### **🔥 Immediate Actions (0-3 months)**
1. **Enterprise Success Program** - Deploy dedicated CSMs for 500+ seat accounts
2. **Greater China Intervention** - Implement urgent regional improvement initiative  
3. **Risk Monitoring System** - Automated alerts for <60% utilization customers
4. **Veteran Re-engagement** - Target 3+ year customers with declining usage

### **📈 Medium-term Initiatives (3-12 months)**
1. **Best Practice Replication** - Scale ANZ/Japan strategies across APAC
2. **Expansion Acceleration** - Target >80% utilization customers for upselling
3. **Complexity Reduction** - Simplify enterprise onboarding processes
4. **Regional Strategy** - Implement localized customer success approaches

### **🎯 Long-term Strategy (12+ months)**
1. **Predictive Analytics** - Advanced modeling using usage patterns
2. **Segmented Success** - Differentiated approaches by size/region/tenure
3. **Market Development** - Address mid-market gap (6-50 seats)
4. **Platform Evolution** - Product improvements based on complexity insights

---

## 📊 Power BI Implementation Guide

### **Dashboard Architecture**

#### **Page 1: Executive Overview**
- APAC baseline metrics cards (92.9% assignment, 74.0% utilization)
- Regional performance ranking with gap analysis
- Customer health distribution (expansion vs risk signals)
- Month-over-month trend lines

#### **Page 2: Customer Segmentation Deep Dive**
- Size band performance comparison highlighting enterprise crisis
- Tenure journey visualization showing lifecycle patterns
- Seat utilization efficiency by segment
- Revenue contribution vs performance analysis

#### **Page 3: Regional Performance Analysis**
- Geographic performance map with utilization heatmap
- Regional ranking with 21.8-point gap highlighted
- Market share vs performance scatter plot
- Greater China improvement opportunity focus

#### **Page 4: Risk & Opportunity Matrix**
- Risk signal dashboard (customers <60% utilization)
- Expansion opportunity identification (customers >80% utilization)
- Performance category trends and predictions
- Customer success intervention priorities

### **Data Model Relationships**
- **Fact Table:** `autodesk_master_usage_data.csv` as central fact table
- **Dimension Tables:** Regional, size band, tenure, and risk matrices as lookup tables
- **Time Intelligence:** Month hierarchy for trend analysis
- **Key Relationships:** AccountID, Region, CustomerSizeBand for filtering

---

## 💼 Business Impact

### **Quantified Value Delivered**
- **$1M+ Revenue Opportunity:** Enterprise customer improvement potential
- **Predictive Churn Prevention:** Early warning system established
- **Regional Priority Framework:** 21.8-point improvement target set
- **Customer Success Optimization:** Clear intervention thresholds defined

### **Strategic Enablement**
- **Executive Decision Support:** Data-driven resource allocation capability
- **Operational Efficiency:** Customer success team targeting framework
- **Performance Monitoring:** Sustainable baseline tracking system
- **Competitive Advantage:** Regional best practice identification

---

## 🔧 How to Reproduce This Analysis

### **Prerequisites**
```bash
pip install pandas numpy jupyter duckdb
```

### **Running the Analysis**
1. **Clone Repository:** `git clone https://github.com/MiguelEnriquePortilla/Autodesk.git`
2. **Open Notebook:** Launch `Autodesk_Practice.ipynb`
3. **Load Data:** Extract datasets from `data/original_datasets.zip`
4. **Execute Analysis:** Run all cells to reproduce 12-step methodology
5. **Generate Datasets:** Processed files automatically created

### **Database Optimization (Optional)**
```bash
python database/create_database.py
```
Creates DuckDB database for SQL-based analysis and improved query performance.

### **Power BI Setup**
1. Extract datasets from `data/processed_datasets.zip`
2. Import all 7 processed CSV files into Power BI
3. Establish relationships using AccountID and Region
4. Create calculated measures for KPIs
5. Build dashboards following architecture guide

---

## 👨‍💻 About This Analysis

This project demonstrates **end-to-end analytical methodology** combining:
- **Statistical rigor** in baseline establishment and trend analysis
- **Business acumen** in translating findings to strategic recommendations  
- **Technical expertise** in data optimization and performance architecture
- **Stakeholder communication** through executive-ready visualization design

**The goal:** Transform complex usage data into actionable business intelligence that drives customer success, revenue optimization, and strategic decision-making across APAC markets.

---

## 📞 Contact

**Miguel Enrique Portilla**  
Data Analyst | Business Intelligence Specialist  
[LinkedIn](https://linkedin.com/in/miguelenriqueportilla) | [GitHub](https://github.com/MiguelEnriquePortilla)

*"Turning data into decisions, insights into impact."*
