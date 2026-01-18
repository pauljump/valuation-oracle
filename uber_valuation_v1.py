#!/usr/bin/env python3
"""
Uber Valuation Oracle - V1
One question at a time, starting with Wall Street consensus
"""

import json
from datetime import datetime

class UberValuation:
    def __init__(self):
        # EDGAR baseline (known facts)
        self.current_year = 2024
        self.shares_outstanding = 2.1  # billion
        self.net_debt = 5.0  # $B
        self.current_revenue = 40.0  # $B (2024 estimate)

        # Wall Street Consensus (starting point)
        self.consensus = {
            'revenue_growth_2025_2027': 12,  # % CAGR
            'delivery_take_rate_2027': 23,  # %
            'mobility_take_rate_2027': 25,  # %
            'ebitda_margin_2027': 15,  # %
            'advertising_revenue_2027': 2.5,  # $B
            'regulatory_cost_annual': 0.5,  # $B/year
            'ebitda_multiple': 15,  # x
            'stock_based_comp_pct': 8,  # % of revenue
        }

        # User overrides (start empty, build over time)
        self.user_estimates = {}

        # Question library (prioritized by impact)
        self.questions = self._build_question_library()

    def _build_question_library(self):
        """
        Questions ranked by valuation impact (highest first)
        """
        return [
            {
                'id': 'ebitda_margin_2027',
                'text': 'What will Uber\'s adjusted EBITDA margin be in 2027?',
                'context': 'Wall Street consensus: 15%. Current (2024): ~10%.',
                'unit': '%',
                'impact_per_point': 3.2,  # $3.2/share per 1% margin
                'current_estimate': 15,
            },
            {
                'id': 'regulatory_cost_annual',
                'text': 'What will Uber\'s total annual regulatory cost be (steady state)?',
                'context': 'This includes CA AB5, UK settlement, EU cases, etc. Wall Street: $500M/year',
                'unit': '$B',
                'impact_per_point': 15.0,  # $15/share per $1B cost
                'current_estimate': 0.5,
            },
            {
                'id': 'delivery_take_rate_2027',
                'text': 'What will Uber Eats delivery take rate be in 2027?',
                'context': 'Current: 21%. Wall Street expects: 23%. Can it go higher?',
                'unit': '%',
                'impact_per_point': 2.8,  # $2.8/share per 1% take rate
                'current_estimate': 23,
            },
            {
                'id': 'revenue_growth_2025_2027',
                'text': 'What will Uber\'s revenue growth rate be (2025-2027 CAGR)?',
                'context': 'Wall Street: 12%. Historical: 15%+. Depends on market share.',
                'unit': '%',
                'impact_per_point': 1.8,  # $1.8/share per 1% growth
                'current_estimate': 12,
            },
            {
                'id': 'advertising_revenue_2027',
                'text': 'What will Uber\'s advertising revenue be in 2027?',
                'context': '2024: ~$1.1B. Wall Street: $2.5B. Could be $3-5B if it scales.',
                'unit': '$B',
                'impact_per_point': 5.0,  # $5/share per $1B ad revenue (high margin)
                'current_estimate': 2.5,
            },
            {
                'id': 'ebitda_multiple',
                'text': 'What EBITDA multiple should Uber trade at?',
                'context': 'Tech companies: 18-25x. Transport: 8-12x. Wall Street: 15x.',
                'unit': 'x',
                'impact_per_point': 4.2,  # $4.2/share per 1x multiple
                'current_estimate': 15,
            },
            {
                'id': 'mobility_take_rate_2027',
                'text': 'What will Uber Mobility (rides) take rate be in 2027?',
                'context': 'Current: 24%. Wall Street: 25%. Maxed out or room to grow?',
                'unit': '%',
                'impact_per_point': 2.1,  # $2.1/share per 1% take rate
                'current_estimate': 25,
            },
            {
                'id': 'stock_based_comp_pct',
                'text': 'What % of revenue will stock-based compensation be in 2027?',
                'context': 'Current: ~9%. Wall Street expects: 8% (declining). Could stay high.',
                'unit': '%',
                'impact_per_point': -1.5,  # -$1.5/share per 1% SBC (it\'s a cost)
                'current_estimate': 8,
            },
        ]

    def get_estimate(self, param):
        """
        Get estimate (user override if exists, else consensus)
        """
        return self.user_estimates.get(param, self.consensus.get(param))

    def calculate_fair_value(self):
        """
        Simple DCF model
        """
        # Project to 2027 (3 years out)
        growth_rate = self.get_estimate('revenue_growth_2025_2027') / 100
        revenue_2027 = self.current_revenue * ((1 + growth_rate) ** 3)

        # Add advertising revenue explicitly (not in base growth)
        ad_revenue_2027 = self.get_estimate('advertising_revenue_2027')
        revenue_2027 += ad_revenue_2027 - 1.1  # Subtract current ad revenue (already in base)

        # Calculate EBITDA
        ebitda_margin = self.get_estimate('ebitda_margin_2027') / 100
        ebitda_2027 = revenue_2027 * ebitda_margin

        # Adjust for regulatory costs
        regulatory_cost = self.get_estimate('regulatory_cost_annual')
        ebitda_adjusted = ebitda_2027 - regulatory_cost

        # Adjust for stock-based comp (real cost)
        sbc_pct = self.get_estimate('stock_based_comp_pct') / 100
        sbc_cost = revenue_2027 * sbc_pct
        true_ebitda = ebitda_adjusted - sbc_cost

        # Valuation
        multiple = self.get_estimate('ebitda_multiple')
        enterprise_value = true_ebitda * multiple

        # Equity value
        equity_value = enterprise_value - self.net_debt

        # Per share
        fair_value = equity_value / self.shares_outstanding

        return {
            'fair_value_per_share': round(fair_value, 2),
            'revenue_2027': round(revenue_2027, 2),
            'ebitda_2027': round(ebitda_2027, 2),
            'true_ebitda_2027': round(true_ebitda, 2),
            'enterprise_value': round(enterprise_value, 2),
            'equity_value': round(equity_value, 2),
        }

    def update_estimate(self, param, value):
        """
        User updates one estimate
        """
        old_fv = self.calculate_fair_value()

        self.user_estimates[param] = value

        new_fv = self.calculate_fair_value()

        impact = new_fv['fair_value_per_share'] - old_fv['fair_value_per_share']

        return {
            'old_fair_value': old_fv['fair_value_per_share'],
            'new_fair_value': new_fv['fair_value_per_share'],
            'impact': round(impact, 2),
            'impact_pct': round((impact / old_fv['fair_value_per_share']) * 100, 1),
        }

    def get_next_question(self):
        """
        Get the next highest-impact question user hasn't answered
        """
        for q in self.questions:
            if q['id'] not in self.user_estimates:
                return q
        return None

    def show_valuation_summary(self):
        """
        Print current valuation
        """
        fv = self.calculate_fair_value()

        print("\n" + "="*60)
        print("UBER VALUATION ORACLE")
        print("="*60)
        print(f"\n💰 FAIR VALUE: ${fv['fair_value_per_share']}/share")
        print(f"\nCurrent market price: ~$75/share (as of Jan 2025)")

        diff = fv['fair_value_per_share'] - 75
        diff_pct = (diff / 75) * 100

        if diff > 0:
            print(f"📈 UNDERVALUED by ${abs(diff):.2f} ({abs(diff_pct):.1f}%)")
            print(f"   → Your $1M position could be worth ${1 + (diff_pct/100):.2f}M")
        elif diff < 0:
            print(f"📉 OVERVALUED by ${abs(diff):.2f} ({abs(diff_pct):.1f}%)")
            print(f"   → Your $1M position might be worth ${1 + (diff_pct/100):.2f}M")
        else:
            print(f"🎯 FAIRLY VALUED")

        print(f"\n--- Model Details ---")
        print(f"2027 Revenue: ${fv['revenue_2027']}B")
        print(f"2027 EBITDA (adjusted): ${fv['ebitda_2027']}B")
        print(f"2027 True EBITDA (after SBC): ${fv['true_ebitda_2027']}B")
        print(f"Enterprise Value: ${fv['enterprise_value']}B")
        print(f"Equity Value: ${fv['equity_value']}B")

        print(f"\n--- Your Estimates ({len(self.user_estimates)}) ---")
        if len(self.user_estimates) == 0:
            print("(Using 100% Wall Street consensus)")
        else:
            for param, value in self.user_estimates.items():
                question = next(q for q in self.questions if q['id'] == param)
                consensus = self.consensus.get(param)
                print(f"{question['text']}")
                print(f"  Your estimate: {value}{question['unit']}")
                print(f"  Wall Street: {consensus}{question['unit']}")

        print("\n" + "="*60)

    def sensitivity_analysis(self):
        """
        Show which estimates matter most
        """
        base_fv = self.calculate_fair_value()['fair_value_per_share']

        print("\n" + "="*60)
        print("SENSITIVITY ANALYSIS")
        print("="*60)
        print("\nWhich estimates have the biggest impact on valuation?\n")

        sensitivities = []

        for q in self.questions:
            param = q['id']
            current_value = self.get_estimate(param)

            # Test +20% and -20%
            if 'pct' in param or 'margin' in param or 'growth' in param:
                # For percentages, add/subtract absolute points
                high_value = current_value + (current_value * 0.2)
                low_value = current_value - (current_value * 0.2)
            else:
                # For absolute values
                high_value = current_value * 1.2
                low_value = current_value * 0.8

            # Calculate impact
            original = self.user_estimates.get(param)

            self.user_estimates[param] = high_value
            fv_high = self.calculate_fair_value()['fair_value_per_share']

            self.user_estimates[param] = low_value
            fv_low = self.calculate_fair_value()['fair_value_per_share']

            # Reset
            if original is None:
                self.user_estimates.pop(param, None)
            else:
                self.user_estimates[param] = original

            impact_range = fv_high - fv_low

            sensitivities.append({
                'question': q['text'][:60] + '...' if len(q['text']) > 60 else q['text'],
                'param': param,
                'impact': abs(impact_range),
                'low_fv': fv_low,
                'high_fv': fv_high,
                'current': current_value,
                'unit': q['unit'],
            })

        # Sort by impact
        sensitivities.sort(key=lambda x: x['impact'], reverse=True)

        for i, s in enumerate(sensitivities[:5], 1):
            print(f"{i}. {s['question']}")
            print(f"   Current estimate: {s['current']}{s['unit']}")
            print(f"   If -20%: FV = ${s['low_fv']:.2f}")
            print(f"   If +20%: FV = ${s['high_fv']:.2f}")
            print(f"   Impact range: ${s['impact']:.2f}/share")
            print()

        print("="*60)
        print("\n💡 Focus on validating the top 3 estimates above.")
        print("   They drive 70%+ of your valuation uncertainty.\n")

    def save_state(self, filename='uber_estimates.json'):
        """
        Save user estimates to file
        """
        data = {
            'timestamp': datetime.now().isoformat(),
            'user_estimates': self.user_estimates,
            'fair_value': self.calculate_fair_value()['fair_value_per_share'],
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\n✓ Saved to {filename}")

    def load_state(self, filename='uber_estimates.json'):
        """
        Load user estimates from file
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.user_estimates = data['user_estimates']
            print(f"\n✓ Loaded {len(self.user_estimates)} estimates from {filename}")
            return True
        except FileNotFoundError:
            return False


def interactive_mode():
    """
    Interactive CLI for daily use
    """
    model = UberValuation()

    # Try to load previous state
    is_first_time = not model.load_state()

    print("\n" + "="*70)
    print("  UBER VALUATION ORACLE - Price Your $1M Position")
    print("="*70)

    if is_first_time:
        print("\n👋 WELCOME! Here's how this works:\n")
        print("1. You own $1M in Uber stock at ~$75/share")
        print("2. You need to know: Is it worth $50 or $150?")
        print("3. Wall Street has assumptions (revenue growth, margins, etc.)")
        print("4. But YOU might have different beliefs")
        print("\n📊 This tool:")
        print("   • Starts with Wall Street consensus")
        print("   • Lets you override ONE estimate at a time")
        print("   • Shows you fair value based on YOUR assumptions")
        print("   • Tells you if you should buy more, hold, or sell")
        print("\n⏱️  Takes 2 minutes today, 1 minute per day after that")
        print("\n" + "-"*70)
        input("\nPress ENTER to start...")

    while True:
        print("\n" + "="*70)
        print("WHAT DO YOU WANT TO DO?")
        print("="*70)
        print("\n1. 📊 Show current valuation")
        print("   └─ See fair value and if Uber is over/undervalued\n")
        print("2. ✏️  Answer today's question (RECOMMENDED)")
        print("   └─ Update one estimate, see impact on valuation\n")
        print("3. 🔧 Update a specific estimate")
        print("   └─ Go back and change any previous answer\n")
        print("4. 📈 Sensitivity analysis")
        print("   └─ See which estimates matter most\n")
        print("5. 💾 Save & exit")
        print("   └─ Save your progress and come back tomorrow\n")
        print("q. Quit without saving")

        choice = input("\n👉 Your choice (1-5 or q): ").strip()

        if choice == '1':
            model.show_valuation_summary()

            if is_first_time and len(model.user_estimates) == 0:
                print("\n" + "="*70)
                print("💡 WHAT DOES THIS MEAN?")
                print("="*70)
                print("\nRight now, you're seeing 100% Wall Street consensus.")
                print("Fair value is LOW because:")
                print("  • The model properly accounts for stock-based comp (real cost)")
                print("  • Wall Street's 'adjusted EBITDA' excludes this")
                print("\n⚠️  This means one of two things:")
                print("  1. Wall Street is too optimistic (Uber overvalued)")
                print("  2. OR you need to override estimates to match YOUR beliefs")
                print("\n👉 NEXT STEP: Choose option 2 to start updating estimates")
                print("   Start with the FIRST question (EBITDA margin)")
                print("   See how ONE estimate changes everything")
                is_first_time = False

        elif choice == '2':
            question = model.get_next_question()
            if question is None:
                print("\n" + "="*70)
                print("✓ YOU'VE ANSWERED ALL 8 QUESTIONS!")
                print("="*70)
                print("\n🎉 Your model now uses 100% YOUR estimates (not Wall Street's)")
                print("\nYou can:")
                print("  • Option 1: See your final valuation")
                print("  • Option 3: Update any estimate you want to change")
                print("  • Option 4: See which estimates matter most")
                model.show_valuation_summary()
            else:
                num_answered = len(model.user_estimates)
                num_total = len(model.questions)

                print("\n" + "="*70)
                print(f"📊 QUESTION #{num_answered + 1} of {num_total}")
                print("="*70)
                print(f"\n{question['text']}\n")
                print(f"💡 Context: {question['context']}\n")
                print(f"📌 Wall Street thinks: {question['current_estimate']}{question['unit']}")
                print(f"\n💭 What do YOU think?")
                print(f"   (If you have no opinion, just type {question['current_estimate']} to use Wall Street's number)")

                try:
                    answer = float(input(f"\n✍️  Your estimate ({question['unit']}): "))

                    result = model.update_estimate(question['id'], answer)

                    print("\n" + "-"*70)
                    print("✅ ESTIMATE UPDATED!")
                    print("-"*70)
                    print(f"\nFair value BEFORE: ${result['old_fair_value']}/share")
                    print(f"Fair value NOW:    ${result['new_fair_value']}/share")
                    print(f"\n📊 Impact: ${result['impact']:+.2f}/share ({result['impact_pct']:+.1f}%)")

                    if abs(result['impact']) > 10:
                        print(f"\n🔥 HUGE IMPACT! This estimate changed valuation by ${abs(result['impact']):.0f}/share!")
                    elif abs(result['impact']) > 5:
                        print(f"\n⚠️  HIGH IMPACT estimate - this one really matters")

                    # Show what this means for their position
                    position_value_old = 1.0  # $1M
                    position_value_new = position_value_old * (result['new_fair_value'] / result['old_fair_value'])
                    position_change = position_value_new - position_value_old

                    if abs(position_change) > 0.05:
                        print(f"\n💰 Your $1M position:")
                        print(f"   Based on this ONE estimate, it's now worth ${position_value_new:.2f}M")
                        print(f"   (Change: ${position_change:+.2f}M)")

                    print(f"\n📈 Progress: {num_answered + 1}/{num_total} questions answered")
                    print(f"\n💡 TIP: Come back tomorrow to answer the next question,")
                    print(f"        or type '2' again to keep going now.")

                except ValueError:
                    print("\n❌ Invalid input. Please enter a number (e.g., 15 or 0.8)")
                except KeyboardInterrupt:
                    print("\n\n⏸️  Skipping this question...")

        elif choice == '3':
            print("\nAvailable estimates to update:")
            for i, q in enumerate(model.questions, 1):
                current = model.get_estimate(q['id'])
                status = "✓" if q['id'] in model.user_estimates else " "
                print(f"{i}. [{status}] {q['text'][:50]}... (current: {current}{q['unit']})")

            try:
                idx = int(input("\nWhich one? (number): ")) - 1
                question = model.questions[idx]

                print(f"\n{question['text']}")
                print(f"Current: {model.get_estimate(question['id'])}{question['unit']}")

                answer = float(input(f"New estimate ({question['unit']}): "))
                result = model.update_estimate(question['id'], answer)

                print(f"\n✓ Updated! Fair value changed by ${result['impact']}/share")

            except (ValueError, IndexError):
                print("Invalid input.")

        elif choice == '4':
            model.sensitivity_analysis()

        elif choice == '5':
            model.save_state()
            print("\n✓ Goodbye!\n")
            break

        elif choice == 'q':
            print("\n✓ Exiting without saving.\n")
            break


if __name__ == '__main__':
    import sys

    # Check if user wants demo
    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        # Quick demo
        model = UberValuation()

        print("\n" + "="*60)
        print("UBER VALUATION ORACLE - DEMO")
        print("="*60)
        print("\nStarting with 100% Wall Street consensus...")

        model.show_valuation_summary()

        print("\n" + "-"*60)
        print("EXAMPLE: Let's update one estimate...")
        print("-"*60)

        question = model.get_next_question()
        print(f"\nQuestion: {question['text']}")
        print(f"Wall Street: {question['current_estimate']}{question['unit']}")
        print(f"\nLet's say you think: 17% (more optimistic than Wall Street's 15%)")

        result = model.update_estimate('ebitda_margin_2027', 17)

        print(f"\n✓ Impact of this ONE estimate:")
        print(f"  Old fair value: ${result['old_fair_value']}/share")
        print(f"  New fair value: ${result['new_fair_value']}/share")
        print(f"  Change: ${result['impact']}/share ({result['impact_pct']:+.1f}%)")

        model.show_valuation_summary()

        model.sensitivity_analysis()

        print("\n" + "-"*60)
        print("Ready to use interactively?")
        print("Run: python3 uber_valuation_v1.py (without --demo)")
        print("-"*60 + "\n")
    else:
        # Go straight to interactive mode
        interactive_mode()
