class book():  
    def __init__(self,name,page,author):
        print("kayıt")
        self.name= name
        self.page = page
        self.author=author
    def __str__(self):
        return (f"book name: {self.name}, number of book pages: {self.page}, author: {self.author}")
    
sherlock = book("sherlock holmes", 467, "arthur boyle")
print(sherlock)
