package com.example.quizapp.ui.screens

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Slider
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import kotlin.math.roundToInt

@Composable
fun HomeScreen(
    onStartQuiz: (Int, Int) -> Unit
) {
    var questionCount by remember { mutableFloatStateOf(10f) }
    var durationMinutes by remember { mutableFloatStateOf(15f) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(
            text = "Quiz Configuration",
            style = MaterialTheme.typography.headlineLarge,
            modifier = Modifier.padding(bottom = 32.dp)
        )

        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 24.dp)
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text(
                    text = "Number of Questions: ${questionCount.roundToInt()}",
                    style = MaterialTheme.typography.titleMedium
                )
                Slider(
                    value = questionCount,
                    onValueChange = { questionCount = it },
                    valueRange = 5f..50f,
                    steps = 44
                )
            }
        }

        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 32.dp)
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text(
                    text = "Timer Duration: ${durationMinutes.roundToInt()} minutes",
                    style = MaterialTheme.typography.titleMedium
                )
                Slider(
                    value = durationMinutes,
                    onValueChange = { durationMinutes = it },
                    valueRange = 5f..60f,
                    steps = 54
                )
            }
        }

        Button(
            onClick = { onStartQuiz(questionCount.roundToInt(), durationMinutes.roundToInt()) },
            modifier = Modifier.fillMaxWidth().height(56.dp)
        ) {
            Text("Start Quiz")
        }
    }
}
