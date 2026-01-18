---
id: IDEA-160
collection: concepts
directory: valuation-oracle-v3
title: Valuation Oracle V3 - Analyst Method (Bias Removal via CEO Interview)
type: Tool
status: in-development
confidence: Very High
one_liner: Stock valuation tool that removes bias by treating user as company insider answering 30 analyst questions about current reality only (no future predictions)
primary_user: Individual investors with concentrated positions who want to remove bias and quantify beliefs
buyer: Self-use (individual investors), or SaaS for sophisticated investors
distribution_wedge: Personal tool, or productize as "quantified due diligence" platform
revenue_model: Personal use (trade on it), or SaaS ($99-299/mo), or sell insights
time_to_signal_days: 1
related:
- IDEA-159_valuation-oracle
- IDEA-158_uber-intelligence-engine
- IDEA-157_edgar-delta-tracker
---

# Valuation Oracle V3 - Analyst Method

**Remove bias from stock valuation by forcing concrete beliefs about current reality**

---

## Evolution of Concept

### **V1: Wall Street Override Model**
- Started with Wall Street consensus
- User overrides future predictions (e.g., "What will EBITDA margin be in 2027?")
- 8 questions, daily updates
- **Problem:** Asks about future (speculation), not current reality

### **V2: CEO Interview Mode (Initial)**
- Roleplay as CEO answering analyst questions
- 30 questions about "insider knowledge"
- **Problem:** Mixed current + future questions
- **Fixed:** Removed all future questions after user feedback

### **V3: Analyst Method (Current)**
- Based on research into what top equity analysts ACTUALLY do
- 100% current reality questions only
- Questions derived from real analyst methodology
- Two-layer approach: Current reality → Project future

---

## The Core Insight (User's Words)

> "it's not about guessing well, it's about guessing to take bias out of stock evaluation. if an insider actually answered we'd have a perfect valuation. but since you are not an insider it is more so properly assessing the price you should make it"

**Translation:**
- NOT about accuracy of predictions
- It's about **removing bias** by forcing **concrete beliefs**
- If real insider answered → perfect valuation
- Since you're not insider → forces internal consistency of YOUR beliefs
- Makes beliefs **testable** when data disclosed

---

## The Two-Layer Approach

### **Layer 1: CEO Interview (Current Reality ONLY)**

Asks: "What IS true RIGHT NOW?"

**Examples:**
- ✅ "What was revenue last week?"
- ✅ "What IS the delivery take rate today?"
- ✅ "How much did you buy back last quarter?"
- ✅ "What ARE regulatory liabilities on books now?"

**Output:** Snapshot of current state (your beliefs about today)

### **Layer 2: Projection Model (Future Prediction)**

Takes: Current state + public data (EDGAR, trends) → Projects 3 years forward

**Example:**
```
Layer 1: "Take rate IS 24% today" (your belief)
Layer 2: Given 24% today + historical trend of +0.5% per year
         → Projected 2027 take rate: 25.5%
```

**Why Separation Matters:**
- Layer 1: Testable in 3 months (when earnings disclosed)
- Layer 2: Uses your current beliefs + public data (not speculation)
- Removes bias by separating "what is" from "what will be"

---

## Research: What Top Analysts Actually Do

### **Key Findings:**

1. **Focus on 2-4 key drivers** that move stock, not every detail
2. **Ask uncomfortable questions** that probe controversial topics
3. **Force quantification** when management is vague
4. **Separate vanity metrics from what matters**
5. **Connect activity to financials** (not just "interesting facts")

### **Real Questions They Ask:**

**Not:** "How many users do you have?"
**But:** "What % of users acquired via last quarter's promo are still active? Can you maintain growth if you cut incentives in half?"

**Not:** "What's your take rate?"
**But:** "After ALL incentives, credits, refunds - what's the REAL net take rate you're realizing?"

**Not:** "What's your market share?"
**But:** "Are you gaining or losing share THIS MONTH? Which product lines? Is it price-driven or quality-driven?"

### **What They're Really After:**

**Revenue Quality:**
- Organic vs paid growth (what % of growth is from promotions?)
- Retention (cohort behavior, churn rates)
- Unit economics (CAC, LTV, payback period)
- Revenue durability (recurring vs one-time)

**Unit Economics:**
- REAL take rates after all incentives
- Contribution margin by segment
- True cost per transaction
- Segment profitability (which businesses make money?)

**Competitive Dynamics:**
- Market share trends (gaining/losing, where, why?)
- Multi-homing rates (customer switching behavior)
- Pricing power (can you raise prices without losing volume?)
- Competitive moats (barriers to entry, network effects)

**Hidden Costs:**
- Regulatory liabilities (accrued but not paid)
- Legal exposure (lawsuits, settlements)
- Off-balance sheet obligations
- Stock-based comp dilution

