class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g=defaultdict(list)
        course=prerequisites

        for a,b in course:
            g[a].append(b)


        Unseen=0
        Visiting=1
        Visited=2

        states=[Unseen] * numCourses

        def dfs(node):
            state= states[node]
            if state==Visited:
                return True
            elif state==Visiting:
                return False
            states[node]=Visiting


            for i in g[node]:
                if not dfs(i):
                    return False
            
            states[node]=Visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        



        