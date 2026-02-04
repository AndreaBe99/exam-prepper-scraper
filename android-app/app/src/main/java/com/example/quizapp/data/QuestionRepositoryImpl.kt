package com.example.quizapp.data

import android.content.Context
import com.example.quizapp.model.Question
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import kotlinx.serialization.json.Json
import java.io.BufferedReader
import java.io.InputStreamReader
import javax.inject.Inject

class QuestionRepositoryImpl @Inject constructor(
    private val context: Context
) : QuestionRepository {

    override suspend fun getQuestions(): List<Question> = withContext(Dispatchers.IO) {
        val jsonString = context.assets.open("questions.json").use { inputStream ->
            BufferedReader(InputStreamReader(inputStream)).use { it.readText() }
        }
        Json.decodeFromString(jsonString)
    }
}
