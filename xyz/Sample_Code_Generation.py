from openai import OpenAI
import subprocess

from Output_Formatting import filter_out_code
from Information import info

client = OpenAI()

execution_bool = False
test_try = 0

platforms = ['LeetCode', 'CodeForces', 'CodeChef', 'GeeksForGeeks', 'AtCoder']
languages=['python', 'java', 'c++']


platform = platforms[0]
language=languages[1]

extension, file_name = info(platform,language)
file_location = file_name+extension

with open(file_location, "r") as file:
    code_Format = file.read()

def sample_code(language, code_Format):

    global execution_bool
    global test_try

    messages = [
        {
            "role": "system",
            "content": """Your an Expert Programmer of """ + language + """.
                          You will generate a sample compilable format of given code_Format.
                          DON'T TRY TO SOLVE IT IN ANY SENSE.
                          You will Respond only with code in the given Format.
                          No markdown formatting only plain text."""
        },
        {
            "role": "user",
            "content": code_Format
        }
    ]

    while not execution_bool:

        response0 = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        sample_Code, found_Code = filter_out_code(response0.choices[0].message.content)

        with open(file_location, "w") as file:
            file.write(sample_Code)

        messages.append({"role": "assistant", "content": sample_Code})

        if not found_Code:
            messages.append({"role": "user", "content": """You will generate test for the given question in provided format only.
                                                           You will Respond only with code in the provided format only.
                                                           No Markdown formatting.
                                                           Respond in Plain Text only."""})
            execution_bool = False
        else:

            try:
                subprocess.run(["javac", file_location], check=True, capture_output=True, text=True)
                execution_bool = True
                
            except subprocess.CalledProcessError as e:
                execution_msg = e.stderr
                execution_bool = False
                messages.append({"role": "user", "content": execution_msg})

        with open("chat.txt", "w") as chat_file:
            for message in messages:
                chat_file.write(f"{message['role']}: {message['content']}\n")
        print(test_try)
        test_try += 1

if __name__ == '__main__':
    sample_code(language, code_Format)