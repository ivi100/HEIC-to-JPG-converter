@echo off

echo Instalando heif-convert...
python -m pip install --upgrade pip
pip install heif-convert
if %errorlevel% neq 0 (
    echo Error al instalar heif-convert. Abortando.
    echo Comprueba que python esta instalado correctamente
    pause
)

echo Instalacion completa. heif-convert ha sido instalado correctamente.
pause
