@echo off
echo ========================================
echo   COMPILANDO RULETA NAVIDEÑA
echo ========================================
echo.

REM Instalar PyInstaller si no está instalado
echo Verificando PyInstaller...
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando PyInstaller...
    pip install pyinstaller
) else (
    echo PyInstaller ya está instalado
)

echo.
echo Creando ejecutable...
echo.

REM Compilar con PyInstaller
pyinstaller --onefile --windowed --name "RuletaNavideña" --icon=NONE ruleta_compartir.py

echo.
echo ========================================
echo   COMPILACIÓN COMPLETADA
echo ========================================
echo.
echo El ejecutable se encuentra en la carpeta "dist"
echo Archivo: RuletaNavideña.exe
echo.
echo Puedes mover el archivo .exe a cualquier lugar
echo y ejecutarlo sin necesidad de Python instalado.
echo.
pause
