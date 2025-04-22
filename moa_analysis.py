import concurrent.futures
from together import Together
from duckduckgo_search import DDGS
import google.generativeai as genai

def moa_analysis(vulnerability: str, gemini_knowledge: str, code_to_scan: str, together_api_key: str, gemini_api_key: str) -> str:
    client = Together(api_key=together_api_key)

    layer1_models = ["gpt-4o-mini", "claude-3-haiku"]
    layer2_models = [
        "Qwen/Qwen2-72B-Instruct",
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        "databricks/dbrx-instruct"
    ]

    def run_ddgs_chat(model: str, prompt: str) -> str:
        with DDGS() as ddgs:
            response = ddgs.chat(prompt, model=model)
        return f"{model}: {response}"

    def run_together_llm(model: str, prompt: str) -> str:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=1200,
        )
        return f"{model}: {response.choices[0].message.content}"

    layer1_prompt = f"""
    As a security expert specializing in Android app vulnerabilities, analyze the following code for the {vulnerability} vulnerability:

    {code_to_scan}

    Use this knowledge about the vulnerability:
    {gemini_knowledge}

    Your task is to:
    1. Determine if the code contains the {vulnerability} vulnerability
    2. If present, explain where and how the vulnerability manifests
    3. Provide recommendations for fixing the vulnerability
    4. If the vulnerability is not present, explain why the code is secure against this specific threat

    Focus only on the {vulnerability} vulnerability in your analysis.
    """

    # Layer 1: DDGS chat models
    layer1_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(layer1_models)) as executor:
        future_to_model = {executor.submit(run_ddgs_chat, model, layer1_prompt): model for model in layer1_models}
        for future in concurrent.futures.as_completed(future_to_model):
            model = future_to_model[future]
            try:
                result = future.result()
                layer1_results.append(result)
            except Exception as exc:
                print(f'{model} generated an exception: {exc}')

    layer1_results_str = "\n\n".join(layer1_results)

    # Layer 2: Together AI LLMs
    layer2_prompt = f"""
    You are an expert in Android security vulnerabilities. Your task is to analyze and improve upon the following vulnerability assessments.
    Critically evaluate the information, recognizing potential biases or inaccuracies.
    Provide a refined, accurate, and comprehensive analysis of the vulnerability in question.

    Code needed to be scanned is:
    {code_to_scan}

    Use this knowledge about the vulnerability:
    {gemini_knowledge}

    Previous assessments:
    {layer1_results_str}

    Improve upon these assessments, focusing on accuracy, completeness, and actionable insights. You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.
    """

    layer2_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(layer2_models)) as executor:
        future_to_model = {executor.submit(run_together_llm, model, layer2_prompt): model for model in layer2_models}
        for future in concurrent.futures.as_completed(future_to_model):
            model = future_to_model[future]
            try:
                result = future.result()
                layer2_results.append(result)
            except Exception as exc:
                print(f'{model} generated an exception: {exc}')

    layer2_results_str = "\n\n".join(layer2_results)

    # Layer 3: Final aggregation with Gemini 1.5 Flash
    aggregator_prompt = f"""
    As a senior Android security expert, your task is to synthesize the following vulnerability assessments into a single, authoritative analysis.
    Critically evaluate all information, reconcile any contradictions, and provide a comprehensive, accurate, and actionable final report.

    Vulnerability: {vulnerability}

    Code analyzed:
    {code_to_scan}

    Assessments to synthesize:
    {layer2_results_str}

    Provide a final, authoritative analysis that covers:
    1. Presence or absence of the vulnerability
    2. Detailed explanation of how the vulnerability manifests (if present)
    3. Comprehensive recommendations for fixing or mitigating the vulnerability
    4. If not present, a thorough explanation of why the code is secure against this threat
    """

    # Configure Gemini
    genai.configure(api_key=gemini_api_key)

    # Set up Gemini model
    generation_config = {
        "temperature": 0.4,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2000,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    model = genai.GenerativeModel('gemini-1.5-flash-exp-0827', generation_config=generation_config, safety_settings=safety_settings)

    # Generate final response
    response = model.generate_content(aggregator_prompt)
    return response.text

    