from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
	def get(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json(), 200
		return {'message': 'Store not found'}, 404

	def post(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			return {'message': '{} already exist the given store.'.format(name)}, 400
		try:
			store = StoreModel(name)
			store.save_to_db()
		except Exception as error:
			return {'message': 'insertion error not able to add the store. {}'.format(error)}, 500
		return {'message': '{} Store is added in the store family.'.format(name)}, 201

	def delete(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()
		return {'message': 'deleted'}, 201

class StoreList(Resource):
	def get(self):
		try:
			return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}, 200
		except Exception as error:
			return {'message': error}, 500