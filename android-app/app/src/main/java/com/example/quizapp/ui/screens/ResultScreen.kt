package com.example.quizapp.ui.screens

import android.widget.Toast
import androidx.activity.compose.BackHandler
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.example.quizapp.ui.QuizViewModel
// TODO import PdfManager

@Composable
fun ResultScreen(
    viewModel: QuizViewModel,
    onRestart: () -> Unit,
    onHome: () -> Unit,
    onGeneratePdf: () -> Unit
) {
    val uiState by viewModel.uiState.collectAsState()
    
    BackHandler {
        onHome()
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(
            text = if (uiState.passed) "Congratulations!" else "Better Luck Next Time",
            style = MaterialTheme.typography.headlineLarge,
            color = if (uiState.passed) Color.Green else Color.Red
        )
        
        Spacer(modifier = Modifier.height(24.dp))
        
        Text(
            text = "Score: ${uiState.score} / ${uiState.totalQuestions}",
            style = MaterialTheme.typography.displayMedium
        )
        
        val percentage = if (uiState.totalQuestions > 0) (uiState.score * 100 / uiState.totalQuestions) else 0
        Text(
            text = "$percentage%",
            style = MaterialTheme.typography.headlineMedium
        )

        Spacer(modifier = Modifier.height(48.dp))

        if (!uiState.passed || uiState.score < uiState.totalQuestions) {
            Button(
                onClick = onGeneratePdf,
                modifier = Modifier.fillMaxWidth().height(56.dp)
            ) {
                Text("Download Error Report (PDF)")
            }
            Spacer(modifier = Modifier.height(16.dp))
        }

        OutlinedButton(
            onClick = {
                viewModel.resetQuiz()
                onRestart()
            },
            modifier = Modifier.fillMaxWidth().height(56.dp)
        ) {
            Text("Retake Quiz")
        }
        
        Spacer(modifier = Modifier.height(16.dp))
        
        OutlinedButton(
             onClick = {
                viewModel.resetQuiz()
                onHome()
            },
            modifier = Modifier.fillMaxWidth().height(56.dp)
        ) {
            Text("Home")
        }
    }
}
