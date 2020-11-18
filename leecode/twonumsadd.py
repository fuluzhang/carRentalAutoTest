
class Solution:

    def addtwonum(self,num,target):
        ele = {}
        for i in range(len(num)):
            diff = target - num[i]
            if diff in ele.keys():
                return [ele[diff],i]
            else :
                ele[num[i]] = i

if __name__ == '__main__':
    print(Solution().addtwonum([2,3,4,5,7],5))