from credentials import Credentials
from user import User


def createAccount(fname,lname,mail,uName,pass_word):
    '''Creates user account'''
    new_user=User(first_Name=fname,last_Name=lname,user_Name=uName,e_mail=mail,pass_word=pass_word)
    return new_user

def save_Users(user):
    '''saves the user details'''
    user.save_User()

def login(pass_word):
    '''logs in the user by connecting find user'''
    new_user=User.find_User(pass_word)
    return new_user



# Credential functions
def create_Credentials(name,password):
    '''Fucntion that creates credentials of the user '''
    new_credentials=Credentials(name=name,password=password)
    return new_credentials


def save_Cred(cred):
    '''saves user credentials using save credetials function in cred page'''
    cred.save_Credentials()

def gen_Pass():
    '''generates password for user'''
    return  Credentials.genPass()

def display_Cred():
    '''function that displays user credentials by calling display credentials'''
    return Credentials.display_Credentials()


def find_Cred(name):
    '''function to find the user credentials by allowing user to search'''
    return Credentials.find_cred(name)


def check_existing(val):
    '''function to check if the crediats exist'''
    return Credentials.check_cred_Exists(val)

def del_Cred(del_cred):
    ''''function to delete the credentials'''
    del_cred.delete_Account()

def main():
    print("hello Welcome to password locker.What is your name")
    user_name=input()
    print(f"Hello {user_name} please sign in to access or save passwords")
    print('\n')
    while True:
        print("Do you have an account? Use LI to let me know that you want to login")
        print('\n')
        print("Dont have an account? Use CA to tell me to create an accout for you")
        print('\n')
        print("Dont have an account? Use VC to tell me to show you your  accout ")
        print('\n')
        print("Dont you want to Exit? Use EX to tell me to allow you leave") 

        short_code=input().upper()


        if short_code=='CA':
            print("Create Account")
            print("*"*5)
            print('\n')

            print("First Name....................................")
            fname=input()
            print("*"*10)
            print('\n')
        

            print("Last Name.....................................")
            lname=input()
            print("*"*20)
            print('\n')
        


            print("Email ........................................")
            email=input()
            print("*"*20)
            print('\n')
        

            print("user Name.....................................")
            uname=input()
            print("*"*20)
            print('\n')
        


            print("pass_word to Login..................................")
            pNumber=input()
            print("*"*20)
            print('\n')
            

            print("*"*200)
            save_Users(createAccount(fname,lname,uname,email,pNumber))
        
            print("Now you have to login {fname}")

        elif short_code=='LI':
            print("email.......")
            email=input()
            # print("pass_word number.......")
            # pNumber=input()
            logedUser=login(email)


            print(f"Welcome {logedUser.first_Name} its been tough but argh you done")


            print("What do you want to do?")
            print("\n")
            print("For Create credentials---------------------------CC")
            print("\n")
            print("For Display your saved credentials----------------DC")
            print("\n")
            print("For Searching  credentials------------------------SC")
            print("\n")
            print("To Delete credentials------------------------------DL")
            print("\n")
            # print("To Update  credentials-----------------------------UC")
    
            short_code=input().upper()
            if short_code=="CC":
                print("New Credentials")
                print("*"*50)
                print("\n")


                print("Name of site")
                name=input()
                print("\n")


                print("Select either to enter password or create password")
                print("For enter password-------------------------------EP")
                
                print("For Generate password ---------------------------GP")
                com=input().upper()
                print("\n")
                if com=='EP':
                    passw=input()
                    print(passw)
                elif com=='GP':
                    passw=gen_Pass()
                    passww=gen_Pass()
                    print(passw)
                else:
                    print("Dont understand you?")
                save_Cred(create_Credentials(name,passw))
                print(f"New credentials of: {name} with password:{passw} created")
            elif short_code=='DC':
                if display_Cred():
                    for cred in display_Cred():
                        print(f"{cred.name} {cred.password}")
                else:
                    print("Credentials are currently empty create one first ")
            elif short_code=="SC":
                search_val=input().lower()
                
                if search_val=='':
                    print("its empty")
           
                
                
                else:
                    if check_existing(search_val):

                        search_cred=find_Cred(search_val)
                        print(f"{search_cred.name} found with {search_cred.password} as password")

            elif short_code=='DL':
                del_val=input()
                if check_existing(del_val):

                    search_cred=find_Cred(del_val)
                    del_Cred(search_cred)
                    print(f"You have sucessfully deleted {del_val}")
                

        elif short_code=='EX':
            print(f"goobye {user_name}")

        else:
            print(f"Did you really read the instructions {user_name} please retry")


        





            









if __name__=='__main__':
    main()

