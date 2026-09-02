import streamlit as st

st.set_page_config(page_title="Torre de Control", page_icon="📦", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'IBM Plex Sans', sans-serif;
    }
    .stApp {
        background-color: #14171A;
    }
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif !important;
        color: #EFEBE2 !important;
        letter-spacing: 0.02em;
    }
    .stCaption, p, span, label {
        color: #B7BEC4 !important;
    }
    .app-card {
        background-color: #1D2126;
        border-left: 4px solid #F2B233;
        border-radius: 4px;
        padding: 14px 16px;
        margin-bottom: 10px;
    }
    .app-card .app-name {
        font-family: 'IBM Plex Sans', sans-serif;
        font-weight: 600;
        font-size: 1.02rem;
        color: #EFEBE2;
        margin: 0;
    }
    .app-card .app-desc {
        font-size: 0.85rem;
        color: #8A9199;
        margin: 2px 0 0 0;
    }
    .group-label {
        font-family: 'Oswald', sans-serif;
        font-weight: 600;
        font-size: 1.15rem;
        color: #F2B233;
        margin-top: 22px;
        margin-bottom: 6px;
    }
    div[data-testid="stLinkButton"] a {
        background-color: #F2B233 !important;
        color: #14171A !important;
        border: none !important;
        font-weight: 600 !important;
    }
    div[data-testid="stLinkButton"] a:hover {
        background-color: #FFC94D !important;
    }
    .stButton button {
        background-color: #2A2F35 !important;
        color: #6B7278 !important;
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1>Torre de Control</h1>", unsafe_allow_html=True)
st.caption("Acceso directo a tus apps de embarque y documentos — un toque, sin buscar ligas")

APPS = {
    "Walmart": [
        {
            "name": "Plan de Embarque",
            "desc": "CSV del portal → Excel + etiquetas QR/ZPL",
            "url": "https://wm-plan-de-embarque-zauaophkkndxlmbhlthjxc.streamlit.app",
        },
    ],
    "C&A": [
        {
            "name": "Separador de Etiquetas LPN",
            "desc": "PDF 2 por página → hojas 4×6 individuales",
            "url": "https://cprtnanexon2fnucpttzx3.streamlit.app",
        },
        {
            "name": "Packing List",
            "desc": "OC en PDF → Excel de packing list nacional",
            "url": "https://naga-cya-packing-list.streamlit.app",
        },
        {
            "name": "Etiqueta ITEM PACK",
            "desc": "PDF de ITEM PACK → etiquetas Code39 (ZPL/PDF)",
            "url": "https://c-a-qr-etiqueta-5cn5km7qchxsb8rd5xutpb.streamlit.app",
        },
        {
            "name": "Etiqueta Larga Prepack",
            "desc": "Llenado de Excel para etiqueta larga de prepack",
            "url": "https://c-a-llenado-excell-para-etiqueta-larga-prepack-5cnxklkmzptuefq.streamlit.app",
        },
    ],
    "Santory / ZOY": [
        {
            "name": "Packing List Surtido",
            "desc": "OC + captura de surtido → Packing List Santory/ZOY",
            "url": "https://c-a-packing-list-llenado-mtdjqejwxgfd8hqmd2zngp.streamlit.app",
        },
    ],
    "Liverpool": [
        {
            "name": "Carta de Acceso CEDIS",
            "desc": "Anexo 2 — solicitud de acceso de personal externo",
            "url": "https://carta-acceso-liverpool-para-etiquetas-jnstd9iqyj247vfjcmbk6n.streamlit.app",
        },
        {
            "name": "Carta de Recolección de Equipo",
            "desc": "Autorización para arrendar/recoger contenedores y equipo",
            "url": "https://carta-liverpool-arrendar-contenedores-y-entregas-siwv4fpvahvhw.streamlit.app",
        },
    ],
    "Coppel": [
        {
            "name": "Etiqueta Coppel",
            "desc": "En diseño — se agrega en cuanto esté lista",
            "url": "",
        },
    ],
}

for client, apps in APPS.items():
    st.markdown(f"<div class='group-label'>{client}</div>", unsafe_allow_html=True)
    for app in apps:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(
                f"""<div class="app-card">
                        <p class="app-name">{app['name']}</p>
                        <p class="app-desc">{app['desc']}</p>
                    </div>""",
                unsafe_allow_html=True,
            )
        with col2:
            if app["url"]:
                st.link_button("Abrir", app["url"], use_container_width=True)
            else:
                st.button("Pendiente", disabled=True, use_container_width=True, key=f"{client}-{app['name']}")

st.divider()
st.caption("Sugerencia: abre esta página en Safari y usa Compartir → Agregar a pantalla de inicio, para tener un ícono directo en tu iPhone.")
