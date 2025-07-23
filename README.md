# BMI Calculator using LangGraph and Streamlit

A simple Body Mass Index (BMI) calculator built with Streamlit and LangGraph that demonstrates workflow automation for health calculations.

## Features

- Interactive web interface for BMI calculation
- Automated workflow using LangGraph for processing steps
- Real-time BMI categorization (Underweight, Normal, Overweight, Obese)
- Clean, user-friendly interface with form validation

## Requirements

```
streamlit
langgraph
```

## Installation

1. Clone or download the application code
2. Install the required dependencies:
   ```bash
   pip install streamlit langgraph
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter your weight in kilograms and height in meters

4. Click "Calculate BMI" to see your results

## How It Works

The application uses LangGraph to create a sequential workflow with two main processing nodes:

### Workflow Steps

1. **BMI Calculation**: Computes BMI using the formula: `BMI = weight (kg) / height (m)²`
2. **BMI Categorization**: Classifies the result according to standard BMI categories:
   - **Underweight**: BMI < 18.5
   - **Normal**: 18.5 ≤ BMI < 25
   - **Overweight**: 25 ≤ BMI < 30
   - **Obese**: BMI ≥ 30

### Architecture

- **State Management**: Uses TypedDict to define the application state containing weight, height, BMI value, and category
- **Graph Workflow**: LangGraph manages the sequential processing from input validation through final categorization
- **User Interface**: Streamlit provides the web interface with form handling and result display

## Code Structure

- `BMIState`: TypedDict class defining the state structure
- `calculate_bmi()`: Function to compute BMI from weight and height
- `label_bmi()`: Function to categorize BMI value
- `workflow`: LangGraph compilation of the processing pipeline
- Streamlit UI components for user interaction

## Input Validation

- Weight: Minimum 1.0 kg, step increment of 0.5 kg
- Height: Minimum 0.1 m, step increment of 0.01 m

## Output

The application displays:
- Input weight and height values
- Calculated BMI (rounded to 2 decimal places)
- BMI category classification

## Note

This application is for educational and informational purposes only. BMI is a general indicator and should not replace professional medical advice. Consult healthcare professionals for comprehensive health assessments.
