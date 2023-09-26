import streamlit as st
from datetime import datetime
from pytz import timezone

# ################################################################
st.set_page_config(page_title="My work tracking app!", 
                   page_icon='🎉')

# ################################################################

placeholder = st.empty()

def callback():
    st.session_state["input_form_clicked"] = True

if "input_form_clicked" not in st.session_state:
    st.session_state["input_form_clicked"] = False
    
if not st.session_state["input_form_clicked"]:
    with placeholder.form("input_form"):
        htp5="https://lh3.googleusercontent.com/pw/AIL4fc-PpqW403juiRdL0TilMr8xF0tXLQgiYvB7TaAktqjOfs1FIlOYwhkOudAqv4sRhXpB8dIcLp6Q9PwDbZpA-Vk10EWCYmpcP0_-980sVr5Pjt2NORzSb7976tQZ2vukEzzffuGwaf9ABz9dz36veiOfJQ=w2002-h1502-s-no"
        st.image(htp5, width=300)
        st.title("Let's track the time I leave the office!")
        
        response_dropdown = ('Yay!', 'Fantastic!')
        
        a1 = st.selectbox('Have you left the office?',
                            response_dropdown)
    
        submitted = st.form_submit_button("Yes!", on_click=callback)
          
       
        st.write("Made with 💚 by Amine in London!")
        
        if st.session_state["input_form_clicked"]:
            placeholder.empty()
            
if st.session_state["input_form_clicked"]:
    # with placeholder.form("new_form"):
    htp5="https://lh3.googleusercontent.com/pw/AIL4fc-u_AzKi0MTjL8-EAWJBNjO62Nlk3H5T9NTbJw0eJXsOkqDuZe7pTyhU6mWzmHMbTCnHEjU6MotCLRsc5PNGCJ8KbP83ehff-nQ6CzqIwl6J3Q8iviyIsQSKDRzfLYgLqHyCZdUmnORJKPaf4D-N-vzgw=w2002-h1502-s-no"
    st.image(htp5, width=300)
    # time = datetime.now().astimezone(timezone('Europe/UK'))
    # st.write(f"You left at {time} UTC time")
        
