import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QTimer
from ui.main_window import MainWindow
from controller.main_controller import MainController
from utils.logger import get_logger

def main():
    logger = get_logger(__name__)
    logger.info(f"Starting Control Center application")
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Running on: {os.name} platform")
    try:
        # Must be set before QApplication is created for correct HiDPI behaviour
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

        app = QApplication(sys.argv)
        logger.info("QApplication initialized")

        # Log the detected screen geometry for diagnostics
        screen = app.primaryScreen()
        geo = screen.geometry()
        logger.info(f"Primary screen: {geo.width()}x{geo.height()} at ({geo.x()},{geo.y()})")
        controller = MainController()
        controller.start()
        logger.info("Main window displayed")
        exit_code = app.exec_()
        logger.info(f"Application exiting with code {exit_code}")
        sys.exit(exit_code)
    except Exception as e:
        logger.exception("Failed to start application")
        raise

if __name__ == "__main__":
    main()