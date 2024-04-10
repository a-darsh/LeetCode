class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        ans=[]
        for img in image:
            i, j = 0, len(img)-1
            while(i<j):
                img[i], img[j] = img[j], img[i]
                i+=1
                j-=1

            img = [1 if i==0 else 0 for i in img]
            ans.append(img)
        return ans