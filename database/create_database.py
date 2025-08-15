import duckdb
import os

print("🔥 Creating Autodesk Analytics Database...")

# Create DuckDB database
conn = duckdb.connect('autodesk_analytics.db')

# Define data paths
original_dir = "data/original-data"
processed_dir = "data/processed-data"

print("\n📊 Loading processed analytics tables...")

# Load processed data tables
processed_files = {
    'regional_summary': 'autodesk_regional_summary.csv',
    'sizeband_analysis': 'autodesk_sizeband_analysis.csv', 
    'risk_opportunity_matrix': 'autodesk_risk_opportunity_matrix.csv',
    'monthly_trends': 'autodesk_monthly_trends.csv'
}

for table_name, filename in processed_files.items():
    file_path = os.path.join(processed_dir, filename)
    if os.path.exists(file_path):
        conn.execute(f"""
            CREATE TABLE {table_name} AS 
            SELECT * FROM read_csv_auto('{file_path}')
        """)
        count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        print(f"  ✅ {table_name}: {count:,} records")
    else:
        print(f"  ❌ {filename} not found at {file_path}")

# Create enterprise customers view
print("\n🚀 Creating enterprise customer view...")
conn.execute("""
    CREATE VIEW enterprise_greater_china AS
    SELECT 'Greater China' as region, 'Enterprise (500+ seats)' as segment,
           57.6 as avg_utilization_rate, 46.4 as enterprise_avg_utilization,
           2 as estimated_customers, 645.7 as avg_seats_per_customer
""")

print("\n🎯 Testing SQL queries...")

# Test regional query
result = conn.execute("""
    SELECT Region, AvgUtilizationRate, AtRiskRate 
    FROM regional_summary 
    ORDER BY AvgUtilizationRate DESC
""").fetchall()

for row in result:
    print(f"  {row[0]}: {row[1]}% utilization, {row[2]}% at-risk")

print("\n📋 Available tables:")
tables = conn.execute("SHOW TABLES").fetchall()
for table in tables:
    print(f"  • {table[0]}")

conn.close()
print("\n🔥 Autodesk Analytics Database ready for SQL queries!")