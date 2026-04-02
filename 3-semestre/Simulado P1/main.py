from quiz import Quiz

iniciar = input("Deseja iniciar o quiz? 1(sim) 0(nao)")

if iniciar == "1":
    meu_quiz = Quiz()
    meu_quiz.iniciarQuiz()
else:
    print("quiz cancelado. adeus!")
