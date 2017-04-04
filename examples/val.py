import sys
sys.path.append("../")

def press(btn):
    if btn == "YES": app.setEntryValid("a")
    elif btn == "NO": app.setEntryInvalid("a")
    elif btn == "WAIT": app.setEntryWaitingValidation("a")

    if btn == "YES": app.setEntryValid("n")
    elif btn == "NO": app.setEntryInvalid("n")
    elif btn == "WAIT": app.setEntryWaitingValidation("n")

from appJar import gui

app=gui()
app.setBg("yellow")
app.addEntry("n")
app.addValidationEntry("a")
app.setEntryDefault("a", "--valid--")
app.addValidationEntry("b")
app.setEntryDefault("b", "--invalid--")
app.addValidationEntry("c")
app.setEntryDefault("c", "--waiting--")
app.setEntryMaxLength("a", 5)
app.addButtons(["YES", "NO", "WAIT"], press)

app.setEntryValid("a")
app.setEntryInvalid("b")
app.setEntryWaitingValidation("c")
app.setBg("orange")

app.go()
