import tkinter as tk
import tkinter.scrolledtext as tkst
import shelve

root = tk.Tk()
root.title("TSI - Settings")
root.iconbitmap("OBlogoIcon.ico")
root.config(bg="#080808")
root.geometry("0x0+450+220")
root.minsize(660, 440)
# root.maxsize(900, 600)

custom_text_tl = None
settings_db = shelve.open("settings", writeback=True)

try:
    if settings_db["first_time"]:
        pass
except KeyError:
    settings_db["default_and_saved"] = {
        "minutes": [1, 1],
        "unit": [1, 1],
        "theme": [1, 1],
        "text": [1, 1],
        "language": [1, 1],
        "layout": [1, 1]
    }

    settings_db["themes"] = {

        "light_theme": {
            "root": {"fg": "", "bg": "#fafafa"},  # fg
            "welcome_text": {"fg": "#5c69cb", "bg": "#f0e1e1"},

            "show_text_frame": {"fg": "", "bg": "#fafafa"},  # fg
            "typed_text": {"fg": "#5c69cb", "bg": "#fafafa", "insert_bg": "black"},
            "text_to_type": {"fg": "#5c69cb", "bg": "#fafafa", "insert_bg": "black"},
            "tag_correct": {"fg": "#82bce3", "bg": "black"},
            "tag_wrong": {"fg": "#82bce3", "bg": "red"},

            "passed_time": {"fg": "#82bce3", "bg": "#fafafa"},
            "typed_chars": {"fg": "#82bce3", "bg": "#fafafa"},
            "remaining_chars": {"fg": "#82bce3", "bg": "#fafafa"},
            "total_chars": {"fg": "#82bce3", "bg": "#fafafa"},
            "typing_speed": {"fg": "#82bce3", "bg": "#fafafa"},

            "start_label": {"fg": "#e1ac45", "bg": "#fafafa"},
            "change_settings": {"fg": "#e1ac45", "bg": "#fafafa"}
        },

        "dark_theme": {
            "root": {"fg": "", "bg": "#080808"},  # fg
            "welcome_text": {"fg": "white", "bg": "#080808"},

            "show_text_frame": {"fg": "", "bg": "#080808"},  # fg
            "typed_text": {"fg": "#080808", "bg": "white", "insert_bg": "black"},
            "text_to_type": {"fg": "#080808", "bg": "white", "insert_bg": "black"},
            "tag_correct": {"fg": "white", "bg": "black"},
            "tag_wrong": {"fg": "white", "bg": "red"},

            "passed_time": {"fg": "white", "bg": "#080808"},
            "typed_chars": {"fg": "white", "bg": "#080808"},
            "remaining_chars": {"fg": "white", "bg": "#080808"},
            "total_chars": {"fg": "white", "bg": "#080808"},
            "typing_speed": {"fg": "white", "bg": "#080808"},

            "start_label": {"fg": "white", "bg": "#080808"},
            "change_settings": {"fg": "white", "bg": "#080808"}
        },

        "high_contrast": {
            "root": {"fg": "", "bg": "black"},  # fg
            "welcome_text": {"fg": "#0a5ec5", "bg": "black"},

            "show_text_frame": {"fg": "", "bg": "black"},  # fg
            "typed_text": {"fg": "#0a5ec5", "bg": "#000000", "insert_bg": "#0a5ec5"},
            "text_to_type": {"fg": "#0a5ec5", "bg": "#000000", "insert_bg": "#0a5ec5"},
            "tag_correct": {"fg": "#0a5ec5", "bg": "#0a5ec5"},
            "tag_wrong": {"fg": "#0a5ec5", "bg": "red"},

            "passed_time": {"fg": "#0a5ec5", "bg": "black"},
            "typed_chars": {"fg": "#0a5ec5", "bg": "black"},
            "remaining_chars": {"fg": "#0a5ec5", "bg": "black"},
            "total_chars": {"fg": "#0a5ec5", "bg": "black"},
            "typing_speed": {"fg": "#0a5ec5", "bg": "black"},

            "start_label": {"fg": "#0a5ec5", "bg": "black"},
            "change_settings": {"fg": "#0a5ec5", "bg": "black"}
        }
    }

    settings_db["custom_text"] = ""
    settings_db["first_time"] = False
    settings_db["changes_exist"] = False
    settings_db["stored_texts"] = [
        "In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes.",
        "The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python's for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.",
        "When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement's else clause runs when no exception occurs, and a loop's else clause runs when no break occurs. For more on the try statement and exceptions, see Handling Exceptions. The continue statement, also borrowed from C, continues with the next iteration of the loop.",
        "In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function), and their order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument may receive a value more than once.",
        "Looking at this in a bit more detail, it is possible to mark certain parameters as positional-only. If positional-only, the parameters' order matters, and the parameters cannot be passed by keyword. Positional-only parameters are placed before a / (forward-slash). The / is used to logically separate the positional-only parameters from the rest of the parameters. If there is no / in the function definition, there are no positional-only parameters. Parameters following the / may be positional-or-keyword or keyword-only.",
        "Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope.",
        "Before introducing classes, I first have to tell you something about Python's scope rules. Class definitions play some neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what's going on. Incidentally, knowledge about this subject is useful for any advanced Python programmer",
        "If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed. An exception could occur during execution of an except or else clause. Again, the exception is re-raised after the finally clause has been executed.",
        "Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages.",
        "Contrary to JSON, pickle is a protocol which allows the serialization of arbitrarily complex Python objects. As such, it is specific to Python and cannot be used to communicate with applications written in other languages. It is also insecure by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was crafted by a skilled attacker."
    ]
    

