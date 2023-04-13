import streamlit as st
import json

def create_questions_form(json):
    html_form = '<div style="max-width: 600px;">'
    for i, q in enumerate(json):
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

json_data = [    {        "id": 708,        "question": "How can we redirect the output of one command to the another command?",        "description": None,        "answers": {            "answer_a": "Place the commands connected with pipes (|).",            "answer_b": "Use the Xargs command",            "answer_c": "Use the stdin and stdout",            "answer_d": "Use the numbers 1 and 2 for standart input(stdin) and standart output(stdout)",            "answer_e": "Both commands which include stdin and stdout",            "answer_f": None        },        "multiple_correct_answers": "false",        "correct_answers": {            "answer_a_correct": "true",            "answer_b_correct": "false",            "answer_c_correct": "false",            "answer_d_correct": "false",            "answer_e_correct": "false",            "answer_f_correct": "false"        },        "correct_answer": None,        "explanation": None,        "tip": None,        "tags": [            {                "name": "BASH"            },            {                "name": "Linux"            }        ],
        "category": "Linux",
        "difficulty": "Medium"
    }
]

create_questions_form(json_data)
