class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_map = defaultdict(list)
        # sort the tickets     
        tickets.sort()
        for src, dst in tickets:
            adj_map[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj_map:
                return False

            temp = list(adj_map[src])    
            for i, v in enumerate(temp):  
                adj_map[src].pop(i)
                res.append(v)
                
                if dfs(v): 
                    return True
                # backtracking     
                adj_map[src].insert(i, v)      
                res.pop()
            return False    

        dfs("JFK")    
        return res

# time: O(V + E) ^ 2           

        