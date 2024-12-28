import subprocess

try:
    subprocess.run(["javac", r"src\main\java\Solution.java", r"src\main\java\SolutionTest.java"], check=True,
                   capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    execution_msg = e.stderr
    print(execution_msg)