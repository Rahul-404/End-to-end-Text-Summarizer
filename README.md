# **End-to-End Text Summariser Web App**

This project involves an **End-to-End Text Summarization Web App** powered by a custom fine-tuned text summarization model. The app is deployed on AWS (using **ECR/EC2**), and it allows users to input text. The application generates concise and coherent summaries using a Hugging Face model 🤖, optimized on domain-specific data for improved accuracy 🔍.

---

## **Table of Contents**

- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Features](#features)
- [Modeling](#modeling)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## **Installation**

Follow these steps to install and run the project:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rahul-404/End-to-end-Text-Summarizer.git
    cd End-to-end-Text-Summarizer
    ```

2. **Create and activate a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Ensure that you have the correct AWS credentials configured if using AWS services like ECR/EC2 for deployment. Set up any other environment variables if required.

---

## **Project Structure**

The project is organized as follows:

```
End-to-end-Text-Summarizer/
│
├── src/
│   └── textSummarizer/
│       ├── __init__.py                     # Initialization of the project package
│       ├── components/
│       │   ├── __init__.py                 # Component initialization
│       │   ├── data_ingestion.py           # Data ingestion logic (if needed)
│       │   ├── data_transformation.py      # Data preprocessing (text cleaning, etc.)
|       |   ├── data_validation.py
|       |   ├── data_evaluation.py
|       |   └── model_trainer.py            # Fine-tuned text summarizer model
│       ├── pipeline/
│       │   ├── __init__.py                 # Pipeline initialization
│       │   └── summarization_pipeline.py   # Text summarization pipeline logic
|       ├── config/
|       |   ├── __init__.py
|       |   └── configuration.py
|       ├── constants/
|       |   └── __init__.py
|       ├── entity/
|       |   └── __init__.py
|       ├── logging/
|       |   └── __init__.py
|       ├── pipeline/
|       |   ├── __init__.py
|       |   ├── prediction.py
|       |   ├── stage_01_data_ingestion.py
|       |   ├── stage_02_data_validation.py
|       |   ├── stage_03_data_transformation.py
|       |   ├── stage_04_model_trainer.py
|       |   └── stage_05_model_evaluation.py
|       ├── utils
|       |   ├── __init__.py
|       |   └── common.py
│       └── __init__.py                       
├── app.py                                  # Main script for running the app
├── Dockerfile                              # Docker configuration to containerize the app
├── requirements.txt                        # Python dependencies
├── setup.py                                # Setup script for packaging
├── artifacts/                              # Directory to store trained models and outputs
└── README.md                               # Project documentation
```

- **`src/{project_name}/`**: The main source code directory where all the core project files are located.
- **`components/`**: Contains the logic for components like data ingestion, transformation, and model training (if applicable).
- **`pipeline/`**: Contains scripts that define the text summarization pipeline, handling text input and output flow.
- **`exception.py`**: Custom exceptions for error handling.
- **`logger.py`**: Logging utilities to keep track of the application's execution and errors.
- **`utils.py`**: Utility functions used throughout the project, such as metrics calculation or loading pre-trained models.
- **`app.py`**: Main entry point to start the application, interact with the summarizer, and handle user input/output.
- **`Dockerfile`**: Configuration file for containerizing the application using Docker.
- **`requirements.txt`**: Contains the list of dependencies needed to run the project.
- **`setup.py`**: Setup script for packaging and installing the project.
- **`artifacts/`**: Directory for storing models, data, and outputs.

---

## **How to Run the Project**

### 1. **Run the Application**

Once the dependencies are installed, you can start the application by running the following command:

```bash
python app.py
```

This will start a local server (usually at `http://localhost:8501`), allowing users to interact with the text summarization model via a simple web interface.

---

## **Features**

- **Fine-Tuned Summarization Model**: A custom fine-tuned Hugging Face model optimized on domain-specific data to generate accurate summaries.
- **Text Input**: Users can input long-form text or documents for summarization.
- **Concise Summaries**: The app generates concise, accurate summaries of the provided text.
- **AWS Deployment**: The application is deployed on **AWS EC2** using Docker, with the model hosted on **AWS ECR** for scalable production use.

---

## **Modeling**

The text summarizer uses a Hugging Face pre-trained model fine-tuned on domain-specific data. Fine-tuning is performed to ensure that the model provides better and more relevant summaries for specific types of content (e.g., news articles, scientific papers, etc.).

### **Fine-Tuned Model Pipeline**:
1. **Data Preprocessing**: Text is cleaned, tokenized, and prepared for input into the Hugging Face model.
2. **Model Fine-Tuning**: The model is fine-tuned on domain-specific data to improve summarization quality.
3. **Inference**: The fine-tuned model generates the summary for the given input text.

<!-- Example of using the summarizer:

```python
from src.{project_name}.components.summarizer import generate_summary

# Input text to summarize
input_text = """
Machine learning models are algorithms designed to detect patterns in data and make predictions based on those patterns.
They are widely used across industries, including finance, healthcare, and marketing, to analyze large datasets and derive insights.
"""

summary = generate_summary(input_text)
print(f"Summary: {summary}")
``` -->

---

## **Usage**

1. **Run the app**:
   - After starting the app using `python app.py`, open your browser and go to the **app's URL** (usually `http://localhost:8501`).
   
2. **Input Text**:
   - In the provided text box, input the text or document you want to summarize.
   
3. **Generate Summary**:
   - Click on the **"Generate Summary"** button, and the app will display the concise summary generated by the model.

---

## **Contributing**

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or bugfix.
4. Make your changes and test them locally.
5. Push your changes to your fork.
6. Open a pull request with a clear description of your changes.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## **Acknowledgments**

- **Hugging Face**: For providing pre-trained models and fine-tuning tools for text summarization.
- **AWS**: For hosting the application on EC2 and managing the containerized model with ECR.
- **Libraries Used**: 
    - **Transformers** for model loading and fine-tuning.
    - **Flask** or **Streamlit** for web app creation.
    - **Docker** for containerizing the app.
    - **Pandas** and **NumPy** for data preprocessing and manipulation

---

## Workflow

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py