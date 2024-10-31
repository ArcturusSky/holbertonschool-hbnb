from flask_restx import Namespace, Resource, fields
from app.services import facade

# Initialize the Namespace for reviews
review_api = Namespace('reviews', description='Operations for managing reviews')

# Model for review validation and documentation
review_model = review_api.model('Review', {
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
            return review, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @review_api.response(200, 'List of all reviews retrieved successfully')
    def get(self):
        """Retrieve all reviews"""
        reviews = facade.get_all_reviews()
        return reviews, 200

@review_api.route('/<string:review_id>')
class ReviewResource(Resource):
    @review_api.response(200, 'Review details retrieved successfully')
    @review_api.response(404, 'Review not found')
    def get(self, review_id):
        """Retrieve a specific review by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        return review, 200

    @review_api.expect(review_model)
    @review_api.response(200, 'Review updated successfully')
    @review_api.response(404, 'Review not found')
    @review_api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review by ID"""
        try:
            review_data = review_api.payload
            updated_review = facade.update_review(review_id, review_data)
            return updated_review, 200
        except ValueError as e:
            return {'message': str(e)}, 404

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
    @review_api.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieve all reviews associated with a specific place by its ID"""
        reviews = facade.get_reviews_by_place(place_id)
        return reviews, 200 if reviews else 404
