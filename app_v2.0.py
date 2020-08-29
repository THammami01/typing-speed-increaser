import tkinter as tk
# import tkinter.messagebox
import shelve
from random import choice

settings_db = shelve.open("settings")
try:
    if settings_db["first_time"]:
        pass
except KeyError:
    __import__("os").system("python setting_v2.0.py")
    exit()

# Varibales for settings
program_just_started = True
current_theme, themes = None, None
nbr_minutes, in_chars, default_text = None, None, None


def generate_new_text():
    global default_text, avg, nbr_words_in_text
    default_text = choice(settings_db["stored_texts"])
    text_to_type.delete("0.0", tk.END)
    text_to_type.insert("0.0", default_text)
    avg = [len(word) for word in default_text.split()]
    nbr_words_in_text = len(avg)
    avg = sum(avg)//nbr_words_in_text
    remaining_chars.configure(text="Remaining\n" + str(len(default_text) if in_chars else nbr_words_in_text))
    total_chars.configure(text="Total\n" + str(len(default_text) if in_chars else nbr_words_in_text))


def check_changes_in_db():
    global nbr_minutes, in_chars, default_text, themes, current_theme

    nbr_minutes = settings_db["default_and_saved"]["minutes"][1]
    if nbr_minutes == 4:
        nbr_minutes += 1

    if settings_db["default_and_saved"]["unit"][1] == 1:
        in_chars = False  # True if WPM, False if CPM
    else:
        in_chars = True

    if settings_db["default_and_saved"]["theme"][1] == 1:
        current_theme = "light_theme"
    elif settings_db["default_and_saved"]["theme"][1] == 2:
        current_theme = "dark_theme"
    elif settings_db["default_and_saved"]["theme"][1] == 3:
        current_theme = "high_contrast"

    themes = settings_db["themes"]

    if settings_db["custom_text"] != "" and settings_db["default_and_saved"]["text"][1] == 2:
        default_text = settings_db["custom_text"]
    else:
        default_text = choice(settings_db["stored_texts"])


def start_again():

    global started, last_pos, chars, m, s, flash_time, completed_correctly, flash_mode

    start_label.unbind("<1>")
    start_label["text"] = "Start when you're ready :)"
    start_label["font"] = "Caviar Dreams Bold", "10", "bold"

    change_settings.unbind("<1>")
    change_settings["text"] = "Change Text ?"
    change_settings.bind("<1>", lambda key: generate_new_text())

    typed_text.delete("0.0", tk.END)

    passed_time["text"] = "Time\n00:00"
    typed_chars["text"] = "Typed\n0"
    remaining_chars["text"] = "Remaining\n" + \
        str(len(default_text) if in_chars else nbr_words_in_text)
    total_chars["text"] = "Total\n" + \
        str(len(default_text) if in_chars else nbr_words_in_text)
    typing_speed["text"] = "Typing Speed\n0 WPM"

    text_to_type.tag_remove("correct", "0.0", tk.END)
    text_to_type.tag_remove("wrong", "0.0", tk.END)

    last_pos = 0
    chars = 0  # This is for the typing speed only
    flash_time = False
    m, s = 0, -1
    started = False
    flash_mode = False

    start_typing()


def start_typing():  # prevent cheating and see if user started typing or not
    global started
    typed_text.focus()
    if not started:
        if typed_text.get("0.0", tk.END).strip():
            started = True
        typing_speed.after(100, start_typing)
    else:
        start_label.unbind("<1>")
        start_label["text"] = "Typing.."
        start_label["font"] = "Caviar Dreams Bold", "10", "bold"

        change_settings.unbind("<1>")
        change_settings["text"] = "Reset"
        change_settings.bind("<1>", lambda key: start_again())

        root.bind("<Key>", lambda key: add_one_to_chars())

        update_tags()


def add_one_to_chars():
    global chars
    chars += 1


