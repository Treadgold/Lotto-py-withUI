import customtkinter as ctk


class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("250x300")
        self.master.resizable(False, False)
        self.master.wm_title("Lotto Number Generator")
        self.row_number: str = '10'
        self.balls_drawn: str = '6'
        self.max_ball_number: str = '40'
        self.powerball: str = '10'


        #create the rows number label
        self.rows_label = ctk.CTkLabel(self.master, text=f"number of rows {self.row_number}")
        self.rows_label.place(relx=0.5, rely=0.1, anchor="center")

        #Create the rows slider
        slider_rows = ctk.CTkSlider(self.master, from_=1, to=10, number_of_steps=9, command=self.slider_rows_event)
        slider_rows.place(relx=0.5, rely=0.2, anchor="center")


        #create the number of balls drawn label
        self.balls_drawn_label = ctk.CTkLabel(self.master, text=f"balls to draw {self.balls_drawn}")
        self.balls_drawn_label.place(relx=0.5, rely=0.3, anchor="center")
        
        #Create the number of balls drawn slider
        slider_balls_drawn = ctk.CTkSlider(self.master, from_=4, to=12, number_of_steps=8, command=self.slider_balls_drawn_event)
        slider_balls_drawn.place(relx=0.5, rely=0.4, anchor="center")


        #create the max ball number label
        self.max_ball_number_label = ctk.CTkLabel(self.master, text=f"balls to draw {self.balls_drawn}")
        self.max_ball_number_label.place(relx=0.5, rely=0.3, anchor="center")
        
        #Create the max ball number slider
        slider_max_ball_number = ctk.CTkSlider(self.master, from_=20, to=100, number_of_steps=79, command=self.slider_max_ball_number_event)
        slider_max_ball_number.place(relx=0.5, rely=0.6, anchor="center")
        

        #create the powerball label
        self.powerball_label = ctk.CTkLabel(self.master, text=f"powerball max number (0 for no powerball) {self.powerball}")
        self.powerball_label.place(relx=0.5, rely=0.7, anchor="center")
        
        #Create the powerball slider
        slider_powerball = ctk.CTkSlider(self.master, from_=20, to=100, number_of_steps=79, command=self.slider_powerball_event)
        slider_powerball.place(relx=0.5, rely=0.8, anchor="center")
        
        
        #Create the button
        self.button = ctk.CTkButton(self.master, text="Generate Numbers", command=self.get_numbers, corner_radius=20)
        self.button.place(relx=0.5, rely=0.9, anchor="center")
    
    def slider_rows_event(self, value):
        self.row_number = str(int(value))
        self.rows_label.configure(text=f"number of rows {self.row_number}")

    def slider_balls_drawn_event(self, value):
        self.balls_drawn = str(int(value))
        self.balls_drawn_label.configure(text=f"balls to draw {self.balls_drawn}")   
        
    def slider_max_ball_number_event(self, value):
        self.max_ball_number = str(int(value))
        self.max_ball_number_label.configure(text=f"balls to draw {self.max_ball_number}")   

    def slider_powerball_event(self, value):
        self.slider_powerball = str(int(value))
        self.powerball_label.configure(text=f"balls to draw {self.powerball}")          

    def get_numbers(self):
        pass
    


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()