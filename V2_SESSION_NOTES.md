# V2 CEO Interview Mode - Session Notes

**Date:** January 18, 2025
**Status:** Complete and ready to use

---

## What We Built

### **CEO Interview Mode - Bias Removal Tool**

Interactive valuation tool that removes bias by forcing you to commit to specific insider-level beliefs.

**Key Concept:**
- NOT about guessing accurately
- It's about quantifying what you ACTUALLY believe
- Forces internal consistency of beliefs
- Makes beliefs testable when data disclosed

**How It Works:**
1. You roleplay as Uber CEO (Dara Khosrowshahi)
2. Goldman analyst asks 30 questions only insiders know
3. You answer based on what you believe is true NOW
4. Tool calculates fair value based on YOUR answers
5. See if your beliefs imply stock is over/undervalued

---

## Files Created

```
/Users/pjump/Desktop/projects/valuation-oracle/
├── uber_valuation_v2_ceo_mode.py      # The interview tool (NEW)
├── CEO_MODE_README.md                  # Documentation (NEW)
├── V2_SESSION_NOTES.md                 # This file (NEW)
├── uber_valuation_v1.py                # Original version (still works)
├── START_HERE.md                       # Quick start (V1)
└── UBER_VALUATION_README.md            # Full docs (V1)
```

---

## Run It

```bash
cd /Users/pjump/Desktop/projects/valuation-oracle
python3 uber_valuation_v2_ceo_mode.py
```

Takes 10-15 minutes to complete the interview.

---

## The 30 Questions

Questions grouped into 11 categories:

### **1. Revenue & Growth** (3 questions)
- What was revenue last week?
- Mobility GMV growth month-over-month?
- Delivery GMV growth month-over-month?

### **2. Unit Economics** (4 questions)
- ACTUAL Mobility take rate this week?
- ACTUAL Delivery take rate this week?
- Contribution margin on Mobility?
- Contribution margin on Delivery?

### **3. Market Position** (3 questions)
- US rideshare market share right now?
- US delivery market share right now?
- DoorDash pricing vs Uber Eats?

### **4. Profitability** (3 questions)
- Quarterly stock-based comp run rate?
- Adjusted EBITDA margin this quarter?
- TRUE profit margin (EBITDA minus SBC)?

### **5. Churn & Retention** (3 questions)
- Monthly active rider growth rate?
- Driver churn rate monthly?
- Trips per active user trend?

### **6. Regulatory & Risk** (2 questions)
- Regulatory settlements next 12 months?
- Insurance cost trend?

### **7. Capital Allocation** (2 questions)
- Share buyback next 12 months?
- Quarterly capex run rate?

### **8. Autonomous Vehicles** (2 questions)
- Waymo market share in Phoenix?
- % of Uber rides autonomous by 2027?

### **9. Advertising & New Revenue** (2 questions)
- Quarterly ad revenue run rate?
- Ad revenue gross margin?

### **10. Competitive Dynamics** (2 questions)
- % of drivers also drive for DoorDash?
- % of consumers use both apps?

### **11. International** (2 questions)
- % of revenue from outside US+Canada?
- International margin vs US margin?

### **12. Other Bets** (1 question)
- Uber Freight quarterly revenue?

---

## Example Output

### **After Answering Questions:**

```
YOUR VALUATION (Based on Your Insider Beliefs)
=================================================================

💰 FAIR VALUE: $87/share

Current market price: $75/share

📈 UNDERVALUED by $12 (16.0%)
   → Based on YOUR beliefs, Uber should trade at $87
   → Your $1M position is actually worth $1.16M

🎯 ACTION: Consider buying more

--- Model Details ---
Annual Revenue: $42.3B
True EBITDA (after SBC): $4.8B
Multiple Used: 15x
Enterprise Value: $72.0B
Equity Value: $67.0B
```

### **Sensitivity Analysis:**

```
SENSITIVITY: Which Beliefs Drive Your Valuation?
=================================================================

1. What will adjusted EBITDA margin be THIS quarter?
   Impact: $15.44/share range

2. What is quarterly stock-based comp run rate?
   Impact: $11.22/share range

3. What is ACTUAL Mobility take rate this week?
   Impact: $7.44/share range
```

---

## Key Differences from V1

| Feature | V1 (Wall Street Override) | V2 (CEO Interview) |
|---------|---------------------------|-------------------|
| **Questions** | Future predictions ("What will X be in 2027?") | Current reality ("What IS X right now?") |
| **Count** | 8 questions | 30 questions |
| **Usage** | Daily updates (1 per day) | One-time interview (15 min) |
| **Baseline** | Wall Street consensus | Analyst baseline estimates |
| **Purpose** | Override future forecasts | Quantify current beliefs |
| **Testability** | Wait 3 years to validate | Validate quarterly when data disclosed |

---

## Why V2 Is Better for Bias Removal

### **Problem with V1:**
- Asks about 2027 (too far out, pure speculation)
- Only 8 questions (not comprehensive)
- Hard to validate beliefs (have to wait years)

