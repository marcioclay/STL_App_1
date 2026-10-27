import streamlit as st

# Configura a página para ocupação ampla (banner horizontal completo)
st.set_page_config(
    page_title="Mestrado - Computação nas Nuvens",
    layout="wide"
)

# Título da aplicação
st.title("🎈 Mestrado - Computação nas Nuvens")
st.write(
    "Construção de app em cloud [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 1. Bloco / Banner Central de Imagem
st.image(
    "https://pixabay.com/pt/images/search/banner/",
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# 2. Três blocos coloridos inferiores em 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="background-color: #FDE8A5; padding: 20px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; min-height: 100px;">
            <div>
                <h3 style="margin: 0; color: #1E1E1E; font-size: 20px; font-weight: bold;">Save 35%</h3>
                <p style="margin: 4px 0 0 0; color: #4A4A4A; font-size: 13px;">On your first repeat delivery order</p>
            </div>
            <div style="font-size: 36px;">🚚</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="background-color: #E2CEE6; padding: 20px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; min-height: 100px;">
            <div>
                <h3 style="margin: 0; color: #1E1E1E; font-size: 20px; font-weight: bold;">Latest Deals</h3>
                <p style="margin: 4px 0 0 0; color: #4A4A4A; font-size: 13px;">Save up to $393/year</p>
            </div>
            <div style="font-size: 36px;">🐱</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="background-color: #CEF0F7; padding: 20px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; min-height: 100px;">
            <div>
                <h3 style="margin: 0; color: #1E1E1E; font-size: 20px; font-weight: bold;">Top Rate Products</h3>
                <p style="margin: 4px 0 0 0; color: #4A4A4A; font-size: 13px;">Recommended pet favourites</p>
            </div>
            <div style="font-size: 36px;">🦴</div>
        </div>
        """,
        unsafe_allow_html=True
    )