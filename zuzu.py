def zuzu():
    print("Zuzu: Hello! I'm Zuzu. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Zuzu: Goodbye! 👋")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Zuzu: Hello there!")
        elif 'how are you' in user_input:
            print("Zuzu: I'm just code, but I'm running smoothly!")
        else:
            print("Zuzu: I'm still learning. Can you try something else?")

    zuzu()
