# You are given an array of strings names representing filenames. The array is sorted in order of file creation, such that names[i] represents the name of a file created before names[i+1] and after names[i-1] (assume 0-based indexing). Because all files must have unique names, files created later with the same name as a file created earlier should have an additional (k) suffix in their names, where k is the smallest positive integer (starting from 1) that does not appear in previous file names.

# Your task is to iterate through all elements of names (from left to right) and update all filenames based on the above. Return an array of proper filenames.

# Example

# For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be solution(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

# Since names[0] = "doc" and names[1] = "doc", update names[1] = "doc(1)"
# Since names[1] = "doc(1)" and names[3] = "doc(1)", update names[3] = "doc(1)(1)"
# Since names[0] = "doc", names[1] = "doc(1)", and names[4] = "doc", update names[4] = "doc(2)"


def solution(names):
    seen_names = {}
    result = []

    for name in names:
        if name not in seen_names:
            seen_names[name] = 1
            result.append(name)
        else:
            new_name = f"{name}({seen_names[name]})"
            while new_name in seen_names:
                seen_names[name] += 1
                new_name = f"{name}({seen_names[name]})"
            
            seen_names[new_name] = 1
            result.append(new_name)

    return result

