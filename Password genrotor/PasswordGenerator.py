import random  
import string  

def create_password(length):
    
    lower = string.ascii_lowercase  
    upper = string.ascii_uppercase 
    nums = string.digits             
    specials = string.punctuation     

    
    all_chars = lower + upper + nums + specials

    
    password = ""
    for _ in range(length):
        password += random.choice(all_chars)  

    return password  

def main():
    print("Welcome to the Password Generator!")  
    
    while True:  
        user_input = input("Enter the desired password length (minimum 4): ")
        
        
        try:
            length = int(user_input)
            if length < 4:
                print("The password length must be at least 4 characters. Try again.")
                continue  
        except ValueError:
            print("That input is not valid. Please enter a number.")
            continue 
        new_password = create_password(length)

       
        print("Your generated password is:", new_password)

        
        another = input("Would you like to create another password? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thanks for using the Password Generator! Goodbye.")
            break 

if __name__ == "__main__":
    main()
