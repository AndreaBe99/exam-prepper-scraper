package com.example.quizapp.ui.screens

import androidx.activity.compose.BackHandler
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.quizapp.ui.QuizViewModel
import com.example.quizapp.ui.components.OptionRow
import com.example.quizapp.ui.components.TimerDisplay

@Composable
fun QuizScreen(
    viewModel: QuizViewModel,
    questionCount: Int,
    timeLimit: Int,
    onQuizFinished: () -> Unit,
    onNavigateUp: () -> Unit
) {
    val uiState by viewModel.uiState.collectAsState()

    LaunchedEffect(Unit) {
        if (uiState.questions.isEmpty() && !uiState.isLoading) {
            viewModel.loadQuiz(questionCount, timeLimit)
        }
    }

    LaunchedEffect(uiState.isQuizFinished) {
        if (uiState.isQuizFinished) {
            onQuizFinished()
        }
    }
    
    // intercept back press to prevent accidental exit? 
    // For now simple BackHandler to navigate up.
    BackHandler {
        onNavigateUp()
    }

    if (uiState.isLoading) {
        Column(
            modifier = Modifier.fillMaxSize(), 
            verticalArrangement = Arrangement.Center, 
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text("Loading Quiz...")
        }
        return
    }

    if (uiState.questions.isEmpty()) {
        return 
    }

    val currentQuestion = uiState.questions[uiState.currentQuestionIndex]
    
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
            .verticalScroll(rememberScrollState())
    ) {
        // Top Bar
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(
                text = "Question ${uiState.currentQuestionIndex + 1}/${uiState.totalQuestions}",
                style = MaterialTheme.typography.titleMedium
            )
            TimerDisplay(timeLeftMillis = uiState.timeLeftInMillis)
        }
        
        LinearProgressIndicator(
            progress = (uiState.currentQuestionIndex + 1) / uiState.totalQuestions.toFloat(),
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 16.dp)
        )

        // Question Card
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 24.dp)
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text(
                    text = currentQuestion.text,
                    style = MaterialTheme.typography.headlineSmall
                )
                if (currentQuestion.isMultipleChoice()) {
                    Text(
                        text = "(Select all that apply)",
                        style = MaterialTheme.typography.bodySmall,
                        modifier = Modifier.padding(top = 4.dp)
                    )
                }
            }
        }

        // Options
        currentQuestion.options.forEach { (key, text) ->
            val isSelected = uiState.userAnswers[currentQuestion.id]?.contains(key) == true
            // OptionRow from Common.kt
            OptionRow(
                text = text,
                isSelected = isSelected,
                isMultipleChoice = currentQuestion isMultipleChoice(),
                onOptionSelected = {
                    viewModel.submitAnswer(currentQuestion.id, key, currentQuestion.isMultipleChoice())
                }
            )
        }

        Spacer(modifier = Modifier.weight(1f))

        // Navigation Buttons
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(top = 16.dp),
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
             Button(
                onClick = { viewModel.previousQuestion() },
                enabled = uiState.currentQuestionIndex > 0
            ) {
                Text("Previous")
            }
            
            if (uiState.currentQuestionIndex < uiState.totalQuestions - 1) {
                Button(onClick = { viewModel.nextQuestion() }) {
                    Text("Next")
                }
            } else {
                Button(onClick = { viewModel.finishQuiz() }) {
                    Text("Finish")
                }
            }
        }
    }
}
