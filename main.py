import datetime

# --- Prompt Versioning System ---
# This list simulates a simple prompt versioning system.
# In a real application, this might be stored in a database,
# a version control system (like Git for prompts), or a dedicated prompt management tool.
prompt_versions = [
    {
        "id": 1,
        "version_tag": "v1.0-gentle-summary",
        "description": "Initial prompt for customer service bot: gentle summary and general solutions.",
        "prompt_text": "Müşterinin sorununu nazikçe özetle ve çözüm önerileri sun.",
        "created_date": "2023-01-15"
    },
    {
        "id": 2,
        "version_tag": "v1.1-detailed-analysis-3solutions",
        "description": "Updated prompt: detailed analysis, key points, and exactly 3 solutions.",
        "prompt_text": "Müşterinin şikayetini detaylıca analiz et, ana noktaları çıkar ve 3 farklı çözüm önerisi sun.",
        "created_date": "2023-03-10"
    },
    {
        "id": 3,
        "version_tag": "v1.2-concise-single-solution",
        "description": "Refined prompt: concise summary and a single, most suitable solution.",
        "prompt_text": "Müşterinin sorununu kısa ve öz bir şekilde özetle, ardından en uygun tek bir çözüm önerisi sun.",
        "created_date": "2023-05-22"
    },
    {
        "id": 4,
        "version_tag": "v2.0-proactive-upsell",
        "description": "New major version: includes proactive upsell suggestion after resolving the issue.",
        "prompt_text": "Müşterinin sorununu çöz, ardından ilgili olabilecek bir ek ürün veya hizmet önerisi sun.",
        "created_date": "2023-07-01"
    }
]

def get_prompt_by_tag(tag: str) -> dict | None:
    """Retrieves a prompt version by its tag."""
    for prompt_data in prompt_versions:
        if prompt_data["version_tag"] == tag:
            return prompt_data
    return None

def simulate_llm_response(prompt_text: str, customer_issue: str) -> str:
    """
    Simulates an LLM generating a response based on the given prompt.
    In a real scenario, this would involve an API call to an LLM.
    """
    print(f"\n--- Simulating LLM with Prompt ---")
    print(f"Prompt Used: '{prompt_text}'")
    print(f"Customer Issue: '{customer_issue}'")
    print(f"Simulated LLM Output (based on prompt instruction):")

    # This is where the "versioning" impact is demonstrated through different simulated logic
    if "nazikçe özetle" in prompt_text and "çözüm önerileri sun" in prompt_text:
        return f"Merhaba, anladığım kadarıyla '{customer_issue}' konusunda bir sorun yaşıyorsunuz. Size yardımcı olabilecek bazı genel çözümler şunlar: [Çözüm A], [Çözüm B]."
    elif "detaylıca analiz et" in prompt_text and "3 farklı çözüm önerisi sun" in prompt_text:
        return f"Müşterinin '{customer_issue}' şikayeti detaylıca incelenmiştir. Ana noktalar: [Nokta 1], [Nokta 2]. Önerilen 3 çözüm: [Detaylı Çözüm 1], [Detaylı Çözüm 2], [Detaylı Çözüm 3]."
    elif "kısa ve öz bir şekilde özetle" in prompt_text and "en uygun tek bir çözüm önerisi sun" in prompt_text:
        return f"Sorununuz '{customer_issue}' olarak özetlenebilir. En uygun çözüm önerimiz: [Tek ve Net Çözüm]."
    elif "çöz, ardından ilgili olabilecek bir ek ürün veya hizmet önerisi sun" in prompt_text:
        return f"Sorununuz '{customer_issue}' çözülmüştür. Ayrıca, deneyiminizi geliştirecek [Ek Ürün/Hizmet Adı] ürünümüzü inceleyebilirsiniz."
    else:
        return f"LLM, '{prompt_text}' prompt'una göre genel bir yanıt üretti: [Genel Yanıt]."

# --- Main Demonstration ---
if __name__ == "__main__":
    customer_problem_example = "Hesabıma giriş yapamıyorum ve şifremi sıfırlayamıyorum."

    print("--- Prompt Versioning Demonstration ---")
    print("This example shows how different prompt versions can lead to varied LLM behaviors.")

    # Scenario 1: Using the initial prompt version
    print("\n--- Scenario 1: Using v1.0-gentle-summary ---")
    prompt_v1 = get_prompt_by_tag("v1.0-gentle-summary")
    if prompt_v1:
        # The prompt_text is the critical part that changes between versions
        response_v1 = simulate_llm_response(prompt_v1["prompt_text"], customer_problem_example)
        print(f"Response (v1.0): {response_v1}")
    else:
        print("Prompt v1.0 not found.")

    # Scenario 2: Using an updated prompt version for detailed analysis
    print("\n--- Scenario 2: Using v1.1-detailed-analysis-3solutions ---")
    prompt_v1_1 = get_prompt_by_tag("v1.1-detailed-analysis-3solutions")
    if prompt_v1_1:
        # Notice how a small change in prompt text changes the expected output
        response_v1_1 = simulate_llm_response(prompt_v1_1["prompt_text"], customer_problem_example)
        print(f"Response (v1.1): {response_v1_1}")
    else:
        print("Prompt v1.1 not found.")

    # Scenario 3: Using a refined prompt for a concise, single solution
    print("\n--- Scenario 3: Using v1.2-concise-single-solution ---")
    prompt_v1_2 = get_prompt_by_tag("v1.2-concise-single-solution")
    if prompt_v1_2:
        # This demonstrates how prompt versioning helps track and apply specific instructions
        response_v1_2 = simulate_llm_response(prompt_v1_2["prompt_text"], customer_problem_example)
        print(f"Response (v1.2): {response_v1_2}")
    else:
        print("Prompt v1.2 not found.")

    # Scenario 4: Using a new major version with a different objective (upselling)
    print("\n--- Scenario 4: Using v2.0-proactive-upsell ---")
    prompt_v2_0 = get_prompt_by_tag("v2.0-proactive-upsell")
    if prompt_v2_0:
        # Demonstrates evolving prompt strategies over time
        response_v2_0 = simulate_llm_response(prompt_v2_0["prompt_text"], customer_problem_example)
        print(f"Response (v2.0): {response_v2_0}")
    else:
        print("Prompt v2.0 not found.")

    print("\n--- End of Demonstration ---")
    print("This simple setup highlights the importance of managing prompt changes for predictable AI behavior.")
