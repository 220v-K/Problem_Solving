class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sumOfUnits = 0

        boxList = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        for i in boxList:
            if truckSize >= i[0]:
                truckSize -= i[0]
                sumOfUnits += i[0] * i[1]

            elif truckSize > 0 and truckSize < i[0]:
                sumOfUnits += i[1] * truckSize
                truckSize = -1

            else:
                break
        
        return sumOfUnits