class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right =len(people)-1
        left =0
        count =0
        while right >= left:
            weight = people[right]+people[left]
            if people[right] == limit:
                count +=1
                right -=1
            elif weight == limit:
                count +=1
                right -=1
                left +=1
            elif weight > limit:
                count +=1
                right -=1
            else:
                count +=1
                right -=1
                left +=1
        return count