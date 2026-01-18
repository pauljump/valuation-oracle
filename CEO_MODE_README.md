# Uber Valuation Oracle - CEO Interview Mode (V2)

**Remove bias from stock valuation by forcing concrete beliefs**

---

## What This Does

Forces you to commit to specific insider-level beliefs about Uber's current reality.

**NOT about guessing accurately.**
**It's about:**
- Quantifying what you ACTUALLY believe
- Removing bias by making beliefs concrete
- Seeing what price YOUR beliefs imply
- Making beliefs testable (when earnings come out, were you right?)

---

## How It Works

### **You Roleplay as Uber CEO**

A Goldman analyst asks you 30 questions only an insider would know:
- "What was revenue last week?"
- "What IS the real delivery take rate today?"
- "How much will you ACTUALLY spend on buybacks?"

### **Your Answers → Your Valuation**

The tool calculates fair value based on YOUR answers (not Wall Street's).

If fair value is $60 and stock trades at $75 → your beliefs say it's overvalued.
If fair value is $90 and stock trades at $75 → your beliefs say buy more.

---

## Run It Now

```bash
cd /Users/pjump/Desktop/projects/valuation-oracle
python3 uber_valuation_v2_ceo_mode.py
```

Takes 10-15 minutes to complete the interview.

---

## The Questions (30 Total)

Grouped by category:

### **Revenue & Growth (current reality)**
- What was revenue last week?
- What is Mobility GMV growth month-over-month?
- What is Delivery GMV growth month-over-month?

### **Unit Economics (real take rates)**
- What is ACTUAL Mobility take rate this week (after driver incentives)?
- What is ACTUAL Delivery take rate this week (after restaurant incentives)?
- What is contribution margin on rides/deliveries?

### **Market Position (current competitive reality)**
- What is Uber's rideshare market share in US right now?
- What is Uber Eats market share in US food delivery?
- How does DoorDash pricing compare to Uber Eats?

### **Profitability (true economics)**
- What is quarterly stock-based comp run rate? (REAL cost)
- What will adjusted EBITDA margin be this quarter?
- What is TRUE profit margin (EBITDA minus SBC)?

### **Churn & Retention (user/driver health)**
- What is monthly active rider growth rate?
- What % of drivers churn each month?
- Are trips per user increasing or decreasing?

### **Regulatory & Risk (real exposure)**
- How much will Uber pay in regulatory settlements next 12 months?
- Are insurance costs increasing or decreasing?

### **Capital Allocation (what you'll actually do)**
- How much will Uber spend on buybacks next 12 months?
- What is quarterly capex run rate?

### **Autonomous Vehicles (threat/opportunity)**
- What % of Phoenix rides are now Waymo?
- What % of Uber rides will be autonomous by 2027?

### **Advertising & New Revenue**
- What is quarterly ad revenue run rate right now?
- What is gross margin on ad revenue?

### **Competitive Dynamics**
- What % of Uber Eats drivers also drive for DoorDash?
- What % of consumers use both apps?

### **International Exposure**
- What % of revenue is from outside US+Canada?
- How much lower are international margins vs US?

### **Other Bets**
- What is Uber Freight revenue this quarter?

---

## Example Session

```
$ python3 uber_valuation_v2_ceo_mode.py

=================================================================
  UBER VALUATION ORACLE - CEO INTERVIEW MODE
=================================================================

🎭 ROLEPLAY: You are Dara Khosrowshahi (Uber CEO)

📊 A Goldman Sachs analyst is asking you questions.
   These are things only YOU (as CEO) would know.

🎯 PURPOSE:
   • Force yourself to commit to specific beliefs
   • Remove bias by quantifying what you ACTUALLY think
   • See what stock price your beliefs imply

Press ENTER to begin the interview...

=================================================================
QUESTION 1 of 30
=================================================================

📂 Category: Revenue & Growth

❓ What was Uber's total revenue last week?

💡 Why this matters:
   Last quarter: $9.3B over 90 days = ~$103M/day. Current run rate tells if Q4 will beat/miss.

📌 Analyst's baseline estimate: 721$M
   (If you have no opinion, use this)

✍️  Your answer ($M): 750

-------------------------------------------------------------------
✅ ANSWER RECORDED
-------------------------------------------------------------------

Initial fair value: $78.34/share

📊 Progress: 1/30 questions answered

=================================================================
MENU
=================================================================

1. 📝 Continue interview (answer next question)
2. 📊 Show current valuation
3. 📈 Sensitivity analysis (which answers matter most)
4. 🔧 Update a specific answer
5. 📋 View all your answers
6. 💾 Save & exit
q. Quit without saving

👉 Your choice: 1

[continues through all 30 questions...]
```

---

## After Completing Interview

### **See Your Valuation**

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
Shares Outstanding: 1.970B
```

### **See Which Beliefs Drive Valuation**

```
SENSITIVITY: Which Beliefs Drive Your Valuation?
=================================================================

Testing each answer at ±20% to see impact...

1. What is quarterly stock-based comp run rate RIGHT NOW?
   Your answer: 800$M
   If ±20%: Fair value ranges $81.23 - $92.45
   Impact: $11.22/share range

2. What will adjusted EBITDA margin be THIS quarter?
   Your answer: 13%
   If ±20%: Fair value ranges $79.12 - $94.56
   Impact: $15.44/share range

3. What is ACTUAL Mobility take rate this week?
   Your answer: 25%
   If ±20%: Fair value ranges $83.34 - $90.78
   Impact: $7.44/share range

💡 Focus on validating your top 5 answers above.
   They drive 80%+ of your valuation.
```

---

## What This Tells You

### **If fair value > market price:**
Your beliefs imply Uber is undervalued. Consider buying more.

### **If fair value < market price:**
Your beliefs imply Uber is overvalued. Consider trimming.

### **If fair value ≈ market price:**
Your beliefs align with market. Hold.

---

## The Key Insight

**This is NOT about being right.**

It's about quantifying what you ACTUALLY believe so you can:
1. See what that belief implies for valuation
2. Test if your beliefs are internally consistent
3. Validate beliefs when new data comes out (earnings, news)
4. Remove bias from decision-making

---

## Workflow

### **Initial Interview (15 minutes)**
```bash
python3 uber_valuation_v2_ceo_mode.py
# Answer all 30 questions
# See your fair value
# Save answers
```

### **Update When New Info Emerges**
```bash
python3 uber_valuation_v2_ceo_mode.py
# Loads previous answers
# Choose option 4 to update specific answers
# See updated valuation
```

Example: Q4 earnings come out
- Revenue was $10.1B (you guessed $9.8B)
- Take rate disclosed as 24.5% (you guessed 25%)
- Update your beliefs, see new fair value

---

## Files

- `uber_valuation_v2_ceo_mode.py` - The interview tool (run this)
- `uber_ceo_interview.json` - Your answers (auto-saved)
- `CEO_MODE_README.md` - This file

---

## Comparison to V1

**V1 (Wall Street Override):**
- Asked: "What will EBITDA margin be in 2027?"
- You override Wall Street's future predictions
- 8 questions, daily updates

**V2 (CEO Interview):**
- Asks: "What IS EBITDA margin this quarter?"
- You estimate current insider knowledge
- 30 questions, one-time interview

**V2 is better for removing bias because:**
1. Questions about current reality (not future speculation)
2. Forces concrete beliefs about things only insiders know
3. More comprehensive (30 vs 8 questions)
4. Makes beliefs testable when data disclosed

---

## Quick Start

```bash
cd /Users/pjump/Desktop/projects/valuation-oracle
python3 uber_valuation_v2_ceo_mode.py
```

**TL;DR:**
- Roleplay as Uber CEO
- Answer 30 analyst questions
- See what YOUR beliefs imply for stock price
- Remove bias by quantifying beliefs

---

## Status: ✅ READY TO USE

Just run it. Everything works.
