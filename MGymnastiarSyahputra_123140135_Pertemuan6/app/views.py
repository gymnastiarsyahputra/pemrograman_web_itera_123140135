from pyramid.view import view_config
from pyramid.response import Response, FileResponse
from sqlalchemy.exc import IntegrityError
import json
import os

from .models import Matakuliah, get_db_session


def json_response(data, status=200):
    return Response(
        body=json.dumps(data),
        status=status,
        content_type='application/json; charset=utf-8'
    )


@view_config(route_name='list_matakuliah')
def list_matakuliah(request):
    session = get_db_session()
    data = [m.to_dict() for m in session.query(Matakuliah).all()]
    return json_response(data)


@view_config(route_name='openapi_spec')
def openapi_spec(request):
    root = os.path.dirname(os.path.dirname(__file__))  # folder project root
    spec_path = os.path.join(root, 'openapi.yaml')
    return FileResponse(spec_path, request=request, content_type='text/yaml')

@view_config(route_name='docs')
def docs_view(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Docs - Manajemen Matakuliah</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css" />
        <style>
            body { margin: 0; padding: 0; }
            #swagger-ui { max-width: 1000px; margin: 0 auto; }
        </style>
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
        <script>
            window.onload = function() {
                SwaggerUIBundle({
                    url: '/openapi.yaml',
                    dom_id: '#swagger-ui'
                });
            };
        </script>
    </body>
    </html>
    """
    return Response(body=html, content_type='text/html; charset=utf-8')


@view_config(route_name='get_matakuliah')
def get_matakuliah(request):
    session = get_db_session()
    matkul = session.query(Matakuliah).get(request.matchdict['id'])

    if not matkul:
        return json_response({'error': 'Matakuliah tidak ditemukan'}, status=404)

    return json_response(matkul.to_dict())


@view_config(route_name='create_matakuliah')
def create_matakuliah(request):
    session = get_db_session()

    try:
        payload = request.json_body
    except:
        return json_response({'error': 'Body harus JSON'}, status=400)

    required = ['kode_mk', 'nama_mk', 'sks', 'semester']
    for field in required:
        if field not in payload:
            return json_response({'error': f'Field {field} wajib diisi'}, status=400)

    matkul = Matakuliah(
        kode_mk=payload['kode_mk'],
        nama_mk=payload['nama_mk'],
        sks=int(payload['sks']),
        semester=int(payload['semester']),
    )
    session.add(matkul)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        return json_response({'error': 'kode_mk sudah digunakan'}, status=400)

    return json_response(matkul.to_dict(), status=201)


@view_config(route_name='update_matakuliah')
def update_matakuliah(request):
    session = get_db_session()
    matkul = session.query(Matakuliah).get(request.matchdict['id'])

    if not matkul:
        return json_response({'error': 'Matakuliah tidak ditemukan'}, status=404)

    try:
        payload = request.json_body
    except:
        return json_response({'error': 'Body harus JSON'}, status=400)

    if 'kode_mk' in payload:
        matkul.kode_mk = payload['kode_mk']
    if 'nama_mk' in payload:
        matkul.nama_mk = payload['nama_mk']
    if 'sks' in payload:
        matkul.sks = int(payload['sks'])
    if 'semester' in payload:
        matkul.semester = int(payload['semester'])

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        return json_response({'error': 'kode_mk sudah digunakan'}, status=400)

    return json_response(matkul.to_dict())


@view_config(route_name='delete_matakuliah')
def delete_matakuliah(request):
    session = get_db_session()
    matkul = session.query(Matakuliah).get(request.matchdict['id'])

    if not matkul:
        return json_response({'error': 'Matakuliah tidak ditemukan'}, status=404)

    session.delete(matkul)
    session.commit()

    return json_response({'message': 'Matakuliah berhasil dihapus'})
