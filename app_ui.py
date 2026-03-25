import streamlit as st
import dna_engine
import lifestyle_logic

# 1. Page Configuration
st.set_page_config(page_title="Bio-Epigenetic Analyzer", layout="wide")
st.title("🧬 DNA & Epigenetic Health Application")
st.markdown("Analyze how your **Lifestyle (Software)** interacts with your **Genetics (Hardware)**.")

# 2. Sidebar for Inputs
st.sidebar.header("Step 1: Genetic Hardware")
dna_input = st.sidebar.text_area("Enter DNA Sequence (ATGC):", "ATGCCGTAGCGCGCGCATATCGATCGATCGATC")

st.sidebar.header("Step 2: Lifestyle Software")
stress = st.sidebar.slider("Stress Level", 1, 10, 5)
sleep = st.sidebar.number_input("Average Sleep (Hours)", 4, 12, 8)
activity = st.sidebar.selectbox("Physical Activity", ["Low", "Moderate", "High"])

# 3. Execution Block (Triggered by Button)
if st.sidebar.button("Run Health Analysis"):
    # Connect to your Bioinformatics engine
    bio_features = dna_engine.process_genetic_data(dna_input)
    
    # Prepare data for the Predictive Model
    lifestyle_vars = {
        'stress_level': stress,
        'avg_sleep_hours': sleep,
        'physical_activity': activity
    }
    
    # Generate the Pandas-based Risk Report
    risk_df = lifestyle_logic.calculate_epigenetic_risk(lifestyle_vars, bio_features)

    # 4. Display Results
    st.subheader("Final Health Analysis")
    
    # Display the table without the '0' index
    st.table(risk_df.set_index('Metric'))
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("GC Content", f"{bio_features['gc_content']}%")
        st.write(f"**Molecular Weight:** {bio_features['molecular_weight']} u")
    with col2:
        st.metric("Gene Sensitivity", "High" if bio_features['is_cpg_island'] else "Low")
        st.write(f"**Sequence Length:** {len(dna_input)} bp")

    st.divider()
    st.info(f"**Decoded Protein (Biological Output):** {bio_features['protein_sequence']}")
    
    