**Quality of Earnings:**
- Cash conversion (EBITDA → FCF)
- Accounting quality (aggressive vs conservative)
- One-time items vs recurring
- Revenue recognition (pull-forward vs sustainable)

**Management Quality:**
- Capital allocation track record
- Credibility (promises vs delivery)
- Incentive alignment
- Depth of talent (key-man risk)

---

## What I Got Wrong (Before Research)

### **My Original Questions:**

❌ "What was revenue last week?" - Too granular, too noisy
❌ "What % of drivers churn monthly?" - Can estimate from public data
❌ "What's capex run rate?" - Already disclosed in filings
❌ Multi-homing % - Interesting but doesn't drive valuation

### **What I Missed:**

- Didn't probe **WHY** (just asked WHAT)
- Didn't force **trade-offs** ("At what take rate do restaurants churn?")
- Didn't test **quality** ("Of this growth, what % is promotional?")
- Didn't validate **consistency** ("If margins improve, where's the cost cut?")

---

## The Proper Question Framework

Based on research, questions should:

1. **Drive valuation** (affect DCF inputs: growth, margins, moat)
2. **Only insiders know** (can't reverse-engineer from filings)
3. **Testable in 3 months** (when quarterly data disclosed)
4. **Separate quality from noise** (real growth vs bought growth)
5. **Reveal management credibility** (their answers vs reality)

### **Examples of GOOD Questions:**

**Revenue Quality:**
"Of this quarter's bookings growth, what % is from:
- Organic usage increase (users taking more trips)
- Promotional incentives (discounts driving temporary volume)
- Price increases (same volume, higher prices)
- New market expansion (geographic growth)

Quantify each component."

**Unit Economics:**
"After accounting for:
- Driver/restaurant incentives
- Customer promotions
- Refunds and credits
- Fraud and chargebacks
- Payment processing fees

What is your NET take rate on a typical transaction THIS WEEK?"

**Competitive Dynamics:**
"In your top 10 markets by revenue:
- Which are you gaining share? (list)
- Which are you losing share? (list)
- For those losing share: is it price-driven or product-driven?
- Can you reclaim share by matching competitor pricing, or have you lost on product quality?"

**Growth Sustainability:**
"What % of Q4 2024 revenue growth came from:
- Existing customers using more (higher frequency)
- New customers (CAC-driven acquisition)
- Price increases
- Pulling forward demand via promotions

Can you sustain this growth rate if marketing spend drops 30%?"

**Hidden Costs:**
"On your balance sheet, you have $X in 'accrued expenses and other liabilities.'
- How much of that is regulatory/legal exposure?
- What's your internal estimate of likely payout?
- When will this resolve (cases pending)?
- Is the accrued amount adequate or could it be 2x-3x higher?"

---

## The 30 Critical Questions (To Be Built)

Based on research, we need to identify the **10-30 questions that matter most** for valuation.

**Structure:**

**Tier 1: Critical (10 questions)**
- These drive 80% of valuation variance
- Examples: Real take rate, EBITDA margin, growth quality, regulatory exposure

**Tier 2: Important (15 questions)**
- Refine the model, important but not game-changing
- Examples: Segment margins, market share trends, capital allocation

**Tier 3: Contextual (10 questions)**
- Nice to know, low impact on valuation
- Examples: Product mix, international exposure

---

## Methodology: How to Build Question List

### **Step 1: Identify Valuation Drivers**

For Uber (or any stock), what are the 5-10 inputs that drive 90% of fair value?

**Example for Uber:**
1. Revenue growth (2025-2027)
2. EBITDA margin (true, after SBC)
3. Take rate (real, after all incentives)
4. Regulatory cost (annual steady-state)
5. Competitive position (market share trajectory)
6. Capital allocation (buybacks vs dilution)
7. Multiple (is this tech or transport?)

### **Step 2: For Each Driver, Ask Current Reality Question**

**Don't ask:** "What will take rate be in 2027?"
**Ask:** "What IS the real take rate today? And what % of that is from pulling forward demand via promos that will stop?"

**Don't ask:** "What will regulatory cost be?"
**Ask:** "What ARE the regulatory liabilities on your balance sheet today? What % of those do you expect to pay out in next 12 months?"

### **Step 3: Validate Questions Against Criteria**

For each question, check:
- [ ] Only insider would know the answer?
- [ ] Materially affects valuation (>$2-3/share impact)?
- [ ] Testable when next quarter disclosed?
- [ ] Reveals quality vs vanity metric?
- [ ] Can't easily estimate from public data?

If 4/5 yes → keep question
If 3/5 or less → cut it

### **Step 4: Rank by Impact**

Use sensitivity analysis:
- Vary each input by ±20%
- Calculate impact on fair value
- Rank questions by $ impact
- Focus on top 20

---

## Technical Implementation

### **Current State:**

✅ **V1 Built:** Wall Street override model (works but asks wrong questions)
✅ **V2 Built:** CEO interview mode (30 questions, but not all current reality)
✅ **V2 Fixed:** Removed future questions (100% current reality now)

🔲 **V3 To Build:** Rebuild questions based on analyst research

### **Files:**

```
/Users/pjump/Desktop/projects/valuation-oracle/
├── uber_valuation_v1.py              # Wall Street override (original)
├── uber_valuation_v2_ceo_mode.py     # CEO interview (current reality fixed)
├── uber_valuation_v3_analyst.py      # NEW: Proper analyst questions (to build)
├── CEO_MODE_README.md                # V2 docs
├── TWO_LAYER_APPROACH.md             # Explains current vs projection layers
└── ANALYST_RESEARCH.md               # Research findings (to create)
```

### **Next Steps:**

1. Document analyst research (create ANALYST_RESEARCH.md)
2. Build 10 critical questions using proper framework
3. Test with Uber CEO interview simulation
4. Validate: Do answers actually change valuation meaningfully?
5. Expand to 30 questions once core 10 proven

---

## Research Summary (From ChatGPT)

Full research document available separately, key insights:

### **What Top Analysts Do:**

1. **Deep industry expertise** - Go beyond surface data
2. **Creative research methods** - Track parking lots, power usage, app downloads
3. **Strong management access** - Private meetings, channel checks
4. **Focus on 2-4 key drivers** - Ignore noise, concentrate on what matters
5. **Out-of-box validation** - Don't trust management, verify independently

### **The Scuttlebutt Method (Philip Fisher):**

- Talk to competitors, customers, suppliers, former employees
- Ask "who do you fear most and why?"
- Gather qualitative mosaic that public data can't provide
- Warren Buffett: "You can't do too much scuttlebutt"

### **Questions That Separate Vanity from Reality:**

**Vanity:** "We have 100M users"
**Reality:** "How many are active? How many pay? What's retention?"

**Vanity:** "We're #1 in market share"
**Reality:** "By what measure? Revenue, volume, self-serving definition?"

**Vanity:** "$5B in GMV"
**Reality:** "What's your actual revenue? What's net take after all costs?"

**Vanity:** "Adjusted EBITDA of $X"
**Reality:** "What about stock comp? What's real free cash flow?"

### **Tells to Watch For (When Management Answers):**

- **Tone shift** - Defensive, hesitant, rushed = red flag
- **Dodging** - Passing to CFO quickly = discomfort
- **Euphemisms** - "Headwinds," "lumpiness" = problems
- **Qualifying language** - "We believe," "hopefully" = uncertainty
- **Long non-answers** - Deflecting to different topic = hiding something
- **Verbal tics** - "That's a great question..." = stalling

### **Real Examples:**

**Tesla Q1 2018:** Analyst asked about capital needs. Musk refused to answer ("boring, bonehead question"). Stock dropped. His evasion revealed the issue.

**UPS Q2 2024:** Analyst probed product mix. CEO admitted shift to lower-yield services (ground vs air). Revenue growth looked good, but margin pressure hidden.

**Luckin Coffee:** Investigators counted foot traffic, found sales inflation. Stock collapsed when fraud disclosed.

---

## Use Cases

### **1. Personal Position Sizing**

You own $1M in Uber stock. Questions to answer:
1. Is this position too large? Too small?
2. Should I buy more at $75? Or sell?
3. What would change my mind?

**How tool helps:**
- Forces you to commit to beliefs about current state
- Calculates fair value given YOUR beliefs (not Wall Street's)
- Shows which beliefs matter most (sensitivity)
- Makes beliefs testable (validate quarterly)

### **2. Removing Bias**

**Problem:** You WANT Uber to be undervalued (because you own it).

**Solution:** Tool forces concrete numerical commitments:
- Can't say "margins will improve" → must say "margins ARE X% today, up from Y% last quarter"
- Can't handwave → model won't let inconsistent beliefs pass
- Either take rate is 24% or it's not → pick a number

**Result:** If your fair value is $60 but stock is $75, model FORCES you to confront: Either update your beliefs or sell.

### **3. Testing Investment Thesis**

**Thesis:** "Uber is undervalued because autonomous vehicles will boost margins"

**Tool forces specificity:**
- What % of rides are AV TODAY? (Answer: 0.1%)
- What % will be AV in 12 months? (You must estimate)
- At what AV penetration % does margin improve? (Pick a number)
- What's Uber's take rate on AV rides vs human? (Estimate)

**Result:** Your thesis either holds up numerically or it doesn't. Can't hide behind vague optimism.

### **4. Quarterly Validation**

**After Q4 earnings:**
- You estimated: "Take rate is 24.2% today"
- Actual disclosed: 24.5%
- Error: -1.2% (pretty accurate!)

**Or:**
- You estimated: "Q4 revenue will be $11B"
- Actual: $9.8B
- Error: +12% (you were too bullish)

**Learning:** Track where you're right vs wrong. Adjust beliefs accordingly.

---

## Why This Wins

### **Unique Approach:**
No one else quantifies YOUR beliefs into live valuation

### **Continuous Learning:**
Calibration tracking makes you better over time

### **Actionable:**
Not just analysis - tells you when to buy/sell

### **Personal Edge:**
Your domain knowledge becomes quantifiable alpha

### **Compounding Value:**
More estimates → better calibrated → more edge

---

## Risks & Mitigations

**Risk 1: Questions are wrong (don't drive valuation)**
- **Mitigation:** Build from analyst research, validate via sensitivity analysis

**Risk 2: User estimates are noise**
- **Mitigation:** Calibration tracking shows where you're right/wrong

**Risk 3: Too complex, user abandons**
- **Mitigation:** Start with 10 critical questions, expand only if useful

**Risk 4: False confidence**
- **Mitigation:** Always show uncertainty, never "this IS the price"

---

## Success Metrics

**Week 1:**
- 10 critical questions identified (based on analyst method)
- Questions validated (each affects >$3/share in valuation)
- User answers all 10 → initial fair value

**Month 1:**
- Sensitivity analysis shows top 5 drive 80%+ of variance
- At least 1 estimate validated (quarterly data disclosed, compare)
- User makes 1 decision based on model (buy/sell/hold)

**Month 3:**
- 10+ estimates validated
- Calibration score established (accuracy %)
- User refines estimates based on what they learn
- Track: Did model-driven decisions work?

**Month 6:**
- 30 questions answered (expanded from 10 core)
- Calibration improving (learning curve)
- Fair value vs stock price divergences tracked
- Decision: Is edge real? (profitable trades?)

---

## Current Status

**What's Built:**
- ✅ V1: Wall Street override (uber_valuation_v1.py)
- ✅ V2: CEO interview mode, 30 questions, current reality only (uber_valuation_v2_ceo_mode.py)
- ✅ Research complete: What top analysts actually do
- ✅ Framework: How to build proper questions

**What's Next:**
- 🔲 Create IDEA card with all context (THIS DOCUMENT)
- 🔲 Build 10 critical questions using analyst method
- 🔲 Test questions (do they drive valuation?)
- 🔲 Build V3 with proper question set
- 🔲 Validate with real Uber data

---

## Complete Context

### **User Feedback That Shaped This:**

**Initial concept:**
"treat the user as an actual insider even though they are not. they are guessing the exact information that you would want from an insider."

**Refinement:**
"what would an actual analyst be asking the ceo / cfo of uber if they promised to give the answer to whatever they wanted to know"

**Purpose clarification:**
"it's not about guessing well, it's about guessing to take bias out of stock evaluation"

**Current reality pivot:**
"no future only current. and we might be able to predict future though from a culmination of all the public data we find and projecting that from the ceo questionaire"

**Quality check:**
"are you ultrathinking through the actual questions to ask? how do you know?"

### **What Changed:**

1. **V1 → V2:** Future predictions → Current reality
2. **V2 → V3:** Made-up questions → Analyst-researched questions
3. **Single layer → Two layers:** Current state + Public data → Future projection
4. **Generic questions → Specific probes:** "What's revenue?" → "Of this growth, what % is promotional?"

---

## Files to Reference

**Existing Code:**
- `/Users/pjump/Desktop/projects/valuation-oracle/uber_valuation_v2_ceo_mode.py`

**Documentation:**
- `/Users/pjump/Desktop/projects/valuation-oracle/TWO_LAYER_APPROACH.md`
- `/Users/pjump/Desktop/projects/valuation-oracle/CURRENT_ONLY_UPDATE.md`

**Research:**
- ChatGPT research on analyst methods (paste saved separately)

**Related IDEAs:**
- IDEA-159: Original Valuation Oracle concept
- IDEA-158: Uber Intelligence Engine
- IDEA-157: EDGAR Delta Tracker

---

## Next Actions

1. Create `/Users/pjump/Desktop/projects/valuation-oracle-v3/` directory
2. Document analyst research findings
3. Build 10 critical questions framework
4. Implement V3 with proper questions
5. Test and validate

---

**Status:** Research complete, ready to build proper V3

**Confidence:** Very High (research-backed, user-validated approach)

**Time to Signal:** 1 day (can build 10-question prototype immediately)
