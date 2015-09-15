# https://leetcode.com/problems/course-schedule/

# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Find cycle in a directed graph.
        # Topological sort.

        indegree = [0] * numCourses
        children = [[] for p in range(numCourses)]
        
        for pre in prerequisites:
            indegree[pre[0]] += 1
            children[pre[1]].append(pre[0])
            
        courses = set(range(numCourses))
        flag = True
        while flag and len(courses):
            flag = False
            remove = []
            for c in courses:
                if indegree[c] == 0:
                    for child in children[c]:
                        indegree[child] -= 1
                    remove.append(c)
                    flag = True
            for r in remove:
                courses.remove(r)
        return len(courses) == 0