"""
GOLDMINE TERMINAL: Institutional Gold (XAUUSD) Intelligence Architecture
Ultra-Performance Build (Zero-Lag / High-Speed State Engine)
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timezone

# ==============================================================================
# 1. PAGE CONFIG & ZERO-LAG SYSTEM STYLING
# ==============================================================================
st.set_page_config(
    page_title="Goldmine Terminal | XAUUSD Institutional Desk",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: #07090e;
        color: #d1d5db;
    }
    .stApp { background-color: #07090e; }
    
    .terminal-bar {
        background: #0d111a;
        border-bottom: 1px solid #1f2937;
        padding: 10px 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 6px;
        margin-bottom: 16px;
        font-family: "SF Mono", Monaco, Inconsolata, "Fira Mono", "Droid Sans Mono", "Consolas", monospace;
    }
    .gold-accent { color: #d4af37; font-weight: 700; }
    
    .factor-card {
        background: #0d121d;
        border: 1px solid #182234;
        border-radius: 6px;
        padding: 14px 16px;
        margin-bottom: 12px;
    }
    
    .tag {
        font-family: monospace;
        font-size: 0.70rem;
        padding: 2px 7px;
        border-radius: 3px;
        text-transform: uppercase;
        font-weight: 600;
    }
    .tag-macro { background: #1e293b; color: #94a3b8; }
    .tag-pos { background: #27272a; color: #a1a1aa; }
    .tag-phys { background: #1c261e; color: #6ee7b7; }
    .tag-geo { background: #291a1a; color: #fca5a5; }
    
    .status-bullish { color: #10b981; font-weight: 600; }
    .status-bearish { color: #ef4444; font-weight: 600; }
    .status-neutral { color: #f59e0b; font-weight: 600; }
    
    .veto-box {
        background: #240c0c;
        border-left: 4px solid #ef4444;
        padding: 10px 14px;
        border-radius: 4px;
        margin-bottom: 6px;
        font-size: 0.85rem;
        color: #fca5a5;
    }
    
    .session-badge {
        font-family: monospace;
        font-size: 0.72rem;
        padding: 2px 6px;
        border-radius: 3px;
        margin-right: 5px;
    }
    .session-open { background: #064e3b; color: #34d399; }
    .session-closed { background: #1f2937; color: #6b7280; }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. GLOBAL SESSION STATUS
# ==============================================================================
now_utc = datetime.now(timezone.utc)
h = now_utc.hour

def get_badge(name, is_open):
    cls = "session-open" if is_open else "session-closed"
    st_text = "OPEN" if is_open else "CLOSED"
    return f"<span class='session-badge {cls}'>{name}: {st_text}</span>"

sessions_html = (
    get_badge("LON", 7 <= h < 16) +
    get_badge("NYC", 12 <= h < 21) +
    get_badge("TKO", 0 <= h < 9) +
    get_badge("SYD", 21 <= h or h < 6)
)

# ==============================================================================
# 3. COMPLETE 19-FACTOR INSTITUTIONAL MASTER REPOSITORY
# ==============================================================================
FACTORS = {
    "1. CPI & Inflation Expectations": {
        "desk": "Macro & Sovereign", "tag": "tag-macro", "source": "U.S. BLS / FRED",
        "url": "https://fred.stlouisfed.org/series/CPIAUCSL",
        "options": ["Hot / Accelerating (YoY > 3.0%)", "Cooling / Subdued (YoY <= 2.0%)", "Stagflationary (High CPI + Sinking GDP)"],
        "scenarios": {
            "Hot / Accelerating (YoY > 3.0%)": {"score": 1.0, "reason": "Purchasing power degradation.", "impact": "Institutional flight into physical assets.", "action": "Bullish expansion bias."},
            "Cooling / Subdued (YoY <= 2.0%)": {"score": -1.0, "reason": "Disinflation stabilizes cash.", "impact": "Inflation hedge necessity fades.", "action": "Price drags or consolidates."},
            "Stagflationary (High CPI + Sinking GDP)": {"score": 2.0, "reason": "Central banks trapped by supply shock.", "impact": "Bonds and equities dump simultaneously.", "action": "Parabolic multi-quarter bull leg."}
        }
    },
    "2. Geopolitical Risk Premium": {
        "desk": "Geopolitics & Clearing", "tag": "tag-geo", "source": "Caldara & Iacoviello GPR",
        "url": "https://www.matteoiacoviello.com/gpr.htm",
        "options": ["Risk Indices Spike (Direct Conflicts)", "De-escalation Occurs (Accords)", "Prolonged / Chronic Grinds"],
        "scenarios": {
            "Risk Indices Spike (Direct Conflicts)": {"score": 2.0, "reason": "Threat of systemic capital freezes.", "impact": "Flight to zero-counterparty bullion.", "action": "Violent upside expansion with weekend gaps."},
            "De-escalation Occurs (Accords)": {"score": -1.5, "reason": "Normalization of capital routes.", "impact": "Fear premium liquidates into risk assets.", "action": "Sharp 2% to 4% liquidation flushes."},
            "Prolonged / Chronic Grinds": {"score": 0.0, "reason": "Headline desensitization.", "impact": "Focus reverts to real yields.", "action": "Risk premium flatlines."}
        }
    },
    "3. Real Yields (10Y TIPS)": {
        "desk": "Macro & Sovereign", "tag": "tag-macro", "source": "FRED (Series: DFII10)",
        "url": "https://fred.stlouisfed.org/series/DFII10",
        "options": ["High / Rising (> 1.50% to 2.00%+)", "Plunge / Negative (< 0.00% to 0.50%)", "Yield Shock (Spike 30+ bps)"],
        "scenarios": {
            "High / Rising (> 1.50% to 2.00%+)": {"score": -2.0, "reason": "Sovereign debt pays positive real yield.", "impact": "Punitive opportunity cost to hold 0%-yield gold.", "action": "Heavy institutional bearish drag."},
            "Plunge / Negative (< 0.00% to 0.50%)": {"score": 2.0, "reason": "Rate cuts while inflation stays sticky.", "impact": "Opportunity cost vanishes completely.", "action": "Historic bull-market driver."},
            "Yield Shock (Spike 30+ bps)": {"score": -1.5, "reason": "Hawkish Fed surprise or auction tails.", "impact": "Commodity algorithms dump in unison.", "action": "Sudden downward liquidation wicks."}
        }
    },
    "4. Dollar Index (DXY) Correlation": {
        "desk": "Macro & Sovereign", "tag": "tag-macro", "source": "ICE / Investing.com DXY",
        "url": "https://www.investing.com/currencies/us-dollar-index",
        "options": ["Surging / Trending Firm (> 104-106)", "Breaking Down (< 100-102)", "Decoupled (Gold & DXY Rising Together)"],
        "scenarios": {
            "Surging / Trending Firm (> 104-106)": {"score": -1.0, "reason": "Relative U.S. growth / global USD shortage.", "impact": "Bullion costs more in non-USD currencies.", "action": "Persistent upside resistance."},
            "Breaking Down (< 100-102)": {"score": 1.0, "reason": "U.S. deficit widening or dovish easing.", "impact": "Global buying power expands.", "action": "Confirmed upward tailwind."},
            "Decoupled (Gold & DXY Rising Together)": {"score": 2.0, "reason": "Severe sovereign crisis outside U.S.", "impact": "Cash goes to USD, safety goes to Gold.", "action": "Intense institutional risk-aversion."}
        }
    },
    "5. Central Bank Buying": {
        "desk": "Geopolitics & Clearing", "tag": "tag-geo", "source": "IMF IFS / World Gold Council",
        "url": "https://www.gold.org/goldhub/data/central-bank-buying",
        "options": ["Massive Purchases (> 800-1000t/yr)", "Purchases Stall Near Zero", "Sovereign Repatriation Accelerates"],
        "scenarios": {
            "Massive Purchases (> 800-1000t/yr)": {"score": 2.0, "reason": "De-dollarization & sanction defense.", "impact": "Permanently absorbs circulating physical float.", "action": "Impenetrable structural price floor."},
            "Purchases Stall Near Zero": {"score": -1.0, "reason": "FX reserves exhausted defending currencies.", "impact": "Structural floor softens.", "action": "Vulnerable to speculative COMEX paper dumps."},
            "Sovereign Repatriation Accelerates": {"score": 1.5, "reason": "Custodial distrust of Western central banks.", "impact": "London/NY physical tightness spikes.", "action": "Physical supply bottleneck."}
        }
    },
    "6. The COT Report (Speculative Net)": {
        "desk": "Positioning & Algos", "tag": "tag-pos", "source": "CFTC Disaggregated API",
        "url": "https://www.tradingster.com/cot/futures/disagg/088691",
        "options": ["Historic Long Extremes (> 250k-300k)", "Washed Out / Low (< 50k-100k)", "Commercials Aggressively Expand Shorts"],
        "scenarios": {
            "Historic Long Extremes (> 250k-300k)": {"score": -1.5, "reason": "Speculative leverage maxed out.", "impact": "Crowded Long Trap. No buyers remain.", "action": "Do NOT buy breakout highs."},
            "Washed Out / Low (< 50k-100k)": {"score": 1.5, "reason": "Multi-month bear washout complete.", "impact": "Sellers depleted; asymmetrical risk/reward.", "action": "High-conviction long accumulation."},
            "Commercials Aggressively Expand Shorts": {"score": -1.0, "reason": "Miners/banks hedging forward supply.", "impact": "Institutional ceiling capping upside.", "action": "Scale out of extended longs."}
        }
    },
    "7. Gold ETF Flows (SPDR GLD & IAU)": {
        "desk": "Positioning & Algos", "tag": "tag-pos", "source": "State Street / WGC",
        "url": "https://www.gold.org/goldhub/data/gold-etfs-holdings-and-flows",
        "options": ["Sustained Inflows (Multi-Week Additions)", "Heavy Outflows (Persistent Reductions)", "Price Rallies on Heavy Outflows (Divergence)"],
        "scenarios": {
            "Sustained Inflows (Multi-Week Additions)": {"score": 1.5, "reason": "Western wealth allocators buying shares.", "impact": "Trustees physically vault gold bars.", "action": "Multi-month trend continuation."},
            "Heavy Outflows (Persistent Reductions)": {"score": -1.0, "reason": "Capital chasing high cash yields.", "impact": "Custodians liquidate physical bars.", "action": "Dampens rally momentum."},
            "Price Rallies on Heavy Outflows (Divergence)": {"score": 2.0, "reason": "Eastern physical buyers absorb Western sales.", "impact": "Coiled spring dynamic.", "action": "Parabolic squeeze once Western flows flip."}
        }
    },
    "8. Gold-Silver Ratio (GSR)": {
        "desk": "Macro & Sovereign", "tag": "tag-macro", "source": "Spot Ratio (XAU/XAG)",
        "url": "https://www.tradingview.com/symbols/GOLDSILVER/",
        "options": ["Expands High (> 80-90+)", "Compresses Lower (< 65-70)", "Spikes Beyond 100+ (Liquidity Freeze)"],
        "scenarios": {
            "Expands High (> 80-90+)": {"score": 1.0, "reason": "Industrial growth slows; defensive flight.", "impact": "Gold outperforms industrial silver.", "action": "Defensive Risk-Off regime."},
            "Compresses Lower (< 65-70)": {"score": 0.5, "reason": "Broad commodity supercycles.", "impact": "Silver outperforms gold via industrial demand.", "action": "Risk-On commodity cycle."},
            "Spikes Beyond 100+ (Liquidity Freeze)": {"score": 2.0, "reason": "Terminal deflationary shock (2008/2020).", "impact": "Precedes massive liquidity injections.", "action": "Generational buy signal."}
        }
    },
    "9. Seasonality Cycles": {
        "desk": "Positioning & Algos", "tag": "tag-pos", "source": "Seasonax Analytics",
        "url": "https://www.seasonax.com",
        "options": ["High-Demand Window (Aug-Sep & Jan-Feb)", "Summer Lull (Jun-Jul)", "Violent Drop During Strong Window"],
        "scenarios": {
            "High-Demand Window (Aug-Sep & Jan-Feb)": {"score": 1.0, "reason": "Diwali & Chinese Lunar New Year.", "impact": "Physical consumer uptake surges.", "action": "High probability long continuation."},
            "Summer Lull (Jun-Jul)": {"score": -0.5, "reason": "Absence of Asian cultural physical holidays.", "impact": "Choppy, rangebound market drift.", "action": "Avoid breakout trading; play mean reversion."},
            "Violent Drop During Strong Window": {"score": -2.0, "reason": "Macro forces overpowering physical demand.", "impact": "Underlying macro trend is aggressively bearish.", "action": "Trend invalidation; close longs."}
        }
    },
    "10. Gold Attribution Model (GRAM)": {
        "desk": "Macro & Sovereign", "tag": "tag-macro", "source": "World Gold Council",
        "url": "https://www.gold.org/goldhub/data/gold-return-attribution-model",
        "options": ["Dominant: Risk & Uncertainty", "Dominant: Opportunity Cost (Yields/FX)", "Dominant: Momentum / Positioning"],
        "scenarios": {
            "Dominant: Risk & Uncertainty": {"score": 1.5, "reason": "Systemic sovereign stress / tension.", "impact": "Price action blows through standard resistance.", "action": "Ride momentum; do not short resistance."},
            "Dominant: Opportunity Cost (Yields/FX)": {"score": -1.0, "reason": "Rate differentials dictate orders.", "impact": "Traditional quant models in full control.", "action": "Strict adherence to tech levels & yields."},
            "Dominant: Momentum / Positioning": {"score": 0.5, "reason": "CTAs chasing multi-week high wicks.", "impact": "Technically stretched; vulnerable to pullbacks.", "action": "Trail stops tightly on long positions."}
        }
    },
    "11. COMEX Physical Depository Stocks": {
        "desk": "Physical & Arbitrage", "tag": "tag-phys", "source": "CME Metal Statistics",
        "url": "https://www.cmegroup.com/delivery_reports/Gold_Stocks.html",
        "options": ["Registered Inventories Plunge (> 10:1 Ratio)", "Registered Inventories Plentiful & Rising", "Large Blocks Shift Registered -> Eligible"],
        "scenarios": {
            "Registered Inventories Plunge (> 10:1 Ratio)": {"score": 2.0, "reason": "Institutions taking physical contract delivery.", "impact": "Paper shorts face acute physical delivery squeeze.", "action": "High short squeeze probability."},
            "Registered Inventories Plentiful & Rising": {"score": -0.5, "reason": "Dealers depositing and warranting bars.", "impact": "Paper markets operate with zero delivery friction.", "action": "Price driven solely by paper rates."},
            "Large Blocks Shift Registered -> Eligible": {"score": 1.0, "reason": "Owners de-warranting bars to hold privately.", "impact": "Deliverable floating supply contracts.", "action": "Subtle bullish tightening."}
        }
    },
    "12. Options Expiration (OPEX) Pinning": {
        "desk": "Positioning & Algos", "tag": "tag-pos", "source": "CME QuikStrike",
        "url": "https://www.cmegroup.com/tools-information/quikstrike.html",
        "options": ["Approaching OPEX with Strike Clustering", "Spot Blows Through Strike (Gamma Squeeze)", "Post-OPEX Expiration Window"],
        "scenarios": {
            "Approaching OPEX with Strike Clustering": {"score": 0.0, "reason": "Dealers delta-hedging large open interest.", "impact": "The Magnet Effect. Volatility is suppressed.", "action": "Pinning to round numbers until expiry."},
            "Spot Blows Through Strike (Gamma Squeeze)": {"score": 1.5, "reason": "Macro shock forces dealers into short gamma.", "impact": "Market makers buy rising markets to stay neutral.", "action": "Runaway intraday momentum breakouts."},
            "Post-OPEX Expiration Window": {"score": 1.0, "reason": "Expired dealer gamma hedges cleared.", "impact": "Pinning magnet disappears.", "action": "New directional trend expansion begins."}
        }
    },
    "13. Sovereign Fiscal Deficits & Treasury Issuance": {
        "desk": "Macro & Sovereign", "tag": "tag-macro", "source": "U.S. Treasury Data",
        "url": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
        "options": ["Widening Deficits & Exploding Debt Issuance", "Shrinking Deficits / Debt Ceiling Supply Freeze", "Long-Dated Treasury Auction 'Tail'"],
        "scenarios": {
            "Widening Deficits & Exploding Debt Issuance": {"score": 1.5, "reason": "Unchecked spending requires trillions in debt.", "impact": "Anticipation of future debt monetization.", "action": "Multi-year structural tailwind."},
            "Shrinking Deficits / Debt Ceiling Supply Freeze": {"score": -0.5, "reason": "Temporary fiscal spending pauses.", "impact": "Stabilizes fiat perceptions.", "action": "Safe-haven urgency cools."},
            "Long-Dated Treasury Auction 'Tail'": {"score": 1.5, "reason": "Weak demand for long-duration government paper.", "impact": "Systemic debt indigestion.", "action": "Gold acts as primary escape hatch."}
        }
    },
    "14. Sovereign Import Tariffs & Quotas": {
        "desk": "Physical & Arbitrage", "tag": "tag-phys", "source": "DGFT (India) / PBOC",
        "url": "https://dgft.gov.in",
        "options": ["India Cuts Customs Duties (e.g., 15% -> 6%)", "PBOC Expands Import Quotas", "Import Tariffs Raised or Quotas Blocked"],
        "scenarios": {
            "India Cuts Customs Duties (e.g., 15% -> 6%)": {"score": 2.0, "reason": "Government policy curbing illegal smuggling.", "impact": "Domestic prices drop; massive consumer buying unlocked.", "action": "Vaults drain; spot prices jump."},
            "PBOC Expands Import Quotas": {"score": 1.5, "reason": "Accommodating strong Chinese retail demand.", "impact": "Chinese commercial banks import heavily.", "action": "Asia-session bids strengthen."},
            "Import Tariffs Raised or Quotas Blocked": {"score": -1.5, "reason": "Defending domestic foreign exchange reserves.", "impact": "Physical inflows bottleneck.", "action": "Temporary headwind on spot momentum."}
        }
    },
    "15. The East-West Arbitrage (SGE Premium)": {
        "desk": "Physical & Arbitrage", "tag": "tag-phys", "source": "Shanghai Gold Exchange",
        "url": "https://en.sge.com.cn/",
        "options": ["SGE Premium Blows Out ($40-$80+ Above Spot)", "SGE Premium Collapses to Parity / Discount", "Western Spot Drops While SGE Premium Widens"],
        "scenarios": {
            "SGE Premium Blows Out ($40-$80+ Above Spot)": {"score": 2.0, "reason": "Chinese domestic demand vs tight import quotas.", "impact": "Arbitrageurs buy West, ship East.", "action": "Western market makers bid up spot."},
            "SGE Premium Collapses to Parity / Discount": {"score": -1.0, "reason": "Domestic retail exhaustion or surplus supply.", "impact": "The Eastern structural bid is dormant.", "action": "Western rate models regain full control."},
            "Western Spot Drops While SGE Premium Widens": {"score": 1.5, "reason": "Paper markets dumping while physical absorbs.", "impact": "Imminent bottom; physical buying halts drop.", "action": "High-probability reversal long setup."}
        }
    },
    "16. Gold Lease Rates (GLR) & Vault Tightness": {
        "desk": "Physical & Arbitrage", "tag": "tag-phys", "source": "LBMA",
        "url": "https://www.lbma.org.uk",
        "options": ["Lease Rates Spike / GOFO Turns Negative", "Lease Rates Flat / Near Zero", "LBMA Vault Inventories at Multi-Year Lows"],
        "scenarios": {
            "Lease Rates Spike / GOFO Turns Negative": {"score": 2.0, "reason": "Bullion banks short of physical metal.", "impact": "Acute physical shortage.", "action": "Historically precedes explosive spot rallies."},
            "Lease Rates Flat / Near Zero": {"score": 0.0, "reason": "London wholesale vaults operating smoothly.", "impact": "Borrowing physical metal carries zero premium.", "action": "Standard interest-rate pricing rules."},
            "LBMA Vault Inventories at Multi-Year Lows": {"score": 1.5, "reason": "Persistent net shipments to non-Western buyers.", "impact": "Physical market becomes inelastic.", "action": "Asymmetrical upside convexity."}
        }
    },
    "17. Cross-Asset Volatility Spills (MOVE Index)": {
        "desk": "Geopolitics & Clearing", "tag": "tag-geo", "source": "FRED (MOVE Index)",
        "url": "https://fred.stlouisfed.org/series/MOVE",
        "options": ["MOVE Index Spikes Violently (> 120-140+)", "MOVE Index Peaks and Subsides (< 80-90)", "MOVE Flat & Calm While Gold Climbs"],
        "scenarios": {
            "MOVE Index Spikes Violently (> 120-140+)": {"score": -2.0, "reason": "Liquidity shock in U.S. Treasury debt market.", "impact": "Forced Margin-Call Trap.", "action": "Gold counterintuitively dumps. VETO LONGS."},
            "MOVE Index Peaks and Subsides (< 80-90)": {"score": 2.0, "reason": "Fed liquidity backstops arrive; bond panic halts.", "impact": "Forced selling ends; gold stages V-reversal.", "action": "Prime long entry window."},
            "MOVE Flat & Calm While Gold Climbs": {"score": 1.0, "reason": "Orderly capital rotation into hard assets.", "impact": "Sustainable, low-volatility trend expansion.", "action": "Healthy trend-following regime."}
        }
    },
    "18. De-Dollarization & Clearing (Project mBridge)": {
        "desk": "Geopolitics & Clearing", "tag": "tag-geo", "source": "BIS",
        "url": "https://www.bis.org/about/bisih/topics/cbdc/mcbdc_bridge.htm",
        "options": ["Non-SWIFT Multilateral Settlements Expand", "Bilateral Deals Settle with Gold Collateral", "Geopolitical Sanctions Accelerate Parallel Rails"],
        "scenarios": {
            "Non-SWIFT Multilateral Settlements Expand": {"score": 2.0, "reason": "Trade settlements bypassing SWIFT.", "impact": "Gold used as neutral collateral.", "action": "Permanent structural bid outside Western flows."},
            "Bilateral Deals Settle with Gold Collateral": {"score": 1.5, "reason": "Commodity exporters insulating from sanctions.", "impact": "Reduces global demand for dollar reserves.", "action": "Higher structural price floor."},
            "Geopolitical Sanctions Accelerate Parallel Rails": {"score": 1.5, "reason": "Fear of sovereign asset freezes spreads.", "impact": "Re-rating of physical gold as ultimate reserve asset.", "action": "Long-term secular re-pricing."}
        }
    },
    "19. CTA Trend Models & Positioning": {
        "desk": "Positioning & Algos", "tag": "tag-pos", "source": "Prime Brokerage / CFTC",
        "url": "https://www.tradingster.com/cot/futures/disagg/088691",
        "options": ["CTA Max Long (> 80-90%) & Volatility Spikes", "Price Breaks Below CTA Short Flip Trigger", "DBMF / Managed Money Flips Net Short to Net Long"],
        "scenarios": {
            "CTA Max Long (> 80-90%) & Volatility Spikes": {"score": -2.0, "reason": "Mathematical volatility risk budgets full.", "impact": "Forced De-leveraging. Algos dump contracts.", "action": "HARD VETO on buying breakout highs."},
            "Price Breaks Below CTA Short Flip Trigger": {"score": -2.0, "reason": "Medium-term momentum moving averages breached.", "impact": "The Liquidation Cascade.", "action": "Do not catch the falling knife."},
            "DBMF / Managed Money Flips Net Short to Net Long": {"score": 2.0, "reason": "Moving averages crossed bullishly.", "impact": "Algorithmic Tailwind. Computers buy every dip.", "action": "High-conviction pullback accumulation."}
        }
    }
}

# ==============================================================================
# 4. INSTANT STATE ENGINE (DECOUPLED FROM WIDGET LIFECYCLES)
# ==============================================================================
def reset_to_baseline():
    return {f: d["options"][1] for f, d in FACTORS.items()}

if "factor_states" not in st.session_state:
    st.session_state.factor_states = reset_to_baseline()

def set_preset(preset_name):
    st.session_state.factor_states = reset_to_baseline()
    
    if preset_name == "Stagflationary Breakout":
        st.session_state.factor_states["1. CPI & Inflation Expectations"] = "Stagflationary (High CPI + Sinking GDP)"
        st.session_state.factor_states["3. Real Yields (10Y TIPS)"] = "Plunge / Negative (< 0.00% to 0.50%)"
        st.session_state.factor_states["5. Central Bank Buying"] = "Massive Purchases (> 800-1000t/yr)"
        st.session_state.factor_states["17. Cross-Asset Volatility Spills (MOVE Index)"] = "MOVE Flat & Calm While Gold Climbs"
        st.session_state.factor_states["19. CTA Trend Models & Positioning"] = "DBMF / Managed Money Flips Net Short to Net Long"
        
    elif preset_name == "Liquidity Shock / Forced Margin Call":
        st.session_state.factor_states["17. Cross-Asset Volatility Spills (MOVE Index)"] = "MOVE Index Spikes Violently (> 120-140+)"
        st.session_state.factor_states["19. CTA Trend Models & Positioning"] = "CTA Max Long (> 80-90%) & Volatility Spikes"
        st.session_state.factor_states["3. Real Yields (10Y TIPS)"] = "Yield Shock (Spike 30+ bps)"
        
    elif preset_name == "Hawkish Real Yield Drag":
        st.session_state.factor_states["3. Real Yields (10Y TIPS)"] = "High / Rising (> 1.50% to 2.00%+)"
        st.session_state.factor_states["4. Dollar Index (DXY) Correlation"] = "Surging / Trending Firm (> 104-106)"
        st.session_state.factor_states["6. The COT Report (Speculative Net)"] = "Historic Long Extremes (> 250k-300k)"
        
    elif preset_name == "Asian Physical Delivery Squeeze":
        st.session_state.factor_states["15. The East-West Arbitrage (SGE Premium)"] = "SGE Premium Blows Out ($40-$80+ Above Spot)"
        st.session_state.factor_states["11. COMEX Physical Depository Stocks"] = "Registered Inventories Plunge (> 10:1 Ratio)"
        st.session_state.factor_states["16. Gold Lease Rates (GLR) & Vault Tightness"] = "Lease Rates Spike / GOFO Turns Negative"
        st.session_state.factor_states["14. Sovereign Import Tariffs & Quotas"] = "India Cuts Customs Duties (e.g., 15% -> 6%)"
        st.session_state.factor_states["5. Central Bank Buying"] = "Massive Purchases (> 800-1000t/yr)"
        st.session_state.factor_states["17. Cross-Asset Volatility Spills (MOVE Index)"] = "MOVE Flat & Calm While Gold Climbs"
        st.session_state.factor_states["19. CTA Trend Models & Positioning"] = "DBMF / Managed Money Flips Net Short to Net Long"
        st.session_state.factor_states["3. Real Yields (10Y TIPS)"] = "Plunge / Negative (< 0.00% to 0.50%)"

st.sidebar.markdown("### 🎛️ Terminal Controls")

selected_preset = st.sidebar.selectbox(
    "Load Institutional Macro Preset:",
    ["-- Manual Simulation --", "Stagflationary Breakout", "Liquidity Shock / Forced Margin Call", "Hawkish Real Yield Drag", "Asian Physical Delivery Squeeze"],
    key="preset_ui"
)

if "last_preset" not in st.session_state or st.session_state.last_preset != selected_preset:
    st.session_state.last_preset = selected_preset
    if selected_preset != "-- Manual Simulation --":
        set_preset(selected_preset)
        st.rerun()

def hard_reset():
    st.session_state.factor_states = reset_to_baseline()
    st.session_state.preset_ui = "-- Manual Simulation --"
    st.session_state.last_preset = "-- Manual Simulation --"

st.sidebar.button("🔄 Force Reset All to Neutral", on_click=hard_reset)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏛️️ Operational Desks")
selected_desk = st.sidebar.radio(
    "Focus Desk:",
    ["All Operational Desks", "Macro & Sovereign", "Positioning & Algos", "Physical & Arbitrage", "Geopolitics & Clearing"]
)

# ==============================================================================
# 5. HEADER BAR & REGIME ENGINE
# ==============================================================================
st.markdown(f"""
<div class='terminal-bar'>
    <div><span style='font-size: 1.05rem;'><span class='gold-accent'>GOLDMINE TERMINAL</span> // XAUUSD INSTITUTIONAL INTELLIGENCE</span></div>
    <div>{sessions_html}</div>
