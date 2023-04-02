import tkinter as tk
import json
import numpy as np
import joblib

def save_input(income,loan,history):
    input_dict = {
        'TotalIncome': income.get(),
        'LoanAmount': loan.get(),
        'Credit_History': history.get()
    }
    json_string = json.dumps(input_dict)
    print(json_string)
    return json_string

def load_model():
    # Load the saved linear regression model
    model = joblib.load('model.pkl')
    return model

def predict_output(model, input_data):
    # Convert the input data to the format expected by the model
    input_array = np.fromiter(input_data.values(), dtype=float).reshape(1,-1)
    # Use the model to predict the output
    predicted_output = model.predict(input_array)
    return predicted_output

root = tk.Tk()
root.title("User Input Window")

# Add a label and entry fields for income, loan, and history
income_label = tk.Label(root, text="Total Income:")
income_label.pack()
income_entry = tk.Entry(root)
income_entry.pack()

loan_label = tk.Label(root, text="Loan Amount:")
loan_label.pack()
loan_entry = tk.Entry(root)
loan_entry.pack()

history_label = tk.Label(root, text="Credit History:")
history_label.pack()
history_entry = tk.Entry(root)
history_entry.pack()

# Add a button to save the input
save_button = tk.Button(root, text="Save", command=lambda: predict_and_display(income_entry, loan_entry, history_entry))
save_button.pack()

def predict_and_display(income, loan, history):
    input_data = {
        'TotalIncome': income.get(),
        'LoanAmount': loan.get(),
        'Credit_History': history.get()
    }
    
    model = load_model()
    predicted_output = predict_output(model, input_data)
    
    predicted_output_label.config(text=f"Predicted Output: {predicted_output}")
    predicted_output_label.pack()

predicted_output_label = tk.Label(root)

# Start the main loop
root.mainloop()
