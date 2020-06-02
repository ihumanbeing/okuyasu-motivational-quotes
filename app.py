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
    "The secret of getting ahead is getting started.",
    "Your limitation—it’s only your imagination.",
    "Live as if you were to die tomorrow. Learn as if you were to live forever.",
    "That which does not kill us makes us stronger.",
    "Be who you are and say what you feel, because those who mind don’t matter and those who matter don’t mind.",
    "We must not allow other people’s limited perceptions to define us.",
    "Do what you can, with what you have, where you are.",
    "Be yourself; everyone else is already taken.",
    "If you cannot do great things, do small things in a great way.",
    "Always forgive your enemies; nothing annoys them so much.",
    "The only true wisdom is knowing that you know nothing.",
    "A man who views the world the same at 50 as he did at 20 has wasted 30 years of his life.",
    "It takes a great deal of courage to stand up to your enemies, but even more to stand up to your friends.",
    

]

def motivate():

    toaster = ToastNotifier()
    toaster.show_toast("OI JOSUKE!",
    okuyasu.choice(quotes), icon_path="okuyasu.ico", duration=7, threaded=True)

    while toaster.notification_active(): time.sleep(0.1)
    time.sleep(3000)
    motivate()

motivate()
