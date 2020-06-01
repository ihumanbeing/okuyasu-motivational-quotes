from win10toast import ToastNotifier
import time
import random as okuyasu


quotes = [
    "Things start out as hopes and end up as habits.",
    "I love you the more in that I believe you had liked me for my own sake and for nothing else.",
    "But man is not made for defeat. A man can be destroyed but not defeated.",
    "When you reach the end of your rope, tie a knot in it and hang on.",
    "It is better to be feared than loved, if you cannot be both.",
    "The most difficult thing is the decision to act, the rest is merely tenacity. The fears are paper tigers. You can do anything you decide to do. You can act to change and control your life; and the procedure, the process is its own reward.",
    "Do not mind anything that anyone tells you about anyone else. Judge everyone and everything for yourself.",
    "The only journey is the one within.",
    "Life without love is like a tree without blossoms or fruit.",
    "Good judgment comes from experience, and a lot of that comes from bad judgment.",
    "If you cannot do great things, do small things in a great way.",
    "Permanence, perseverance and persistence in spite of all obstacles, discouragements, and impossibilities: It is this, that in all things distinguishes the strong soul from the weak.",
    "It is far better to be alone, than to be in bad company.",
    "Keep your face always toward the sunshine - and shadows will fall behind you.",
    "If opportunity doesn't knock, build a door.",
    "The secret of getting ahead is getting started."

]

def motivate():

    toaster = ToastNotifier()
    toaster.show_toast("OI JOSUKE!",
    okuyasu.choice(quotes), icon_path="okuyasu.ico", duration=7, threaded=True)

    while toaster.notification_active(): time.sleep(0.1)
    time.sleep(3000)
    motivate()

motivate()
