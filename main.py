import streamlit as st
import json
from utils.quizz_api import QuizApiClient, Question




quiz_client = QuizApiClient()
question_client = Question()
#headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

with open('test.json') as fs:
    questions = json.load(fs)



#method that desplays question after start exam button is pressed
def display_question(q):
    st.write(q['question'])
    for answer in q['answers'].items():
        if answer[1] != None:
            st.checkbox(label=str(answer[1]),key=str(answer[0]+answer[1]+str(q['id'])),label_visibility="visible")
        else:
            break

def main_menu():
    with st.sidebar:
        st.image("images/blog-image-16.png")
        st.title("Exam taking platform")
        choice = st.radio("Navigation",["User registration/login","Take exam"])
        return choice


#if choice == "User registration/login":
    
def user_registration_login():
    new_choice= st.radio("Navigation",["Login","Create Account"])
    if new_choice=="Login":
        st.title("Login into your account")
        type_of_user=st.radio("Select type of user",["Student","Teacher"]) 
        email = st.text_input(label="email_login",placeholder="Insert your email address",kwargs=None, disabled=False, label_visibility="hidden")
        password = st.text_input(label="password_login",placeholder="Insert your password here",kwargs=None, disabled=False, label_visibility="hidden",type="password")
    elif new_choice=="Create Account":
        st.title("Create a new account")
        firstname = st.text_input(label="firstname_create",placeholder="Insert your firstname",kwargs=None, disabled=False, label_visibility="hidden")
        lastname = st.text_input(label="lastname_create",placeholder="Insert your lastname",kwargs=None, disabled=False, label_visibility="hidden")
        email_create = st.text_input(label="email_create",placeholder="Insert your email address",kwargs=None, disabled=False, label_visibility="hidden")
        phone = st.text_input(label="phone_create",placeholder="Insert your phone number",kwargs=None, disabled=False, label_visibility="hidden")
        password_create = st.text_input(label="password_create",placeholder="Insert a password",kwargs=None, disabled=False, label_visibility="hidden",type="password")


def take_exam():
    select_topic=st.selectbox("Choose the exam",("linux","DevOps","Docker"))
    st.write('Once you start the exam you will have 10 minutes')
    if st.button(label='Start exam',key="StartExam"):
        st.write('Exam will start in 10 seconds')
        json_response= quiz_client.get_questions(category=select_topic, difficulty='Easy', limit=10)
        to_parse=json.loads(json_response, strict=True)
        #Created a dict with the correct answers after parsing the 
        dict_correct_answers = get_correct_answers(questions)
        create_questions_form(questions)


def main():
    choice = main_menu()
    if choice == "User registration/login":
        user_registration_login()
    elif choice == "Take exam":
        take_exam()


#creates the questions form, takes the json file and creates a HTML with questions and checkboxes for the answers
import json
import streamlit as st

def create_questions_form(json_data):
    html_form = '<div style="max-width: 600px;">'
    for i, q in enumerate(json_data):
        question_text = f'Question <span style="font-size: 24px; font-weight: bold;">{i+1}</span>: '
        question_text += f'<span style="font-weight: normal;">{q["question"]}</span>'
        if q.get("multiple_correct_answers", "false") == "true":
            question_text += '<span style="font-weight: normal;">(**Multiple answers)</span> '
        html_form += f'<h3>{question_text}</h3>'
        for a in q["answers"]:
            if q["answers"][a] is not None:
                html_form += f'<label><input type="checkbox" name="{a}" value="{q["answers"][a]}"> {q["answers"][a]}</label><br>'
        html_form += '<br>'
    html_form += '</div>'
    with st.form(key='my_form'):
        st.write(html_form, unsafe_allow_html=True)
        if st.button('Submit'):
            answerss = {}
            for q in json:
                answerss[q["id"]] = []
                for a in q["answers"]:
                    if q["answers"][a] is not None:
                        if a in st.session_state:
                            if st.session_state[a]:
                                answerss[q["id"]].append(q["answers"][a])
            st.write('Answers:', answerss)
            with open('answers.json', 'w') as f:
                json.dump(answerss, f)
            st.success('Answers saved to answers.json')

    return




#Creates a dictionary with the correct answers after parsing the json file 
#as the key it has the id of the question and the key is a list with the answer or answers
def get_correct_answers(json_data):
    correct_answers_dict = {}
    for question in json_data:
        id = question["id"]
        correct_answers = []
        for answer, is_correct in question["correct_answers"].items():
            if is_correct == "true":
                correct_answers.append(answer[:8])
        correct_answers_dict[str(id)] = correct_answers
    return correct_answers_dict

# Call your main function
if __name__ == "__main__":
    main()



        
                

        
    
    
