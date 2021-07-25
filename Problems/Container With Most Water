class Solution:
    def maxArea(self, height: List[int]) -> int:
        m_area, i, j = 0, 0, len(height) - 1
        while i < j:
            m_area = max(m_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m_area
