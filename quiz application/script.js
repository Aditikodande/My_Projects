const quizData = [
    {
        question: "What is the capital of France?",
        options: ["Berlin", "Paris", "Madrid", "Rome"],
        correctAnswer: 1
    },
    {
        question: "Which planet is known as the Red Planet?",
        options: ["Mars", "Earth", "Venus", "Jupiter"],
        correctAnswer: 0
    },
    {
        question: "Who wrote 'Romeo and Juliet'?",
        options: ["William Shakespeare", "Charles Dickens ", "Mark Twain", "Jane Austen"],
        correctAnswer: 0
    },
    {
        question: "What is the largest ocean on Earth?",
        options: ["Atlantic", "Indian", "Pacific", "Southern"],
        correctAnswer: 2
    }
];

let currentQuestionIndex = 0;
let score = 0;

function loadQuestion() {
    const questionData = quizData[currentQuestionIndex];
    document.getElementById("question").textContent = questionData.question;
    
    const options = document.querySelectorAll(".option");
    options.forEach((option, index) => {
        option.textContent = questionData.options[index];
        option.disabled = false; // Re-enable buttons when loading a new question
    });

    document.getElementById("next-button").style.display = "none"; // Hide Next button until answer is selected
}

function answerQuestion(index) {
    const questionData = quizData[currentQuestionIndex];
    
    if (index === questionData.correctAnswer) {
        score++;
    }

    // Disable all options after answering
    const options = document.querySelectorAll(".option");
    options.forEach(option => option.disabled = true);

    // Show the "Next Question" button
    document.getElementById("next-button").style.display = "block";
}

function nextQuestion() {
    currentQuestionIndex++;
    
    if (currentQuestionIndex < quizData.length) {
        loadQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById("quiz-container").style.display = "none";
    document.getElementById("result-container").style.display = "block";
    document.getElementById("score").textContent = score + " / " + quizData.length;
}

function restartQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    document.getElementById("quiz-container").style.display = "block";
    document.getElementById("result-container").style.display = "none";
    loadQuestion();
}

// Initialize quiz
loadQuestion();
