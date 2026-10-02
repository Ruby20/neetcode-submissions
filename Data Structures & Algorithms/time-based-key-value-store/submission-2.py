class TimeMap:

    def __init__(self):
        self.store = {} # key=string values = [<val, timestamp>] list
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])    

        
    def get(self, key: str, timestamp: int) -> str:
        # need to search by both key and timestamp
        res = ""
        values = self.store.get(key, [])
        
        # binary search
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res


        
