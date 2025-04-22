
# LLMPatronous 🧙🛡️

**Your AI-Powered Security Guardian for Android Applications**

LLMPatronous is an innovative framework designed for the static analysis of vulnerabilities within Android application codebases. It leverages the power of multiple Large Language Models (LLMs) through a Mixture of Agents (MoA) architecture and Retrieval Augmented Generation (RAG) to provide comprehensive, accurate, and efficient security assessments.

https://github.com/user-attachments/assets/003329dc-dbb2-46d8-8fc3-7ec827abc558

## The Problem

The rapid growth of the mobile app market, dominated by Android, highlights a critical need for robust application security. Current vulnerability detection methods often fall short:
*   **Static Analysis Tools:** While useful, they often generate a significant number of false positives (sometimes exceeding 40%), wasting valuable developer time.
*   **Manual Code Audits:** Thorough but expensive and time-consuming, failing to keep pace with modern rapid release cycles.
This gap leaves millions of users vulnerable. There's a clear demand for more accurate, automated, and scalable security solutions.

## Our Solution: LLMPatronous

LLMPatronous addresses these challenges by utilizing cutting-edge AI techniques:

*   **Leveraging LLMs:** Harnesses the contextual understanding and reasoning capabilities of various LLMs to analyze code for security flaws.
*   **Mixture of Agents (MoA):** Employs a multi-layered architecture where different specialized LLMs (agents) collaborate to analyze specific vulnerability types, enhancing accuracy and reducing false positives compared to single-model solutions.
*   **Retrieval Augmented Generation (RAG):** Integrates with a knowledge base (Pinecone Vector Database) to provide LLMs with up-to-date, context-specific information about known vulnerabilities and secure coding practices, overcoming LLM knowledge cutoffs and improving analysis quality.
*   **Large Codebase Processing:** Integrates with the Google AI Studio API, enabling the analysis of extensive codebases (even thousands of lines) in a single run, which many traditional tools struggle with.
*   **Comprehensive Reporting:** Utilizes powerful models like OpenAI's o1-preview to generate detailed, professional Vulnerability Assessment Reports based on the findings of the analysis layers.

## ✨ Key Features & Highlights

*   **AI-Powered Static Analysis:** Deep code analysis for Android applications using multiple LLMs.
*   **Mixture of Agents (MoA) Architecture:** Developed by Together AI, this approach combines the strengths of diverse LLMs (GPT-4o-mini, Claude-3-haiku, Qwen-2-72B-Instruct, Meta-Llama/Llama-3.1-70B-Instruct-Turbo, Meta-Llama/Llama-3.1-405B-Instruct-Turbo, Databricks/DBRX-Instruct, Gemini-1.5 Pro) for refined detection accuracy.
*   **Retrieval Augmented Generation (RAG):** Ensures real-time, comprehensive insights using Pinecone vector database.
*   **High Accuracy:** Achieved **81.9% accuracy** on predefined vulnerability lists during testing, significantly reducing false positives.
*   **Scalability:** Handles large codebases efficiently via Google AI Studio API integration.
*   **Professional Reporting:** Generates detailed Vulnerability Assessment Reports using advanced models like OpenAI o1-preview.
*   **Reduced False Positives:** The MoA approach, using diverse LLMs tailored to specific security aspects, minimizes false positives common in single-LLM or traditional static analysis.

## 💻 Technology Stack

*   **Core Language:** Python
*   **LLMs:**
    *   Google Gemini 1.5 Pro (Initial Check/Code Processing via AI Studio API)
    *   GPT-4o-mini, Claude-3-haiku (MoA Layer 1)
    *   Qwen-2-72B-Instruct, Meta-Llama/Llama-3.1-70B-Instruct-Turbo, Meta-Llama/Llama-3.1-405B-Instruct-Turbo, Databricks/DBRX-Instruct (MoA Layer 2 via Together AI)
    *   OpenAI o1-preview (Final Report Generation)
*   **AI Frameworks/Concepts:** Mixture of Agents (MoA), Retrieval Augmented Generation (RAG)
*   **Vector Database:** Pinecone
*   **APIs:** Google AI Studio API, OpenAI API, Together AI API, Pinecone API
*   **Libraries:** `google-generativeai`, `openai`, `together`, `pinecone-client`, `python-dotenv`, etc. (Refer to `requirements.txt`)

## ⚙️ Prerequisites

*   Python 3.x installed
*   `pip` (Python package installer)
*   Git (for cloning)
*   **API Keys:**
    *   Google AI Studio API Key (for Gemini models & codebase processing)
    *   OpenAI API Key (for the o1-preview report generation model)
    *   Together AI API Key (for the MoA layer models)
    *   Pinecone API Key and Environment details (for RAG)

## 🔧 Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Rajesh9998/LLMPatronus
    cd LLMPatronos
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    *   Create a file named `.env` in the root directory of the project.
    *   Add your API keys to the `.env` file:
        ```env
        GOOGLE_API_KEY="YOUR_GOOGLE_AI_STUDIO_API_KEY"
        OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
        TOGETHER_API_KEY="YOUR_TOGETHER_AI_API_KEY"
        PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
        PINECONE_ENVIRONMENT="YOUR_PINECONE_ENVIRONMENT"
        PINECONE_INDEX_NAME="YOUR_PINECONE_INDEX_NAME" # e.g., rag
        ```
    *   Replace the placeholder values with your actual credentials.

## ▶️ Running LLMPatronous

1.  **Activate Virtual Environment (if used):**
    ```bash
    source venv/bin/activate # Or `venv\Scripts\activate` on Windows
    ```

2.  **Run the Main Application:**
    ```bash
    python app.py
    ```

3.  **Provide Input:** The application will prompt you to:
    *   `Enter the folder path to crawl:` Provide the full path to the directory containing the Android application source code you want to analyze (e.g., `C:/Users/panda/Downloads/Vuldroid-master`).

4.  **Analysis Process:** LLMPatronous will then:
    *   Initialize and set up Pinecone.
    *   Crawl the specified folder, identifying relevant code files (`.java`, `.xml`, `.gradle`).
    *   Combine the content of these files into a temporary file.
    *   Begin detecting vulnerabilities using the multi-layered MoA and RAG approach.
    *   Log the progress and detected vulnerabilities to the console.
    *   Generate a final, professional `Final_Report.md` in the project directory upon completion.

5.  **View Results:** Monitor the console for real-time progress. Once finished, open `Final_Report.md` to view the comprehensive vulnerability assessment.

## ✨ Key Learnings from Development

*   The **Mixture of Agents (MoA)** approach is pivotal for leveraging the diverse strengths of multiple AI models to tackle complex cybersecurity challenges effectively.
*   **Retrieval Augmented Generation (RAG)** significantly enhances the accuracy and timeliness of vulnerability analysis by providing models with relevant, up-to-date context.
*   Strong **leadership and collaboration** are essential for navigating the complexities of integrating multiple advanced AI systems and achieving ambitious project goals.

## 🚀 Future Directions

While LLMPatronous demonstrates significant potential, future development could include:
*   Expanding the range of supported programming languages and platforms.
*   Integrating more sophisticated static and dynamic analysis techniques alongside LLMs.
*   Developing automated remediation suggestion capabilities.
*   Improving the granularity and customization of the MoA agent interactions.
*   Enhancing the user interface for easier interaction and result visualization.

## 📄 License


This project is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

![CC BY 4.0 License Badge](https://i.creativecommons.org/l/by/4.0/88x31.png)

You are free to:
*   **Share** — copy and redistribute the material in any medium or format for any purpose, even commercially.
*   **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
*   **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

For the full license text, see: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

