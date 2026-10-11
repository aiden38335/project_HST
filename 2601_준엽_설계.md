# HST(Health Science and Technology) Guide Project Specification

## 1\. Project Name

HST Guide

## 2\. Project Overview

HST Guide is a project/ app that has a combined function of many things such as(ex. summary, platform to share discoveries, studying quiz and etc) to help individuals to easily access the idea of HST but to also give a platform and app that helps students to inquire about HST in more accessible and easier way. Like a combined education system

## 3\. Why I Chose This Project

HST is a very complex part and major to study in, it requires a lot of time and effort as well as a lot of resources even to start being educated about it.

This will help students in these majors to freely use the App to help them study about HST as a whole

I want to create an app that helps students:

- summarize long research papers and give them the core ideas   
- quiz or making question sets for students   
- a shared space where everyone can upload their findings   
- A detailed feedback with HST lens 

## 4\. Target Users

The main users are High school to University Students learning HST or anything on those lanes 

The app may be useful for subjects such as:

- Science   
- Math   
- Biology   
- Engineering 

## 5\. Main Features

### 5.1 Enter a Passage

The user can type or paste an English passage into a text box.

The passage could be in any length, However in the case that the Passage doesn't make sense or if off logic, it would and potentially ask more clarification

### 5.2 Create an AI Summary

The user would paste or upload any files regarding HST(Ex. Research papers) 

The AI reads the passage and creates a short summary.

The summary should:

- include the main ideas  
- be easier to read than the original passage  
- only use information from the passage  
- More concise 

### 5.3 Find Important Words

The app finds words that appear often in the passage.

Common words such as `the`, `a`, `is`, and `of` should not be included.

The app shows several important words to the user. → certain terminologies 

### 5.4 Create Fill-in-the-Blank Questions

The app uses important words to create questions.

For example, the original sentence may be:

Plants use sunlight to make food.

- A bit more comprehensive could also be fine  
  - Text to text is a bit to rigid and easy

The question will be:

Plants use \_\_\_\_\_ to make food.

The correct answer is:

sunlight

### 5.5 Check Answers

The user types an answer for each question.

When the user clicks the check button, the app compares the answers with the correct answers.

The app then shows:

- the number of correct answers  
- the total number of questions  
- the correct answers

## 6\. App Pages

### Study Page

The Study page includes:

- a passage input box  
- a sample passage button  
- a create study set button  
- an AI summary  
- a list of important words

### Quiz Page

The Quiz page includes:

- fill-in-the-blank questions  
- answer boxes  
- a check answers button  
- the final score  
- correct answer information  
- Long answer question

## 7\. Technologies

I plan to use:

- Python  
- Streamlit  
- a free Hugging Face AI model

Streamlit will be used to create the web interface.

The Hugging Face model will be used to summarize the passage, check answers, create lectures, and execute Feedback based on the resources given 

Python will be used to find \_\_\_\_\_\_\_\_\_\_\_

## 8\. First Version

The first version of AI Study Mate will include:

- English passage input  
- AI summary generation  
- important word extraction  
- fill-in-the-blank questions  
- automatic scoring

## 9\. Features Not Included Yet

The first version will not include:

- user accounts  
- login  
- PDF uploads  
- a database  
- saved scores  
- charts  
- multiple-choice questions  
- Korean passages  
- voice input

These features may be added later.

## 10\. Basic Program Flow

The user enters an English passage.

                ↓

The user clicks the create button.

                ↓

The AI creates a summary.

                ↓

The program finds important words.

                ↓

The program creates blank questions.

                ↓

The user answers the questions.

                ↓

The program checks the answers.

                ↓

The user sees the score.

## 11\. Minimum Requirements

The first version is complete when:

- the user can enter an English passage  
- the app can create a summary  
- the app can find important words  
- the app can create fill-in-the-blank questions  
- the user can type answers  
- the app can check the answers  
- the app can show a score

## 12\. Questions to Decide Later

I will decide these details while developing the project:

- How long should the summary be?  
- How many important words should the app show?  
- How many quiz questions should the app create?  
- What is the minimum passage length?  
- Should uppercase and lowercase answers be treated as the same?  
- Which free AI model should I use?  
- Should the AI model run locally or through an online service?  
- What colors and design should the app use?  
- What should happen when the AI cannot create a summary?

