import streamlit as s

a = f"""
<h2 style="text-align:center;color:orangered;">CALCULATOR</h2>
"""

s.markdown(a, unsafe_allow_html=True)

with s.expander("See operations which can be performed here ..."):
  opr2='+ : Addition'
  opr3="- : Subtraction"
  opr4="* : Multiplication"
  opr5="/ : Division"
  opr6="//: Division (Returns integer value)"
  opr7="% : Modulo (Returns remainder)"
  opr8="**: To find Power"
    
  s.markdown(f"##### {opr2}")
  s.markdown(f"##### {opr3}")
  s.markdown(f"##### {opr4}")
  s.markdown(f"##### {opr5}")
  s.markdown(f"##### {opr6}")
  s.markdown(f"##### {opr7}")
  s.markdown(f"##### {opr8}")



s.markdown("<h4>Perform calcultions here</h4>", unsafe_allow_html=True)

b = s.text_input("Click Here")
# b=b.lower()

if len(b) == 0:
  s.warning("Enter the values")

elif b.isalnum():
  temp = 0
  for i in b:
    if i.isalpha():
      temp = 1
  if temp == 1:
    s.error("Enter Numbers And Opertators Only")
if b.isnumeric():
  s.success("")

if len(b) != 0:
  s.markdown("#### You have Entered")

  s.markdown(f"## {b}=")


def calculate(a):
  if len(a) == 0:
    # s.warning("Please enter values to be calculated and see answer here")
    return None
  if b.isalnum():
    temp = 0
    for i in b:
      if i.isalpha():
        temp = 1
    if temp == 1:
      return "handle"
  
  else:
    try:
      return eval(a)
    except(Exception) as e:
      return "a"


c = calculate(b)
if c == None:
  s.warning("Please enter values to be calculated and see answer here")
elif c == "handle":
  s.error("Math Error : Enter Number And Operators Only")
elif c=="a":
  s.error("Math Error")
else:
  s.markdown(f"## {c}")
