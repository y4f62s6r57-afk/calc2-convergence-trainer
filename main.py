
methods = (
    "Geometric", "p-series", "Divergence", "Integral",
    "Comparison", "Alternating", "Ratio", "Root")


results = (
    "Converges absolutely", "Converges conditionally",
    "Diverges", "Test is inconclusive")


questions = [
    {
        "series": "sum (1/2)^n",
        "hint": "Look for a constant common ratio.",
        "method": 1,
        "result": 1,
        "explanation": "The common ratio is 1/2. Its absolute value is less than 1."
    },
    {
        "series": "sum 2^n",
        "hint": "Look for a constant common ratio.",
        "method": 1,
        "result": 3,
        "explanation": "The common ratio is 2, so the terms do not go to zero."
    },
    {
        "series": "sum 1/n^2",
        "hint": "Look at the power of n in the denominator.",
        "method": 2,
        "result": 1,
        "explanation": "This is a p-series with p = 2. It converges because p > 1."
    },
    {
        "series": "sum 1/n",
        "hint": "Use the rule for a sum of 1/n^p.",
        "method": 2,
        "result": 3,
        "explanation": "Here p = 1. A p-series converges only when p > 1."
    },
    {
        "series": "sum n/(n+1)",
        "hint": "Check whether the terms go to zero.",
        "method": 3,
        "result": 3,
        "explanation": "The terms go to 1. Since they do not go to zero, the series diverges."
    },
    {
        "series": "sum 1/n",
        "hint": "Use only the test that checks whether the terms go to zero.",
        "method": 3,
        "result": 4,
        "explanation": "The terms go to zero, so this test is inconclusive. The series itself diverges."
    },
    {
        "series": "sum 1/(n*(ln(n))^2), starting at n=2",
        "hint": "Use the improper integral of the term formula.",
        "method": 4,
        "result": 1,
        "explanation": "The function is positive, continuous, and decreasing for x >= 2. "
                       "Using u = ln(x) gives a finite integral of 1/u^2."
    },
    {
        "series": "sum 1/(n^2+1)",
        "hint": "Compare the terms directly with 1/n^2.",
        "method": 5,
        "result": 1,
        "explanation": "The terms are positive and smaller than 1/n^2, which gives a convergent series."
    },
    {
        "series": "sum (-1)^(n+1)/n",
        "hint": "Check the alternating terms, then check the absolute values.",
        "method": 6,
        "result": 2,
        "explanation": "The magnitudes decrease to zero, but the absolute-value series is harmonic and diverges."
    },
    {
        "series": "sum 3^n/n!",
        "hint": "Divide the next term by the current term.",
        "method": 7,
        "result": 1,
        "explanation": "The absolute ratio is 3/(n+1). Its limit is 0, which is less than 1."
    },
    {
        "series": "sum (n/(2*n+1))^n",
        "hint": "Take the nth root of the absolute value of the term.",
        "method": 8,
        "result": 1,
        "explanation": "The nth root is n/(2*n+1). Its limit is 1/2, which is less than 1."
    }
]


def get_number(prompt, maximum):
    while True:
        try:
            number = int(input(prompt))
            if 1 <= number <= maximum:
                return number
            print("Enter a number from 1 to", maximum)
        except ValueError:
            print("Please enter a whole number.")


def show_options(options):
    number = 1
    for option in options:
        print(number, "-", option)
        number = number + 1


def ask_question(question):
    print("\nSeries:", question["series"])
    print("Hint:", question["hint"])

    print("\nWhich test should you use?")
    show_options(methods)
    method_answer = get_number("Choice: ", len(methods))

    print("\nWhat does the requested test tell you?")
    show_options(results)
    result_answer = get_number("Choice: ", len(results))

    points = 0
    if method_answer == question["method"]:
        print("Method: correct!")
        points = points + 1
    else:
        print("Correct method:", methods[question["method"] - 1])

    if result_answer == question["result"]:
        print("Conclusion: correct!")
        points = points + 1
    else:
        print("Correct conclusion:", results[question["result"] - 1])

    print("Explanation:", question["explanation"])
    return points


class Quiz:
    def run(self, question_list, missed, scores, title):
        if len(question_list) == 0:
            print("\nThere are no questions to practice here yet.")
            return

        print("\n" + title)
        print("Questions available:", len(question_list))
        count = get_number("How many questions? ", len(question_list))

        round_questions = []
        for index in range(count):
            round_questions.append(question_list[index])

        total = 0
        number = 1
        for question in round_questions:
            print("\nQuestion", number, "of", count)
            points = ask_question(question)
            total = total + points

            if points == 2:
                if question in missed:
                    missed.remove(question)
            else:
                if question not in missed:
                    missed.append(question)

            print("Running score:", total, "/", number * 2)
            number = number + 1

        possible = count * 2
        percentage = total / possible * 100
        print("\nRound score:", total, "/", possible)
        print("Percentage:", round(percentage, 1), "%")
        print("Questions left to retry:", len(missed))

        score = {"title": title, "earned": total, "possible": possible}
        scores.append(score)


def show_guide():
    print("\nQUICK TEST GUIDE")
    print("Geometric: Find the common ratio. A nonzero geometric series converges if |r| < 1.")
    print("p-series: For a sum of 1/n^p, it converges if p > 1.")
    print("Divergence: If the terms do not approach zero, the series diverges.")
    print("Integral: Use a positive, continuous, decreasing function that matches the terms.")
    print("Comparison: Compare with a known series using an inequality.")
    print("Alternating: Check that the magnitudes decrease to zero.")
    print("Ratio: Find the limit of the absolute ratio of consecutive terms.")
    print("Root: Find the limit of the nth root of the absolute term.")
    print("Ratio and root: Below 1 means absolute convergence. Above 1 means divergence.")
    print("A ratio or root limit of 1 means the test is inconclusive.")



def show_scores(scores):
    if len(scores) == 0:
        print("\nNo completed rounds yet.")
        return

    print("\nSCORES FOR THIS RUN")
    total_earned = 0
    total_possible = 0

    for score in scores:
        print(score["title"], "-", score["earned"], "/", score["possible"])
        total_earned = total_earned + score["earned"]
        total_possible = total_possible + score["possible"]

    print("Overall:", total_earned, "/", total_possible)


def main():
    quiz = Quiz()
    missed = []
    scores = []
    running = True

    print("CALC 2 CONVERGENCE TEST TRAINER")
    print("Each question is worth 2 points: one for the test and one for the result.")
    print("Assume each series starts at n=1 unless the question says otherwise.")

    while running:
        print("\n1. Mixed quiz")
        print("2. Practice by topic")
        print("3. Retry missed questions")
        print("4. Short test guide")
        print("5. Quit")
        choice = get_number("Menu choice: ", 5)

        if choice == 1:
            quiz.run(questions, missed, scores, "Mixed quiz")
            show_scores(scores)
        elif choice == 2:
            print("\nPick a topic.")
            show_options(methods)
            topic = get_number("Topic: ", len(methods))

            topic_questions = []
            for question in questions:
                if question["method"] == topic:
                    topic_questions.append(question)

            quiz.run(topic_questions, missed, scores, methods[topic - 1])
            show_scores(scores)
        elif choice == 3:
            quiz.run(missed, missed, scores, "Retry")
            show_scores(scores)
        elif choice == 4:
            show_guide()
        else:
            running = False

    print("\nGoodbye!")


main()