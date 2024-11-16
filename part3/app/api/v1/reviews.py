from flask_restx import Namespace, Resource, fields
from flask import jsonify
from app.api.v1.instance_facade import facade

# Initialize the Namespace for reviews
review_api = Namespace('reviews', description='Operations for managing reviews')

# Model for review validation and documentation
review_model = review_api.model('Review', {
    'title': fields.String(required=True, description='Title of the review'),
    'text': fields.String(required=True, description='Content of the review'),
    'rating': fields.Integer(required=True, description='Rating (1-5 scale)'),
    'user_id': fields.String(required=True, description='ID of the user who wrote the review'),
    'place_id': fields.String(required=True, description='ID of the place being reviewed')
})

@review_api.route('/')
class ReviewList(Resource):
    @review_api.expect(review_model)
    @review_api.response(201, 'Review successfully created')
    @review_api.response(400, 'Invalid input data')
    def post(self):
        """Create a new review"""
        try:
            review_data = review_api.payload
            review = facade.create_review(review_data)
            return {
                'title':review.title,
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.owner.id,
                'place_id': review.place_id
            }, 201
        except ValueError as e:
            return {'message': str(e)}, 400

@review_api.route('/all')
class ShowAllReviews(Resource):
    """Resource for showing all reviews."""

    @review_api.response(200, 'Reviews details retrieved successfully')
    @review_api.response(404, 'No review found')
    def get(self):
        """Retrieve all reviews."""
        all_reviews = facade.get_all_reviews()
        
        if not all_reviews:
            return {'error': 'No review found'}, 404

        reviews_data = [
            {
                'title':review.title,
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.owner.id,
                'place_id': review.place_id
            }
            for review in all_reviews
        ]
        
        return reviews_data, 200

@review_api.route('/<string:review_id>')
class ReviewResource(Resource):
    @review_api.response(200, 'Review details retrieved successfully')
    @review_api.response(404, 'Review not found')
    def get(self, review_id):
        """Retrieve a specific review by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        return {
            'title': review.title,
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.owner.id,
            'place_id': review.place_id
        }, 200


@review_api.route('/<string:review_id>')
class ReviewResource(Resource):
    @review_api.expect(review_model, partial=True)
    @review_api.response(200, 'Review updated successfully')
    @review_api.response(404, 'Review not found')
    @review_api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review by ID"""
        review_data = review_api.payload
        
        try:
            updated_review = facade.update_review(review_id, review_data)
            return {
                'title': updated_review.title,
                'id': updated_review.id,
                'text': updated_review.text,
                'rating': updated_review.rating,
                'user_id': updated_review.owner.id,
                'place_id': updated_review.place_id
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400

@review_api.route('/delete/<string:review_id>')
class DeleteReview(Resource):
    @review_api.response(200, 'Review deleted successfully')
    @review_api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review by ID"""
        deleted = facade.delete_review(review_id)

        if not deleted:
            return {'message': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200

@review_api.route('/places/<string:place_id>/reviews')
class PlaceReviewList(Resource):
    @review_api.response(200, 'List of reviews for the specified place retrieved successfully')
    @review_api.response(404, 'Place not found or no reviews found')
    def get(self, place_id):
        """Retrieve all reviews associated with a specific place by its ID"""
        reviews = facade.get_reviews_by_place(place_id)
        
        if not reviews:
            return {'message': 'No reviews found for this place'}, 404

        reviews_list = [
            {
                'id': review.id,
                'title': review.title,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.owner.id,
                'place_id': review.place_id
            }
            for review in reviews
        ]

        return reviews_list, 200