import streamlit as st
import requests
import subprocess
from pathlib import Path

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Agentic AI PPT Generator",
    page_icon="🧠",
    layout="centered",
)

# ---------------------------
# PAGE HEADER
# ---------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#4A90E2;">
        🧠 Agentic-Based PowerPoint Generator
    </h1>
    <p style="text-align:center; font-size:18px; color:#555;">
        Generate clean, professional PPTX files using your custom prompt.
    </p>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# MAIN INPUT CARD
# ---------------------------
st.markdown(
    """
    <div style="
        background-color:#F7F9FC; 
        padding:25px; 
        border-radius:12px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
        <h3 style="color:#333;">📄 Enter Your PPT Instructions</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

prompt = st.text_area(
    "",
    placeholder="Describe your PPT content here...\n\nExample:\n- Title slide about Agentic AI\n- Slide explaining Generative AI vs Agentic AI\n- Use bullet points\n- Add clean layout",
    height=200
)

# ---------------------------
# GENERATE BUTTON
# ---------------------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    generate_clicked = st.button("🚀 Generate PPT", use_container_width=True)

# ---------------------------
# BACKEND PROCESSING
# ---------------------------
output_file_path = r"C:\Users\udayk\Videos\recording\power\power\Data_Science_with_Gen_AI_and_Agentic_AI.pptx"

if generate_clicked:
    if not prompt.strip():
        st.warning("⚠️ Please enter instructions before generating the PPT.")
    else:
        with st.spinner("Generating your presentation... This may take a few seconds ⏳"):
            try:
                # Call your n8n webhook
                response = requests.post(
                    url="https://rishiiwanth.app.n8n.cloud/webhook-test/a8c2b161-9c4c-4461-b9f0-f2e91e5c53f5",
                    json={"prompt": prompt}
                )

                if response.status_code == 200:
                    st.success("✅ PowerPoint code received successfully!")

                    # Save python file
                    with open("app1.py", "w") as file:
                        file.write(response.json()["output"].strip("```python"))

                    # Execute python file to generate PPT
                    subprocess.run(["python", "app1.py"])

                    st.success("🎉 PPT generated successfully!")

                else:
                    st.error("❌ Failed to generate PPT. Please try again.")

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")

# ---------------------------
# DOWNLOAD SECTION
# ---------------------------
if Path(output_file_path).exists():
    st.markdown("---")
    st.markdown(
        "<h3 style='text-align:center; color:#4A90E2;'>📥 Your File is Ready</h3>",
        unsafe_allow_html=True
    )

    with open(output_file_path, "rb") as f1:
        st.download_button(
            label="⬇️ Download PPTX File",
            data=f1,
            file_name="Generated_Presentation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            use_container_width=True,
        )
else:
    st.info("ℹ️ Generate a PPT to enable download.")
