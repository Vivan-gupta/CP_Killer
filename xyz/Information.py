platforms = ['LeetCode', 'CodeForces', 'CodeChef', 'GeeksForGeeks', 'AtCoder']
languages=['python', 'java', 'c++']
extensions={'java': '.java', 'python': '.py', 'c++': '.cpp'}
file_location = {
                 'java':{
                            'LeetCode': 'Java/src/main/java/Solution',
                            'GeeksForGeeks': 'Java/src/main/java/Solution',
                            'CodeForces': 'Java/src/main/java/Main',
                            'CodeChef': 'Java/src/main/java/Main',
                            'AtCoder': 'Java/src/main/java/Main'
                        },
                 'python':{
                            'LeetCode': 'Python/Solution',
                            'GeeksForGeeks': 'Python/Solution',
                            'CodeForces': 'Python/Main',
                            'CodeChef': 'Python/Main',
                            'AtCoder': 'Python/Main'
                          },
                 'C++':{
                        'LeetCode': 'C++/Solution',
                        'GeeksForGeeks': 'C++/Solution',
                        'CodeForces': 'C++/Main',
                        'CodeChef': 'C++/Main',
                        'AtCoder': 'C++/Main'
                       },
                }

def info(platform, language):
    global platforms
    global languages
    global extensions
    global file_location
    return extensions[language],file_location[language][platform]
    