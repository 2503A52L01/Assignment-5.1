"""
Simplified Recommendation System with Explainable AI
Uses only built-in Python libraries to avoid dependency issues
"""

import math
import random
from collections import defaultdict

class SimpleExplainableRecommendationSystem:
    def __init__(self):
        self.user_item_matrix = {}
        self.user_similarities = {}
        self.users = set()
        self.items = set()
        
    def fit(self, interactions):
        """Fit the recommendation system on interaction data"""
        # Create user-item matrix
        for user_id, item_id, rating in interactions:
            self.users.add(user_id)
            self.items.add(item_id)
            
            if user_id not in self.user_item_matrix:
                self.user_item_matrix[user_id] = {}
            self.user_item_matrix[user_id][item_id] = rating
        
        # Calculate user similarities
        self._calculate_similarities()
    
    def _calculate_similarities(self):
        """Calculate cosine similarities between users"""
        user_vectors = {}
        
        # Create user vectors
        for user_id in self.users:
            user_vectors[user_id] = []
            for item_id in self.items:
                rating = self.user_item_matrix.get(user_id, {}).get(item_id, 0)
                user_vectors[user_id].append(rating)
        
        # Calculate cosine similarities
        user_list = list(self.users)
        for i, user1 in enumerate(user_list):
            self.user_similarities[user1] = {}
            vec1 = user_vectors[user1]
            
            for j, user2 in enumerate(user_list):
                if i != j:
                    vec2 = user_vectors[user2]
                    similarity = self._cosine_similarity(vec1, vec2)
                    if similarity > 0:
                        self.user_similarities[user1][user2] = similarity
    
    def _cosine_similarity(self, vec1, vec2):
        """Calculate cosine similarity between two vectors"""
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(b * b for b in vec2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0
        
        return dot_product / (magnitude1 * magnitude2)
    
    def recommend_for_user(self, user_id, top_n=5):
        """Generate recommendations for a specific user with explanations"""
        if user_id not in self.users:
            return [], "User not found in the system"
        
        # Get user's rated items
        user_ratings = self.user_item_matrix.get(user_id, {})
        rated_items = set(user_ratings.keys())
        
        # Find similar users
        similar_users = self._find_similar_users(user_id)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(user_id, similar_users, rated_items)
        
        # Get top N recommendations with explanations
        top_recommendations = []
        for item_id, score in recommendations[:top_n]:
            explanation = self._generate_explanation(user_id, item_id, similar_users)
            top_recommendations.append({
                'item_id': item_id,
                'score': score,
                'explanation': explanation
            })
            
        return top_recommendations
    
    def _find_similar_users(self, user_id, top_k=5):
        """Find similar users based on cosine similarity"""
        if user_id not in self.user_similarities:
            return []
        
        similar_users = []
        for other_user, similarity in self.user_similarities[user_id].items():
            similar_users.append((other_user, similarity))
        
        similar_users.sort(key=lambda x: x[1], reverse=True)
        return similar_users[:top_k]
    
    def _generate_recommendations(self, user_id, similar_users, rated_items):
        """Generate recommendations based on similar users"""
        recommendations = {}
        
        for other_user, similarity in similar_users:
            other_ratings = self.user_item_matrix.get(other_user, {})
            
            for item_id, rating in other_ratings.items():
                if item_id not in rated_items and rating >= 3:  # Only consider items rated 3+
                    if item_id not in recommendations:
                        recommendations[item_id] = 0
                    recommendations[item_id] += similarity * rating
        
        # Sort by recommendation score
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return sorted_recommendations
    
    def _generate_explanation(self, user_id, item_id, similar_users):
        """Generate explanation for why an item is recommended"""
        explanations = []
        
        # Check similar users who rated this item highly
        for other_user, similarity in similar_users:
            other_ratings = self.user_item_matrix.get(other_user, {})
            other_rating = other_ratings.get(item_id, 0)
            
            if other_rating >= 4:  # Users who rated this item 4 or 5
                explanations.append(
                    f"Similar user {other_user} rated this item {other_rating}/5 "
                    f"(similarity: {similarity:.2f})"
                )
        
        if not explanations:
            explanations.append("This item is popular among users with similar preferences")
            
        return explanations
    
    def evaluate_explanations(self, explanations):
        """Evaluate the quality of explanations"""
        if not explanations:
            return {"score": 0, "feedback": "No explanations available"}
        
        quality_scores = []
        for explanation in explanations:
            score = self._score_explanation(explanation)
            quality_scores.append(score)
        
        avg_score = sum(quality_scores) / len(quality_scores)
        
        return {
            'average_score': avg_score,
            'feedback': self._get_feedback(avg_score)
        }
    
    def _score_explanation(self, explanation):
        """Score an individual explanation (0-1 scale)"""
        score = 0.0
        
        if "rated this item" in explanation and "similarity" in explanation:
            score += 0.8  # Specific and data-driven
        elif "popular among users" in explanation:
            score += 0.5  # General explanation
        else:
            score += 0.3  # Generic explanation
        
        return min(score, 1.0)
    
    def _get_feedback(self, score):
        """Get feedback based on score"""
        if score >= 0.7:
            return "Excellent explanations - clear and specific"
        elif score >= 0.5:
            return "Good explanations - generally understandable"
        elif score >= 0.3:
            return "Fair explanations - somewhat vague"
        else:
            return "Poor explanations - not very helpful"

def generate_sample_data(num_users=20, num_items=15, num_interactions=100):
    """Generate sample interaction data"""
    interactions = []
    
    for _ in range(num_interactions):
        user_id = random.randint(0, num_users - 1)
        item_id = random.randint(0, num_items - 1)
        rating = random.randint(1, 5)
        interactions.append((user_id, item_id, rating))
    
    return interactions

def main():
    """Main demonstration function"""
    print("=" * 60)
    print("SIMPLIFIED EXPLAINABLE RECOMMENDATION SYSTEM")
    print("=" * 60)
    
    # Generate sample data
    print("\nGenerating sample data...")
    data = generate_sample_data()
    print(f"Generated {len(data)} interactions")
    
    # Initialize and fit the system
    print("\nTraining recommendation system...")
    rec_system = SimpleExplainableRecommendationSystem()
    rec_system.fit(data)
    
    # Test with a few users
    test_users = [0, 1, 2]
    
    print(f"\nGenerating recommendations for {len(test_users)} users...")
    print("-" * 60)
    
    all_explanations = []
    
    for user_id in test_users:
        print(f"\nRecommendations for User {user_id}:")
        print("-" * 40)
        
        recommendations = rec_system.recommend_for_user(user_id, top_n=3)
        
        if not recommendations:
            print("No recommendations available.")
            continue
        
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. Item {rec['item_id']} (score: {rec['score']:.2f})")
            print("   Explanation:")
            for explanation in rec['explanation']:
                print(f"   - {explanation}")
                all_explanations.append(explanation)
            print()
    
    # Evaluate explanations
    print("=" * 60)
    print("EXPLANATION QUALITY EVALUATION")
    print("=" * 60)
    
    evaluation = rec_system.evaluate_explanations(all_explanations)
    print(f"Average Quality Score: {evaluation['average_score']:.2f}")
    print(f"Feedback: {evaluation['feedback']}")
    
    print("\n" + "=" * 60)
    print("SYSTEM SUMMARY")
    print("=" * 60)
    print("✓ Recommendation system with explainable AI implemented")
    print("✓ Uses only built-in Python libraries (no external dependencies)")
    print("✓ Provides specific reasons for each recommendation")
    print("✓ Includes explanation quality evaluation")
    print("✓ Ready for demonstration")

if __name__ == "__main__":
    main()
