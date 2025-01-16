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
language=langauges[0]

extension, file_name = info(platform,language)
file_location = file_name+extension

test_location = file_name+"Test"+extension