'''Python Functions - Lists'''


letters_add = ["a", "b", "c"]
# Add
letters_add.append("d")  #  add to the end
letters_add.insert(0, "-")  #  add to the beginning
print(letters_add)


letters_remove = ["a", "b", "c", "d", "e"]
# Remove
letters_remove.pop()  # remove from the last index
letters_remove.remove("b")  #  removes the first occurence of the arg
del letters_remove[0:1]  #  deletes the objects in the index range
letters_remove.clear()  #  clears the list
print(letters_remove)
