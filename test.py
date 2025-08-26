import openai
openai.api_key = "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"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input ("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)