def update_time():
    global m, s, flash_time, started, settings_db, completed_correctly, flash_mode, program_just_started

    def restart_program():
        root.destroy()
        __import__("os").system("python app_v2.0.py")

    if settings_db["changes_exist"]:
        settings_db["changes_exist"] = False

        if not program_just_started:
            start_label["text"] = "Changes detected, restart ?"
            start_label["font"] = "Caviar Dreams Bold", "10", "bold underline"
            start_label.bind("<1>", lambda key: restart_program())
        else:
            program_just_started = False

    if started and m == nbr_minutes or completed_correctly:
        start_label["text"] = "Start typing again ?"
        start_label["font"] = "Caviar Dreams Bold", "10", "bold underline"
        start_label.bind("<1>", lambda key: start_again())
        # change_settings.place(
        #     relx=.4, rely=.8, relheight=.19, relwidth=.29)
        change_settings.unbind("<1>")
        change_settings["text"] = "Change Text ?"
        change_settings.bind("<1>", lambda key: generate_new_text())
        started = False
        completed_correctly = False
        flash_mode = True

    elif (not started) and m == nbr_minutes or flash_mode:
        if s == -1: s = 0
        if flash_time:
            passed_time["text"] = f"Time\n{m:02}:{s:02}"
        else:
            passed_time["text"] = f"Time\n"
        flash_time = not flash_time

    elif started and m != nbr_minutes:
        if typed_text.get("0.0", tk.END).strip(" \n") == default_text:
            completed_correctly = True
        else:
            if s == 59:
                m += 1
                s = 0
            else:
                s += 1
            passed_time["text"] = f"Time\n{m:02}:{s:02}"
    passed_time.after(1000, update_time)


