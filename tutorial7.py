import tkinter as tk

root = tk.Tk()
root.title("Weight Predictor 2024")

main_canvas = tk.Canvas(root, width=400, height=300)
main_canvas.pack()

title_label = tk.Label(root, text="Weight Predictor", font=("Helvetica", 25))
main_canvas.create_window(200, 25, window=title_label)

sub_label = tk.Label(root, text="Insert your weight in KG")
main_canvas.create_window(200, 75, window=sub_label)

entry_text = tk.Entry(root)
main_canvas.create_window(200, 100, window=entry_text)

def function():
    text_entry = entry_text.get()
    result_label = tk.Label(root, text="You weigh: " + text_entry + "KG", font=("Helvetica", 20))
    main_canvas.create_window(200, 150, window=result_label)


calculate_button = tk.Button(text="Calculate", command=function, fg="black")
main_canvas.create_window(200, 150, window=calculate_button)

root.mainloop()
