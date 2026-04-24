# ================================================
# Executive Summary Generator
# Afficionado Coffee Roasters
# ================================================

summary = """
================================================================================
                        EXECUTIVE SUMMARY
           Afficionado Coffee Roasters — Sales Performance Report
                         Data Analysis | 2025
================================================================================

PREPARED FOR : Government & Business Stakeholders
PREPARED BY  : Data Analytics Team
SUBJECT      : Time-Based Sales Performance Analysis

────────────────────────────────────────────────────────────────────────────────
BUSINESS OVERVIEW
────────────────────────────────────────────────────────────────────────────────
Afficionado Coffee Roasters is a specialty coffee retail chain with 3 active
locations across New York City: Hell's Kitchen, Astoria, and Lower Manhattan.
This report summarizes key findings from a transaction-level sales analysis
covering 149,116 transactions and $698,812 in total revenue for 2025.

────────────────────────────────────────────────────────────────────────────────
KEY PERFORMANCE INDICATORS
────────────────────────────────────────────────────────────────────────────────
  Total Revenue              :  $698,812.33
  Total Transactions         :  149,116
  Average Transaction Value  :  $4.69
  Number of Store Locations  :  3
  Peak Revenue Hour          :  10:00 AM – 11:00 AM
  Top Performing Store       :  Hell's Kitchen (33.8% of revenue)
  Top Product Category       :  Coffee
  Top Individual Product     :  Sustainably Grown Organic Lg

────────────────────────────────────────────────────────────────────────────────
CRITICAL FINDINGS
────────────────────────────────────────────────────────────────────────────────
1. MORNING DOMINANCE
   55.6% of all daily revenue is generated between 6 AM and 11 AM.
   This confirms that the morning commute window is the single most
   important revenue period for the business.

2. PEAK HOUR: 10 AM – 11 AM
   The 10th hour consistently records the highest transaction volume
   and revenue across all three store locations simultaneously.

3. BALANCED STORE PERFORMANCE
   All three locations perform within 1% of each other in revenue share:
     • Hell's Kitchen   : 33.8%
     • Astoria          : 33.2%
     • Lower Manhattan  : 32.9%
   This indicates a healthy, distributed customer base with no single
   store dependency.

4. AFTERNOON REVENUE GAP
   Revenue drops by nearly 47% after 12 PM compared to morning peak.
   The afternoon period (12 PM – 4 PM) contributes only 29.3% of revenue,
   representing a significant operational opportunity.

5. EVENING UNDERPERFORMANCE
   The evening period (5 PM – 9 PM) contributes just 15.1% of revenue,
   suggesting limited evening customer engagement across all locations.

────────────────────────────────────────────────────────────────────────────────
STRATEGIC RECOMMENDATIONS
────────────────────────────────────────────────────────────────────────────────
1. WORKFORCE OPTIMIZATION
   Align staff schedules with demand peaks. Maximum staffing between
   8 AM – 11 AM; reduced staffing post 1 PM. Estimated cost savings:
   10–15% reduction in labor costs through smart scheduling.

2. AFTERNOON ACTIVATION STRATEGY
   Launch time-limited promotions (e.g., "2-for-1 Cold Brew 2–4 PM")
   to stimulate the identified afternoon revenue gap.

3. EVENING EXPANSION
   Pilot evening-specific product lines (cold brews, specialty drinks,
   light food pairings) and community events to capture untapped
   evening foot traffic.

4. PRODUCT PORTFOLIO FOCUS
   Double down on the Coffee category — particularly large-size premium
   blends — which drive the highest per-transaction revenue values.

5. DATA-DRIVEN OPERATIONS
   Deploy the Streamlit analytics dashboard across all store managers
   to enable real-time, location-specific decision making.

────────────────────────────────────────────────────────────────────────────────
CONCLUSION
────────────────────────────────────────────────────────────────────────────────
The analysis confirms that Afficionado Coffee Roasters has a strong, consistent
revenue base with clear temporal patterns. By acting on the morning peak
dominance, addressing the afternoon revenue gap, and optimizing staffing
schedules, the business can improve operational efficiency and unlock new
revenue opportunities — particularly in the afternoon and evening windows.

This evidence-based approach positions Afficionado Coffee Roasters for
sustainable, data-driven growth across all store locations.

================================================================================
   CONFIDENTIAL | Afficionado Coffee Roasters | Data Analytics Division | 2025
================================================================================
"""

with open("executive_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print(summary)
print("\n✅ Executive Summary saved as: executive_summary.txt")