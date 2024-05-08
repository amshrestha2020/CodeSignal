# Domain name forwarding lets GoDaddy domain owners automatically redirect their site visitors to a different site URL. Sometimes the visitors have to go through multiple redirects before ending up on the correct site.

# Using the DNS Manager, GoDaddy customers can view redirects in a simple visual format. One handy feature is the ability to group the domains by the final website they redirect to. Your task is to implement this feature.

# For the given redirects list, organize its domains into groups where for a specific group each domain eventually redirects visitors to the same website.

# Example

# For

# redirects = [["godaddy.net", "godaddy.com"], 
#              ["godaddy.org", "godaddycares.com"], 
#              ["godady.com", "godaddy.com"],
#              ["godaddy.ne", "godaddy.net"]]
# the output should be

# solution(redirects) = [["godaddy.com", "godaddy.ne", "godaddy.net", "godady.com"], 
#                        ["godaddy.org", "godaddycares.com"]]
# In the first group, "godaddy.ne" redirects to "godaddy.net", which in turn redirects to "godaddy.com". "godady.com" redirects visitors to "godaddy.com" as well.
# In the second group, "godaddy.org" redirects visitors to "godaddycares.com".

# Note, that domains in each group are sorted lexicographically and groups themselves are sorted lexicographically by the domain they redirect to. So in the example, the first group goes before the second because "godaddy.com" is lexicographically smaller than "godaddycares.com".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.array.string redirects

# Each of redirects[i] consists of two domains. The second element is the domain to which the first element redirects. Each domain is a string that may consist of lowercase English letters, hyphens ('-') and full stops ('.').
# It is guaranteed that domain redirects do not contain cycles, i.e. it is impossible to get back to the current site after any number of redirects. It is also guaranteed that each domain redirects to no more than one another domain, i.e. for each i ≠ j redirects[i][0] ≠ redirects[j][0].

# Guaranteed constraints:
# 1 ≤ redirects.length ≤ 15,
# redirects[i].length == 2,
# 1 ≤ redirects[i][j].length ≤ 25.

# [output] array.array.string

# Return the array of domain groups, such that each domain from redirects belongs to one of the group, and domains from one group redirect visitors to the same website. Arrange the domains in each group in lexicographical order, and sort the groups by the domains they redirect to (also lexicographically).


def solution(redirects):
    # Create a dictionary to store the final redirect for each domain
    final_redirects = {}
    for domain, redirect in redirects:
        # If the redirect is not in the dictionary, add it
        if redirect not in final_redirects:
            final_redirects[redirect] = redirect
        # Update the final redirect for the domain
        final_redirects[domain] = final_redirects[redirect]
        # Update the final redirect for all domains that point to the current redirect
        for key, value in final_redirects.items():
            if value == domain:
                final_redirects[key] = final_redirects[domain]
    
    # Create a dictionary to store the domains for each final redirect
    groups = {}
    for domain, final_redirect in final_redirects.items():
        # If the final redirect is not in the dictionary, add it
        if final_redirect not in groups:
            groups[final_redirect] = []
        # Add the domain to the group
        groups[final_redirect].append(domain)
    
    # Sort the domains in each group
    for group in groups.values():
        group.sort()
    
    # Sort the groups by the final redirect and return them
    return sorted(groups.values(), key=lambda group: final_redirects[group[0]])

# Test case
print(solution([["godaddy.net", "godaddy.com"], 
                ["godaddy.org", "godaddycares.com"], 
                ["godady.com", "godaddy.com"],
                ["godaddy.ne", "godaddy.net"]]))
# Output: [["godaddy.com", "godaddy.ne", "godaddy.net", "godady.com"], 
#          ["godaddy.org", "godaddycares.com"]]
