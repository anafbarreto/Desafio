import coverage
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_process_data(client):
    # Test case: no file
    response = client.get('/process')
    assert response.status_code == 400
    assert response.json['error'] == 'Nenhum arquivo informado'

    # Test case: file that doesn't exist
    response = client.get('/process?file_paths=arquivo_que_nao_existe.txt')
    assert response.status_code == 404
    assert response.json['error'] == 'Arquivo inexistente: arquivo_que_nao_existe.txt'

def test_display_data(client):
    # Test case: no data processed
    response = client.get('/display')
    assert response.status_code == 404
    assert response.json['error'] == 'Nenhum dado processado ainda'
    
     # Test case: Data processed successfully
    response = client.get('/process?file_paths=data_1.txt&file_paths=data_2.txt')
    assert response.status_code == 200
    assert response.json['message'] == 'Dados processados com sucesso'

    # Test case: Order ID not found
    response = client.get('/display?order_id=05')
    assert response.status_code == 404
    assert response.json['error'] == 'ID do pedido não encontrado: 05'

    # Test case: Invalid start date
    response = client.get('/display?start_date=2021-87-98')
    assert response.status_code == 400
    assert response.json['error'] == 'Data de início inválida: 2021-87-98'

    # Test case: Invalid end date
    response = client.get('/display?end_date=2021-12-40')
    assert response.status_code == 400
    assert response.json['error'] == 'Data de término inválida: 2021-12-40'

    # Test case: Successfully filtered data
    response = client.get('/display?order_id=751&start_date=2021-01-01&end_date=2021-12-31')
    assert response.status_code == 200
    
    # Test case: Successfully filtered data (just order id)
    response = client.get('/display?order_id=751')
    assert response.status_code == 200
    
    # Test case: Successfully filtered data (just start date)
    response = client.get('/display?start_date=2021-01-01')
    assert response.status_code == 200
  
    # Test case: Successfully filtered data (just end date)
    response = client.get('/display?end_date=2021-12-31')
    assert response.status_code == 200
   
    # Test case: Successfully filtered data (date range)
    response = client.get('/display?start_date=2021-01-01&end_date=2021-12-31')
    assert response.status_code == 200
    
cov = coverage.Coverage()
cov.start()
pytest.main(['test.py'])
cov.stop()
cov.html_report(directory='coverage_html_report')