def say_myself(name, old, man=True):
    print("My name is %s." % name)
    print("My age id %d." % old)

    if man:
        print("Male.")
    else:
        print("Female.")

say_myself("Jun", 25, False)