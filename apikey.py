# OpenAl Challenge(Problem Statement)

# In the Python file, write a program to perform a POST request to the OpenAl API endpoint https://api.openai.com/v1/chat/completions to generate a text completion based on a given prompt. The

# prompt will be hardcoded into your program.

# The prompt will be: "Define 'photosynthesis".

# Set max_tokens to 150, and temperature to 0.1 in your request. These parameters will control the length and creativity of the generated text, respectively.

# Finally, console log the generated text as a string. Do not modify the line with API_KEY_DO_NOT_MODIFY.

# Example Input:

# Who is the first President of the United States?

# Example Output:

# {

# id: "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",

# object: "text_completion",

# created: 1589478378,

# model: "gpt-40",

# choices: [

# {

# text: "\n\nThe first President of the

# United States was George Washington.",

# index:

# 6,

# logprobs: null,

# finish_reason: "length"

# }
# ],

# usage: {

# prompt_tokens: 10,

# completion_tokens: 11,

# total_tokens: 21

# }

# }

# Provide this problem solution based on above statement and based on below provideed code and also explain what will do

# import requests

# import json

# OPENAI_API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'

# ΟΡΕΝΑΙ ΑΡΙ_ΚΕY - API_KEY_DO_NOT_MODIFY

# def fetch_chat_completion(messages):

# headers = {}

# data = {}

# response requests.post(OPENAI_API_ENDPOINT, headers-headers, data-json.dumps(data))

# 11 response.status_code-200:

# return response

# else:

# raise Exception("Error fetching completion: + response.text)

# def main():

# messages

# try:

# completion fetch_chat_completion(messages)

# print(f'Generated text: (completion}')

# except Exception as e:

# print(str(e))

# if name main':

# main()

import requests
import json

OPENAI_API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'

# DO NOT MODIFY THIS VARIABLE
API_KEY =  ''
def fetch_chat_completion(messages):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 150,
        "temperature": 0.1
    }

    response = requests.post(OPENAI_API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching completion: " + response.text)

def main():
    # Hardcoded prompt as system/user messages (Chat format)
    messages = [
        {"role": "user", "content": "Define 'photosynthesis'"}
    ]

    try:
        completion = fetch_chat_completion(messages)
        # Extract generated message text
        generated_text = completion["choices"][0]["message"]["content"]
        print(f'Generated text: {generated_text}')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
