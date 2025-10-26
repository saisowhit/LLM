

import gradio as gr
from mistalai.models.chat_completion import ChatMessage
from mistalai.client import MistalClient

def get_chat_response(user_input):
    message=[ChatMessage(role='user',content=user_input)]
    content=chat_response.choices[0].message.content
    return content

##Gradio Interface
iface=gr.Interface(fn=get_chat_response,inputs="text",outputs="text",title="Mistal AI Chatbot",description="Ask the bot")


iface.launch()