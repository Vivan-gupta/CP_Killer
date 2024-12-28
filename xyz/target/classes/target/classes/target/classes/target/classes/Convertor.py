import sys

from openai import OpenAI
import subprocess

from Output_Formatting import filter_out_code
from Sample_Code_Generation import sample_code
from Test_Code_Generation import test_code


client = OpenAI()

languages=['python', 'java', 'c++']
extensions={'java':'.java', 'python':'.py', 'c++':'.cpp'}

with open("Solution"+extensions[languages[0]], "r") as file:
    from_Code = file.read()
with open("Solution"+extensions[languages[1]], "r") as file:
    to_Code_Format = file.read()
with open("Question.txt", "r") as file:
    Question = file.read()
with open(languages[1] + "_Test_Format" + extensions[languages[1]], "r") as file:
    test_Format = file.read()

sample_code(languages[1], extensions[languages[1]], to_Code_Format)

with open("Solution"+extensions[languages[1]], "r") as file:
    to_Code_Format = file.read()

test_code(languages[1], extensions[languages[1]], Question, to_Code_Format, test_Format)

messages = [
    {
        "role": "system",
        "content": """Your an Expert Programmer of """+languages[0]+""" & """+languages[1]+""" .
                      You will convert the given """+languages[0]+""" code to """+languages[1]+""" code.
                      You DON'T TOUCH THE LOGIC IT WILL BE AS IT IS.
                      If the output code format is provided you will respond only in it.
                      No Markdown formatting.
                      Respond in Plain Text only."""
    },
    {
        "role": "user",
        "content": from_Code
    },
    {
        "role": "user",
        "content": to_Code_Format
    },
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
                                    "content": to_Code_Format
                                }
                            )
    output_Code, found_Code = filter_out_code(response2.choices[0].message.content)

    with open("Solution" + extensions[languages[1]], "w") as file:
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
            lines = run_result.stdout.strip().splitlines()
            execution_msg = None if len(lines) == 0 or not lines[0].strip() else lines[0].strip()
            execution_bool = lines[1].strip().lower() == 'true' if len(lines) > 1 else None
            RE_found = lines[2].strip().lower() == 'true' if len(lines) > 2 else None
            if not execution_bool and not RE_found:
                messages=messages[:3]
                messages.append({"role": "assistant", "content": output_Code})
                execution_msg = """I said DON'T TOUCH THE LOGIC IT WILL BE AS IT IS.
                Only change if it is not possible or needed."""

        except subprocess.CalledProcessError as e:
            execution_msg = e.stderr
            execution_bool = False

        messages.append({"role": "user", "content": execution_msg})

    with open("chat.txt", "w") as chat_file:
        for message in messages:
            chat_file.write(f"{message['role']}: {message['content']}\n\n\n")

    test_try+=1

    if execution_bool:
        print("Xtra_input = ", end="")
        Xtra_input = sys.stdin.read()
        if Xtra_input != "":
            messages.append({"role": "user", "content": Xtra_input})
            execution_bool = False