import streamlit as st

st.title("Interview Session")
st.text("This is a set of questions for this interview session")
fname = st.text_input("What is your first name?", "Enter name")

lname = st.text_input("What is your last name?", "Enter name")

status = st.radio("Select Gender: ", ('Male', 'Female')) 

# conditional statement to print 
if (status == 'Male'): 
     st.success("Male") 
else: 
     st.success("Female")

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Writing', 'Sports', 'Video Games', 'Others']) 
# print the selected hobby 
st.write("Your hobby is: ", hobby)

hobby = st.selectbox("Education: ", ['Secondary', 'Tertiery Bsc', 'Tertiery MSc', 'Others']) 

st.markdown("### Quick Qizz Session")
quest1 = st.selectbox("How many states in Nigeria? ", ['30', '25', '36', '46', 'Others']) 
q1 = int(quest1)
quest2 = st.selectbox("How many planets in our solar system? ", ['5', '9', '7', '8', 'Others']) 
q2 = int(quest2)
quest3 = st.number_input("What year did Nigeria gain independence?")
q3 = int(quest3)
quest4 = st.text_input("What is  12 + 5 - 2 (3+5) ?", "0")

counter=0
if(st.button("Submit")): 
     if quest1 == q1:
          counter+=1
     if quest2 == q2: 
          counter+=1
     if quest3 == q3: 
          counter+=1 
     if quest4 == "1": 
          counter+=1 
    perct = ((counter/4) * 100)     
    st.write("Thanks for participating. You got ", counter, " of 4 correctly, which is ",perct, "%")

