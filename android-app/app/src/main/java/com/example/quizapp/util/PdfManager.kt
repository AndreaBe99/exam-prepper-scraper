package com.example.quizapp.util

import android.content.ContentValues
import android.content.Context
import android.graphics.Paint
import android.graphics.pdf.PdfDocument
import android.os.Build
import android.os.Environment
import android.provider.MediaStore
import android.widget.Toast
import com.example.quizapp.model.Question
import java.io.IOException

object PdfManager {

    fun generateReport(
        context: Context,
        questions: List<Question>,
        userAnswers: Map<String, List<String>>
    ) {
        val wrongAnswers = questions.filter { question ->
            val userSelected = userAnswers[question.id]?.sorted() ?: emptyList()
            val correct = question.correctAnswers.sorted()
            userSelected != correct
        }

        if (wrongAnswers.isEmpty()) {
            Toast.makeText(context, "No wrong answers to report!", Toast.LENGTH_SHORT).show()
            return
        }

        val pdfDocument = PdfDocument()
        val pageInfo = PdfDocument.PageInfo.Builder(595, 842, 1).create() // A4 size
        var page = pdfDocument.startPage(pageInfo)
        var canvas = page.canvas
        val paint = Paint()
        paint.textSize = 12f

        var yPosition = 40f
        val xPosition = 40f
        val lineHeight = 20f

        paint.textSize = 18f
        paint.isFakeBoldText = true
        canvas.drawText("Quiz Error Report", xPosition, yPosition, paint)
        yPosition += 40f
        paint.textSize = 12f
        paint.isFakeBoldText = false
        
        // Simple loop to draw text. If it overflows, we should start new page, but for simplicity we assume it fits or simple truncation.
        // A robust solution would measure text and paginate.
        
        wrongAnswers.forEachIndexed { index, question ->
            if (yPosition > 800) {
                 pdfDocument.finishPage(page)
                 page = pdfDocument.startPage(pageInfo)
                 canvas = page.canvas
                 yPosition = 40f
            }
        
            paint.isFakeBoldText = true
            canvas.drawText("Q${index + 1}: ${question.text}", xPosition, yPosition, paint)
            yPosition += lineHeight
            
            val userSelected = userAnswers[question.id]?.joinToString(", ") ?: "None"
            paint.isFakeBoldText = false
            canvas.drawText("Your Answer: $userSelected", xPosition + 10, yPosition, paint)
            yPosition += lineHeight
            
            val correct = question.correctAnswers.joinToString(", ")
            canvas.drawText("Correct Answer: $correct", xPosition + 10, yPosition, paint)
            yPosition += lineHeight * 2
        }

        pdfDocument.finishPage(page)

        try {
            savePdf(context, pdfDocument)
        } catch (e: IOException) {
            e.printStackTrace()
            Toast.makeText(context, "Error saving PDF: ${e.message}", Toast.LENGTH_SHORT).show()
        } finally {
            pdfDocument.close()
        }
    }

    private fun savePdf(context: Context, pdfDocument: PdfDocument) {
        val fileName = "Quiz_Report_${System.currentTimeMillis()}.pdf"
        
        val contentValues = ContentValues().apply {
            put(MediaStore.MediaColumns.DISPLAY_NAME, fileName)
            put(MediaStore.MediaColumns.MIME_TYPE, "application/pdf")
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                put(MediaStore.MediaColumns.RELATIVE_PATH, Environment.DIRECTORY_DOCUMENTS)
            }
        }

        val resolver = context.contentResolver
        val uri = resolver.insert(MediaStore.Files.getContentUri("external"), contentValues)

        if (uri != null) {
            resolver.openOutputStream(uri).use { outputStream ->
                if (outputStream != null) {
                    pdfDocument.writeTo(outputStream)
                    Toast.makeText(context, "PDF saved to Documents", Toast.LENGTH_LONG).show()
                }
            }
        } else {
             Toast.makeText(context, "Failed to create file", Toast.LENGTH_SHORT).show()
        }
    }
}
