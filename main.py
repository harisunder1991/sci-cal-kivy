import math
"asin": math.asin,
"acos": math.acos,
"atan": math.atan,
})
return env


def evaluate(self):
if not self.expr.strip():
return ""
try:
# Restrict builtins
result = eval(self.expr, {"__builtins__": {}}, self._build_env())
# Clean floats like 1.0 -> 1
if isinstance(result, float) and result.is_integer():
result = int(result)
return str(result)
except Exception:
return "Error"




class SciCalcApp(App):
display_text = StringProperty("0")
mode_label = StringProperty("DEG")
is_deg = BooleanProperty(True)


def __init__(self, **kwargs):
super().__init__(**kwargs)
self.state = CalcState()


def build(self):
return Builder.load_file("calculator.kv")


def on_button(self, token):
if token == "C":
self.state.clear()
self.display_text = "0"
return
if token == "⌫":
self.state.backspace()
self.display_text = self.state.expr or "0"
return
if token == "=":
val = self.state.evaluate()
self.display_text = val
# keep result as new expr if valid number
if val != "Error":
self.state.expr = val
return
self.state.append(token)
self.display_text = self.state.expr


def on_toggle_mode(self):
self.state.toggle_deg_rad()
self.is_deg = self.state.deg_mode
self.mode_label = "DEG" if self.state.deg_mode else "RAD"




if __name__ == "__main__":
SciCalcApp().run()
