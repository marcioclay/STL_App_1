import streamlit as st


st.set_page_config(
    page_title="Mestrado - Cloud",
    layout="wide"
)


st.title("Mestrado - Cloud")
st.subheader("Home")


banner_url = "https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=1200&q=80"
st.image(banner_url, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="background-color: #FFF2B2; padding: 24px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; min-height: 110px;">
            <div>
                <h3 style="margin: 0; color: #1E1E1E; font-size: 20px; font-weight: bold;">Save 35%</h3>
                <p style="margin: 4px 0 0 0; color: #555; font-size: 13px;">On your first repeat delivery order</p>
            </div>
            <div style="font-size: 38px;">🚚</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="background-color: #E2D0E6; padding: 24px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; min-height: 110px;">
            <div>
                <h3 style="margin: 0; color: #1E1E1E; font-size: 20px; font-weight: bold;">Latest Deals</h3>
                <p style="margin: 4px 0 0 0; color: #555; font-size: 13px;">Save up to $393/year</p>
            </div>
            <div style="font-size: 38px;">🐱</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="background-color: #D3F2F8; padding: 24px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; min-height: 110px;">
            <div>
                <h3 style="margin: 0; color: #1E1E1E; font-size: 20px; font-weight: bold;">Top Rate Products</h3>
                <p style="margin: 4px 0 0 0; color: #555; font-size: 13px;">Recommended pet favourites</p>
            </div>
            <div style="font-size: 38px;">🦴</div>
        </div>
        """,
        unsafe_allow_html=True
    )

1. Sync the dependencies

   ```
   $ uv sync
   ```

2. Run the app

   ```
   $ uv run streamlit run streamlit_app.py
   ```
