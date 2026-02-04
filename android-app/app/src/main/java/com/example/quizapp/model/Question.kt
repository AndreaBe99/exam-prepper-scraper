package com.example.quizapp.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Question(
    val id: String,
    val text: String,
    val options: Map<String, String>,
    @SerialName("correct_answers")
    val correctAnswers: List<String>
) {
    fun isMultipleChoice(): Boolean = correctAnswers.size > 1
}
