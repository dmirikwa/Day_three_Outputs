class BinarySearch(list):

    def __init__(self,a,b):
        self.length = a
        self.b = b

        
        for num in range(self.length):
            self.append(self.b)
            self.b +=b

        

    def search(self, num):
        
        upper = (self.length - 1)
        lower = 0
        count = 0
        notfound =True
  
            
          
        while lower <= upper and notfound:
            mid = (lower + upper) //2
            mid_value = self[mid] 
            if num > mid_value:
                lower = mid + 1
                count += 1
            elif num < mid_value:
                upper = mid - 1
                count += 1
            else:
                count += 1
                
                return {'count': count, 'index': mid}
        return {"count":count,"index":-1}
