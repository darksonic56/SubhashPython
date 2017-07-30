
import logging, sys
logging.basicConfig(level=logging.DEBUG, format ='%(asc time)s - %(levelname)s - %(message)s')
logging.DEBUG('Start of Program')            
#n = int(n)            
def factorial(n):
        logging.DEBUG('Start of factorial(%s)' % (n))
        #n = sys.modules['__builtin__'].n
       
      # Subhash Test Code with Python tst
        
        total  = 1
        ##total = int(total)
        
        for i in range(1, n + 1):
                  
                        total = total * i 
                        logging.DEBUG('i is %s, total is %s' % (total, i))
                        logging.DEBUG('Return value is %s' % (total))
                        ##total = sys.modules['__builtin__'].total 
                        return total
                

print(factorial(5))
logging.DEBUG('End of Program')      
