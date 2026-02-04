package com.example.quizapp.ui

import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.platform.LocalContext
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.navigation
import androidx.navigation.navArgument
import com.example.quizapp.ui.screens.HomeScreen
import com.example.quizapp.ui.screens.QuizScreen
import com.example.quizapp.ui.screens.ResultScreen
import com.example.quizapp.util.PdfManager

@Composable
fun QuizNavHost(navController: NavHostController) {
    val context = LocalContext.current
    
    NavHost(navController = navController, startDestination = "home") {
        composable("home") {
            HomeScreen(
                onStartQuiz = { count, time ->
                    navController.navigate("quiz/$count/$time")
                }
            )
        }

        navigation(
            startDestination = "question",
            route = "quiz/{count}/{time}",
            arguments = listOf(
                navArgument("count") { type = NavType.IntType },
                navArgument("time") { type = NavType.IntType }
            )
        ) {
            composable("question") { backStackEntry ->
                val parentEntry = remember(backStackEntry) {
                    navController.getBackStackEntry("quiz/{count}/{time}")
                }
                val viewModel = hiltViewModel<QuizViewModel>(parentEntry)
                val count = parentEntry.arguments?.getInt("count") ?: 10
                val time = parentEntry.arguments?.getInt("time") ?: 15

                QuizScreen(
                    viewModel = viewModel,
                    questionCount = count,
                    timeLimit = time,
                    onQuizFinished = {
                        navController.navigate("result")
                    },
                    onNavigateUp = {
                        navController.popBackStack("home", inclusive = false)
                    }
                )
            }

            composable("result") { backStackEntry ->
                val parentEntry = remember(backStackEntry) {
                    navController.getBackStackEntry("quiz/{count}/{time}")
                }
                val viewModel = hiltViewModel<QuizViewModel>(parentEntry)
                
                ResultScreen(
                    viewModel = viewModel,
                    onRestart = {
                        // Pop back to question, effectively restarting with same params or we can go home
                        // To restart: pop to question. VM needs reset.
                        navController.popBackStack("question", inclusive = false)
                    },
                    onHome = {
                        navController.popBackStack("home", inclusive = false)
                    },
                    onGeneratePdf = {
                        // Trigger PDF Generation
                        val state = viewModel.uiState.value
                        PdfManager.generateReport(context, state.questions, state.userAnswers)
                    }
                )
            }
        }
    }
}