def update_tags():
    global last_pos

    text_to_type.delete("0.0", tk.END)
    text_to_type.insert("0.0", default_text)
    tt = len(typed_text.get("0.0", tk.END)) - 1  # typed text :D

    # text_to_type.tag_remove("correct", "0.0")
    # text_to_type.tag_remove("wrong", "0.0")

    if default_text.startswith(typed_text.get("0.0", tk.END).strip("\n")):
        text_to_type.tag_add("correct", "1.0", "1." + str(tt))
        last_pos = tt
    else:
        text_to_type.tag_add("correct", "1.0", "1." + str(last_pos))
        text_to_type.tag_add("wrong", "1." + str(last_pos), "1." + str(tt))

    if in_chars:
        typed_chars["text"] = "Typed\n" + str(tt)
        remaining_chars["text"] = "Remaining\n" + str(len(default_text) - tt)
        try:
            typing_speed["text"] = "Typing Speed\n" + \
                str(chars*60 // (m*60 + s)) + " CPM"
        except ZeroDivisionError:
            pass
    else:
        tw = len(typed_text.get("0.0", tk.END).split())  # typed words
        typed_chars["text"] = "Typed\n" + str(tw)
        remaining_chars["text"] = "Remaining\n" + str(nbr_words_in_text - tw)
        try:
            typing_speed["text"] = "Typing Speed\n" + \
                str(chars//6 * 60 // (m*60 + s)) + " WPM"  # str(chars//avg * 60 // (m*60 + s)) + " WPM"  
                # 6 characters is the average
        except ZeroDivisionError:
            pass

    if started:
        text_to_type.after(100, update_tags)


check_changes_in_db()
root = tk.Tk()
root.title("TSI")
root.iconbitmap(r"OBlogoIcon.ico")
root.config(bg=themes[current_theme]["root"]["bg"])
root.geometry("0x0+450+220")
root.minsize(660, 440)
# root.maxsize(900, 600)

root.focus_force()
# Used varibales
avg = [len(word) for word in default_text.split()]
nbr_words_in_text = len(avg)
avg = sum(avg)//nbr_words_in_text
last_pos = 0
chars = 0  # This is for the typing speed only
m, s = 0, -1
flash_time = True
started = False
completed_correctly = False
flash_mode = False

welcome_text = tk.Label(
    root, text="Typing Speed Increaser", width=600, pady=10, font=(
        "Caviar Dreams Bold", "16", "bold"), fg=themes[current_theme]["welcome_text"]["fg"], bg=themes[current_theme]["welcome_text"]["bg"], relief=tk.RIDGE, borderwidth=2)
welcome_text.pack(side=tk.TOP, fill=tk.BOTH,
                  anchor=tk.CENTER, padx=10, pady=10)

show_text_frame = tk.Frame(root, bg=themes[current_theme]["show_text_frame"]["bg"], width=600)
show_text_frame.pack(side=tk.TOP, fill=tk.BOTH,
                     anchor=tk.CENTER, expand=True, padx=10, pady=10)

typed_text = tk.Text(show_text_frame, padx=5, pady=5, insertbackground=themes[current_theme]["typed_text"]["insert_bg"], font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["typed_text"]["fg"], bg=themes[current_theme]["typed_text"]["bg"], wrap=tk.WORD, relief=tk.RIDGE, borderwidth=2)

text_to_type = tk.Text(show_text_frame, padx=5, pady=5, selectbackground=themes[current_theme]["typed_text"]["insert_bg"], insertbackground=themes[current_theme]["typed_text"]["insert_bg"], font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["text_to_type"]["fg"], bg=themes[current_theme]["text_to_type"]["bg"], wrap=tk.WORD, relief=tk.RIDGE, borderwidth=2)
text_to_type.insert("0.0", default_text)
text_to_type.tag_add("correct", "1.0", "1.0")
text_to_type.tag_config("correct", foreground=themes[current_theme]["tag_correct"]["fg"], background=themes[current_theme]["tag_correct"]["bg"])
text_to_type.tag_add("wrong", "1.0", "1.0")
text_to_type.tag_config("wrong", foreground=themes[current_theme]["tag_wrong"]["fg"], background=themes[current_theme]["tag_wrong"]["bg"])

passed_time = tk.Label(show_text_frame, text="Time\n00:00", font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["passed_time"]["fg"], bg=themes[current_theme]["passed_time"]["bg"], relief=tk.RIDGE, borderwidth=2)
typed_chars = tk.Label(show_text_frame, text="Typed\n0", font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["typed_chars"]["fg"], bg=themes[current_theme]["typed_chars"]["bg"], relief=tk.RIDGE, borderwidth=2)
remaining_chars = tk.Label(show_text_frame, text="Remaining\n" + str(len(default_text) if in_chars else nbr_words_in_text), font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["remaining_chars"]["fg"], bg=themes[current_theme]["remaining_chars"]["bg"], relief=tk.RIDGE, borderwidth=2)
total_chars = tk.Label(show_text_frame, text="Total\n" + str(len(default_text) if in_chars else nbr_words_in_text), font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["total_chars"]["fg"], bg=themes[current_theme]["total_chars"]["bg"], relief=tk.RIDGE, borderwidth=2)
typing_speed = tk.Label(show_text_frame, text="Typing Speed\n0 CPM" if in_chars else "Typing Speed\n0 WPM", font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["typing_speed"]["fg"], bg=themes[current_theme]["typing_speed"]["bg"], relief=tk.RIDGE, borderwidth=2)

start_label = tk.Label(show_text_frame, text="Start when you're ready :)", font=(
    "Caviar Dreams Bold", "10", "bold"), fg=themes[current_theme]["start_label"]["fg"], bg=themes[current_theme]["start_label"]["bg"])

change_settings = tk.Label(show_text_frame, text="Change Text ?", font=(
    "Caviar Dreams Bold", "10", "bold underline"), fg=themes[current_theme]["change_settings"]["fg"], bg=themes[current_theme]["change_settings"]["bg"])
change_settings.bind("<1>", lambda key: generate_new_text())

typed_text.place(relx=.0, rely=.0, relheight=.39, relwidth=.8)
text_to_type.place(relx=.0, rely=.40, relheight=.39, relwidth=.8)

passed_time.place(relx=.81, rely=.0, relheight=.19, relwidth=.19)
typed_chars.place(relx=.81, rely=.2, relheight=.19, relwidth=.19)
remaining_chars.place(relx=.81, rely=.4, relheight=.19, relwidth=.19)
total_chars.place(relx=.81, rely=.6, relheight=.19, relwidth=.19)
typing_speed.place(relx=.81, rely=.8, relheight=.19, relwidth=.19)

start_label.place(relx=.1, rely=.8, relheight=.19, relwidth=.29)
change_settings.place(relx=.4, rely=.8, relheight=.19, relwidth=.29)

update_time()
start_typing()

root.mainloop()
