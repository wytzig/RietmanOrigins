# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rietman = Character("Ronnie")
define shadow_man = Character("Shadow")
define buyer_kalimero = Character("Kalimero")
define buyer_drake = Character("Drake")
define leib_weissman = Character("Leib Weissman")
define terrorists = Character("Pieter and Mohammed")
define spa_girl1 = Character("Ivanka")
define spa_girl2 = Character("Johanna")

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
    show rietman_serious1 at truecenter, Transform(zoom=1.5)

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
    show y_rietman_bar_fullbody at truecenter

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

    show drake at linker_onderhoek, Transform(zoom=1.5)
    buyer_drake "Ronnie? Who are you talking to?"
    hide drake

    show blackies
    show y_rietman_bar_fullbody at Transform(xalign=0.0, yalign=1.0)
    shadow_man "The painting remembers, Rietman. And so do I."

    scene bg painting
    hide y_rietman_bar

    rietman "You see, gentlemen, this painting isn’t just a piece of art."
    rietman "It’s alive. And it whispers in the night."


    show drake at right
    show kalimero at linker_onderhoek
    buyer_kalimero "Wait, are you saying—?"

    hide blackies
    show drake at rechter_onderhoek, Transform(zoom=2.0)
    show rietman_cool at linker_onderhoek
    show blackies_peniskoker at truecenter, Transform(zoom=2)
    shadow_man "Tell them, Ronnie. Tell them how you became a liquidator. A legend. A man feared in whispers."

    rietman "A master hustler, a dealmaker, a liquidator of both assets and... problems."
    rietman "I rememberecd Leibmanns words as they were still resonating with me.."
    rietman "All those moments go I...."
    "....."
    "....."
    "I.."
    show kalimero
    buyer_kalimero "Tell us Rietman!"
    hide kalimero
    show rietman_serious1 at linker_onderhoek
    hide rietman_cool
    rietman "I sold them"
    "..." with vpunch
    buyer_drake "you sold who? "
    rietman "them blackies"
    "..." with vpunch
    rietman "it was not my proudest moment, but hearing their voices made me mad. "
    rietman "then I got a call from within to find and meet up with leib weissman again"
    rietman "I remember it like it was yesterday.."

    show bg old_ship
    hide blackies_peniskoker
    hide drake
    rietman "aye, you there!"
    leib_weissman "... huh? me? what's happening grandpa?"
    rietman "oy voy! I am no grandpa but the one and only Ronnie R Rietman, .."
    rietman "trader... hustler..."
    "Leib weissman give a stare while ronny introduces him"
    "Like he already knows what Ronnie will say, long before he would even say it."
    ".. but at one moment"
    "oy voy! " with vpunch
    rietman "So here I have a proposition for you leib"
    leib_weissman "oh? lets hear of it"
    rietman "yes yes, since a couple of months since I have seen you fight off those drunkards in the bar, I have been seeting these...."
    rietman "these..."
    leib_weissman "?"
    rietman "these blackies."
    leib_weissman "...." with vpunch
    rietman "and I would like to sell them"
    leib_weissman "....." with vpunch
    "really?... did rietman really try to..."
    leib_weissman "I will give you 6,5 sheckles old hustler!"
    "the sheckles were really valuable"
    "the king just announched a party and Ronnie knew that if he could get in the party, he would have the best change to meet merchant from all over the barony"
    rietman "we have a deal"

    "and so it began, Rietman would bring first the 2 'blackies' - as he would often call them, from his warehouse where he had stored the painting to the harbor where an eager youngh Leib would await them to put them on his newest ships. "
    "the men... or evil sprits were promised lands of work, gold, fame and woman. But would often arrive in the new land not as men, but as animals"
    "rietman prospered, but one day, leib was missing"
    "it seemed that all mention of his name did not bring no meaning to the people anymore"
    "but ronnie knew, he understood that his jewish hero would be sailing with them, finding a fountain in the new world and discover the power of eternal youth. "
    "if Rietman would be young again.. oh wat would he do"

    show y_rietman_bar

    "our yough Rietman, as brave, innocent of a trader as you could get it. Balls deep in shady deals"

    hide y_rietman_bar

    show drake
    buyer_drake "And what about the ‘sex master’ part?"

    show rietman_serious_body
    rietman "Ah, that story... That story costs 500 golden ducats."

    menu:
        "Pay 500 golden ducats":
            jump sauna_story
        "Refuse to pay":
            rietman "Urghh."
            return

label sauna_story:

    scene bg finnish_sauna
    show young_rietman at truecenter

    rietman "Ah, the sauna on nude day... A place of warmth, steam, and opportunity."
    "The air was thick with mist, laughter, and the occasional flirtatious glance."
    "Young Rietman stepped inside, towel loosely draped over his shoulder, eyes scanning the scene."

    show spa_girl1 at rechter_onderhoek, Transform(zoom=1.5), Position(yanchor=1.0, ypos=0.75)
    spa_girl1 "Oh my, a new face! Welcome, traveler."
    show spa_girl2 at linker_onderhoek, Transform(zoom=1.5), Position(yanchor=1.0, ypos=0.75)
    spa_girl2 "You look weary, are you okay handsome?!"
    rietman "Ladies, please, no need for introductions. I am but a humble merchant, seeking relaxation."
    "The women giggled, their eyes full of curiosity."

    # More steamy interactions can follow...

    return