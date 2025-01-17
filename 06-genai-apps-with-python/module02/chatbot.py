from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Class to interact with the model
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Class to optimize input and efficiently pass to model as tokens
tokenizer = AutoTokenizer.from_pretrained(model_name)

# [input_1, output_1, input_2, output_2,...]
conversation_history = []

# # transformers expects to receive the conversation history as a string,
# # with each element separated by the newline character '\n'
# history_string = "\n".join(conversation_history)
#
# input_text = "Hello, how are you doing?"
#
# inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
# print(inputs)
#
# # Print out the vocabulary map of the model
# #print(tokenizer.vocab)
#
# outputs = model.generate(**inputs)
# print(outputs)
#
# response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
# print(response)
#
# conversation_history.append(input_text)
# conversation_history.append(response)
# print(conversation_history)

while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)
    # Get the input data from the user
    input_text = input("> ")
    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    # Generate the response from the model
    outputs = model.generate(**inputs)
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    print(response)
    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
