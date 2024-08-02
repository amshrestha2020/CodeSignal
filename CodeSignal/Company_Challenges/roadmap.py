You have a roadmap, which is the list of tasks that your team needs to complete. Each task in this list has a title, a start date, an end date, and a list of the people who will be working on it. You are given some queries, each of which contains a specific person's name and a date. For each query that is made, you need to return the list of tasks on which that person will be working on the date specified in the query, sorted by the tasks' end dates. If their end dates are equal, then sort by the tasks' titles.

Example

For

tasks =
[["A", "2017-02-01", "2017-03-01", "Sam", "Evan", "Troy"],
 ["B", "2017-01-16", "2017-02-15", "Troy"],
 ["C", "2017-02-13", "2017-03-13", "Sam", "Evan"]]
and

queries =
[["Evan", "2017-03-10"],
 ["Troy", "2017-02-04"]]
the output should be
solution(tasks, queries) = [["C"], ["B", "A"]].
On "2017-03-10" Evan only has task "C".
Troy will be working on two tasks on "2017-02-04", "A" and "B". We sort these tasks by their end dates. "A" has an end date of "2017-03-01" and "B" has an end date "2017-02-15". Since the end date for "B" is sooner than the end date for "A", we should return them as ["B", "A"].



from datetime import datetime

def solution(tasks, queries):
    # Helper function to check if a date is within the range
    def is_within_date_range(start, end, query_date):
        return start <= query_date <= end
    
    # Convert date strings to datetime objects for comparison
    tasks_with_dates = [
        [task[0], datetime.strptime(task[1], '%Y-%m-%d'), datetime.strptime(task[2], '%Y-%m-%d')] + task[3:]
        for task in tasks
    ]
    
    # Prepare the result list
    result = []
    
    # Process each query
    for person, query_date_str in queries:
        query_date = datetime.strptime(query_date_str, '%Y-%m-%d')
        person_tasks = []
        
        for task in tasks_with_dates:
            task_title, task_start_date, task_end_date, *workers = task
            if person in workers and is_within_date_range(task_start_date, task_end_date, query_date):
                person_tasks.append((task_title, task_end_date))
        
        # Sort by end date, then by title
        person_tasks.sort(key=lambda x: (x[1], x[0]))
        
        # Extract only the titles for the final result
        sorted_titles = [title for title, _ in person_tasks]
        result.append(sorted_titles)
    
    return result

# Example usage:
tasks = [
    ["A", "2017-02-01", "2017-03-01", "Sam", "Evan", "Troy"],
    ["B", "2017-01-16", "2017-02-15", "Troy"],
    ["C", "2017-02-13", "2017-03-13", "Sam", "Evan"]
]
queries = [
    ["Evan", "2017-03-10"],
    ["Troy", "2017-02-04"]
]
print(solution(tasks, queries))  # Output: [["C"], ["B", "A"]]
