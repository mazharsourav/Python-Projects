print("Welcome to the Ancient Egypt Mystery Story!")
print("Fill in the blanks to uncover a haunting tale...\n")

# Collect inputs
name = input("Enter your name: ")
object_found = input("Name an object (e.g., amulet, scroll): ")
animal = input("Name an animal (e.g., cat, snake): ")
adjective = input("Enter an adjective (e.g., dusty, glowing): ")
verb_past = input("Enter a verb (past tense, e.g., ran, screamed): ")
emotion = input("Enter an emotion (e.g., fear, awe): ")

# First story
story = f"""
Deep beneath the sands of Egypt, explorer {name} brushed away centuries of dust from a hidden chamber wall.
Inside, carved in faded hieroglyphs, was a warning: "Do not disturb the Tomb of Shadows."
Ignoring the ancient message, {name} stepped inside and discovered a {adjective} {object_found} resting on a stone altar.
Suddenly, the air grew cold. A faint unknown sound echoed through the chamber as the spirit of an ancient {animal} slithered into view.
{name} {verb_past} back, heart pounding with {emotion}, but it was too late—the curse had already begun.
Some say the explorer was never seen again. Others whisper that on certain nights, the {animal}'s shadow still guards the tomb.
"""

print(story)


choice = input("Dare you return? (yes/no) ").strip().lower()

if choice == "yes":
    continuation = f"""
With trembling hands, {name} stepped forward once more. The {object_found} in their bag began to pulse softly,
as if alive. Torches lit themselves on the wall, revealing a hidden staircase spiraling downward.
At the bottom, a grand chamber opened—a throne room untouched by time. Seated on a cracked obsidian throne was
a statue of the {animal}, eyes glowing {adjective} in the dim light. As {name} approached, the statue turned its head.
A voice filled the room: "You carry the {object_found}. You have awakened the Guardian. You cannot leave...
until your purpose is fulfilled." And so began {name}'s second journey—one not of discovery, but of survival.

The sands above shifted once more, sealing the entrance... for now.
"""
    print(continuation)
else:
    ending = f"""
Wise choice.

Most who disturb what sleeps beneath the sand do not return to tell the tale.
But on silent nights, some still hear the whisper of a {animal}... and feel a cold breeze that carries the scent of {adjective} air.
Perhaps the curse waits for someone else.

Farewell.
"""
    print(ending)
