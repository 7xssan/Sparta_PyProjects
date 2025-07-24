story1 = {
    "start": "once upon a time...",
    "middle": "the hero then...",
    "end": "and they lived happily ever after..."
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["start"])
print(story1["middle"])
print(story1["end"])
story1["character"] = "hasan"
print(story1)
print(f"The end. I hope you enjoyed the story about {story1["character"]}!")
