package com.example.quizapp.ui.components

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Checkbox
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun OptionRow(
    text: String,
    isSelected: Boolean,
    isMultipleChoice: Boolean,
    onOptionSelected: () -> Unit
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onOptionSelected() }
            .padding(8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        if (isMultipleChoice) {
            Checkbox(
                checked = isSelected,
                onCheckedChange = { onOptionSelected() }
            )
        } else {
            RadioButton(
                selected = isSelected,
                onClick = { onOptionSelected() }
            )
        }
        Text(
            text = text,
            style = MaterialTheme.typography.bodyLarge,
            modifier = Modifier.padding(start = 8.dp)
        )
    }
}

@Composable
fun TimerDisplay(
    timeLeftMillis: Long,
    modifier: Modifier = Modifier
) {
    val totalSeconds = timeLeftMillis / 1000
    val minutes = totalSeconds / 60
    val seconds = totalSeconds % 60
    
    val color = if (minutes < 2) MaterialTheme.colorScheme.error else MaterialTheme.colorScheme.onSurface
    
    Text(
        text = String.format("%02d:%02d", minutes, seconds),
        style = MaterialTheme.typography.headlineMedium,
        color = color,
        modifier = modifier
    )
}
