import streamlit as st
import dna_engine
import lifestyle_logic

st.set_page_config(page_title="Bio-Epigenetic App", layout="centered")
st.title("🧬 Genomix: Epigenetic Analysis System")
st.write("An interdisciplinary tool for DNA decoding and health risk prediction.")

# Sidebar Inputs
st.sidebar.header("User Genetic & Lifestyle Data")
dna_seq = st.sidebar.text_area("DNA Sequence", "ATGCCGTAGCGCGCGCATATCGATCGATCGATC")
stress = st.sidebar.slider("Stress Level", 1, 10, 5)
sleep = st.sidebar.number_input("Sleep Hours", 4, 12, 7)
activity = st.sidebar.selectbox("Activity Level", ["Low", "Moderate", "High"])

if st.sidebar.button("Analyze System"):
    # 1. Biological Computation
    bio_data = dna_engine.process_genetic_data(dna_seq)
    
    # 2. Predictive Analysis
    lifestyle_vars = {
        'stress_level': stress, 
        'avg_sleep_hours': sleep, 
        'physical_activity': activity
    }
    risk_df = lifestyle_logic.calculate_epigenetic_risk(lifestyle_vars, bio_data)
    
    # 3. Visual Display (The "Application")
    st.subheader("Results Overview")
    st.table(risk_df)
    
    col1, col2 = st.columns(2)
    col1.metric("GC Content", f"{bio_data['gc_content']}%")
    col2.metric("Gene Sensitivity", "High" if bio_data['is_cpg_island'] else "Low")
    
    st.info(f"**Decoded Protein Sequence:** {bio_data['protein_sequence']}")