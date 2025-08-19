import os
import base64 #for encoding our img so it doesnt lose any value

GROQ_API_KEY =os.environ.get("GROQ_API_KEY")

# image_path="acne.jpg"
def image_encoded(image_path):
    image_file=open(image_path,"rb") #read the binary in this image
    return base64.b64encode(image_file.read()).decode("utf-8")

from groq import Groq
query="Is there something wrong with my face ?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def image_analysis_using_query(query, model, image_encoded):
    client=Groq()
    messages= [
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text": query
                },
                {
                    "type":"image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_encoded}"
                    }
                }
            ]
        }
    ]

    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content