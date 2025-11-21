@echo off
setlocal

REM Nome do ambiente virtual
set VENV=venv

REM Verifica se o ambiente virtual já existe
if not exist "%VENV%\Scripts\activate.bat" (
    echo Criando ambiente virtual...
    python -m venv %VENV%
)

REM Ativa o ambiente virtual
call %VENV%\Scripts\activate.bat

REM Instala o Streamlit (se necessário)
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo Instalando Streamlit...
    pip install streamlit
)

REM Executa o script com Streamlit
echo Iniciando o app...
streamlit run Oi.py

REM Mantém a janela aberta
echo.
pause