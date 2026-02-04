package com.example.quizapp.data

import com.example.quizapp.model.Question

interface QuestionRepository {
    suspend fun getQuestions(): List<Question>
}
