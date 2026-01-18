#!/usr/bin/env python3
"""
Uber Valuation Oracle - V2 CEO Interview Mode

Roleplay as Uber CEO answering analyst questions.
Forces concrete beliefs about current reality to remove bias from valuation.
"""

import json
from datetime import datetime

class UberCEOInterview:
    def __init__(self):
        # Known facts from public filings
        self.shares_outstanding = 2.1  # billion
        self.net_debt = 5.0  # $B
        self.last_quarter_revenue = 9.3  # $B (Q3 2024)
        self.market_price = 75  # $/share (current)

        # User's answers (insider knowledge estimates)
        self.answers = {}

        # Question library
        self.questions = self._build_ceo_questions()

    def _build_ceo_questions(self):
        """
        Questions a Goldman analyst would ask Uber CEO in private meeting.
        These are things only insiders know RIGHT NOW.
        """
        return [
            # === REVENUE & GROWTH (Current Reality) ===
            {
                'id': 'revenue_last_week',
                'category': 'Revenue & Growth',
                'text': 'What was Uber\'s total revenue last week?',
                'context': 'Last quarter: $9.3B over 90 days = ~$103M/day. Current run rate tells if Q4 will beat/miss.',
                'unit': '$M',
                'baseline': 103 * 7,  # ~$721M per week
                'impact_weight': 8,
            },
            {
                'id': 'mobility_gmv_growth_mom',
                'category': 'Revenue & Growth',
                'text': 'What is Mobility GMV growth rate month-over-month right now?',
                'context': 'Are rides accelerating or decelerating vs last month?',
                'unit': '%',
                'baseline': 2.0,  # 2% MoM = ~27% YoY
                'impact_weight': 7,
            },
            {
                'id': 'delivery_gmv_growth_mom',
                'category': 'Revenue & Growth',
                'text': 'What is Delivery GMV growth rate month-over-month right now?',
                'context': 'Is Uber Eats growing faster or slower than last month?',
                'unit': '%',
                'baseline': 1.5,  # 1.5% MoM = ~20% YoY
                'impact_weight': 7,
            },

            # === UNIT ECONOMICS (Real Take Rates & Margins) ===
            {
                'id': 'mobility_take_rate_current',
                'category': 'Unit Economics',
                'text': 'What is the ACTUAL Mobility take rate this week (after driver incentives)?',
                'context': 'Public filings show ~24%, but what\'s the TRUE rate after all promotions?',
                'unit': '%',
                'baseline': 24.0,
                'impact_weight': 9,
            },
            {
                'id': 'delivery_take_rate_current',
                'category': 'Unit Economics',
                'text': 'What is the ACTUAL Delivery take rate this week (after restaurant incentives)?',
                'context': 'Public filings show ~23%, but what\'s the TRUE rate after all promotions?',
                'unit': '%',
                'baseline': 23.0,
                'impact_weight': 9,
            },
            {
                'id': 'contribution_margin_mobility',
                'category': 'Unit Economics',
                'text': 'What is contribution margin on Mobility rides right now (after insurance, support)?',
                'context': 'Revenue minus direct variable costs per ride.',
                'unit': '%',
                'baseline': 65,
                'impact_weight': 8,
            },
            {
                'id': 'contribution_margin_delivery',
                'category': 'Unit Economics',
                'text': 'What is contribution margin on Delivery orders right now (after support, fraud)?',
                'context': 'Revenue minus direct variable costs per order.',
                'unit': '%',
                'baseline': 55,
                'impact_weight': 8,
            },

            # === MARKET POSITION (Current Competitive Reality) ===
            {
                'id': 'us_rideshare_market_share',
                'category': 'Market Position',
                'text': 'What is Uber\'s ACTUAL rideshare market share in the US right now?',
                'context': 'Versus Lyft. What % of all ride-hailing trips are Uber?',
                'unit': '%',
                'baseline': 74,
                'impact_weight': 6,
            },
            {
                'id': 'us_delivery_market_share',
                'category': 'Market Position',
                'text': 'What is Uber Eats ACTUAL market share in US food delivery right now?',
                'context': 'Versus DoorDash, Grubhub. What % of all food delivery orders?',
                'unit': '%',
                'baseline': 25,
                'impact_weight': 6,
            },
            {
                'id': 'doordash_pricing_vs_uber',
                'category': 'Market Position',
                'text': 'How much cheaper/expensive is DoorDash than Uber Eats on average right now?',
                'context': 'For same restaurant, same order. Positive = DoorDash more expensive.',
                'unit': '%',
                'baseline': -5,  # DoorDash 5% cheaper
                'impact_weight': 5,
            },

            # === PROFITABILITY (True Economics) ===
            {
                'id': 'stock_based_comp_run_rate',
                'category': 'Profitability',
                'text': 'What is quarterly stock-based compensation run rate RIGHT NOW?',
                'context': 'This is a REAL cost (dilutes shareholders). What\'s the current quarterly burn?',
                'unit': '$M',
                'baseline': 750,  # ~$3B/year
                'impact_weight': 10,
            },
            {
                'id': 'ebitda_margin_current_quarter',
                'category': 'Profitability',
                'text': 'What will adjusted EBITDA margin be THIS quarter?',
                'context': 'Before stock-based comp. Last quarter was ~11%. Is it improving?',
                'unit': '%',
                'baseline': 11.5,
                'impact_weight': 10,
            },
            {
                'id': 'true_profit_margin_current',
                'category': 'Profitability',
                'text': 'What is TRUE profit margin this quarter (EBITDA minus stock-based comp)?',
                'context': 'This is what actually flows to shareholders after dilution.',
                'unit': '%',
                'baseline': 3.0,  # 11.5% EBITDA - 8% SBC
                'impact_weight': 10,
            },

            # === CHURN & RETENTION (User/Driver Health) ===
            {
                'id': 'monthly_active_riders_growth',
                'category': 'Churn & Retention',
                'text': 'What is monthly active platform consumer growth rate (MoM)?',
                'context': 'Are you gaining or losing users vs last month?',
                'unit': '%',
                'baseline': 1.0,  # 1% MoM = 12.7% YoY
                'impact_weight': 7,
            },
            {
                'id': 'driver_churn_rate_monthly',
                'category': 'Churn & Retention',
                'text': 'What % of active drivers churn each month?',
                'context': 'How many drivers who drove last month won\'t drive this month?',
                'unit': '%',
                'baseline': 8,
                'impact_weight': 5,
            },
            {
                'id': 'trips_per_active_user_mom',
                'category': 'Churn & Retention',
                'text': 'Are trips per active user increasing or decreasing vs last month?',
                'context': 'Positive = users taking more trips. Negative = frequency declining.',
                'unit': '%',
                'baseline': 0.5,  # Slight increase
                'impact_weight': 6,
            },

            # === REGULATORY & RISK (Current Exposure) ===
            {
                'id': 'regulatory_liabilities_on_books',
                'category': 'Regulatory & Risk',
                'text': 'What are total outstanding regulatory liabilities on the balance sheet RIGHT NOW?',
                'context': 'CA AB5, UK employment cases, EU regulations. What\'s accrued/reserved today?',
                'unit': '$M',
                'baseline': 800,
                'impact_weight': 6,
            },
            {
                'id': 'insurance_cost_trend',
                'category': 'Regulatory & Risk',
                'text': 'Is insurance cost per trip increasing or decreasing vs last quarter?',
                'context': 'Claims, accidents, fraud. Are costs going up or down?',
                'unit': '%',
                'baseline': 2,  # 2% increase
                'impact_weight': 5,
            },

            # === CAPITAL ALLOCATION (Current Spending) ===
            {
                'id': 'share_buyback_last_quarter',
                'category': 'Capital Allocation',
                'text': 'How much did Uber spend on share buybacks last quarter?',
                'context': 'Announced $7B authorization. What was the ACTUAL buyback amount last quarter?',
                'unit': '$M',
                'baseline': 500,  # $500M per quarter
                'impact_weight': 7,
            },
            {
                'id': 'capex_run_rate',
                'category': 'Capital Allocation',
                'text': 'What is quarterly capex run rate right now?',
                'context': 'Data centers, office space, infrastructure. What are you spending?',
                'unit': '$M',
                'baseline': 100,
                'impact_weight': 3,
            },

            # === AUTONOMOUS VEHICLES (Current Reality) ===
            {
                'id': 'waymo_market_share_phoenix',
                'category': 'Autonomous Vehicles',
                'text': 'What % of rideshare trips in Phoenix are now Waymo (not Uber/Lyft)?',
                'context': 'Phoenix is Waymo\'s biggest market. How much share have they taken?',
                'unit': '%',
                'baseline': 5,
                'impact_weight': 4,
            },
            {
                'id': 'autonomous_rides_on_uber_current',
                'category': 'Autonomous Vehicles',
                'text': 'What % of Uber rides THIS WEEK are autonomous (Waymo partnership)?',
                'context': 'Uber partners with Waymo in some cities. What % of total Uber rides are AV right now?',
                'unit': '%',
                'baseline': 0.1,  # Very small currently
                'impact_weight': 3,
            },

            # === ADVERTISING & NEW REVENUE ===
            {
                'id': 'advertising_revenue_run_rate',
                'category': 'Advertising & New Revenue',
                'text': 'What is quarterly advertising revenue run rate RIGHT NOW?',
                'context': 'Restaurant ads, promoted listings. Last quarter was ~$300M. Growing?',
                'unit': '$M',
                'baseline': 350,
                'impact_weight': 7,
            },
            {
                'id': 'advertising_margin',
                'category': 'Advertising & New Revenue',
                'text': 'What is gross margin on advertising revenue?',
                'context': 'Almost pure profit, or do you have real costs to serve ads?',
                'unit': '%',
                'baseline': 85,
                'impact_weight': 6,
            },

            # === COMPETITIVE DYNAMICS ===
            {
                'id': 'driver_switching_to_doordash',
                'category': 'Competitive Dynamics',
                'text': 'What % of Uber Eats drivers also drive for DoorDash?',
                'context': 'Multi-homing weakens your pricing power with drivers.',
                'unit': '%',
                'baseline': 60,
                'impact_weight': 4,
            },
            {
                'id': 'consumer_switching_apps',
                'category': 'Competitive Dynamics',
                'text': 'What % of Uber Eats users also use DoorDash regularly?',
                'context': 'Multi-homing weakens pricing power with consumers.',
                'unit': '%',
                'baseline': 40,
                'impact_weight': 4,
            },

            # === INTERNATIONAL EXPOSURE ===
            {
                'id': 'international_revenue_pct',
                'category': 'International',
                'text': 'What % of total revenue is from outside US+Canada right now?',
                'context': 'International growth vs US maturity. Where is the future?',
                'unit': '%',
                'baseline': 35,
                'impact_weight': 5,
            },
            {
                'id': 'international_margin_vs_us',
                'category': 'International',
                'text': 'How much lower are international margins vs US margins?',
                'context': 'Negative = international is less profitable. E.g., -500 bps = 5% lower.',
                'unit': 'bps',
                'baseline': -300,  # 3% lower
                'impact_weight': 5,
            },

            # === FREIGHT & OTHER BETS ===
            {
                'id': 'freight_quarterly_revenue',
                'category': 'Other Bets',
                'text': 'What is Uber Freight revenue THIS quarter?',
                'context': 'Trucking logistics. Is it growing or dying?',
                'unit': '$M',
                'baseline': 300,
                'impact_weight': 2,
            },
        ]

    def get_question(self, idx):
        """Get question by index"""
        if 0 <= idx < len(self.questions):
            return self.questions[idx]
        return None

    def answer_question(self, question_id, value):
        """Record answer to a question"""
        self.answers[question_id] = value

    def calculate_fair_value(self):
        """
        Calculate fair value based on CEO's answers.
        This is a simplified model - real analysts use multi-page Excel.
        """

        # === 1. ESTIMATE CURRENT QUARTERLY REVENUE ===
        if 'revenue_last_week' in self.answers:
            current_quarterly_revenue = (self.answers['revenue_last_week'] / 1000) * (365/4) / 7
        else:
            current_quarterly_revenue = self.last_quarter_revenue

        # === 2. PROJECT ANNUAL REVENUE ===
        mobility_growth = self.answers.get('mobility_gmv_growth_mom', 2.0)
        delivery_growth = self.answers.get('delivery_gmv_growth_mom', 1.5)
        avg_growth_monthly = (mobility_growth + delivery_growth) / 2

        # Compound 12 months out
        annual_revenue = current_quarterly_revenue * 4 * ((1 + avg_growth_monthly/100) ** 12)

        # === 3. CALCULATE TRUE EBITDA ===
        ebitda_margin_pct = self.answers.get('ebitda_margin_current_quarter', 11.5)
        ebitda = annual_revenue * (ebitda_margin_pct / 100)

        # Subtract stock-based comp (REAL cost)
        sbc_quarterly = self.answers.get('stock_based_comp_run_rate', 750) / 1000  # Convert to $B
        sbc_annual = sbc_quarterly * 4

        true_ebitda = ebitda - sbc_annual

        # Subtract regulatory costs (current liabilities)
        regulatory_cost = self.answers.get('regulatory_liabilities_on_books', 800) / 1000
        true_ebitda -= regulatory_cost

        # === 4. ADD HIGH-MARGIN ADVERTISING ===
        ad_revenue_quarterly = self.answers.get('advertising_revenue_run_rate', 350) / 1000
        ad_revenue_annual = ad_revenue_quarterly * 4
        ad_margin = self.answers.get('advertising_margin', 85) / 100

        ad_ebitda = ad_revenue_annual * ad_margin
        true_ebitda += ad_ebitda

        # === 5. APPLY MULTIPLE ===
        # Multiple depends on growth and market position
        user_growth = self.answers.get('monthly_active_riders_growth', 1.0)

        if user_growth > 2.0:
            multiple = 18  # High growth
        elif user_growth > 1.0:
            multiple = 15  # Medium growth
        else:
            multiple = 12  # Low growth

        enterprise_value = true_ebitda * multiple

        # === 6. SUBTRACT DEBT, ADD BUYBACK IMPACT ===
        equity_value = enterprise_value - self.net_debt

        # Account for buybacks (reduces share count)
        # Project annual buyback from last quarter's run rate
        buyback_quarterly = self.answers.get('share_buyback_last_quarter', 500) / 1000  # Convert to $B
        buyback_annual = buyback_quarterly * 4
        shares_bought_back = buyback_annual / self.market_price
        shares_outstanding_adjusted = self.shares_outstanding - shares_bought_back

        # === 7. PER SHARE VALUE ===
        fair_value_per_share = equity_value / shares_outstanding_adjusted

        return {
            'fair_value_per_share': round(fair_value_per_share, 2),
            'annual_revenue': round(annual_revenue, 2),
            'true_ebitda': round(true_ebitda, 2),
            'enterprise_value': round(enterprise_value, 2),
            'equity_value': round(equity_value, 2),
            'multiple_used': multiple,
            'shares_outstanding': round(shares_outstanding_adjusted, 3),
        }

    def show_valuation(self):
        """Display current valuation based on answers"""
        val = self.calculate_fair_value()

        print("\n" + "="*70)
        print("YOUR VALUATION (Based on Your Insider Beliefs)")
        print("="*70)

        print(f"\n💰 FAIR VALUE: ${val['fair_value_per_share']}/share")
        print(f"\nCurrent market price: ${self.market_price}/share")

        diff = val['fair_value_per_share'] - self.market_price
        diff_pct = (diff / self.market_price) * 100

        if diff > 10:
            print(f"\n📈 UNDERVALUED by ${abs(diff):.2f} ({abs(diff_pct):.1f}%)")
            print(f"   → Based on YOUR beliefs, Uber should trade at ${val['fair_value_per_share']}")
            print(f"   → Your $1M position is actually worth ${1 + (diff_pct/100):.2f}M")
            print(f"\n🎯 ACTION: Consider buying more")
        elif diff < -10:
            print(f"\n📉 OVERVALUED by ${abs(diff):.2f} ({abs(diff_pct):.1f}%)")
            print(f"   → Based on YOUR beliefs, Uber should trade at ${val['fair_value_per_share']}")
            print(f"   → Your $1M position is actually worth ${1 + (diff_pct/100):.2f}M")
            print(f"\n⚠️  ACTION: Consider trimming position")
        else:
            print(f"\n🎯 FAIRLY VALUED (within 10% of your fair value)")
            print(f"\n✓ ACTION: Hold current position")

        print(f"\n--- Model Details ---")
        print(f"Annual Revenue: ${val['annual_revenue']}B")
        print(f"True EBITDA (after SBC): ${val['true_ebitda']}B")
        print(f"Multiple Used: {val['multiple_used']}x")
        print(f"Enterprise Value: ${val['enterprise_value']}B")
        print(f"Equity Value: ${val['equity_value']}B")
        print(f"Shares Outstanding: {val['shares_outstanding']}B")

        print("\n" + "="*70)

    def sensitivity_analysis(self):
        """Show which beliefs matter most"""
        base_val = self.calculate_fair_value()['fair_value_per_share']

        print("\n" + "="*70)
        print("SENSITIVITY: Which Beliefs Drive Your Valuation?")
        print("="*70)
        print("\nTesting each answer at ±20% to see impact...\n")

        impacts = []

        for q in self.questions:
            if q['id'] not in self.answers:
                continue

            original = self.answers[q['id']]

            # Test +20%
            self.answers[q['id']] = original * 1.2
            val_high = self.calculate_fair_value()['fair_value_per_share']

            # Test -20%
            self.answers[q['id']] = original * 0.8
            val_low = self.calculate_fair_value()['fair_value_per_share']

            # Restore
            self.answers[q['id']] = original

            impact_range = val_high - val_low

            impacts.append({
                'question': q['text'][:55] + '...' if len(q['text']) > 55 else q['text'],
                'current': f"{original}{q['unit']}",
                'impact': abs(impact_range),
                'low': val_low,
                'high': val_high,
            })

        # Sort by impact
        impacts.sort(key=lambda x: x['impact'], reverse=True)

        for i, imp in enumerate(impacts[:8], 1):
            print(f"{i}. {imp['question']}")
            print(f"   Your answer: {imp['current']}")
            print(f"   If ±20%: Fair value ranges ${imp['low']:.2f} - ${imp['high']:.2f}")
            print(f"   Impact: ${imp['impact']:.2f}/share range")
            print()

        print("="*70)
        print("\n💡 Focus on validating your top 5 answers above.")
        print("   These drive 80%+ of your valuation.\n")

    def save_state(self, filename='uber_ceo_interview.json'):
        """Save answers"""
        data = {
            'timestamp': datetime.now().isoformat(),
            'answers': self.answers,
            'fair_value': self.calculate_fair_value()['fair_value_per_share'],
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\n✓ Saved {len(self.answers)} answers to {filename}")

    def load_state(self, filename='uber_ceo_interview.json'):
        """Load previous answers"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.answers = data['answers']
            print(f"\n✓ Loaded {len(self.answers)} previous answers")
            return True
        except FileNotFoundError:
            return False


def interactive_interview():
    """Run the CEO interview"""
    interview = UberCEOInterview()

    # Try to load previous session
    is_first_time = not interview.load_state()

    print("\n" + "="*70)
    print("  UBER VALUATION ORACLE - CEO INTERVIEW MODE")
    print("="*70)

    if is_first_time:
        print("\n🎭 ROLEPLAY: You are Dara Khosrowshahi (Uber CEO)")
        print("\n📊 A Goldman Sachs analyst is asking you questions.")
        print("   These are things only YOU (as CEO) would know.")
        print("\n🎯 PURPOSE:")
        print("   • Force yourself to commit to specific beliefs")
        print("   • Remove bias by quantifying what you ACTUALLY think")
        print("   • See what stock price your beliefs imply")
        print("\n⚠️  This is NOT about guessing accurately.")
        print("   It's about removing bias and making beliefs testable.")
        print("\n📝 There are ~30 questions covering:")
        print("   • Current revenue & growth")
        print("   • Real take rates & margins")
        print("   • Market share & competition")
        print("   • True profitability (including stock-based comp)")
        print("   • Regulatory risks")
        print("   • Capital allocation")
        print("\n⏱️  Takes 10-15 minutes to complete.")
        print("   You can save and come back anytime.")

        print("\n" + "-"*70)
        input("\nPress ENTER to begin the interview...")

    # Main loop
    while True:
        print("\n" + "="*70)
        print("MENU")
        print("="*70)
        print("\n1. 📝 Continue interview (answer next question)")
        print("2. 📊 Show current valuation")
        print("3. 📈 Sensitivity analysis (which answers matter most)")
        print("4. 🔧 Update a specific answer")
        print("5. 📋 View all your answers")
        print("6. 💾 Save & exit")
        print("q. Quit without saving")

        choice = input("\n👉 Your choice: ").strip()

        if choice == '1':
            # Find next unanswered question
            next_idx = None
            for i, q in enumerate(interview.questions):
                if q['id'] not in interview.answers:
                    next_idx = i
                    break

            if next_idx is None:
                print("\n" + "="*70)
                print("✅ INTERVIEW COMPLETE!")
                print("="*70)
                print("\nYou've answered all questions.")
                print("Your valuation is now based 100% on YOUR beliefs.\n")
                interview.show_valuation()
                print("\n💡 TIP: Use option 3 to see which beliefs drive your valuation most.")
                continue

            q = interview.questions[next_idx]
            answered = len(interview.answers)
            total = len(interview.questions)

            print("\n" + "="*70)
            print(f"QUESTION {answered + 1} of {total}")
            print("="*70)
            print(f"\n📂 Category: {q['category']}")
            print(f"\n❓ {q['text']}")
            print(f"\n💡 Why this matters:")
            print(f"   {q['context']}")
            print(f"\n📌 Analyst's baseline estimate: {q['baseline']}{q['unit']}")
            print(f"   (If you have no opinion, use this)")

            try:
                answer = float(input(f"\n✍️  Your answer ({q['unit']}): "))

                old_val = interview.calculate_fair_value()['fair_value_per_share'] if len(interview.answers) > 0 else 75

                interview.answer_question(q['id'], answer)

                new_val = interview.calculate_fair_value()['fair_value_per_share']
                impact = new_val - old_val

                print("\n" + "-"*70)
                print("✅ ANSWER RECORDED")
                print("-"*70)

                if len(interview.answers) > 1:
                    print(f"\nFair value before: ${old_val:.2f}/share")
                    print(f"Fair value now:    ${new_val:.2f}/share")
                    print(f"Impact:            ${impact:+.2f}/share")

                    if abs(impact) > 5:
                        print(f"\n🔥 HIGH IMPACT belief! This changed valuation by ${abs(impact):.0f}/share")
                else:
                    print(f"\nInitial fair value: ${new_val:.2f}/share")

                print(f"\n📊 Progress: {len(interview.answers)}/{len(interview.questions)} questions answered")

            except ValueError:
                print("\n❌ Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\n\n⏸️  Skipping this question...")

        elif choice == '2':
            if len(interview.answers) == 0:
                print("\n⚠️  You haven't answered any questions yet.")
                print("   Choose option 1 to start the interview.")
            else:
                interview.show_valuation()

        elif choice == '3':
            if len(interview.answers) < 3:
                print("\n⚠️  Answer at least 3 questions first to see sensitivity analysis.")
            else:
                interview.sensitivity_analysis()

        elif choice == '4':
            if len(interview.answers) == 0:
                print("\n⚠️  No answers to update yet.")
                continue

            print("\nYour answers so far:")
            for i, q in enumerate(interview.questions, 1):
                if q['id'] in interview.answers:
                    print(f"{i}. {q['text'][:50]}... = {interview.answers[q['id']]}{q['unit']}")

            try:
                idx = int(input("\nWhich question? (number): ")) - 1
                q = interview.questions[idx]

                if q['id'] not in interview.answers:
                    print("\n⚠️  You haven't answered that question yet.")
                    continue

                print(f"\n{q['text']}")
                print(f"Current answer: {interview.answers[q['id']]}{q['unit']}")

                new_answer = float(input(f"New answer ({q['unit']}): "))

                old_val = interview.calculate_fair_value()['fair_value_per_share']
                interview.answers[q['id']] = new_answer
                new_val = interview.calculate_fair_value()['fair_value_per_share']

                print(f"\n✓ Updated! Fair value changed by ${new_val - old_val:+.2f}/share")

            except (ValueError, IndexError):
                print("\n❌ Invalid input.")

        elif choice == '5':
            print("\n" + "="*70)
            print("YOUR ANSWERS")
            print("="*70)

            # Group by category
            by_category = {}
            for q in interview.questions:
                if q['id'] in interview.answers:
                    cat = q['category']
                    if cat not in by_category:
                        by_category[cat] = []
                    by_category[cat].append({
                        'text': q['text'],
                        'answer': interview.answers[q['id']],
                        'unit': q['unit'],
                        'baseline': q['baseline'],
                    })

            for cat, items in by_category.items():
                print(f"\n📂 {cat}")
                for item in items:
                    diff = item['answer'] - item['baseline']
                    marker = "🔼" if diff > 0 else "🔽" if diff < 0 else "➡️"
                    print(f"   {marker} {item['text']}")
                    print(f"      Your answer: {item['answer']}{item['unit']} (baseline: {item['baseline']}{item['unit']})")

            print("\n" + "="*70)

        elif choice == '6':
            interview.save_state()
            if len(interview.answers) > 0:
                print("\n📊 Final Valuation:")
                interview.show_valuation()
            print("\n✓ See you next time!\n")
            break

        elif choice == 'q':
            print("\n⚠️  Exiting without saving.\n")
            break


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        print("\n" + "="*70)
        print("DEMO MODE")
        print("="*70)
        print("\nThis shows what the CEO Interview looks like.")
        print("Run without --demo to actually use the tool.\n")

        interview = UberCEOInterview()

        # Show first 3 questions
        for i in range(3):
            q = interview.questions[i]
            print(f"\n--- Question {i+1} ---")
            print(f"{q['text']}")
            print(f"Context: {q['context']}")
            print(f"Baseline: {q['baseline']}{q['unit']}\n")

        print("... and 27 more questions\n")
        print("Ready to start? Run: python3 uber_valuation_v2_ceo_mode.py\n")
    else:
        interactive_interview()
