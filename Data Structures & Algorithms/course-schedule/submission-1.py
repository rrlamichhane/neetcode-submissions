from collections import deque
from typing import List

"""
Determine if it is possible to finish all courses given prerequisites.

Algorithm/Approach:
- Model courses as nodes in a directed graph where an edge bi -> ai indicates
  course ai depends on course bi.
- Use Kahn's algorithm (BFS-based topological sort) to detect cycles:
  - Compute indegree for each node (number of prerequisites remaining).
  - Initialize a queue with all nodes of indegree 0 (courses with no remaining prerequisites).
  - Repeatedly pop from the queue, "take" the course, and decrement indegrees
    of its dependents. If any dependent reaches indegree 0, enqueue it.
  - Count how many courses are processed. If we process all courses, the graph
    is acyclic and all courses can be finished; otherwise, a cycle exists and
    it's impossible to finish all courses.

Key Data Structures:
- adjacency list (list[list[int]]) to store outgoing edges for each course
- indegree array (list[int]) to track remaining prerequisites per course
- queue (collections.deque) for BFS over courses ready to be taken

Invariants:
- The queue contains exactly the courses whose current indegree is zero.
- indegree[c] always equals the number of prerequisites of c not yet taken.

Optimality:
- Kahn's algorithm runs in O(V + E) time and uses O(V + E) space, which is optimal
  for processing a graph of V courses and E prerequisite relationships.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Return True if it is possible to finish all courses given prerequisites.
        Implements Kahn's algorithm for topological sorting to detect cycles.
        """
        # Build adjacency list and indegree counts
        adjacency: List[List[int]] = [[] for _ in range(numCourses)]
        indegree: List[int] = [0] * numCourses

        for course, prereq in prerequisites:
            adjacency[prereq].append(course)
            indegree[course] += 1

        # Initialize queue with courses that have no prerequisites
        queue: deque[int] = deque(i for i in range(numCourses) if indegree[i] == 0)

        taken = 0  # count of courses we can take
        while queue:
            current = queue.popleft()
            taken += 1
            # Reduce indegree of dependent courses
            for dependent in adjacency[current]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)

        # If we processed all courses, there is no cycle
        return taken == numCourses