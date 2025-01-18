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
language = languages[1]

extension, file_name = info(platform,language)
file_location = file_name+extension

test_location = file_name+"Test"+extension

import subprocess

def executioner(language, file_name, extension, file_location, run_code=True):
    execution_bool = False
    messages = []

    try:
        if language == "java":
            compile_process = subprocess.run(["javac", file_location], check=True, capture_output=True, text=True)
            execution_bool = True
            messages.append({"role": "system", "content": "Compilation successful"})
            if run_code:
                run_process = subprocess.run(["java", file_name], check=True,capture_output=True, text=True)
                messages.append({"role": "system", "content": run_process.stdout})

        elif language == "c++":
            executable = file_name+".exe"\
                if run_code else "a.exe"
            compile_process = subprocess.run(["g++", "-o", executable, file_location], check=True, capture_output=True, text=True)
            execution_bool = True
            messages.append({"role": "system", "content": "Compilation successful"})
            if run_code:
                run_process = subprocess.run([f"./{executable}"], check=True, capture_output=True, text=True)
                messages.append({"role": "system", "content": run_process.stdout})

        elif language == "python":
            if run_code:
                run_process = subprocess.run(["python", file_location], check=True, capture_output=True, text=True)
                execution_bool = True
                messages.append({"role": "system", "content": run_process.stdout})

        else:
            messages.append({"role": "system", "content": "Unsupported language"})
            execution_bool = False

    except subprocess.CalledProcessError as e:
        execution_msg = e.stderr
        execution_bool = False
        messages.append({"role": "user", "content": execution_msg})

    return messages, execution_bool

if __name__ == '__main__':
    executioner(language, file_name, extension, file_location, True)
