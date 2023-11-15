def poser_question(question, reponse, chances_restantes = 3):
    while chances_restantes > 0:
        reponse_utilisateur = input(question)
        if reponse_utilisateur.lower() == reponse.lower():
            print("Bonne réponse!")
            return chances_restantes
        else:
            chances_restantes -= 1
            print(f"Mauvaise réponse. Il vous reste {chances_restantes} chances.")
    return chances_restantes 

def executer_quiz():
    chances_restantes = 3
    for i in range(len(questions)):
        chances_restantes = poser_question(questions[i], reponses[i], chances_restantes)


