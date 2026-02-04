package com.example.quizapp.ui

import android.os.CountDownTimer
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.quizapp.data.QuestionRepository
import com.example.quizapp.model.Question
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch
import javax.inject.Inject

data class QuizState(
    val questions: List<Question> = emptyList(),
    val currentQuestionIndex: Int = 0,
    val userAnswers: Map<String, List<String>> = emptyMap(), // QuestionId -> Selected Option Keys (A, B, etc.)
    val timeLeftInMillis: Long = 0,
    val isQuizFinished: Boolean = false,
    val score: Int = 0,
    val totalQuestions: Int = 0,
    val passed: Boolean = false,
    val isLoading: Boolean = false,
    val error: String? = null
)

@HiltViewModel
class QuizViewModel @Inject constructor(
    private val repository: QuestionRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(QuizState())
    val uiState: StateFlow<QuizState> = _uiState.asStateFlow()

    private var timer: CountDownTimer? = null

    fun loadQuiz(questionCount: Int, timeLimitMinutes: Int) {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true, isQuizFinished = false, error = null, userAnswers = emptyMap(), currentQuestionIndex = 0) }
            try {
                val allQuestions = repository.getQuestions()
                val shuffledQuestions = allQuestions.shuffled().take(questionCount)
                
                _uiState.update { 
                    it.copy(
                        questions = shuffledQuestions, 
                        totalQuestions = shuffledQuestions.size,
                        isLoading = false
                    ) 
                }
                startTimer(timeLimitMinutes * 60 * 1000L)
            } catch (e: Exception) {
                _uiState.update { it.copy(isLoading = false, error = e.message) }
            }
        }
    }

    private fun startTimer(durationMillis: Long) {
        timer?.cancel()
        timer = object : CountDownTimer(durationMillis, 1000) {
            override fun onTick(millisUntilFinished: Long) {
                _uiState.update { it.copy(timeLeftInMillis = millisUntilFinished) }
            }

            override fun onFinish() {
                finishQuiz()
            }
        }.start()
    }

    fun submitAnswer(questionId: String, selectedOptionKey: String, isMultipleChoice: Boolean) {
        _uiState.update { state ->
            val currentAnswers = state.userAnswers[questionId] ?: emptyList()
            val newAnswers = if (isMultipleChoice) {
                if (currentAnswers.contains(selectedOptionKey)) {
                    currentAnswers - selectedOptionKey
                } else {
                    currentAnswers + selectedOptionKey
                }
            } else {
                listOf(selectedOptionKey)
            }
            state.copy(userAnswers = state.userAnswers + (questionId to newAnswers))
        }
    }

    fun nextQuestion() {
        _uiState.update { state ->
            if (state.currentQuestionIndex < state.questions.size - 1) {
                state.copy(currentQuestionIndex = state.currentQuestionIndex + 1)
            } else {
                state
            }
        }
    }
    
    fun previousQuestion() {
         _uiState.update { state ->
            if (state.currentQuestionIndex > 0) {
                state.copy(currentQuestionIndex = state.currentQuestionIndex - 1)
            } else {
                state
            }
        }
    }

    fun finishQuiz() {
        timer?.cancel()
        calculateScore()
    }

    private fun calculateScore() {
        _uiState.update { state ->
            var correctCount = 0
            state.questions.forEach { question ->
                val userSelected = state.userAnswers[question.id]?.sorted() ?: emptyList()
                val correct = question.correctAnswers.sorted()
                if (userSelected == correct) {
                    correctCount++
                }
            }
            val percentage = if (state.totalQuestions > 0) (correctCount.toDouble() / state.totalQuestions.toDouble()) * 100 else 0.0
            val passed = percentage >= 70 // 70% pass mark
            state.copy(
                isQuizFinished = true, 
                score = correctCount, 
                passed = passed
            )
        }
    }
    
    fun resetQuiz() {
         timer?.cancel()
        _uiState.value = QuizState()
    }

    override fun onCleared() {
        super.onCleared()
        timer?.cancel()
    }
}
