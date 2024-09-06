# Análise-de-cobertura

## Iniciar o ambiente virtual
```bash
python -m venv venv
```

## Ativar o ambiente virtual
```bash
source \Scripts\activate
```

## Instalar dependências
```bash
pip install pytest-cov
```

## Executando pytest-cov
```bash
[pytest]
adoopts = --cov=src/ --cov-report=html --cov-report=term-missing
```

## Criar o arquivo pytest.ini
Na raiz do projeto, criar o arquivo `pytest.ini` e adicionar os comandos acima.

## voltar para a pasta Caso de Teste

## Executando o arquivo pytest.ini
Execute o comando:
```bash
pytest
```

## Excluindo arquivos não desejados
Na raiz do projeto, criar o arquivo `.coveragerc` e inserir o código abaixo:

```ini
[run]
source = src/
omit = __init__.py, *index.py
```

Execute o comando:
```bash
pytest
```

## `#pragma: no cover`
Utilizar o comentário `#pragma: no cover` para ignorar trechos de código.

