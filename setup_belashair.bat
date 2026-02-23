import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"Executando: {cmd}")
    subprocess.check_call(cmd, shell=True)

# Atualizar pip
run_cmd(f"{sys.executable} -m pip install --upgrade pip")

# Instalar bibliotecas necessárias
libs = [
    "streamlit",
    "pandas",
    "streamlit-option-menu",
    "streamlit-fullcalendar",
    "Pillow"

]

for lib in libs:
    run_cmd(f"{sys.executable} -m pip install {lib}")

print("✅ Todas as bibliotecas foram instaladas com sucesso!")

