import streamlit as st

from config import ENABLE_ANIMATIONS


@st.cache_data(show_spinner=False)
def _global_css(enable_animations: bool) -> str:
    motion_css = """
    @media (prefers-reduced-motion: no-preference) {
      .block-container { animation: pageIn .55s var(--ease-out) both; }
      .tm-card, .tour-card, .metric-card, .chart-card, .ticket-card { animation: cardIn .56s var(--ease-out) both; }
      .tm-card:nth-of-type(2), .tour-card:nth-of-type(2) { animation-delay: 60ms; }
      .tm-card:nth-of-type(3), .tour-card:nth-of-type(3) { animation-delay: 120ms; }
      .tm-card:nth-of-type(4), .tour-card:nth-of-type(4) { animation-delay: 180ms; }
      .hero-premium::before { animation: drift 10s ease-in-out infinite alternate; }
      .hero-premium::after { animation: drift2 12s ease-in-out infinite alternate; }
      .hero-word { animation: wordIn .7s var(--ease-out) both; }
      .hero-word:nth-child(2) { animation-delay: .12s; }
      .hero-word:nth-child(3) { animation-delay: .24s; }
      .hero-subtitle, .hero-actions, .hero-stats { animation: fadeUp .8s var(--ease-out) both; animation-delay: .42s; }
      .marquee-track { animation: marquee 28s linear infinite; }
      .badge.pending, .few-seats { animation: pulseSoft 1.7s ease-in-out infinite; }
      .success-mark path { animation: drawCheck .9s var(--ease-out) both; }
      .plane-float { animation: planeFloat 5s ease-in-out infinite; }
    }
    """ if enable_animations else ""
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
    :root {{
      --navy:#0B1F3A; --deep-blue:#12356B; --teal:#14B8A6; --cyan:#22D3EE;
      --orange:#FF8A3D; --amber:#F59E0B; --bg:#F5F7FB; --surface:#FFFFFF;
      --text:#0F172A; --muted:#64748B; --success:#16A34A; --danger:#DC2626;
      --gradient-hero: linear-gradient(135deg, #0B1F3A 0%, #12356B 42%, #14B8A6 100%);
      --gradient-cta: linear-gradient(135deg, #FF8A3D 0%, #F59E0B 100%);
      --gradient-card: linear-gradient(145deg, rgba(255,255,255,.98), rgba(236,253,245,.75));
      --radius-sm:12px; --radius-md:16px; --radius-lg:24px; --pill:999px;
      --shadow-soft: 0 12px 35px rgba(15,23,42,.08);
      --shadow-med: 0 18px 50px rgba(15,23,42,.12);
      --shadow-elevated: 0 26px 70px rgba(11,31,58,.18);
      --glow-teal: 0 0 0 4px rgba(20,184,166,.14), 0 18px 38px rgba(20,184,166,.26);
      --glow-orange: 0 0 0 4px rgba(255,138,61,.14), 0 18px 38px rgba(255,138,61,.24);
      --ease-out: cubic-bezier(.22,1,.36,1);
    }}
    html {{ scroll-behavior:smooth; }}
    html, body, [class*="st-"], [data-testid="stAppViewContainer"] {{
      font-family: Inter, system-ui, -apple-system, Segoe UI, sans-serif;
      color: var(--text);
    }}
    ::selection {{ background: rgba(34,211,238,.28); color: var(--navy); }}
    ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
    ::-webkit-scrollbar-thumb {{ background: linear-gradient(var(--teal), var(--deep-blue)); border-radius: var(--pill); }}
    [data-testid="stAppViewContainer"] {{ background:
      radial-gradient(circle at 12% 7%, rgba(34,211,238,.16), transparent 34%),
      radial-gradient(circle at 84% 12%, rgba(255,138,61,.14), transparent 30%),
      var(--bg); }}
    .main .block-container {{ padding-top: 1.35rem; max-width: 1240px; }}
    #MainMenu, footer, [data-testid="stDecoration"], [data-testid="stStatusWidget"] {{ display:none !important; }}
    header[data-testid="stHeader"] {{ background: transparent; }}
    h1,h2,h3 {{ font-family:"Plus Jakarta Sans", Inter, system-ui, sans-serif; letter-spacing:-.025em; color:var(--text); }}
    h1 {{ font-size: clamp(2rem, 4vw, 3.25rem); line-height:1.04; }}
    h2 {{ font-size: clamp(1.35rem, 2.5vw, 2rem); }}
    .muted {{ color: var(--muted); }} .tiny {{ font-size:.82rem; }} .price {{ color:var(--orange); font-weight:800; }}

    [data-testid="stSidebar"] {{
      background: linear-gradient(180deg, #08172B, #0B1F3A 48%, #092F43);
      border-right: 1px solid rgba(255,255,255,.08);
      box-shadow: 20px 0 55px rgba(11,31,58,.24);
    }}
    [data-testid="stSidebar"] * {{ color:#EFF6FF; }}
    .nav-brand {{ display:flex; align-items:center; gap:.75rem; padding:.75rem .25rem 1rem; }}
    .brand-mark {{ width:44px;height:44px;border-radius:15px;display:grid;place-items:center;background:linear-gradient(135deg,var(--teal),var(--cyan));box-shadow:0 12px 28px rgba(20,184,166,.35);font-weight:900;color:#06233d; }}
    .brand-title {{ font:800 1.05rem "Plus Jakarta Sans",Inter,sans-serif; }}
    .brand-sub {{ font-size:.73rem;color:#BFEAF0; }}
    .user-chip {{ display:flex;align-items:center;gap:.7rem;padding:.75rem;border:1px solid rgba(255,255,255,.12);border-radius:18px;background:rgba(255,255,255,.08);margin:.6rem 0 1rem; }}
    .avatar {{ width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:var(--gradient-cta);color:white;font-weight:900; }}
    .role-badge {{ display:inline-flex;padding:.18rem .55rem;border-radius:var(--pill);background:rgba(34,211,238,.15);color:#A5F3FC;font-size:.7rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em; }}
    [data-testid="stSidebar"] [role="radiogroup"] label {{
      border-radius:16px; padding:.55rem .75rem; margin:.18rem 0; border:1px solid transparent;
      transition: transform .18s ease, background .18s ease, border-color .18s ease;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label:hover {{ background:rgba(255,255,255,.09); transform:translateX(4px); }}
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{
      background:linear-gradient(90deg, rgba(20,184,166,.28), rgba(34,211,238,.08));
      border-color:rgba(34,211,238,.36); box-shadow: inset 4px 0 0 var(--cyan);
    }}

    .hero-premium {{
      position:relative; overflow:hidden; min-height:560px; border-radius:28px; padding:4.4rem 3.2rem;
      color:white; background: var(--gradient-hero); background-size:300% 300%;
      box-shadow: var(--shadow-elevated); isolation:isolate;
    }}
    .hero-premium::before, .hero-premium::after {{
      content:""; position:absolute; border-radius:50%; filter: blur(28px); opacity:.65; z-index:-1; transform:translateZ(0);
    }}
    .hero-premium::before {{ width:290px;height:290px;background:rgba(34,211,238,.36);right:8%;top:12%; }}
    .hero-premium::after {{ width:230px;height:230px;background:rgba(255,138,61,.32);left:54%;bottom:4%; }}
    .hero-content {{ max-width:760px; position:relative; z-index:2; }}
    .hero-eyebrow {{ display:inline-flex; gap:.45rem; align-items:center; padding:.45rem .75rem; border:1px solid rgba(255,255,255,.22); border-radius:var(--pill); background:rgba(255,255,255,.12); backdrop-filter:blur(14px); font-weight:800; font-size:.82rem; }}
    .hero-title {{ color:white; font-size:clamp(3rem, 7vw, 6rem); line-height:.92; margin:.9rem 0 1rem; }}
    .hero-word {{ display:inline-block; margin-right:.22em; }}
    .hero-gradient {{ background:linear-gradient(90deg,#fff,#A7F3D0,#FFCF8A,#fff); -webkit-background-clip:text; background-clip:text; color:transparent; }}
    .hero-subtitle {{ color:#E2E8F0; max-width:650px; font-size:1.18rem; line-height:1.75; }}
    .hero-actions {{ display:flex; flex-wrap:wrap; gap:.9rem; margin-top:1.5rem; }}
    .cta-pill, .ghost-pill {{ display:inline-flex; align-items:center; gap:.55rem; padding:.88rem 1.15rem; border-radius:var(--pill); font-weight:900; text-decoration:none; }}
    .cta-pill {{ background:var(--gradient-cta); color:white; box-shadow:var(--glow-orange); }}
    .ghost-pill {{ color:white; border:1px solid rgba(255,255,255,.28); background:rgba(255,255,255,.12); }}
    .plane-float {{ position:absolute; right:10%; top:19%; color:rgba(255,255,255,.76); }}
    .hero-stats {{ display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.9rem;margin-top:2rem;max-width:640px; }}
    .hero-stat {{ padding:1rem;border:1px solid rgba(255,255,255,.16);border-radius:18px;background:rgba(255,255,255,.11);backdrop-filter:blur(16px); }}
    .hero-stat strong {{ display:block;color:white;font-size:1.45rem; }}
    .hero-stat span {{ color:#D9F7FA;font-size:.82rem; }}
    .marquee {{ overflow:hidden; margin:1rem 0 1.6rem; border-radius:18px; background:rgba(255,255,255,.7); border:1px solid rgba(226,232,240,.75); }}
    .marquee-track {{ display:flex; gap:.8rem; width:max-content; padding:.75rem; }}
    .marquee:hover .marquee-track {{ animation-play-state:paused; }}
    .dest-chip {{ white-space:nowrap; padding:.55rem .85rem;border-radius:var(--pill);background:white;border:1px solid #E2E8F0;box-shadow:var(--shadow-soft);font-weight:800;color:var(--deep-blue); }}

    .tm-card, .tour-card, .metric-card, .chart-card, .ticket-card {{
      background: var(--gradient-card); border:1px solid rgba(226,232,240,.92); border-radius:var(--radius-lg);
      box-shadow:var(--shadow-soft); padding:1.05rem; height:100%; position:relative; overflow:hidden;
      transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
    }}
    .tm-card:hover, .tour-card:hover, .metric-card:hover, .chart-card:hover, .ticket-card:hover {{ transform:translateY(-5px); box-shadow:var(--shadow-med); border-color:rgba(20,184,166,.35); }}
    .tour-card {{ padding:0; }}
    .tour-media {{ height:190px; overflow:hidden; position:relative; background:linear-gradient(135deg,#DFF7F4,#E0F2FE); }}
    .tour-media img {{ width:100%; height:100%; object-fit:cover; display:block; transition:transform .55s var(--ease-out); }}
    .tour-card:hover .tour-media img {{ transform:scale(1.08); }}
    .tour-media::after {{ content:""; position:absolute; inset:0; background:linear-gradient(180deg, transparent 35%, rgba(11,31,58,.68)); opacity:.75; transition:opacity .22s ease; }}
    .tour-card:hover .tour-media::after {{ opacity:.9; }}
    .tour-body {{ padding:1rem; }}
    .tour-title {{ margin:.15rem 0 .35rem; font-size:1.13rem; }}
    .tour-meta {{ display:flex; flex-wrap:wrap; gap:.45rem; margin:.65rem 0; }}
    .chip {{ display:inline-flex; align-items:center; gap:.3rem; padding:.32rem .55rem; border-radius:var(--pill); background:#F1F5F9; color:#334155; font-size:.75rem; font-weight:800; }}
    .category-badge {{ position:absolute; left:.85rem; top:.85rem; z-index:2; color:white; padding:.38rem .65rem; border-radius:var(--pill); font-size:.76rem; font-weight:900; box-shadow:0 10px 22px rgba(15,23,42,.22); }}
    .cat-adventure {{ background:#EA580C; }} .cat-beach {{ background:#0891B2; }} .cat-heritage {{ background:#7C3AED; }}
    .cat-family {{ background:#2563EB; }} .cat-honeymoon {{ background:#DB2777; }} .cat-nature {{ background:#16A34A; }} .cat-international {{ background:#0F766E; }}
    .price-badge {{ position:absolute; right:.85rem; bottom:.85rem; z-index:2; padding:.55rem .75rem; border-radius:16px; background:white; color:var(--orange); font-weight:900; box-shadow:var(--shadow-soft); transform:translateY(4px); transition:transform .22s ease; }}
    .tour-card:hover .price-badge {{ transform:translateY(0); }}
    .few-seats {{ display:inline-flex; align-items:center; gap:.35rem; color:#92400E; background:#FEF3C7; border-radius:var(--pill); padding:.3rem .55rem; font-size:.72rem; font-weight:900; }}
    .seat-meter {{ height:9px; border-radius:var(--pill); background:#E2E8F0; overflow:hidden; margin:.7rem 0 .3rem; }}
    .seat-meter span {{ display:block; height:100%; width:var(--fill); background:linear-gradient(90deg,var(--success),var(--teal),var(--cyan)); border-radius:inherit; }}
    .metric-card {{ display:flex; gap:.8rem; align-items:center; }}
    .metric-icon {{ width:46px;height:46px;border-radius:16px;display:grid;place-items:center;background:linear-gradient(135deg,var(--teal),var(--cyan));color:white;flex:0 0 auto; }}
    .metric-card .label {{ color:var(--muted);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em; }}
    .metric-card .value {{ color:var(--text);font-size:1.55rem;font-weight:900;margin-top:.1rem; }}
    .metric-trend {{ color:var(--success);font-size:.76rem;font-weight:800; }}
    .badge {{ display:inline-flex;align-items:center;gap:.4rem;padding:.34rem .62rem;border-radius:var(--pill);font-size:.77rem;font-weight:900;white-space:nowrap; }}
    .badge::before {{ content:""; width:7px;height:7px;border-radius:50%; background:currentColor; }}
    .badge.confirmed,.badge.paid,.badge.allocated {{ background:#DCFCE7;color:#166534; }}
    .badge.modified {{ background:#DBEAFE;color:#1D4ED8; }} .badge.pending,.badge.unpaid {{ background:#FEF3C7;color:#92400E; }}
    .badge.cancelled,.badge.failed {{ background:#FEE2E2;color:#991B1B; }} .badge.completed {{ background:#CCFBF1;color:#0F766E; }}
    .stepper {{ display:flex;align-items:center;gap:.5rem;margin:1rem 0; }}
    .step {{ display:flex;align-items:center;gap:.45rem;padding:.55rem .8rem;border-radius:var(--pill);background:#E2E8F0;color:#64748B;font-weight:900;font-size:.78rem; }}
    .step.active,.step.done {{ background:linear-gradient(135deg,var(--teal),var(--cyan));color:white;box-shadow:var(--glow-teal); }}
    .step-line {{ flex:1; height:3px; border-radius:var(--pill); background:linear-gradient(90deg,var(--teal),#E2E8F0); }}
    .ticket-card {{ background:linear-gradient(135deg,#FFFFFF,#ECFEFF); border-left:6px dashed rgba(20,184,166,.55); }}
    .success-mark path {{ stroke-dasharray:60; stroke-dashoffset:60; }}
    .chart-card {{ padding:1rem; margin-bottom:1rem; }}
    .chart-title {{ display:flex;align-items:center;justify-content:space-between;margin-bottom:.5rem; }}
    .chart-title strong {{ font-family:"Plus Jakarta Sans",Inter,sans-serif; }}
    .empty-state {{ text-align:center;padding:2.4rem;border:1px dashed #CBD5E1;border-radius:var(--radius-lg);background:rgba(255,255,255,.75); }}

    .stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] button {{
      border-radius:var(--pill) !important; min-height:44px; font-weight:900 !important; border:1px solid rgba(15,118,110,.22) !important;
      transition:transform .18s ease, box-shadow .18s ease, background .18s ease !important;
    }}
    .stButton > button:hover, .stDownloadButton > button:hover, [data-testid="stFormSubmitButton"] button:hover {{ transform:translateY(-2px); box-shadow:var(--shadow-soft); }}
    button[kind="primary"], [data-testid="stFormSubmitButton"] button[kind="primary"] {{
      background:var(--gradient-cta) !important; border-color:transparent !important; color:white !important; box-shadow:var(--glow-orange) !important;
    }}
    [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input, [data-testid="stDateInput"] input, textarea {{
      border-radius:16px !important; border:1px solid #CBD5E1 !important; background:rgba(255,255,255,.9) !important;
    }}
    [data-testid="stTextInput"] input:focus, [data-testid="stNumberInput"] input:focus, [data-testid="stDateInput"] input:focus, textarea:focus {{
      border-color:var(--teal) !important; box-shadow:var(--glow-teal) !important;
    }}
    [data-testid="stAlert"] {{ border-radius:18px; border:1px solid rgba(20,184,166,.18); box-shadow:var(--shadow-soft); }}
    [data-testid="stMetric"] {{ background:white;border-radius:18px;padding:1rem;border:1px solid #E2E8F0;box-shadow:var(--shadow-soft); }}
    [data-testid="stDataFrame"] {{ border-radius:18px; overflow:hidden; box-shadow:var(--shadow-soft); border:1px solid #E2E8F0; }}
    details {{ border-radius:18px !important; border:1px solid #E2E8F0 !important; background:white !important; box-shadow:var(--shadow-soft); }}
    .stTabs [data-baseweb="tab-list"] {{ gap:.35rem; background:white; border-radius:var(--pill); padding:.35rem; box-shadow:var(--shadow-soft); }}
    .stTabs [data-baseweb="tab"] {{ border-radius:var(--pill); font-weight:900; }}

    @keyframes pageIn {{ from {{ opacity:0; transform:translateY(16px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes cardIn {{ from {{ opacity:0; transform:translateY(16px) scale(.98); }} to {{ opacity:1; transform:translateY(0) scale(1); }} }}
    @keyframes fadeUp {{ from {{ opacity:0; transform:translateY(18px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes wordIn {{ from {{ opacity:0; transform:translateY(28px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes drift {{ from {{ transform:translate3d(0,0,0); }} to {{ transform:translate3d(-26px,18px,0); }} }}
    @keyframes drift2 {{ from {{ transform:translate3d(0,0,0) scale(1); }} to {{ transform:translate3d(22px,-18px,0) scale(1.08); }} }}
    @keyframes marquee {{ from {{ transform:translateX(0); }} to {{ transform:translateX(-50%); }} }}
    @keyframes pulseSoft {{ 0%,100% {{ transform:scale(1); }} 50% {{ transform:scale(1.035); }} }}
    @keyframes planeFloat {{ 0%,100% {{ transform:translateY(0) rotate(-8deg); }} 50% {{ transform:translateY(-18px) rotate(3deg); }} }}
    @keyframes drawCheck {{ to {{ stroke-dashoffset:0; }} }}
    {motion_css}
    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{ animation:none !important; transition:none !important; scroll-behavior:auto !important; }}
    }}
    @media (max-width: 992px) {{
      .hero-premium {{ min-height:480px;padding:3rem 1.6rem; }}
      .hero-stats {{ grid-template-columns:1fr; }}
    }}
    @media (max-width: 640px) {{
      .main .block-container {{ padding-left:.85rem;padding-right:.85rem; }}
      .hero-premium {{ border-radius:18px; min-height:430px; }}
      .hero-actions {{ flex-direction:column; }}
      .stepper {{ flex-wrap:wrap; }}
    }}
    </style>
    """


def inject_global_styles():
    st.markdown(_global_css(ENABLE_ANIMATIONS), unsafe_allow_html=True)
