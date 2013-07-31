



from domain.user import *
        
    

def main():  
    
    dic  = {}
    
    user =  User("Maksym", "Stepanenko", 28)
    
    dic[user] = "first user"
    
    for key, value in dic.items():
        print( "key = '%s', value = '%s'" % (key, value) )
    
    
    print("main done")

if __name__ == '__main__':
    main()