def get_custom_text():
    global custom_text_tl

    def check_entered_text():
        txt = ct_text.get("0.0", tk.END).strip(" \n").replace("\n", " ").replace("  ", " ")
        if len(txt) < 250:
            ct_save.configure(text="Less than 250 ! Try again ?")
        elif len(txt) > 385:
            ct_save.configure(text="More than 385 ! Try again ?", )
        else:
            ct_save.configure(text="Text is saved ! :)", font=(
                "Caviar Dreams Bold", "10", "bold"))
            ct_save.unbind("<1>")
            settings_db["custom_text"] = txt
            text_nbr.set(2)
            custom_text_tl.after(3000, custom_text_tl.destroy)


    text_nbr.set(1)
    if custom_text_tl is None:
        custom_text_tl = tk.Toplevel()
        custom_text_tl.title("TSI - Custom Text")
        custom_text_tl.iconbitmap(r"OBlogoIcon.ico")
        custom_text_tl.geometry("0x0+400+220")
        custom_text_tl.config(bg="#080808")
        custom_text_tl.minsize(600, 400)
        custom_text_tl.maxsize(800, 600)
        welc_label = tk.Label(custom_text_tl, text="Typing Speed Increaser", width=600, pady=10, font=(
                "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
        welc_label.pack(side=tk.TOP, fill=tk.BOTH,
                        anchor=tk.CENTER, padx=10, pady=10)

        ct_frame = tk.Frame(custom_text_tl, height=30, bg="#080808", padx=40)
        ct_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.CENTER)

        ct_label = tk.Label(ct_frame, text="Min 250 characters, max 385 and no new lines :)", width=10, pady=0, font=(
                "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", anchor="w")
        ct_label.place(relx=.0, rely=.0, relheight=1, relwidth=.6)

        ct_save = tk.Label(ct_frame, text="Save", width=10, pady=0, font=(
                "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808", anchor="e")
        ct_save.place(relx=.6, rely=.0, relheight=1, relwidth=.4)
        ct_save.bind("<1>", lambda key: check_entered_text())

        ct_text = tkst.ScrolledText(custom_text_tl, padx=5, pady=5, font=(
        "Caviar Dreams Bold", "10", "bold"), fg="black", bg="white", wrap=tk.WORD, relief=tk.RIDGE, borderwidth=2)
        ct_text.pack(side=tk.TOP, fill=tk.BOTH,
                        anchor=tk.CENTER, expand=True, padx=10, pady=10)
        
        if settings_db["custom_text"] != "":
            ct_text.insert("0.0", settings_db["custom_text"])
        
        custom_text_tl.focus_force()
    
    elif custom_text_tl.winfo_exists():
        custom_text_tl.focus_force()
    else:
        custom_text_tl = None
        # del welc_label, ct_frame, ct_label, ct_save, ct_text
        get_custom_text()


def show_about():
    about_tl = tk.Toplevel()
    about_tl.title("TSI - About")
    about_tl.iconbitmap(r"OBlogoIcon.ico")
    about_tl.geometry("0x0+400+220")
    about_tl.config(bg="#080808")
    about_tl.minsize(280, 475)
    about_tl.maxsize(560, 950)
    about_label = tk.Label(about_tl, text="Typing Speed Increaser", width=600, pady=10, font=(
            "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
    about_label.pack(side=tk.TOP, fill=tk.BOTH,
                      anchor=tk.CENTER, padx=10, pady=10)
    cont = "TSI (Typing Speed Increaser)\n\nVersion 2.0.0\n\n\nProgram that helps students and everyone practice and increase their typing speed."
    about_text = tk.Label(about_tl, text=cont, width=10, wraplength=250, pady=0, font=(
            "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808")
    about_text.pack(side=tk.TOP, fill=tk.BOTH,
                      anchor=tk.CENTER, padx=10, pady=10)
    
    me_link = tk.Label(about_tl, text="Developed by: Tarek Hammami", width=10, wraplength=250, pady=0, font=(
            "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808")
    me_link.pack(side=tk.TOP, fill=tk.BOTH,
                      anchor=tk.CENTER, padx=10, pady=10)
    me_link.bind("<1>", lambda key: __import__("webbrowser").open("https://www.facebook.com/thammami.me"))
    
    islaib_link = tk.Label(about_tl, text="Student at HIALCS (ISLAI) Beja", width=10, wraplength=250, pady=0, font=(
            "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808")
    islaib_link.pack(side=tk.TOP, fill=tk.BOTH,
                      anchor=tk.CENTER, padx=10, pady=10)
    islaib_link.bind("<1>", lambda key: __import__("webbrowser").open("https://islaib.rnu.tn/"))

    made_in = tk.Label(about_tl, text="Made In TUNISIA", width=10, wraplength=250, pady=0, font=(
            "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808")
    made_in.pack(side=tk.TOP, fill=tk.BOTH,
                      anchor=tk.CENTER, padx=10, pady=70)

    about_tl.focus_force()


def quit_settings():
    settings_db.close()
    exit()


def save_settings():
    global settings_db

    if settings_db["default_and_saved"]["minutes"][1] != nbr_min.get() or \
        settings_db["default_and_saved"]["unit"][1] != tp_unit.get() or \
        settings_db["default_and_saved"]["theme"][1] != wh_theme.get() or \
        settings_db["default_and_saved"]["text"][1] != text_nbr.get() or \
        settings_db["default_and_saved"]["language"][1] != wh_lang.get() or \
        settings_db["default_and_saved"]["layout"][1] != keyboard_lay.get():

        settings_db["changes_exist"] = True
        settings_db["default_and_saved"]["minutes"][1] = nbr_min.get()
        settings_db["default_and_saved"]["unit"][1] = tp_unit.get()
        settings_db["default_and_saved"]["theme"][1] = wh_theme.get()
        settings_db["default_and_saved"]["text"][1] = text_nbr.get()
        settings_db["default_and_saved"]["language"][1] = wh_lang.get()
        settings_db["default_and_saved"]["layout"][1] = keyboard_lay.get()

    root.after(1000, quit_settings)


def enable_and_disable():
    if wh_lang.get() == 1 or wh_lang.get() == 2:
        qwerty_keyboard["state"] = tk.NORMAL
        azerty_keyboard["state"] = tk.DISABLED  # for the moment :)
        arabic_keyboard["state"] = tk.DISABLED
        if keyboard_lay.get() == 3:
            keyboard_lay.set(1)
    else:
        qwerty_keyboard["state"] = tk.DISABLED
        azerty_keyboard["state"] = tk.DISABLED
        arabic_keyboard["state"] = tk.NORMAL
        if keyboard_lay.get() != 3:
            keyboard_lay.set(3)


def show_settings():
    nbr_min.set(settings_db["default_and_saved"]["minutes"][1])
    tp_unit.set(settings_db["default_and_saved"]["unit"][1])
    wh_theme.set(settings_db["default_and_saved"]["theme"][1])
    text_nbr.set(settings_db["default_and_saved"]["text"][1])
    wh_lang.set(settings_db["default_and_saved"]["language"][1])
    keyboard_lay.set(settings_db["default_and_saved"]["layout"][1])
    enable_and_disable()


def reset_settings():
    global settings_db
    settings_db["default_and_saved"]["minutes"][1] = settings_db["default_and_saved"]["minutes"][0]
    settings_db["default_and_saved"]["unit"][1] = settings_db["default_and_saved"]["unit"][0]
    settings_db["default_and_saved"]["theme"][1] = settings_db["default_and_saved"]["theme"][0]
    settings_db["default_and_saved"]["text"][1] = settings_db["default_and_saved"]["text"][0]
    settings_db["default_and_saved"]["language"][1] = settings_db["default_and_saved"]["language"][0]
    settings_db["default_and_saved"]["layout"][1] = settings_db["default_and_saved"]["layout"][0]
    show_settings()


welcome_text = tk.Label(
    root, text="Typing Speed Increaser - Setting Page", width=600, pady=10, font=(
        "Caviar Dreams Bold", "16", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
welcome_text.pack(side=tk.TOP, fill=tk.BOTH,
                  anchor=tk.CENTER, padx=10, pady=10)

settings_frame = tk.Frame(root, bg="#080808", width=600, padx=30)
settings_frame.pack(side=tk.TOP, fill=tk.BOTH,
                    anchor=tk.CENTER, expand=True, padx=10, pady=10)

side_1 = tk.Frame(settings_frame, bg="#080808")
side_2 = tk.Frame(settings_frame, bg="#080808")
side_3 = tk.Frame(settings_frame, bg="#080808")
bottom_side = tk.Frame(settings_frame, bg="#080808", padx=40)
side_1.place(relx=.0, rely=.0, relheight=.74, relwidth=.30)
side_2.place(relx=.35, rely=.0, relheight=.74, relwidth=.30)
side_3.place(relx=.70, rely=.0, relheight=.74, relwidth=.30)
bottom_side.place(relx=0, rely=.80, relheight=.20, relwidth=1)

nbr_minutes = tk.Label(side_1, text="Minutes", font=(
    "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
nbr_minutes.pack(side=tk.TOP, fill=tk.X, pady=10)

nbr_min = tk.IntVar()
min_1 = tk.Radiobutton(side_1, text="1 Minute", variable=nbr_min, value=1, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
min_2 = tk.Radiobutton(side_1, text="2 Minutes", variable=nbr_min, value=2, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
min_3 = tk.Radiobutton(side_1, text="3 Minutes", variable=nbr_min, value=3, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
min_5 = tk.Radiobutton(side_1, text="5 Minutes", variable=nbr_min, value=4, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
min_1.pack(anchor=tk.W, padx=10)
min_2.pack(anchor=tk.W, padx=10)
min_3.pack(anchor=tk.W, padx=10)
min_5.pack(anchor=tk.W, padx=10)

typing_speeding_unit = tk.Label(side_1, text="Unit", font=(
    "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
typing_speeding_unit.pack(side=tk.TOP, fill=tk.X, pady=10)

tp_unit = tk.IntVar()
wpm_choice = tk.Radiobutton(side_1, text="WPM", variable=tp_unit, value=1, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
cpm_choice = tk.Radiobutton(side_1, text="CPM", variable=tp_unit, value=2, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
wpm_choice.pack(anchor=tk.W, padx=10)
cpm_choice.pack(anchor=tk.W, padx=10)

theme = tk.Label(side_2, text="Theme", font=(
    "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
theme.pack(side=tk.TOP, fill=tk.X, pady=10)

wh_theme = tk.IntVar()
light_theme = tk.Radiobutton(side_2, text="Light", variable=wh_theme, value=1, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
dark_theme = tk.Radiobutton(side_2, text="Dark", variable=wh_theme, value=2, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
high_contrast = tk.Radiobutton(side_2, text="High Contrast", variable=wh_theme, value=3, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
light_theme.pack(anchor=tk.W, padx=10)
dark_theme.pack(anchor=tk.W, padx=10)
high_contrast.pack(anchor=tk.W, padx=10)

choose_text = tk.Label(side_2, text="Text", font=(
    "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
choose_text.pack(side=tk.TOP, fill=tk.X, pady=10)

text_nbr = tk.IntVar()
random_text = tk.Radiobutton(side_2, text="Random Text", variable=text_nbr, value=1, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
custom_text = tk.Radiobutton(side_2, text="Custom Text", variable=text_nbr, value=2, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black", command=get_custom_text)
random_text.pack(anchor=tk.W, padx=10)
custom_text.pack(anchor=tk.W, padx=10)

language = tk.Label(side_3, text="Language", font=(
    "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
language.pack(side=tk.TOP, fill=tk.X, pady=10)

wh_lang = tk.IntVar()
english = tk.Radiobutton(side_3, text="English", variable=wh_lang, value=1, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black", command=enable_and_disable)
french = tk.Radiobutton(side_3, text="French", variable=wh_lang, value=2, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black", command=enable_and_disable, state=tk.DISABLED)
arabic = tk.Radiobutton(side_3, text="Arabic", variable=wh_lang, value=3, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black", command=enable_and_disable, state=tk.DISABLED)
english.pack(anchor=tk.W, padx=10)
french.pack(anchor=tk.W, padx=10)
arabic.pack(anchor=tk.W, padx=10)

keyboard_layout = tk.Label(side_3, text="Keyboard", font=(
    "Caviar Dreams Bold", "12", "bold"), fg="white", bg="#080808", relief=tk.RIDGE, borderwidth=2)
keyboard_layout.pack(side=tk.TOP, fill=tk.X, pady=10)

keyboard_lay = tk.IntVar()
qwerty_keyboard = tk.Radiobutton(side_3, text="Qwerty", variable=keyboard_lay, value=1, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black")
azerty_keyboard = tk.Radiobutton(side_3, text="Azerty", variable=keyboard_lay, value=2, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black", state=tk.DISABLED)
arabic_keyboard = tk.Radiobutton(side_3, text="Arabic (102)", variable=keyboard_lay, value=3, font=(
    "Caviar Dreams Bold", "10", "bold"), fg="white", bg="#080808", selectcolor="black", state=tk.DISABLED)
qwerty_keyboard.pack(anchor=tk.W, padx=10)
azerty_keyboard.pack(anchor=tk.W, padx=10)
arabic_keyboard.pack(anchor=tk.W, padx=10)

results_btn = tk.Label(bottom_side, text="Results", font=(
    "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808")
about_btn = tk.Label(bottom_side, text="About", font=(
    "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808")
reset_btn = tk.Label(bottom_side, text="Reset", font=(
    "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808")
save_btn = tk.Label(bottom_side, text="Save", font=(
    "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808")
quit_btn = tk.Label(bottom_side, text="Quit", font=(
    "Caviar Dreams Bold", "10", "bold underline"), fg="white", bg="#080808")

results_btn.place(relx=0, rely=.0, relheight=1, relwidth=.20)
about_btn.place(relx=.20, rely=.0, relheight=1, relwidth=.20)
reset_btn.place(relx=.40, rely=.0, relheight=1, relwidth=.20)
save_btn.place(relx=.60, rely=.0, relheight=1, relwidth=.20)
quit_btn.place(relx=.80, rely=.0, relheight=1, relwidth=.20)

about_btn.bind("<1>", lambda key: show_about())
reset_btn.bind("<1>", lambda key: reset_settings())
save_btn.bind("<1>", lambda key: save_settings())
quit_btn.bind("<1>", lambda key: root.after(1000, quit_settings))

show_settings()

root.mainloop()
