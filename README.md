# Personalized Course & Learning Path Recommender

### Artificial Intelligence Lab Project

**Submitted To:** Mr. Mehmood-ul-Haq  
**Team Members:** Naveera Aamir (2024CE93) & Muhammad Afnan Abbas (2024CE03)

---

## 1. Problem Statement
Many online learners and students struggle with information overload and difficulty in choosing appropriate courses tailored to their unique background and career goals. Beginners, self-taught professionals, and university students often lose motivation or follow inefficient learning sequences. Solving this problem is crucial to minimize wasted study time, improve course completion rates, and maximize personal skill development.

## 2. Core Concept
This project delivers a Personalized Course and Learning Path Recommender web application that analyzes a user's interests, target career goals, and prior learning history. Using collaborative filtering and recommendation algorithms, the system evaluates dynamic user profiles to suggest customized course sequences. The platform will feature an interactive user dashboard where learners can discover tailored recommendations and track their progress through step-by-step learning paths.

## 3. Objectives
* Design a dynamic user profile module that captures user skills, preferences, and learning history.
* Develop a recommendation engine utilizing collaborative filtering algorithms to generate personalized course sequences.
* Implement a full-stack web application with an intuitive dashboard for learners to visualize and follow their custom learning paths.

## 4. Technology Stack
* **Programming Language:** Python
* **Backend Framework:** Django
* **Database:** Supabase
* **Machine Learning:** Scikit-learn (K-Nearest Neighbors, Cosine Similarity, Singular Value Decomposition, Non-Negative Matrix Factorization, K-Means Clustering, Term Frequency-Inverse Document Frequency)
* **Frontend:** HTML, CSS, JavaScript, Bootstrap

## 5. Workflow Architecture
### Input Phase
The user creates an account and completes an initial setup assessment by entering their career goals, areas of interest, existing skills, and past course completion history.

### Processing Phase
* **Data Preprocessing & Vectorization:** The system standardizes and processes user input, indexing skills, course features, and historical interactions.
* **Collaborative Filtering Engine:** The machine learning module computes user-to-user and item-to-item similarity scores based on historical behavior from users with similar learning profiles.
* **Learning Path Generation:** The system structures the recommended courses into a logical, step-by-step sequential path, scaling smoothly from foundational to advanced topics.

### Output Phase
The backend serves a tailored dashboard displaying a personalized sequence of recommended courses, complete with difficulty indicators, estimated completion timelines, and visual progress tracking tools.
