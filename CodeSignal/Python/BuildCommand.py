# While migrating to a new operation system, you faced an unexpected problem: now you need to create a new build command for your favorite text editor plugin. The build command is stored as a JSON file that you should now update. In order to make the transition simpler, you decided to write a program that will create a template of the build command by replacing everything but dictionaries in given jsonFile with their default values: numbers with 0, strings with "" and lists with [].

# It is guaranteed that there are only aforementioned types in the given JSON file.

# Example

# For

# jsonFile =
# """
# {
#     "version": "0.1.0",
#     "command": "c:python",
#     "args": ["app.py"],
#     "problemMatcher": {
#         "fileLocation": ["relative", "${workspaceRoot}"],
#         "pattern": {
#             "regexp": "^(.*)+s$",
#             "message": 1
#         }
#     }
# }
# """
# the output should be

# solution(jsonFile) =
# """
# {
#     "version": "",
#     "command": "",
#     "args": [],
#     "problemMatcher": {
#         "fileLocation": [],
#         "pattern": {
#         "regexp": "",
#         "message": 0
#         }
#     }
# }
# """


import json

def solution(jsonFile):
    data = json.loads(jsonFile)

    def process_dict(d):
        for k in d:
            if isinstance(d[k], dict):
                process_dict(d[k])
            elif isinstance(d[k], list):
                d[k] = []
            elif isinstance(d[k], str):
                d[k] = ""
            else:
                d[k] = 0

    process_dict(data)
    return json.dumps(data)
