# Which Version Should I Use?

Two versions available:

---

## **V2: CEO Interview Mode** ⭐ RECOMMENDED

**Use this if you want to:**
- Remove bias from your stock evaluation
- Quantify what you ACTUALLY believe about Uber
- Answer questions like a CEO would
- Test beliefs quarterly when data disclosed

**What it does:**
You roleplay as Uber CEO answering 30 analyst questions about current reality:
- "What was revenue last week?"
- "What IS the real take rate today?"
- "How much will you ACTUALLY buy back?"

**Run it:**
```bash
python3 uber_valuation_v2_ceo_mode.py
```

**Time:** 10-15 minutes (one-time interview)

**Read more:** `CEO_MODE_README.md`

---

## **V1: Wall Street Override**

**Use this if you want to:**
- Override Wall Street's future predictions
- Answer one question per day (8 days total)
- Focus on 2027 forecasts

**What it does:**
Starts with Wall Street consensus, lets you override one estimate at a time:
- "What will EBITDA margin be in 2027?"
- "What will take rate be in 2027?"

**Run it:**
```bash
python3 uber_valuation_v1.py
```

**Time:** 1-2 minutes per day (8 questions total)

**Read more:** `START_HERE.md`

---

## **Quick Comparison**

| Feature | V1 | V2 ⭐ |
|---------|----|----|
| **Questions** | Future predictions | Current reality |
| **Count** | 8 questions | 30 questions |
| **Time** | 1-2 min/day for 8 days | 15 min one-time |
| **Testability** | Wait 3 years | Validate quarterly |
| **Bias Removal** | Moderate | High |
| **Comprehensiveness** | Basic | Detailed |

---

## **Recommendation**

**Use V2 (CEO Interview Mode)** unless you specifically want the daily habit of V1.

V2 is better for:
- Removing bias (forces concrete beliefs about reality)
- Comprehensiveness (30 vs 8 questions)
- Testability (can validate in 3 months, not 3 years)
- Internal consistency (model won't let beliefs contradict)

---

## **Can I Use Both?**

Yes! They're independent:
- V1 saves to `uber_estimates.json`
- V2 saves to `uber_ceo_interview.json`

You can run both and compare the results.

---

## **Quick Start**

### **For V2 (Recommended):**
```bash
cd /Users/pjump/Desktop/projects/valuation-oracle
python3 uber_valuation_v2_ceo_mode.py
```

### **For V1:**
```bash
cd /Users/pjump/Desktop/projects/valuation-oracle
python3 uber_valuation_v1.py
```

---

**TL;DR: Use V2 unless you want the daily habit of V1**
