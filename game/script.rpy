# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rietman = Character("Ronnie")
define shadow_man = Character("Shadow")
define buyer_kalimero = Character("Kalimero")
define buyer_drake = Character("Drake")
define leib_weissman = Character("Leib Weissman")
define terrorists = Character("Pieter and Mohammed")

transform linker_bovenhoek:
    anchor (0.0, 0.0)
    xalign 0.0
    yalign 0.0

transform rechter_bovenhoek:
    anchor (1.0, 0.0)
    xalign 1.0
    yalign 0.0

transform linker_onderhoek:
    anchor (0.0, 1.0)
    xalign 0.0
    yalign 1.0

transform rechter_onderhoek:
    anchor (1.0, 1.0)
    xalign 1.0
    yalign 1.0

label start:

    scene bg painting
    show rietman_serious1 at truecenter

    rietman "Super amazing that you guys are all here."
    rietman "Today, we are here for a magical opportunity to own a fine piece of art, aye!"

    show kalimero at left

    show drake at Transform(zoom=1.5, xalign=1.0, yalign=1.0)
#     show drake at Transform(zoom=1.5)  # 1.5x the original size
#     show drake at right

    buyer_kalimero "You keep saying ‘magical,’ but we need to know—what’s so special about it?"
    buyer_drake "Yeah, why should we care?"

    show rietman_serious1

    rietman "Oh, my friends, you don’t just ‘care’ about this painting. This painting? It changes your life."
    rietman "But before we get into that, let me tell you something about how I got here."

    scene bg bar
    show y_rietman_bar at truecenter

    rietman "It all started in a little bar, back when no one believed in me."
    rietman "I was just a kid with a dream, a few coins, and a sharp tongue."

    buyer_kalimero "So, what happened?"

    rietman "A miracle happened. Or maybe just sheer luck."
    rietman "I was at the bar, looking for my first deal, when I met two drunks with more money than sense."

    show terrorists at left

    buyer_kalimero "And you hustled them?"

    rietman "No! Not at first. They thought I was a joke."
    "But then Leib Weissman walked in." with vpunch

    show leib at Transform(zoom=1.5, xalign=1.0)

    rietman "A legend, a force of nature. Some say he had divine connections."
    rietman "He looked at me, saw something, and whispered one word—'Trade.'"
    rietman "From that moment, things just started falling into place."

    scene bg shadow_realm
    show blackies at truecenter

    shadow_man "But fate isn’t free, Ronnie. You should know that better than anyone."

    rietman "What the—?! Blackies?"

    show drake at Transform(zoom=1.5, xalign=1.0, yalign=1.0)
    buyer_drake "Ronnie? Who are you talking to?"
    hide drake

    show blackies
    show y_rietman_bar at Transform(xalign=0.0, yalign=1.0)
    shadow_man "The painting remembers, Rietman. And so do I."

    scene bg painting

    show y_rietman_bar
    rietman "You see, gentlemen, this painting isn’t just a piece of art."
    rietman "It’s alive. And it whispers in the night."

    show drake at right
    buyer_kalimero "Wait, are you saying—?"

    hide blackies
    show blackies_peniskoker at rechter_onderhoek
    shadow_man "Tell them, Ronnie. Tell them how you became a liquidator. A legend. A man feared in whispers."

    rietman "A master hustler, a dealmaker, a liquidator of both assets and... problems."

    buyer_drake "And what about the ‘sex master’ part?"

    rietman "That, my friend, is a story for another day."

    # This ends the game.

    return
