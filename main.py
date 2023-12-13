from Question import Question

#question prompts in an array
question_prompts = [
    "Where is Mango Sticky Rice originally from?\n(a) Vietnam\n(b) Japan\n(c) Thailand\n(d) Cambodia\n\n",
    "Where is Sticky Toffee Pudding originally from?\n(a) Spain\n(b) Australia\n(c) Germany\n(d) Britain\n\n",
    "Where is Tanghulu originally from?\n(a) China\n(b) Japan\n(c) Korea\n(d) Taiwan\n\n",
    "Where are Crepes originally from?\n(a) France\n(b) Italy\n(c) Spain\n(d) Germany\n\n",
    "Where is Knafeh originally from?\n(a) Egypt\n(b) Palestine\n(c) Lebanon\n(d) Qatar\n\n",
    "Where is Bungeoppang originally from?\n(a) Korea\n(b) Taiwan\n(c) Singapore\n(d) Thailand\n\n",
    "Where is Basbousa originally from?\n(a) Kuwait\n(b) Nigeria\n(c) Morocco\n(d) Egypt\n\n",
    "Where is Jalebi originally from?\n(a) Afghanistan\n(b) Iran\n(c) India\n(d) Nepal\n\n",
    "Where are Brigadeiros originally from?\n(a) Brazil\n(b) Argentina\n(c) Peru\n(d) Portugal\n\n",
    "Where is Halo Halo originally from?\n(a) Guam\n(b) Philippines\n(c) Indonesia\n(d) New Zealand\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
]




#algorithm to run test
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print(str(score) + "/" + str(len(questions)) + " correct!!! Hope you're not hungry now :]")

run_test(questions)