### **Solution in V2:**
- Asks about current quarter (testable in 3 months)
- 30 questions (comprehensive view)
- Questions are what insiders actually know
- Forces concrete beliefs about reality vs vague opinions

---

## The Core Insight

**From user:**
> "it's not about guessing well, it's about guessing to take bias out of stock evaluation. if an insider actually answered we'd have a perfect valuation. but since you are not an insider it is more so properly assessing the price you should make it"

**Translation:**
- If a real insider answered these 30 questions accurately → perfect valuation
- Since you're NOT an insider, you're guessing
- But guessing forces you to commit to specific beliefs
- Seeing the valuation those beliefs imply removes bias
- You can't say "Uber is undervalued" while believing margins are 3% - the model won't let beliefs be inconsistent

---

## Use Cases

### **1. Initial Position Sizing**
Run the interview before buying Uber stock.
See what YOUR beliefs imply for fair value.
Size position accordingly.

### **2. Quarterly Updates**
After earnings, update your answers:
- Were you right about revenue?
- Was take rate higher/lower than you thought?
- Update beliefs, see new fair value

### **3. Testing Investment Thesis**
You think Uber is undervalued because of X.
Run the interview - does X actually justify higher price?
Model forces internal consistency.

### **4. Removing Bias**
You WANT Uber to be undervalued (you own it).
Interview forces you to commit to specific numbers.
Can't handwave - either margins are 15% or they're not.

---

## Technical Notes

### **Valuation Model:**

```python
# Step 1: Project annual revenue
current_quarterly_revenue = (revenue_last_week / 1000) * (365/4) / 7
annual_revenue = current_quarterly_revenue * 4 * ((1 + avg_monthly_growth) ** 12)

# Step 2: Calculate true EBITDA
ebitda = annual_revenue * (ebitda_margin_pct / 100)
true_ebitda = ebitda - sbc_annual - regulatory_cost + ad_ebitda

# Step 3: Apply multiple (depends on growth)
if user_growth > 2%: multiple = 18x
elif user_growth > 1%: multiple = 15x
else: multiple = 12x

enterprise_value = true_ebitda * multiple

# Step 4: Calculate equity value
equity_value = enterprise_value - net_debt

# Step 5: Adjust for buybacks
shares_outstanding_adjusted = shares_outstanding - (buyback_amount / market_price)

# Step 6: Per share value
fair_value = equity_value / shares_outstanding_adjusted
```

### **What Gets Weighted Most:**
1. Stock-based comp (massive impact on true profitability)
2. EBITDA margin (drives earnings)
3. Take rates (unit economics)
4. Growth rates (affects multiple)
5. Buybacks (reduces share count)

### **What Matters Less:**
- International margin differential
- Freight revenue (small)
- Capex (relatively small)

---

## Next Steps

### **Today:**
1. Run the interview
2. See your fair value
3. Compare to $75 market price
4. Decide: Buy more, hold, or trim?

### **After Q4 Earnings (Feb 2025):**
1. Load saved answers
2. Update based on disclosed data
3. See new fair value
4. Validate: Were your beliefs directionally correct?

### **Ongoing:**
Update answers when you learn new information:
- News about regulatory settlements
- Competitor pricing changes
- Autonomous vehicle progress
- Market share shifts

---

## User Feedback That Shaped V2

### **Initial Concept:**
"treat the user as an actual insider even though they are not. they are guessing the exact information that you would want from an insider."

### **Refinement:**
"what would an actual analyst be asking the ceo / cfo of uber if they promised to give the the answer to whatever they wanted to know"

### **Purpose Clarification:**
"it's not about guessing well, it's about guessing to take bias out of stock evaluation"

### **Final Confirmation:**
"yes exactly. can we build that"

---

## Files to Reference

**V2 Files:**
- `/Users/pjump/Desktop/projects/valuation-oracle/uber_valuation_v2_ceo_mode.py`
- `/Users/pjump/Desktop/projects/valuation-oracle/CEO_MODE_README.md`
- `/Users/pjump/Desktop/projects/valuation-oracle/V2_SESSION_NOTES.md`

**V1 Files (still useful):**
- `/Users/pjump/Desktop/projects/valuation-oracle/uber_valuation_v1.py`
- `/Users/pjump/Desktop/projects/valuation-oracle/START_HERE.md`

---

## Status: ✅ READY TO USE

Everything is built and documented.

Just run: `python3 uber_valuation_v2_ceo_mode.py`

---

## Key Accomplishment

Built a tool that removes bias from stock valuation by:
1. Forcing concrete beliefs about current reality (not vague future predictions)
2. Asking what only insiders would know (revenue last week, real take rates)
3. Calculating fair value based on YOUR beliefs (not Wall Street's)
4. Making beliefs testable (validate quarterly when data disclosed)
5. Showing which beliefs drive valuation (sensitivity analysis)

**This is the "bias removal" version the user wanted.**