</div>
""", unsafe_allow_html=True)

total_score = 0.0
active_vetoes = []

for factor, data in FACTORS.items():
    current_choice = st.session_state.factor_states.get(factor, data["options"][1])
    scen = data["scenarios"].get(current_choice, data["scenarios"][data["options"][1]])
    total_score += scen["score"]
    
    if factor == "19. CTA Trend Models & Positioning" and "CTA Max Long" in current_choice:
        active_vetoes.append("ALGORITHMIC VETO: CTA systematic risk limits full. Volatility spike triggers forced de-leveraging. DO NOT BUY HIGHS.")
    if factor == "17. Cross-Asset Volatility Spills (MOVE Index)" and "MOVE Index Spikes" in current_choice:
        active_vetoes.append("LIQUIDITY SHOCK VETO: Bond market panic (MOVE > 120). Leveraged funds dumping gold for USD margin calls. VETO LONGS.")
    if factor == "3. Real Yields (10Y TIPS)" and "High / Rising" in current_choice:
        active_vetoes.append("MACRO HEADWIND: 10Y Real Yields > 1.80%. Sovereign debt opportunity cost actively draining speculative paper allocations.")

alignment_pct = int((total_score / 35.0) * 100)
alignment_pct = max(-100, min(100, alignment_pct))

col_m1, col_m2, col_m3 = st.columns([1.2, 1.2, 2.6])

with col_m1:
    delta_label = "Bullish" if alignment_pct > 15 else ("Bearish" if alignment_pct < -15 else "Neutral")
    st.metric("Macro Alignment", f"{alignment_pct}%", delta=delta_label)

with col_m2:
    if alignment_pct >= 35:
        st.markdown("<p style='font-size: 0.8rem; margin:0;'>REGIME CLASSIFICATION</p><h3 class='status-bullish' style='margin:0;'>BULLISH EXPANSION</h3>", unsafe_allow_html=True)
    elif alignment_pct <= -35:
        st.markdown("<p style='font-size: 0.8rem; margin:0;'>REGIME CLASSIFICATION</p><h3 class='status-bearish' style='margin:0;'>BEARISH DISTRIBUTION</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='font-size: 0.8rem; margin:0;'>REGIME CLASSIFICATION</p><h3 class='status-neutral' style='margin:0;'>RANGEBOUND CHURN</h3>", unsafe_allow_html=True)

with col_m3:
    if active_vetoes:
        for v in active_vetoes:
            st.markdown(f"<div class='veto-box'><b>⚠️ EXECUTION VETO:</b> {v}</div>", unsafe_allow_html=True)
    else:
        st.success("✅ Trade Clearance: No institutional risk-limit vetoes active across the 19 factors.")

st.markdown("---")

# ==============================================================================
# 6. HIGH-PERFORMANCE OPERATIONAL MATRIX
# ==============================================================================
cols = st.columns(2)
idx = 0

for factor_name, data in FACTORS.items():
    if selected_desk != "All Operational Desks" and data["desk"] != selected_desk:
        continue
        
    url_target = data["url"]
    source_label = data["source"]
    desk_label = data["desk"]
    tag_class = data["tag"]
    
    with cols[idx % 2]:
        st.markdown(f"""
        <div class='factor-card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <span class='tag {tag_class}'>{desk_label}</span>
                <span style='font-size: 0.72rem;'><a href='{url_target}' target='_blank' style='color: #60a5fa; text-decoration: none;'>📡 {source_label}</a></span>
            </div>
            <h4 style='margin: 8px 0 6px 0; color: #f3f4f6;'>{factor_name}</h4>
        """, unsafe_allow_html=True)
        
        current_val = st.session_state.factor_states.get(factor_name, data["options"][1])
        default_index = data["options"].index(current_val) if current_val in data["options"] else 1
        
        selected = st.selectbox(
            "State Evaluation:",
            data["options"],
            index=default_index,
            key=f"widget_{factor_name}",
            label_visibility="collapsed"
        )
        
        st.session_state.factor_states[factor_name] = selected
        scen = data["scenarios"][selected]
        
        if scen["score"] > 0:
            badge = f"<span class='status-bullish'>▲ Bullish Flow (+{scen['score']})</span>"
        elif scen["score"] < 0:
            badge = f"<span class='status-bearish'>▼ Bearish Drag ({scen['score']})</span>"
        else:
            badge = "<span class='status-neutral'>◆ Neutral / Pinning (0)</span>"
            
        st.markdown(f"""
            <div style='margin-top: 6px; font-size: 0.84rem;'>{badge} &nbsp;|&nbsp; <b>Plausible Reason:</b> {scen["reason"]}</div>
            <div style='margin-top: 4px; font-size: 0.82rem; color: #9ca3af;'><b>Scenario & Impact:</b> {scen["impact"]}</div>
            <div style='margin-top: 6px; padding: 6px 10px; background: #111827; border-left: 3px solid #d4af37; font-size: 0.82rem; color: #e5e7eb;'>
                <b>Institutional Action:</b> {scen["action"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    idx += 1