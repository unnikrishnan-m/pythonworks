class movie:

    title:str

    ratiing:int

    run_time:int

    director:str

    genre:str

#initialising instance variable constructor

#python __init__


    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title
        
        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.run_time,self.director,self.genre)

movie_instance1=movie()

movie_instance1.set_movie("arm",7,160,"jithin lal","action drama")

movie_instance1.display()






