import streamlit as st
from langgraph.graph import StateGraph, START, END
from typing import TypedDict


# Step 1: Define the BMI State
class BMIState(TypedDict, total=False):
    weight_kg: float
    height_m: float
    bmi: float
    category: str


# Step 2: BMI Calculation Function
def calculate_bmi(state: BMIState) -> BMIState:
    weight = state["weight_kg"]
    height = state["height_m"]
    bmi = weight / (height ** 2)
    state["bmi"] = round(bmi, 2)
    return state


# Step 3: BMI Label Function
def label_bmi(state: BMIState) -> BMIState:
    bmi = state["bmi"]
    if bmi < 18.5:
        state["category"] = "Underweight"
    elif 18.5 <= bmi < 25:
        state["category"] = "Normal"
    elif 25 <= bmi < 30:
        state["category"] = "Overweight"
    else:
        state["category"] = "Obese"
    return state


# Step 4: Build LangGraph workflow
graph = StateGraph(BMIState)
graph.add_node("calculate_bmi", calculate_bmi)
graph.add_node("label_bmi", label_bmi)
graph.add_edge(START, "calculate_bmi")
graph.add_edge("calculate_bmi", "label_bmi")
graph.add_edge("label_bmi", END)
workflow = graph.compile()


# Step 5: Streamlit UI
st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("🧮 BMI Calculator using LangGraph")

with st.form("bmi_form"):
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.5)
    height = st.number_input("Enter your height (m):", min_value=0.1, step=0.01)
    submitted = st.form_submit_button("Calculate BMI")

if submitted:
    input_state = {"weight_kg": weight, "height_m": height}
    result = workflow.invoke(input_state)

    st.subheader("📊 Result")
    st.write(f"**Weight:** {result['weight_kg']} kg")
    st.write(f"**Height:** {result['height_m']} m")
    st.write(f"**BMI:** {result['bmi']}")
    st.write(f"**Category:** {result['category']}")
