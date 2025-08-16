# 🎯 Autodesk APAC Customer Analytics
**Comprehensive Data Analysis Methodology Demonstration**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

## 📊 **Project Overview**

**Business Challenge:** Analyze APAC customer usage patterns to identify performance baselines, risk signals, and expansion opportunities.

**My Analytical Approach:** Transform 955,033 usage records into actionable business intelligence through systematic methodology, strategic segmentation, and stakeholder-optimized deliverables.

### **🔗 Access Project Files:**
- **📓 [Complete Analysis Notebook](https://github.com/MiguelEnriquePortilla/Autodesk/blob/main/Autodesk_Practice.ipynb)** (GitHub - 12-step methodology)
- **📁 [Processed Datasets (7 CSV files)](https://drive.google.com/file/d/1vFi0aHdNAqQ6B43lWH9-WKwRkhLAO2Ik/view?usp=sharing)** (Google Drive)
- **📁 [Original Raw Data](https://drive.google.com/file/d/1oog32UgIkkc7N0kjL1EPDS0KKJCuO9AH/view?usp=sharing)** (Google Drive)
- **📊 [Power BI Dashboard](https://drive.google.com/file/d/1sA_9BnoHAfUEI4ctTosSTtxpusFzI0CZ/view?usp=sharing)** (Google Drive)

---

## 🔬 **My 12-Step Analytical Methodology**

### **Phase 1: Foundation & Discovery**

#### **Step 1 - Data Architecture Assessment**
**My Decision:** Rather than jumping into analysis, I started by understanding data quality and scope to establish analytical confidence.

**Methodology:** Comprehensive validation of 955K usage records + 242K account dimensions
- Verified zero missing values across all fields
- Confirmed no duplicate records
- Mapped 6 APAC regions and 4-month temporal coverage

**Why This Matters:** I never build insights on shaky foundations. Data quality drives analytical credibility.

#### **Step 2 - Customer Lifecycle Mapping**
**My Decision:** I chose to analyze customer tenure distribution first because lifecycle stage often explains performance variations.

**Strategic Finding:** 47.1% of customers are 3+ year veterans, indicating strong retention foundation but potential for veteran performance decline patterns.

**Analytical Pivot:** This high veteran percentage led me to prioritize lifecycle analysis in my segmentation strategy.

#### **Step 3 - Business Health Indicators**
**My Decision:** Before diving into usage metrics, I established macro business health through revenue performance ratios.

**Key Metrics Established:**
- 2.6x Expansion/Contraction ratio (healthy growth signal)
- 1.6% monthly churn rate (benchmark for risk analysis)

**Why This Approach:** These ratios became my North Star metrics for validating later usage-based insights.

### **Phase 2: Technical Optimization**

#### **Step 4 - Metric Validation & Standardization**
**Critical Discovery:** Raw metrics were in decimal format (0-1), not business-friendly percentages.

**My Technical Decision:** Rather than accepting data as-is, I implemented systematic validation to ensure stakeholder-ready outputs.

**Quality Assurance Process:**
- Converted all rates to percentage format for business communication
- Validated calculation logic against business rules
- Established metric definitions for consistent interpretation

#### **Step 5 - Business Rule Implementation**
**Strategic Challenge:** Found utilization rates >100% in 2.69% of records.

**My Analytical Choice:** Instead of excluding data, I implemented business-logical capping at 100% to preserve data volume while maintaining analytical integrity.

**Impact:** Retained full dataset while establishing realistic performance bounds for stakeholder consumption.

### **Phase 3: Strategic Segmentation**

#### **Step 6 - Performance Baseline Establishment**
**My Methodology:** Comprehensive statistical analysis across all metrics to establish organizational benchmarks.

**Benchmarks Established:**
- Assignment Rate: 92.9% average, 100% median
- Utilization Rate: 74.0% average, 100% median

**Strategic Value:** These baselines became the foundation for all subsequent performance comparisons and risk thresholds.

#### **Step 7 - Customer Size Segmentation Strategy**
**My Segmentation Decision:** I chose 8 granular size bands (1, 2-5, 6-10, 11-25, 26-50, 51-100, 101-500, 500+) instead of traditional small/medium/large categories.

**Rationale:** Suspected that performance patterns would be more nuanced than broad categories would reveal.

**Validation:** This granular approach uncovered the enterprise paradox that would have been hidden in traditional segmentation.

#### **Step 8 - Customer Size Performance Analysis**
**Shocking Discovery:** Complete performance inversion - largest customers show worst performance.

**The Enterprise Paradox I Uncovered:**
- 1 seat customers: 98.3% assignment rate
- 500+ seat customers: 58.5% assignment rate
- **40-point performance gap** favoring smaller customers

**My Analytical Pivot:** This counterintuitive finding forced me to investigate enterprise deployment complexity as a root cause, leading to new strategic recommendations.

### **Phase 4: Advanced Pattern Recognition**

#### **Step 9 - Customer Lifecycle Performance Tracking**
**My Hypothesis:** Customer performance should improve with tenure and experience.

**Surprising Validation:** Hypothesis was **completely wrong**.
- New customers (Q1): 94.4% assignment, 88.9% utilization
- Veterans (3+ years): 74.9% utilization
- **14-point performance advantage** for new customers

**Strategic Implications:** This finding shifted my recommendations toward veteran re-engagement programs rather than new customer acquisition focus.

#### **Step 10 - Regional Performance Comparative Analysis**
**My Regional Strategy:** Instead of treating APAC as homogeneous, I analyzed each region independently to identify best practices and intervention opportunities.

**Critical Regional Gap Discovered:**
- Top Performer: ANZ (97.2% assignment, 79.4% utilization)
- Bottom Performer: Greater China (82.8% assignment, 57.6% utilization)
- **21.8-point utilization gap** requiring immediate intervention

**Strategic Outcome:** This analysis established clear regional priority framework and best practice replication opportunities.

#### **Step 11 - Predictive Risk & Opportunity Modeling**
**My Predictive Approach:** I linked usage behavior patterns to business outcomes to create early warning systems.

**Predictive Thresholds Established:**
- **Churn Risk:** <60% utilization strongly correlates with customer churn
- **Expansion Opportunity:** >80% utilization correlates with account growth
- **22-point predictive separation** between risk and opportunity segments

**Business Value:** Created actionable intervention framework for customer success teams.

### **Phase 5: Data Architecture & Optimization**

#### **Step 12 - Stakeholder-Optimized Dataset Architecture**
**My Data Strategy:** Rather than delivering one massive dataset, I designed 7 purpose-built datasets optimized for different stakeholder needs and analytical use cases.

**Architectural Decisions:**

**1. Master Usage Data (955K records)**
- **Purpose:** Complete drill-down capability from insights to account details
- **Optimization:** Pre-computed performance flags (HighPerformer, AtRisk, ExpansionCandidate)
- **Business Logic:** Calculated UnusedSeats, UnassignedSeats to avoid runtime calculations

**2. Regional Performance Summary (6 regions)**
- **Purpose:** Executive-level regional comparison and intervention prioritization
- **Strategic Fields:** Performance rankings, market share correlation, regional risk rates
- **Stakeholder Focus:** C-level decision making on regional strategy

**3. Customer Size Analysis (8 size bands)**
- **Purpose:** Enterprise crisis focus and complexity analysis
- **Key Innovation:** RevenueContribution vs AvgUtilizationRate reveals ROI crisis
- **Strategic Value:** Highlights enterprise deployment challenges requiring specialized approaches

**4. Customer Lifecycle Journey (9 tenure segments)**
- **Purpose:** Lifecycle optimization and veteran re-engagement targeting
- **Analytical Enhancement:** LifecycleStage groupings enable journey mapping
- **Business Application:** Quantifies veteran customer re-engagement opportunity

**5. Risk & Opportunity Matrix (5 performance categories)**
- **Purpose:** Predictive customer success and resource allocation
- **Predictive Analytics:** Growth vs Risk classification with intervention thresholds
- **Operational Value:** Guides customer success team prioritization

**6. Monthly Trend Analysis (24 month-region combinations)**
- **Purpose:** Performance tracking against established baselines
- **Trend Analytics:** UtilizationEfficiency trending and seasonal pattern identification
- **Strategic Monitoring:** Deteriorating region early warning system

**7. Executive Summary (4 months)**
- **Purpose:** Board-level APAC performance narrative
- **Executive Metrics:** Month-over-month change indicators and baseline comparisons
- **Communication Focus:** Simple, high-level performance velocity tracking

---

## 🛠️ **Technical Architecture Decisions**

### **Technology Stack Rationale:**

**Python + Pandas:** Chosen for statistical analysis depth and data transformation flexibility  
**Jupyter Notebook:** Ensures reproducible analysis workflow and methodology documentation  
**Power BI:** Selected for executive dashboard interactivity and stakeholder familiarity  
**Google Drive:** Efficient data storage and secure sharing for large datasets

### **Performance Optimization Strategy:**
- Pre-aggregated summaries eliminate dashboard loading delays
- Calculated business logic embedded at dataset level, not visual level
- Proper relational structure via AccountID, Region keys for seamless joins
- CSV format optimization for cross-platform compatibility and query performance

### **Data Quality Assurance:**
- Zero missing values validated across all datasets
- No duplicates confirmed through systematic checking
- Business rule validation applied (utilization rate capping)
- Format standardization for stakeholder accessibility

---
## 📊 **Dashboard Architecture & Design Methodology**

### **My Stakeholder-Driven Visualization Strategy:**

Rather than creating a one-size-fits-all dashboard, I designed three interconnected pages, each optimized for different decision-making levels and analytical needs within the organization. Each page represents a deliberate design choice based on how different stakeholders consume and act on data.

---

#### **📈 Page 1: Executive Summary - C-Level Strategic Overview**

**My Design Decision:** C-level executives need instant comprehension of business health with minimal cognitive load. They scan top-to-bottom, left-to-right, and require immediate answers to "How are we performing?" and "Where should we focus?"


<img width="1313" height="734" alt="Executive Summary Dashboard" src="https://github.com/user-attachments/assets/8497b78e-f363-4025-bc29-aada6800a9b3" />


**Strategic Design Choices:**

**KPI Cards (Top Row):** I positioned the four critical baseline metrics (74.0% utilization, 92.9% assignment, 253K customers, 4M seats) prominently at the top because executives need context before diving into analysis.

**Regional Market Treemap (Bottom Left):** The size-coded treemap immediately communicates market share distribution across APAC regions. I chose this visualization because area size intuitively represents market importance - executives can instantly see that Japan and Greater China dominate market share.

**Regional Performance Ranking (Top Right):** The ranked table format allows executives to immediately identify best/worst performing regions. ANZ at the top (97.2% assignment) vs Greater China at bottom (82.8% assignment) creates clear accountability and intervention priorities.

**Customer Health Distribution (Bottom Left):** The pie chart shows business health at-a-glance - 75.1% flat performance means stable revenue base, while 15% expansion opportunities indicate growth potential.

**Performance Trends (Bottom Right):** The time series enables executives to spot trajectory changes and seasonal patterns across APAC markets.

**Why This Layout Works:** Follows executive scanning behavior - context first (KPIs), then market overview (treemap), actionable priorities (ranking), and performance health (pie + trends).

---

#### **🎯 Page 2: Customer Segmentation Analysis - Operational Deep-Dive**

**My Design Decision:** Operations teams need drill-down capability for intervention planning. They require detailed patterns, specific metrics, and the ability to identify which customer segments need immediate attention.


<img width="1312" height="741" alt="Customer Segmentation Dashboard" src="https://github.com/user-attachments/assets/945d2bf1-a2df-4591-8e24-068348fb847e" />


**Analytical Design Elements:**

**Size Band Performance Gap (Top Left):** The horizontal bar chart immediately reveals the counterintuitive enterprise paradox - 500+ seat customers show worst performance (58.5% assignment vs 98.3% for 1-seat customers). I chose horizontal bars because the 40-point performance gap is visually dramatic and impossible to miss.

**Customer Lifecycle Journey (Top Right):** The line chart traces performance across tenure segments, revealing that new customers (Q1: 94.4% assignment) significantly outperform veterans (3+ years: 74.9% utilization). This pattern drives strategic recommendations for veteran re-engagement programs.

**Customer Distribution Treemap (Bottom Left):** Shows market composition - 54.7% single-seat customers dominate volume, while enterprise customers represent tiny volume but high revenue impact. This visualization helps operations teams understand intervention resource allocation.

**Performance Matrix (Bottom Right):** The detailed table provides specific metrics for customer success teams to identify intervention targets. The 500+ seats segment shows 43.3% at-risk rate and only 46.4% utilization - clear intervention priority.

**Why This Approach Works:** Operations teams need both visual patterns (charts) and specific data (tables) to execute customer success strategies. The combination enables pattern recognition and tactical planning.

---

#### **⚠️ Page 3: Risk Analysis Framework - Predictive Customer Success**

**My Design Decision:** Customer success teams need predictive indicators and intervention priorities. This page transforms usage patterns into early warning systems and proactive customer health management.


<img width="1312" height="732" alt="Risk Analysis Dashboard" src="https://github.com/user-attachments/assets/9b32499a-1c56-4405-a072-c423f4545a57" />


**Predictive Design Elements:**

**Customer Health Distribution (Top Left):** The horizontal bar chart prioritizes business categories by intervention urgency. "Flat" customers (largest segment) represent stability, while "Contraction" and "Churn" segments require immediate customer success intervention.

**Customer Performance Matrix (Top Right):** This detailed table provides account-level data for customer success teams. The 955,033 total usage records roll up to specific intervention targets - customers with low utilization rates flagged for proactive outreach.

**Regional Risk vs Performance Matrix (Bottom Left):** The bubble chart plots each region's risk profile vs performance, with bubble size representing market importance. Greater China appears as a large bubble in the high-risk zone - clear intervention priority. ANZ appears in the high-performance, low-risk quadrant - best practice source.

**Risk Evolution Trends (Bottom Right):** The area chart tracks risk patterns over time by region, enabling customer success teams to identify deteriorating markets before they become critical. The trend analysis provides early warning capabilities.

**Why This Framework Works:** Transforms reactive customer success into proactive intervention by providing clear risk signals, intervention priorities, and predictive indicators for each market.

---

### **🎯 Design Philosophy Integration:**

**Multi-Level Storytelling:** Each page tells the same story at different analytical depths - executives see strategic overview, operations see tactical patterns, customer success sees intervention priorities.

**Visual Hierarchy:** Consistent color coding, logical flow, and intuitive navigation ensure stakeholders can quickly find relevant insights without cognitive overload.

**Actionable Intelligence:** Every visualization drives specific business actions - not just pretty charts, but decision-support tools that enable data-driven customer success strategy.

**Scalable Architecture:** The three-page structure can accommodate additional regions, segments, or time periods without losing clarity or usability.

This dashboard architecture demonstrates my approach to transforming complex analytical findings into stakeholder-optimized business intelligence that drives customer success, revenue optimization, and strategic decision-making across APAC markets.

---

## 📈 **Strategic Insights & Business Impact**

### **Critical Findings That Drove Strategy:**

**The Enterprise Paradox:** 500+ seat customers (highest revenue) show worst performance (58.5% vs 98.3% for single-seat)
- **My Analysis:** Enterprise deployment complexity requires specialized onboarding
- **Strategic Recommendation:** Dedicated enterprise customer success program

**The Veteran Performance Decline:** New customers outperform 3+ year veterans by 14 points
- **My Analysis:** Product adoption decay over time without refresher engagement
- **Strategic Recommendation:** Veteran re-engagement and advanced training programs

**The Regional Performance Gap:** 21.8-point utilization difference between ANZ and Greater China
- **My Analysis:** Cultural, linguistic, or support model differences affecting adoption
- **Strategic Recommendation:** Localized customer success approaches and best practice replication

**Predictive Risk Modeling:** Usage patterns provide 22-point separation between churn risk and expansion opportunity
- **My Analysis:** Early intervention capability through behavior monitoring
- **Strategic Recommendation:** Automated alerting system for customer success teams

---

## 📊 **Dashboard Architecture & Stakeholder Communication**

### **Executive Dashboard Design Philosophy:**
My approach to stakeholder communication through data visualization:

**Executive Level (C-Suite):**
- APAC baseline metric cards (92.9% assignment, 74.0% utilization)
- Regional performance ranking with intervention priorities
- Month-over-month trend indicators

**Operational Level (Customer Success):**
- Risk signal dashboard (customers <60% utilization)
- Expansion opportunity identification (customers >80% utilization)
- Customer health distribution analysis

**Strategic Level (Regional Management):**
- Geographic performance heatmap
- Market share vs performance analysis
- Best practice identification framework

---

## 🗂️ **Repository Structure**

```
autodesk-apac-customer-analytics/
├── 📓 Autodesk_Practice.ipynb           # Complete 12-step methodology
├── 📁 [Processed Datasets](drive-link)  # 7 optimized CSV files
├── 📁 [Original Data](drive-link)       # Raw source data
├── 📊 [Power BI Dashboard](drive-link)  # Interactive executive dashboard
└── 📋 README.md                         # This methodology documentation
```

---

## 🚀 **Quick Start Guide**

### **View Analysis Immediately:**
- **📓 [Open Analysis Notebook](https://github.com/MiguelEnriquePortilla/Autodesk/blob/main/Autodesk_Practice.ipynb)** (GitHub - no setup required)
- **📊 [Download Power BI Dashboard](https://drive.google.com/file/d/1sA_9BnoHAfUEI4ctTosSTtxpusFzI0CZ/view?usp=sharing)** (Google Drive)

### **Reproduce Analysis Locally:**
```bash
# Clone repository
git clone https://github.com/MiguelEnriquePortilla/Autodesk.git
cd Autodesk

# Install dependencies
pip install pandas numpy jupyter matplotlib seaborn

# Download datasets from Google Drive links above
# Extract to local directory

# Launch analysis
jupyter notebook Autodesk_Practice.ipynb
```

### **Power BI Dashboard Setup:**
1. Download Power BI file from Google Drive link above
2. Download processed datasets from Google Drive
3. Open .pbix file in Power BI Desktop
4. Update data source connections to local CSV files
5. Refresh data and explore interactive dashboards

---

## 💡 **What This Project Demonstrates**

### **Analytical Thinking:**
- **Systematic methodology:** 12-step structured approach to complex problems
- **Hypothesis-driven analysis:** Testing assumptions and pivoting based on findings
- **Pattern recognition:** Identifying counterintuitive insights (enterprise paradox, veteran decline)

### **Technical Expertise:**
- **Data optimization:** Purpose-built datasets for different stakeholder needs
- **Performance architecture:** CSV optimization for large dataset efficiency
- **Visualization strategy:** Executive-level dashboard design and communication

### **Business Acumen:**
- **Stakeholder alignment:** Different analytical outputs for different decision-making levels
- **Strategic recommendations:** Linking analytical findings to actionable business strategy
- **Risk assessment:** Predictive modeling for customer success intervention

### **Communication Skills:**
- **Executive reporting:** Translating technical findings into business impact
- **Visual storytelling:** Dashboard architecture for different audience needs
- **Documentation:** Comprehensive methodology tracking for reproducibility

---

## 🎯 **Project Outcomes & Strategic Value**

This analysis framework demonstrates my approach to transforming complex datasets into strategic business intelligence:

✅ **Established Performance Baselines:** 92.9% assignment, 74.0% utilization benchmarks  
✅ **Identified Critical Risk Patterns:** Enterprise customer success crisis requiring intervention  
✅ **Created Predictive Framework:** Early warning system for churn risk and expansion opportunities  
✅ **Designed Scalable Architecture:** 7-dataset structure optimized for ongoing analysis  
✅ **Delivered Executive Intelligence:** Power BI dashboard enabling data-driven decision making

**The Strategic Goal:** Transform usage data into actionable customer success strategy, revenue optimization, and competitive advantage across APAC markets through systematic analytical methodology.

---

**Miguel Enrique Portilla**  
*Data Analyst | Business Intelligence Specialist*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/miguelenriqueportilla)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MiguelEnriquePortilla)

*"Turning complex data into strategic advantage through systematic analytical methodology."*
