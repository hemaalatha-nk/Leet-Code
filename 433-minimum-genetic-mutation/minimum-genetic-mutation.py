class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        if endGene not in bank:
            return -1

        graph= collections.defaultdict(list)

        for gene in bank:

            for i in range(len(gene)):

                transforms= gene[:i]+"*"+gene[i+1:]

                graph[transforms].append(gene)

        queue=collections.deque([(startGene,0)])
       

        visited=set()

        while queue:
                gene,distance=queue.popleft()

                if gene==endGene:
                    return distance
                
                visited.add(gene)

                for i in range(len(gene)):
                    transform=gene[:i]+"*"+gene[i+1:]


                    posible_matches=graph.get(transform,None)

                    if posible_matches:
                        for match in posible_matches:
                            if match  not in visited:
                                queue.append((match,distance+1))
        return -1




        
        