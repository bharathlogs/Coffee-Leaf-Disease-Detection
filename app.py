import streamlit as st
from streamlit_option_menu import option_menu
from components import detection, dataset, disease_tracking, team

st.set_page_config(
    page_title="Coffee Leaf AI", page_icon=":material/eco:",
    layout="wide", initial_sidebar_state="auto",
)

THEME_COLORS = {
    "DARK": {
        "primaryColor": "#71D9A0", "backgroundColor": "#101713",
        "secondaryBackgroundColor": "#19231D", "textColor": "#E9F0EB",
    },
    "LIGHT": {
        "primaryColor": "#237A50", "backgroundColor": "#F5F7F3",
        "secondaryBackgroundColor": "#FFFFFF", "textColor": "#20382A",
    },
}

if "dark_theme" not in st.session_state:
    st.session_state.dark_theme = True
current_theme = THEME_COLORS["DARK" if st.session_state.dark_theme else "LIGHT"]
p, bg, surface, text = (current_theme[k] for k in (
    "primaryColor", "backgroundColor", "secondaryBackgroundColor", "textColor"
))

st.markdown(f"""
<style>
:root {{ --leaf-accent: {p}; --leaf-bg: {bg}; --leaf-surface: {surface}; --leaf-text: {text}; }}
.stApp {{ background: var(--leaf-bg); color: var(--leaf-text); }}
[data-testid="stHeader"] {{ background: transparent; }}
[data-testid="stMainBlockContainer"] {{ max-width: 1260px; padding: 2.4rem 3.5rem 4rem; }}
[data-testid="stSidebar"] {{ background: var(--leaf-surface); border-right: 1px solid {p}18; }}
[data-testid="stSidebarUserContent"] {{ padding: 2rem 1.4rem; }}
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
    color: var(--leaf-text); font-size: .75rem; letter-spacing: .12em; font-weight: 600;
}}
[data-testid="stSidebar"] hr {{ margin: 1.2rem 0; opacity: .5; }}
[data-testid="stSidebar"] label p, [data-testid="stCaptionContainer"] p {{ color: {text}A6; }}
[data-testid="stSelectbox"] [role="combobox"] {{ color: var(--leaf-text); }}
[data-testid="stSelectbox"] > div > div {{ background: var(--leaf-surface); }}
[data-testid="stWidgetLabel"] p {{ color: var(--leaf-text); }}
h1, h2, h3 {{ color: var(--leaf-text); letter-spacing: -.035em; }}
.leaf-brand {{ padding: 0 0 1.5rem; color: var(--leaf-text); font-size: 1.35rem; font-weight: 700; letter-spacing: -.05em; }}
.leaf-brand span {{ color: var(--leaf-accent); }}
.leaf-brand small {{ display: block; color: {text}80; font-size: .66rem; font-weight: 500; letter-spacing: .16em; margin-top: .5rem; }}
.leaf-hero {{ display: grid; grid-template-columns: 1.45fr 1fr; gap: 1.5rem; align-items: center; padding: 2rem 0 1.5rem; }}
.leaf-eyebrow {{ color: var(--leaf-accent); font-size: .68rem; letter-spacing: .16em; font-weight: 600; text-transform: uppercase; }}
.leaf-hero h1 {{ font-size: clamp(2rem, 3.8vw, 3.5rem); line-height: 1.08; font-weight: 650; margin: .9rem 0 1rem; padding: 0; }}
.leaf-hero h1 em {{ color: var(--leaf-accent); font-style: normal; }}
.leaf-hero p {{ color: {text}A6; line-height: 1.65; font-size: .93rem; max-width: 31rem; margin-bottom: 1.2rem; }}
.leaf-hero img {{ width: 100%; height: 260px; object-fit: cover; border-radius: 24px 6px 24px 6px; opacity: .88; }}
.leaf-tags {{ display: flex; flex-wrap: wrap; gap: .5rem; }}
.leaf-tags span {{ border: 1px solid {p}30; border-radius: 30px; padding: .3rem .7rem; color: {text}B3; font-size: .69rem; }}
.st-key-instructions_container, .st-key-container_with_border, .st-key-side_border {{
    background: var(--leaf-surface); border: 1px solid {p}20; border-radius: 18px; padding: 1.5rem;
}}
.st-key-instructions_container h3 {{ font-size: 1.2rem; padding-top: 0; }}
[class*="st-key-disease_card_"] {{ border: 1px solid {p}25; border-radius: 14px; padding: 1.1rem; background: var(--leaf-surface); }}
[data-testid="stFileUploader"] {{ border: 1px dashed {p}55; border-radius: 13px; background: {p}06; padding: .4rem; }}
[data-testid="stFileUploaderDropzone"] {{ background: transparent; }}
.stButton > button {{ border-radius: 10px; border-color: {p}35; transition: border-color .18s, background .18s; }}
.stButton > button:hover {{ border-color: var(--leaf-accent); background: {p}12; }}
.stButton > button:focus-visible {{ outline: 2px solid var(--leaf-accent); outline-offset: 3px; }}
.leaf-footer {{ margin-top: 2rem; padding-top: 1rem; border-top: 1px solid {p}18; color: {text}75; font-size: .72rem; line-height: 1.6; }}
.stApp {{
    background: radial-gradient(ellipse at 8% 8%, {p}1C, transparent 45%),
                radial-gradient(ellipse at 90% 65%, {p}12, transparent 48%), var(--leaf-bg);
    background-attachment: fixed;
}}
[data-testid="stSidebar"] {{
    background: {surface}A6; backdrop-filter: blur(28px) saturate(140%);
    -webkit-backdrop-filter: blur(28px) saturate(140%); border-right: 1px solid #FFFFFF12;
}}
.leaf-hero, .st-key-instructions_container, .st-key-container_with_border,
.st-key-side_border, [class*="st-key-disease_card_"] {{
    background: linear-gradient(130deg, #FFFFFF0B, #FFFFFF03), {surface}70;
    border: 1px solid #FFFFFF18; box-shadow: inset 0 1px 0 #FFFFFF09, 0 12px 45px #00000018;
    backdrop-filter: blur(22px) saturate(135%); -webkit-backdrop-filter: blur(22px) saturate(135%);
}}
.leaf-hero {{ border-radius: 22px; padding: 1.8rem; margin: 1.2rem 0 .7rem; }}
.leaf-hero img {{ height: 240px; border: 1px solid #FFFFFF1A; box-shadow: 0 8px 30px #00000025; }}
.leaf-hero h1 {{ font-size: clamp(2rem, 3.4vw, 3.1rem); }}
.leaf-tags span {{ background: {p}08; }}
[data-testid="stFileUploader"] {{ background: {p}06; border-color: {p}48; }}
.stButton > button {{ background: #FFFFFF06; box-shadow: inset 0 1px 0 #FFFFFF08; }}
@media (max-width: 850px) {{
    [data-testid="stMainBlockContainer"] {{ padding: 1.4rem 1.3rem 3rem; }}
    .leaf-hero {{ gap: 1rem; padding: 1.3rem; }}
    .leaf-hero img {{ height: 220px; }}
}}
@media (max-width: 600px) {{
    .leaf-hero {{ grid-template-columns: 1fr; padding-top: 1rem; }}
    .leaf-hero img {{ height: 150px; object-position: center 40%; }}
    .leaf-hero h1 {{ font-size: 2.2rem; }}
    .st-key-instructions_container {{ padding: 1.1rem; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown(
    '<div class="leaf-brand">Coffee Leaf <span>AI</span><small>A CLOSER LOOK AT LEAF HEALTH</small></div>',
    unsafe_allow_html=True,
)
tab = option_menu(
    None, ["Home", "Dataset", "Map", "Team"],
    icons=["house", "database", "map", "people"], default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "5px!important", "background-color": surface + "B3", "border-radius": "12px"},
        "icon": {"color": p, "font-size": "14px"},
        "nav-link": {"font-size": "13px", "text-align": "center", "color": text,
                     "border-radius": "8px", "margin": "0", "--hover-color": p + "14"},
        "nav-link-selected": {"color": p, "background-color": p + "18", "font-weight": "600"},
    },
)

if tab == "Home":
    detection.main(THEME_COLORS)
elif tab == "Dataset":
    dataset.main()
elif tab == "Map":
    disease_tracking.main(THEME_COLORS)
elif tab == "Team":
    team.main(THEME_COLORS)

st.markdown(
    '<div class="leaf-footer">Built with computer vision. Predictions are model estimates; '
    'confidence scores do not establish accuracy on new photos.</div>', unsafe_allow_html=True,
)
