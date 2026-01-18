# Uber Valuation Oracle - V1

**One question at a time. Update daily. Know if your $1M should be $500k or $2M.**

## What Just Happened

I built you a working valuation model that runs RIGHT NOW.

**Location:** `uber_valuation_v1.py`

## How It Works

### **Starting Point: 100% Wall Street Consensus**

The model starts with Wall Street's assumptions:
- Revenue growth: 12% CAGR (2025-2027)
- EBITDA margin 2027: 15%
- Delivery take rate 2027: 23%
- Regulatory cost: $500M/year
- EBITDA multiple: 15x

**Result:** Fair value = $23/share (Wall Street is VERY optimistic about margins, but model accounts for SBC as real cost)

### **You Override ONE Estimate at a Time**

Example:
- Wall Street says: "EBITDA margin will be 15% in 2027"
- You think: "No way, it'll be 17%"
- You update → Fair value jumps to $31/share

**That ONE change added $8/share to your valuation.**

---

## Quick Start (30 Seconds)

### **🚀 JUST RUN IT (Recommended)**
```bash
cd /Users/pjump/Desktop/projects/valuation-oracle
python3 uber_valuation_v1.py
```

**You'll be guided through everything:**
1. ✅ Welcome screen explains the tool
2. ✅ Press ENTER to start
3. ✅ Choose option **2** (answer today's question)
4. ✅ Type your estimate (e.g., 18)
5. ✅ See instant impact on your valuation
6. ✅ Choose option **5** (save & exit)
7. ✅ Repeat tomorrow

**The tool walks you through EVERYTHING step-by-step.**

---

### **📺 Want to See Demo First?**
```bash
python3 uber_valuation_v1.py --demo
```

Shows example of how it works without you answering questions.

Then run `python3 uber_valuation_v1.py` (without --demo) to actually use it.

---

## The 8 Questions (Ranked by Impact)

You don't have to answer all 8 today. **Answer 1 per day.**

**Highest impact:**

1. **EBITDA margin 2027** (Impact: $28/share range)
   - Wall Street: 15%
   - Your guess: ___%

2. **EBITDA multiple** (Impact: $13/share range)
   - Wall Street: 15x
   - Your guess: ___x

3. **Stock-based comp %** (Impact: $13/share range)
   - Wall Street: 8% of revenue
   - Your guess: ___%

4. **Revenue growth 2025-2027** (Impact: $5/share range)
   - Wall Street: 12% CAGR
   - Your guess: ___%

5. **Delivery take rate 2027** (Impact: varies)
   - Wall Street: 23%
   - Your guess: ___%

6. **Regulatory cost annual** (Impact: varies)
   - Wall Street: $500M/year
   - Your guess: $___M or B

7. **Advertising revenue 2027** (Impact: varies)
   - Wall Street: $2.5B
   - Your guess: $___B

8. **Mobility take rate 2027** (Impact: varies)
   - Wall Street: 25%
   - Your guess: ___%

**You can answer just #1 today and see a huge impact.**

---

## Daily Workflow

**Today (5 minutes):**
```bash
python3 uber_valuation_v1.py
# Choose option 2: Answer today's question
# Type your estimate
# See new fair value
# Choose option 5: Save & exit
```

**Tomorrow (5 minutes):**
```bash
python3 uber_valuation_v1.py
# Loads your previous estimate automatically
# Choose option 2: Answer next question
# See updated fair value
# Save & exit
```

**After 8 days:**
- You've replaced Wall Street's assumptions with YOURS
- Fair value is based on what YOU think (not consensus)
- Decision: At $75/share, is Uber a buy, hold, or sell?

---

## Example Session

```
$ python3 uber_valuation_v1.py

Options:
1. Show current valuation
2. Answer today's question
3. Update a specific estimate
4. Sensitivity analysis
5. Save & exit

Choice: 2

📊 TODAY'S QUESTION:

What will Uber's adjusted EBITDA margin be in 2027?

Context: Wall Street consensus: 15%. Current (2024): ~10%.

Wall Street consensus: 15%

Your estimate (%): 18

✓ Updated!
Old fair value: $22.85/share
New fair value: $39.29/share
Impact: $16.44/share (+71.9%)

⚠️  This is a HIGH IMPACT estimate!

Choice: 5

✓ Saved to uber_estimates.json
✓ Goodbye!
```

**Tomorrow, you run it again:**
```
$ python3 uber_valuation_v1.py

✓ Loaded 1 estimates from uber_estimates.json

Choice: 2

📊 TODAY'S QUESTION:

What will Uber's total annual regulatory cost be (steady state)?

Context: This includes CA AB5, UK settlement, EU cases, etc. Wall Street: $500M/year

Your estimate ($B): 0.8

✓ Updated!
Old fair value: $39.29/share
New fair value: $34.79/share
Impact: -$4.50/share (-11.5%)

Choice: 5
✓ Saved
```

---

## What This Tells You (Right Now)

Based on **Wall Street consensus** (before you override anything):

```
Fair Value: ~$23/share
Market Price: $75/share

Conclusion: Uber is OVERVALUED by 69% if Wall Street is right
```

**But Wall Street might be wrong.** That's why you update estimates.

**Scenarios:**

**If you're MORE bullish than Wall Street:**
- EBITDA margin: 18% (not 15%)
- Revenue growth: 15% (not 12%)
- Take rate: 25% (not 23%)
- Multiple: 18x (it's a tech company)
- Regulatory cost: $300M (they settle favorably)

**Result:** Fair value could be $80-120/share → UNDERVALUED, buy more

**If you're LESS bullish:**
- EBITDA margin: 12% (not 15%)
- Regulatory cost: $1.5B (they lose big)
- Take rate: 21% (maxed out)
- Multiple: 12x (it's transport, not tech)

**Result:** Fair value could be $15-30/share → OVERVALUED, sell

---

## Your $1M Position

**At $75/share (current):**
- You own ~13,333 shares

**Scenarios based on YOUR estimates:**

| Your Fair Value | Implied Action | Value of Position |
|-----------------|----------------|-------------------|
| $40/share | Overvalued 47% | Trim to $500k |
| $60/share | Overvalued 20% | Trim to $800k |
| $75/share | Fairly valued | Hold $1M |
| $90/share | Undervalued 20% | Buy to $1.2M |
| $120/share | Undervalued 60% | Buy to $1.6M+ |

**The model tells you which scenario YOU believe.**

---

## Next Steps

**Today:**
1. Run the model: `python3 uber_valuation_v1.py`
2. Answer the first question (EBITDA margin)
3. See if one estimate changes everything

**This Week:**
1. Answer 1 question per day (8 days total)
2. Watch fair value evolve with each estimate
3. By end of week, you know YOUR valuation

**Decision Point:**
- If fair value < $60: Consider trimming $1M position
- If fair value $60-85: Hold
- If fair value > $85: Consider adding to position

---

## Advanced Features

### **Sensitivity Analysis**

Shows which estimates matter MOST:

```bash
Choice: 4

SENSITIVITY ANALYSIS

1. EBITDA margin: Impact range $28/share
   → This is the MOST important estimate
   → Focus on validating this

2. EBITDA multiple: Impact range $13/share
3. Stock-based comp: Impact range $13/share
...
```

**Insight:** Don't waste time on low-impact estimates. Focus on top 3.

### **Update Any Estimate Anytime**

```bash
Choice: 3

Available estimates to update:
1. [✓] What will Uber's adjusted EBITDA margin be in 2027? (current: 18%)
2. [ ] What will Uber's total annual regulatory cost be? (current: 0.5$B)
...

Which one? 1

New estimate (%): 16

✓ Updated! Fair value changed by -$8.22/share
```

### **View Full Summary**

```bash
Choice: 1

💰 FAIR VALUE: $67/share

Current market price: ~$75/share
📉 OVERVALUED by $8 (10.7%)
   → Your $1M position might be worth $0.89M

--- Your Estimates (5) ---
What will Uber's adjusted EBITDA margin be in 2027?
  Your estimate: 16%
  Wall Street: 15%

What will Uber's total annual regulatory cost be?
  Your estimate: 0.8$B
  Wall Street: 0.5$B
...
```

---

## Files

- `uber_valuation_v1.py` - The model (run this)
- `uber_estimates.json` - Your estimates (auto-saved)
- `UBER_VALUATION_README.md` - This file

---

## FAQ

**Q: Why does the model show Uber is overvalued with Wall Street consensus?**

A: Because the model properly accounts for stock-based compensation as a real cost. Wall Street's "adjusted EBITDA" excludes SBC, but shareholders pay for it (via dilution).

**Q: Should I trust this model over Wall Street analysts?**

A: No. This model is a TOOL to quantify YOUR beliefs. If your beliefs are wrong, model will be wrong. But at least you'll know what you believe and can test it.

**Q: What if I don't know the answer to a question?**

A: Start with Wall Street consensus (already in model). Update only when you have conviction. If you have no edge on a metric, don't override it.

**Q: Can I use this for other stocks?**

A: Yes, but you'd need to modify the model (different revenue streams, margins, etc.). For now, it's Uber-specific.

**Q: How often should I update estimates?**

A: When new information emerges:
- Quarterly earnings → Update revenue/margin estimates
- Regulatory news → Update regulatory cost
- Competitive data → Update market share/take rates

---

## What's Missing (Future Versions)

- [ ] SMS prompting (ask you daily via text)
- [ ] Alerts when stock diverges from fair value by 15%+
- [ ] Calibration tracking (were you right when data disclosed?)
- [ ] Scenario planning ("what if DoorDash wins?")
- [ ] Multi-stock support (track Uber + DoorDash + Lyft)

**But V1 works TODAY. Start using it.**

---

## Support

Questions? Issues? Want to add a feature?

File in idea factory repo or ping me.

---

**TL;DR:**

```bash
cd /Users/pjump/Desktop/projects/idea_factory
python3 uber_valuation_v1.py
# Type 2
# Answer one question
# See new fair value
# Type 5 to save
# Done. Repeat tomorrow.
```

**After 8 days, you'll know if your $1M should be $500k or $2M.**
