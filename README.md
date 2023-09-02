# AI-Loan-Prediction

AI-Loan-Prediction is an application that uses machine learning to predict loan eligibility. It helps customers and financial institutions make informed decisions about loan approvals.

## Installation

To run this application, you need to have the following dependencies installed:

- **numpy**: Install using `pip install numpy`
- **pandas**: Install using `pip install pandas`
- **joblib**: Install using `pip install joblib`

## Usage

Follow these steps to use the AI-Loan-Prediction application:

1. Run the machine learning model training script:

- python model.py
- Ensure the model is successfully trained and saved.

2. Start the graphical user interface (GUI) for loan predictions:

- python gui.py
- The GUI allows you to input customer information and receive instant loan eligibility predictions.

## How It Works

AI-Loan-Prediction employs data preprocessing, feature engineering, and logistic regression to predict loan status accurately. Key steps include:

- Data preprocessing to handle missing values and data transformation.
- Feature engineering to create new relevant features like 'TotalIncome_log' and 'LoanAmount_log.'
- Model training using logistic regression for accurate loan status predictions.
- Cross-validation to assess model performance.

The `model.py` script trains the model and saves it as 'model.pkl,' which is then loaded by the GUI (`gui.py`) for real-time loan predictions.

AI-Loan-Prediction streamlines the loan approval process, providing data-driven insights for confident lending decisions.
