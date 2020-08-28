class Solution:
    def trap(self, height: List[int]) -> int:
        
        l_height = [0] * len(height)
        r_height = [0] * len(height)
        
        tmp_max = 0
        for i in range(len(height)):
            l_height[i] = max(tmp_max - height[i], 0)
            tmp_max = max(tmp_max, height[i])
            
        tmp_max = 0
        for j in range(len(height)-1,-1,-1):
            r_height[j] = max(tmp_max - height[j], 0)
            tmp_max = max(tmp_max, height[j])
            
        trap_water = 0
        
        for i in range(len(height)):
            trap_water += min(l_height[i], r_height[i])
        
        #print(l_height, r_height)
            
        return trap_water
