class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        MyMap={}
        for n in nums:
            MyMap[n]=MyMap.get(n, 0)+1
        ritorno=[]
        MyMap_sorted = dict(sorted(MyMap.items(), key=lambda x: -x[1]))
        K = list(MyMap_sorted.keys())
        print(K)
        for i in range(k):
            ritorno.append(K[i])
        return ritorno