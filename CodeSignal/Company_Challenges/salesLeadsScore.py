# You are provided the following information about sales leads:

# An array of names, where names[i] is the name of the ith sales lead.
# An array of times in the system, where time[i] is the time spend for work during the year (in days) for ith sales lead.
# An array of net values, where netValue[i] is the net value of the ith sales lead.
# An array of vacation statuses, where isOnVacation[i] shows if the ith sales lead is on vacation or not.
# Your task is to return the sales leads in decreasing order of their score. Only sales leads not on vacation should be returned. The score for the ith lead is calculated as netValue[i] * time[i] / 365. In case of equal scores, the lead with greater time should go first. In case of equal scores and times, the lead with the lexicographically smaller name should go first.

# It's guaranteed that at least one isOnVacation[i] is false.

# Example

# For names = ["lead1", "lead2", "lead3", "lead4", "lead5"], time = [250, 300, 250, 260, 310], netValue = [1000, 800, 1100, 1200, 1000], and isOnVacation = [true, false, true, false, false], the output should be solution(names, time, netValue, isOnVacation) = ["lead4", "lead5", "lead2"].

# Lead with i = 0 is on vacation, so they won't be included.
# Lead with i = 1 has score 800 * 300 / 365 = 657.53.
# Lead with i = 2 is on vacation, so they won't be included.
# Lead with i = 3 has score 1200 * 260 / 365 = 854.79.
# Lead with i = 4 has score 1000 * 310 / 365 = 849.32.
# The results should include the leads at indices 3, 4, and 1, so the answer is ["lead4", "lead5", "lead2"].


def solution(names, time, netValue, isOnVacation):
    # Create a list of tuples containing name, score, time spent, and vacation status
    sales_leads = [(names[i], netValue[i] * time[i] / 365, time[i], isOnVacation[i]) for i in range(len(names))]

    # Filter out sales leads who are not on vacation
    sales_leads = [lead for lead in sales_leads if not lead[3]]

    # Sort sales leads based on score, time spent, and lexicographically smaller name
    sales_leads.sort(key=lambda x: (-x[1], -x[2], x[0]))

    # Extract names of sorted sales leads
    sorted_names = [lead[0] for lead in sales_leads]

    return sorted_names

# Test case
names = ["lead1", "lead2", "lead3", "lead4", "lead5"]
time = [250, 300, 250, 260, 310]
netValue = [1000, 800, 1100, 1200, 1000]
isOnVacation = [True, False, True, False, False]
print(solution(names, time, netValue, isOnVacation))  # Output: ["lead4", "lead5", "lead2"]
