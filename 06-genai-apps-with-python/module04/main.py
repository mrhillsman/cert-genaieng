import os
import gradio as gr
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import VLLMOpenAI
from transformers import pipeline

model="ibm-granite/granite-3.1-2b-instruct"

openai_api_key = 'EMPTY'
openai_api_base = 'http://127.0.0.1:8000/v1'
llm = VLLMOpenAI(model_name=model, openai_api_base=openai_api_base, openai_api_key=openai_api_key)

temp = """
<s><<SYS>>
List the key points with details from the context: 
[INST] The context : {context} [/INST] 
<</SYS>>
"""

# here is the simplified version of the prompt template
# temp = """#

# List the key points with details from the context:
# The context : {context}
# """
#pt = PromptTemplate(input_variables=["context"],template=temp)
prompt = ChatPromptTemplate(template_format='jinja2', messages=messages)

chain = prompt | llm

resp = llm.invoke({"input": "What is the capital of Texas?"})
print(resp)

# def transcript_audio(audio_file):
# # Initialize the speech-to-text pipeline from Hugging Face Transformers
# # This uses the "openai/whisper-tiny.en" model for automatic speech recognition (ASR)
# # The `chunk_length_s` parameter specifies the chunk length in seconds for processing
#     pipe = pipeline(
#       task="automatic-speech-recognition",
#       model="openai/whisper-tiny.en",
#       chunk_length_s=30,
#     )
#     # Perform speech recognition on the audio file
#     # The `batch_size=8` parameter indicates how many chunks are processed at a time
#     # The result is stored in `prediction` with the key "text" containing the transcribed text
#     output = pipe(audio_file, batch_size=8)
#     print(output)
#     prediction = output["text"]
#     return prediction
#
# # Set up Gradio interface
# audio_input = gr.Audio(sources=["upload"], type="filepath")  # Audio input
# output_text = gr.Textbox()  # Text output
# # Create the Gradio interface with the function, inputs, and outputs
# iface = gr.Interface(fn=transcript_audio,
#                      inputs=audio_input, outputs=output_text,
#                      title="Audio Transcription App",
#                      description="Upload the audio file")
# # Launch the Gradio app
# iface.launch(server_name="0.0.0.0", server_port=7860)