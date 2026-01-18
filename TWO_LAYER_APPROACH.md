# Two-Layer Approach: Current Reality → Future Projection

**Fixed:** V2 now asks **100% current reality questions only** (no future).

Then we can build predictions from that current state.

---

## Layer 1: CEO Interview (Current Reality ONLY)

### **What It Does**

Establishes "what IS true RIGHT NOW" by asking 30 insider-knowledge questions.

**Examples:**
- "What was revenue last week?" (not "what will it be next year?")
- "What IS the delivery take rate today?" (not "what will it be in 2027?")
- "How much did you buy back last quarter?" (not "how much will you buy back?")
- "What are regulatory liabilities on books now?" (not "what will you pay?")
- "What % of rides are autonomous THIS WEEK?" (not "what % will be in 2027?")

### **Output:**

A snapshot of Uber's current reality:
```json
{
  "revenue_last_week": 750,           // $M
  "mobility_take_rate_current": 25,   // %
  "delivery_take_rate_current": 23.5, // %
  "ebitda_margin_current_quarter": 12,// %
  "stock_based_comp_run_rate": 800,   // $M/quarter
  "monthly_active_riders_growth": 1.2,// % MoM
  // ... 24 more
}
```

This is "the truth as you believe it today."

---

## Layer 2: Projection Model (Current + Public Data → Future)

### **What It Does**

Takes current reality (from CEO interview) + public data → projects 3 years forward.

### **Inputs:**

**From CEO Interview (Current State):**
- Revenue run rate (last week extrapolated)
- Current growth rates (Mobility MoM, Delivery MoM)
- Current take rates
- Current margins
- Current SBC run rate
- Current user growth

**From Public Data:**
- Historical trends (from EDGAR)
- Analyst forecasts (for comparison)
- Market size estimates (TAM)
- Competitor data (DoorDash, Lyft)
- Regulatory filings
- Industry growth rates

### **Projection Logic:**

```
Step 1: Project Revenue Growth
─────────────────────────────
Current quarterly revenue: $10B (from last week * 13)
Current MoM growth: 1.5% (from CEO interview)
Compound 12 months: 1.015^12 = 19.6% YoY
→ Revenue 2025: $11.96B/quarter

Industry TAM growth: 12% (from public data)
Uber's share trajectory: Flat (from market share answers)
→ Constrain growth to 15% (below 19.6% run rate)

Projected 2027 revenue: $14B/quarter = $56B/year


Step 2: Project Margins
────────────────────────
Current EBITDA margin: 12% (from CEO interview)
Historical improvement: +1.5% per year (from EDGAR)
→ 2027 margin: 12% + (1.5% * 3) = 16.5%

Constraint check:
- Current take rate: 24% (from CEO interview)
- Take rate ceiling: 28% (from industry data)
- Room to expand: Yes
→ 16.5% margin is feasible


Step 3: Project Costs
──────────────────────
Stock-based comp:
- Current: $800M/quarter = 8% of revenue
- Historical trend: -0.5% per year (from EDGAR)
- 2027: 6.5% of revenue

Regulatory:
- Current liabilities: $800M (from CEO interview)
- Annual settlements: Assume $300M/year ongoing (from public cases)


Step 4: Calculate 2027 Fair Value
──────────────────────────────────
Revenue 2027: $56B
EBITDA margin: 16.5%
EBITDA: $9.24B
Minus SBC (6.5% of rev): -$3.64B
Minus regulatory: -$0.3B
True EBITDA: $5.3B

Multiple: 15x (growth-adjusted)
Enterprise Value: $79.5B
Minus net debt: -$5B
Equity Value: $74.5B

Shares (after 3 years buybacks): 2.0B
Fair Value: $37/share
```

---

## Why This Works

