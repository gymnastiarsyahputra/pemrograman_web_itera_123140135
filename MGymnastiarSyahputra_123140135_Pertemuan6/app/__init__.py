from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import Base, init_engine, configure_session


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')

    init_engine(engine)
    configure_session(engine)
    Base.metadata.create_all(bind=engine)

    config = Configurator(settings=settings)

    # CRUD Routes
    config.add_route('list_matakuliah',   '/api/matakuliah',      request_method='GET')
    config.add_route('create_matakuliah', '/api/matakuliah',      request_method='POST')
    config.add_route('get_matakuliah',    '/api/matakuliah/{id}', request_method='GET')
    config.add_route('update_matakuliah', '/api/matakuliah/{id}', request_method='PUT')
    config.add_route('delete_matakuliah', '/api/matakuliah/{id}', request_method='DELETE')

    # OpenAPI spec route
    config.add_route('openapi_spec', '/openapi.yaml', request_method='GET')
    config.add_route('docs', '/docs', request_method='GET')

    config.scan()  # cukup satu kali

    return config.make_wsgi_app()
