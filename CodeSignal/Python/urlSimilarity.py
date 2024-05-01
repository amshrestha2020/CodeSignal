# You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in for their browsers which will check if the page they are trying to visit is similar to the one in the blacklist.

# For that, you've thought of the special algorithm that for two URLs url1 and url2 computes their similarity as following:

# Initially their similarity is 0
# Then, it is increased by the following rules:
# +5, if the same protocol is used in both URLs.
# +10, if url1 and url2 have the same address.
# +k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
# +1 if for each varNames common between them. Additional +1 if the respective values are equal too.
# URLs are given in the following format: protocol://address[(/path)*][?query] (where query = varName=value(&varName=value)*, parts given in [] are optional, and parts in ()* may be repeated several times). Each of the named elements (i.e. protocol, address, path, varName and value) are guaranteed to contain only alphanumeric characters and periods.

# Given the two URLs url1 and url2, compute their similarity using the algorithm described above.

# Example

# For

# url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
# and

# url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
# the output should be
# solution(url1, url2) = 19.

# Because these URLs have the same protocols, addresses, first path component (home) and two varNames, with one also having the same value in both of them.
# So the resulting similarity is thus 5 + 10 + 1 + 1 + 1 + 1 = 19.

from urllib.parse import urlparse, parse_qs

def solution(url1, url2):
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)

    similarity = 0

    # +5, if the same protocol is used in both URLs.
    if parsed_url1.scheme == parsed_url2.scheme:
        similarity += 5

    # +10, if url1 and url2 have the same address.
    if parsed_url1.netloc == parsed_url2.netloc:
        similarity += 10

    # +k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
    path1 = parsed_url1.path.split('/')[1:]  # Ignore the first empty string before the first '/'
    path2 = parsed_url2.path.split('/')[1:]  # Ignore the first empty string before the first '/'
    similarity += sum(1 for p1, p2 in zip(path1, path2) if p1 == p2)

    # +1 if for each varNames common between them. Additional +1 if the respective values are equal too.
    query1 = parse_qs(parsed_url1.query)
    query2 = parse_qs(parsed_url2.query)
    common_keys = set(query1.keys()) & set(query2.keys())
    similarity += len(common_keys)
    similarity += sum(1 for key in common_keys if query1[key] == query2[key])

    return similarity

