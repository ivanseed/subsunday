from flask_restful import Resource, reqparse, marshal_with, fields

from http import HTTPStatus

from models import Vote


vote_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'game': fields.String,
}

vote_parser = reqparse.RequestParser()
vote_parser.add_argument('username', type=str, required=True)
vote_parser.add_argument('game', type=str, required=True)


class VotesResource(Resource):

    def __init__(self, store):
        self.session = store.session

    @marshal_with(vote_fields)
    def get(self):
        return self.session.query(Vote).all()

    @marshal_with(vote_fields)
    def post(self):
        args = vote_parser.parse_args()

        by_username = (Vote.username == args['username'])
        vote = self.session.query(Vote).filter(by_username).first()

        if vote:
            vote.game = args['game']
            status = HTTPStatus.OK
        else:
            vote = Vote(**args)
            self.session.add(vote)
            status = HTTPStatus.CREATED

        self.session.commit()

        return vote, status
