class library:
    def __init__(self,lis,name):
        self.booklis=lis
        self.name=name
        self.affordDict={}

    def displayBooks(self):
        print(f"We have following books in our library:{self.name}")
        for book in self.booklis:
            print(book)

    def affordBook(self,user,book):
        if book not in self.affordDict.keys():
            self.affordDict.update({book:user})
            self.booklis.remove(book)
            print("Updated,you can take the book")
        else:
            print("Book is already taken by someone {self.affordDict[book]}")

    def addBook(self,book):
        self.booklis.append(book)
        print("book has been added")

    def returnBook(self,book):
        self.affordDict.pop(book)
        self.booklis.append(book)
        print("Your book have been sucessfully returned")


if __name__=="__main__":
    x=library(["python","c","c++","c#","java","HTML","CSS","Artifical intelligence","machine learning",".net"],"Rahul")
    while(True):
        print(f"Welcome to the {x.name}'s library.Enter your choice to continue")
        print("1. DisplayBooks")
        print("2. Afford book")
        print("3. Add book")
        print("4. Return book")
        user_choice=input()
        if user_choice not in["1","2","3","4"]:
            continue
        else:
            user_choice=int(user_choice)


        if user_choice==1:
            x.displayBooks()

        elif user_choice==2:
            book=input("enter the name of the book you want to afford: ")
            user=input("enter your name: ")
            x.affordBook(user,book)
            
        elif user_choice==3:
            book=input("enter the name of the book you want to add: ")
            x.addBook(book)

        elif user_choice==4:
            book=input("enter the name of boook you want to return: ")
            x.returnBook(book)

        else:
            print("Not a valid option")

    
