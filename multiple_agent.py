import time

def ai_provider_1(prompt):
    time.sleep(1)
    return "Response from GPT-like model"

def ai_provider_2(prompt):
    time.sleep(2)
    return "Response from Gemini-like model"

prompt = input("Enter your prompt: ")

start_1 = time.time()
response_1 = ai_provider_1(prompt)
latency_1 = time.time() - start_1

start_2 = time.time()
response_2 = ai_provider_2(prompt)
latency_2 = time.time() - start_2

print("\n--- AI Comparison ---")
print("Provider 1 Response:", response_1)
print("Latency:", round(latency_1, 2), "seconds\n")

print("Provider 2 Response:", response_2)
print("Latency:", round(latency_2, 2), "seconds")
