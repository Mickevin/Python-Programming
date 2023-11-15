from functions import executer_quiz, poser_question

questions = [
    "Combien de fois la France a-t-elle remporté la Coupe du monde de football ? ",
    "Quand Apple a-t-elle été fondée ? ",
    "Qui a fondé SpaceX ? "
]
reponses = [
    "2",
    "1976",
    "Elon Musk"
]


def executer_quiz():
    chances_restantes = 3
    for i in range(len(questions)):
        chances_restantes = poser_question(questions[i], reponses[i], chances_restantes)

executer_quiz()
