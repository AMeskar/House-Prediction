from abc import ABC, abstractmethod

class Dinner(ABC):

    def serve_Dinner(self):

        self.serve_entry()
        self.serve_main()
        self.serve_dessert()
        self.serve_Tea_or_Coffe()
    
    @abstractmethod
    def serve_entry(self):
        pass

    @abstractmethod
    def serve_main(self):
        pass

    @abstractmethod
    def serve_dessert(self):
        pass

    @abstractmethod
    def serve_Tea_or_Coffe(self):
        pass

class Morrocan_Dinner(Dinner):

    def serve_entry(self):
        print('Salade Necoise')

    def serve_main(self):
        print('Tajine djaj o khodera')

    def serve_dessert(self):
        print('halwa d choclat')

    def serve_Tea_or_Coffe(self):
        print('Atay o l9ahwa')

class Italian_Dinner(Dinner):

    def serve_entry(self):
        print('Brushetto')

    def serve_main(self):
        print('pasta')

    def serve_dessert(self):
        print('cheese cake')

    def serve_Tea_or_Coffe(self):
        print('beers')

class Chineese_Dinner(Dinner):

    def serve_entry(self):
        print('sera9 zite')

    def serve_main(self):
        print('mokh dba3')

    def serve_dessert(self):
        print('sera9 zit m9ly')

    def serve_Tea_or_Coffe(self):
        print('boul dl hmar')

if __name__=="__main__":

    serving = Morrocan_Dinner()
    serving.serve_Dinner()

    serving = Italian_Dinner()
    serving.serve_Dinner()

    serving = Chineese_Dinner()
    serving.serve_Dinner()