### **Layer 1 (Current Reality) Benefits:**
- ✅ Removes bias (forces concrete beliefs about now, not speculation about future)
- ✅ Testable quarterly (when earnings disclosed, validate your beliefs)
- ✅ No conflation with predictions (separates "what is" from "what will be")
- ✅ Establishes baseline everyone can agree on

### **Layer 2 (Projection) Benefits:**
- ✅ Uses public data to constrain projections (not just gut feel)
- ✅ Can update when new data emerges (new EDGAR filing, competitor earnings)
- ✅ Transparent logic (can see exactly how current state → future value)
- ✅ Can run scenarios (optimistic vs pessimistic on each assumption)

---

## Example: Full Workflow

### **Step 1: Run CEO Interview (15 min)**

```bash
python3 uber_valuation_v2_ceo_mode.py
```

Answer 30 questions about current reality.

Output saved to: `uber_ceo_interview.json`

### **Step 2: Gather Public Data (30 min)**

From EDGAR:
- Last 5 quarters revenue growth
- Last 5 quarters margin trend
- SBC as % of revenue trend
- Historical buyback amounts

From Competitor Filings:
- DoorDash growth rate
- DoorDash take rate
- Industry TAM estimates

From News:
- Regulatory case status
- Autonomous vehicle partnerships

### **Step 3: Run Projection Model (Future Tool)**

```bash
python3 uber_projection_model.py
```

Loads:
- Current state (from CEO interview JSON)
- Public data (from EDGAR scraper)

Outputs:
- 2027 revenue forecast
- 2027 EBITDA forecast
- Fair value (3 years out)
- Confidence intervals based on variance in estimates

### **Step 4: Decision**

```
Current Price: $75
Fair Value (3yr): $92
→ Implied CAGR: 7%
→ Decision: Hold or buy more (if you believe the projections)
```

---

## Tools Needed

### **✅ Built:**
- Layer 1: CEO Interview (`uber_valuation_v2_ceo_mode.py`)

### **🔲 To Build:**
- Layer 2: Projection Model
  - Takes current state JSON
  - Loads public data from EDGAR
  - Projects forward using trends
  - Outputs fair value with scenarios

---

## Future Enhancement: Projection Model

```python
class UberProjectionModel:
    def __init__(self, current_state_json, edgar_data):
        self.current = load_json(current_state_json)  # From CEO interview
        self.historical = edgar_data  # From EDGAR scraper

    def project_revenue(self, years=3):
        # Use current growth rate + historical trend + TAM constraints
        pass

    def project_margins(self, years=3):
        # Use current margin + historical improvement rate
        pass

    def project_costs(self, years=3):
        # SBC trend, regulatory trend
        pass

    def calculate_fair_value(self):
        # Combine projections → terminal value → discount → fair value
        pass

    def sensitivity_analysis(self):
        # Show how each assumption affects fair value
        pass

    def scenarios(self):
        # Bull case, base case, bear case
        pass
```

---

## Key Insight

**Layer 1 (CEO interview):** Removes bias by forcing concrete beliefs about TODAY

**Layer 2 (Projection model):** Uses those beliefs + public data to predict TOMORROW

**Separation is critical:**
- Layer 1: "I believe take rate is 24% today" (testable in 3 months)
- Layer 2: "Given 24% today and industry trends, it'll be 26% in 3 years" (projection with uncertainty)

---

## Next Steps

### **1. V2 is now fixed (current reality only)**

All 30 questions ask about NOW:
- ✅ No "what will X be in 2027?"
- ✅ Only "what IS X right now?"
- ✅ Testable when next earnings disclosed

### **2. Can build Layer 2 projection model**

Would you like me to build the projection model that:
- Takes CEO interview answers
- Combines with public data (EDGAR filings)
- Projects 3 years forward
- Outputs fair value with scenarios?

---

## Status

**Layer 1:** ✅ Complete (V2 CEO Interview Mode)
**Layer 2:** 🔲 Not yet built (Projection Model)

Ready to build Layer 2 when you want it.
