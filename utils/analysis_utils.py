import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def perform_analysis(q_text, df):
    # Placeholder: You will parse q_text to determine the task
    # and return a result matching requested format
    answers = []

    # Example: dummy answers
    answers.append(1)  # e.g., how many $2bn movies before 2000
    answers.append("Titanic")
    answers.append(0.485782)
    answers.append(generate_sample_plot())

    return answers

def generate_sample_plot():
    # Create dummy scatterplot
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [4, 5, 6])
    ax.plot([1, 2, 3], [4.2, 5.1, 6.2], "r--")  # dotted red regression line
    ax.set_xlabel("Rank")
    ax.set_ylabel("Peak")

    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode("utf-8")
    return f"data:image/png;base64,{img_str}"
