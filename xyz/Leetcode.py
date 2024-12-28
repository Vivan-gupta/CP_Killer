from openai import OpenAI
import subprocess

from Output_Formatting import filter_out_code
from Sample_Code_Generation import sample_code
from Test_Code_Generation import test_code

from pyexpat.errors import messages

client = OpenAI()

language = "Java"
extension = ".java"

with open("Question.txt", "r") as file:
    Question = file.read()
with open(language + "_Format" + extension, "r") as file:
    code_Format = file.read()
with open(language + "_Test_Format" + extension, "r") as file:
    test_Format = file.read()

#Sample Code Generation
sample_code(language, extension, code_Format)

with open("Solution"+extension, "r") as file:
    sample_Code = file.read()

test_code(language, extension, Question, sample_Code, test_Format)

method = "use java"

messages = [
    {
        "role": "system",
        "content": """Your an Expert """ + language + """ Programmer.
                      You will solve the given question in provided format only.
                      You will Respond only with code in the provided format only.
                      You will respond in code.
                      No Markdown formatting.
                      Respond in Plain Text only."""
    },
    {
        "role": "user",
        "content": Question
    },
    {
        "role": "user",
        "content": method
    },
    {
        "role": "user",
        "content": code_Format
    }
]

execution_bool = False
test_try = 0

while not execution_bool:

    print(test_try)

    response2 = client.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=messages,
                                prediction={
                                    "type": "content",
                                    "content": sample_Code
                                }
                            )
    output_Code, found_Code = filter_out_code(response2.choices[0].message.content)

    with open("Solution" + extension, "w") as file:
        file.write(output_Code)

    messages.append({"role": "assistant", "content": output_Code})

    if not found_Code:
        messages.append({"role": "user", "content": """You will solve the given question in provided format only.
                                                           You will Respond only with code in the provided format only.
                                                           No Markdown formatting.
                                                           Respond in PLain Text only."""})
        execution_bool = False
    else:
        try:
            subprocess.run(["javac", "Solution.java"], check=True, capture_output=True, text=True)
            run_result = subprocess.run(["java", "SolutionTest"], capture_output=True, text=True, check=True)
            execution_msg, _, execution_bool = run_result.stdout.rpartition(' ')
            execution_bool = execution_bool.strip().lower() == 'true'
        except subprocess.CalledProcessError as e:
            execution_msg = e.stderr
            execution_bool = False

        messages.append({"role": "user", "content": execution_msg})

    with open("chat.txt", "w") as chat_file:
        for message in messages:
            chat_file.write(f"ChatBot: {message['content']}\n\n\n")

    test_try+=1