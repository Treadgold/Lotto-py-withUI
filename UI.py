import customtkinter as ctk
import newlotto

class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("900x600")
        self.master.resizable(False, False)
        self.master.wm_title("Lotto Number Generator")
        self.row_number: str = '10'
        self.balls_drawn: str = '6'
        self.max_ball_number: str = '40'
        self.powerball: str = '10'


        #create the rows number label
        self.rows_label = ctk.CTkLabel(self.master, text=f"number of rows {self.row_number}")
        self.rows_label.place(relx=0.25, rely=0.1, anchor="e")
        #Create the rows slider
        slider_rows = ctk.CTkSlider(self.master, from_=1, to=30, number_of_steps=29, command=self.slider_rows_event)
        slider_rows.place(relx=0.25, rely=0.2, anchor="e")
        slider_rows.set(int(self.row_number))


        #create the number of balls drawn label
        self.balls_drawn_label = ctk.CTkLabel(self.master, text=f"balls to draw {self.balls_drawn}")
        self.balls_drawn_label.place(relx=0.25, rely=0.3, anchor="e")
        #Create the number of balls drawn slider
        slider_balls_drawn = ctk.CTkSlider(self.master, from_=4, to=9, number_of_steps=5, command=self.slider_balls_drawn_event)
        slider_balls_drawn.place(relx=0.25, rely=0.4, anchor="e")
        slider_balls_drawn.set(int(self.balls_drawn))



        #create the max ball number label
        self.max_ball_number_label = ctk.CTkLabel(self.master, text=f"max ball number {self.max_ball_number}")
        self.max_ball_number_label.place(relx=0.25, rely=0.5, anchor="e")
        #Create the max ball number slider
        slider_max_ball_number = ctk.CTkSlider(self.master, from_=20, to=100, number_of_steps=80, command=self.slider_max_ball_number_event)
        slider_max_ball_number.place(relx=0.25, rely=0.6, anchor="e")
        slider_max_ball_number.set(int(self.max_ball_number))
        

        #create the powerball label
        self.powerball_label = ctk.CTkLabel(self.master, text=f"powerball max {self.powerball}")
        self.powerball_label.place(relx=0.25, rely=0.7, anchor="e")
        #Create the powerball slider
        slider_powerball = ctk.CTkSlider(self.master, from_=0, to=100, number_of_steps=101, command=self.slider_powerball_event)
        slider_powerball.place(relx=0.25, rely=0.8, anchor="e")
        slider_powerball.set(int(self.powerball))
        
        
        #Create the button
        self.button = ctk.CTkButton(self.master, text="Generate Numbers", command=self.populate_box, corner_radius=20)
        self.button.place(relx=0.25, rely=0.9, anchor="e")

        #create the text box
        self.text_box = ctk.CTkTextbox(self.master, width=640, height=500, font=("Courier", 23))
        self.text_box.place(relx=0.98, rely=0.5, anchor="e")
    
    def slider_rows_event(self, value):
        self.row_number = str(int(value))
        self.rows_label.configure(text=f"number of rows {self.row_number}")
        

    def slider_balls_drawn_event(self, value):
        self.balls_drawn = str(int(value))
        self.balls_drawn_label.configure(text=f"balls to draw {self.balls_drawn}")
               

        
    def slider_max_ball_number_event(self, value):
        self.max_ball_number = str(int(value))
        self.max_ball_number_label.configure(text=f"max ball number {self.max_ball_number}")
         

    def slider_powerball_event(self, value):
        self.powerball = str(int(value))
        self.powerball_label.configure(text=f"powerball max {self.powerball}")
              

    def populate_box(self):
        self.text_box.delete("1.0", "100.0")
        final_lines = newlotto.get_lines(
            int(self.row_number),
            int(self.max_ball_number),
            int(self.balls_drawn),
            int(self.powerball)
            )

        for line in final_lines:
            # check result as tuple will have powerball, else just normal line
            if type(line) is tuple:
                self.text_box.insert("1.0", str(line[0]) + str(line[1]) + "\n")
            else:
                self.text_box.insert("1.0", str(line) + "\n")
        pass
    


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()