class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the point on/in the rectangle closest to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate squared distance from closest point to circle center
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        
        # Overlap occurs if squared distance <= radius^2
        return dx * dx + dy * dy <= radius * radius