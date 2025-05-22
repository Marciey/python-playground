import heapq

# Define the Task class
class Task:
    def __init__(self, name, duration, dependencies):
        self.name = name
        self.duration = duration
        self.dependencies = dependencies

# Heuristic function: estimate the remaining tasks' total duration
def heuristic(remaining_tasks):
    return sum(task.duration for task in remaining_tasks)

# A* Search for task scheduling
def a_star_scheduling(tasks):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, 0, [], tasks))  # (priority, cost, current_schedule, remaining_tasks)

    while open_set:
        priority, cost, current_schedule, remaining_tasks = heapq.heappop(open_set)

        # Check if all tasks are scheduled
        if not remaining_tasks:
            return current_schedule, cost

        for task in remaining_tasks:
            # Check dependencies are satisfied
            if all(dep in [t.name for t in current_schedule] for dep in task.dependencies):
                new_schedule = current_schedule + [task]
                new_remaining = [t for t in remaining_tasks if t != task]
                new_cost = cost + task.duration
                new_priority = new_cost + heuristic(new_remaining)

                # Use tuple representation of the schedule for closed_set
                schedule_tuple = tuple(t.name for t in new_schedule)

                if schedule_tuple not in closed_set:
                    heapq.heappush(
                        open_set,
                        (new_priority, new_cost, new_schedule, new_remaining),
                    )
                    closed_set.add(schedule_tuple)

    return [], float('inf')
# Greedy algorithm for task scheduling
def greedy_scheduling(tasks):
    schedule = []
    remaining_tasks = tasks[:]
    while remaining_tasks:
        # Choose the task with the shortest duration and no unmet dependencies
        available_tasks = [t for t in remaining_tasks if all(dep in [s.name for s in schedule] for dep in t.dependencies)]
        if not available_tasks:
            raise Exception("Unresolvable dependencies!")
        next_task = min(available_tasks, key=lambda t: t.duration)
        schedule.append(next_task)
        remaining_tasks.remove(next_task)
    return schedule

# Example tasks
tasks = [
    Task("A", 3, []),
    Task("B", 2, ["A"]),
    Task("C", 1, ["A"]),
    Task("D", 4, ["B", "C"]),
]

# Run A* Search
a_star_schedule, total_time = a_star_scheduling(tasks)
print("A* Schedule:", [t.name for t in a_star_schedule], "Total Time:", total_time)

# Run Greedy Algorithm
greedy_schedule = greedy_scheduling(tasks)
print("Greedy Schedule:", [t.name for t in greedy_schedule], "Total Time:", sum(t.duration for t in greedy_schedule))
