from openai import OpenAI
import subprocess

from Output_Formatting import filter_out_code
from Sample_Code_Generation import sample_code
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

test_location = file_name+"Test"+extension

# print(test_location)

with open("Question.txt", "r") as file:
    Question = file.read()
with open(file_location, "r") as file:
    code_Format = file.read()
with open(language + "_Test_Format", "r") as file:
    test_Format = file.read()

#Sample Code Generation
sample_code(language, code_Format)
with open(file_location, "r") as file:
    sample_Code = file.read()

def test_code(language, Question, sample_Code, test_Format):

    global execution_bool
    global test_try

    messages = [
        {
            "role": "system",
            "content": """Your an Testing Expert of """ + language + """.
                          You will generate tests for a given program in the given format only from the provided test cases in the end.
                          You will also generate that sample testcase function in provided format using constrains given in test cases in end.
                          You will Respond only with code in the given Format.
                          No markdown formatting only plain text."""
        },
        {
            "role": "user",
            "content": Question
        },
        {
            "role": "user",
            "content": sample_Code
        },
        {
            "role": "user",
            "content": test_Format
        }
    ]

    while not execution_bool:

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            prediction={
                "type": "content",
                "content": test_Format
            },
        )

        Testing_Code, found_Code = filter_out_code(response.choices[0].message.content)

        with open(test_location, "w") as file:
            file.write(Testing_Code)

        messages.append({"role": "assistant", "content": Testing_Code})

        if not found_Code:
            messages.append({"role": "user", "content": """You will generate test for the given question in provided format only.
                                                           You will Respond only with code in the provided format only.
                                                           No Markdown formatting.
                                                           Respond in Plain Text only."""})
            execution_bool = False

        else:
            try:
                subprocess.run(["javac", file_location, test_location], check=True, capture_output=True, text=True)
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
    test_code(language, Question, sample_Code, test_Format)
