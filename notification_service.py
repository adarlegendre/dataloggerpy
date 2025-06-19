import sys
import time
import logging
from datetime import datetime
import win32serviceutil
import win32service
import win32event
import servicemanager
import os
import subprocess

class NotificationService(win32serviceutil.ServiceFramework):
    _svc_name_ = "RadarNotificationService"
    _svc_display_name_ = "Radar Notification Service"
    _svc_description_ = "Manages and sends radar data notifications based on configured schedule"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

        # Set up logging
        log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notification_service.log')
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('NotificationService')

    def SvcStop(self):
        """Stop the service"""
        self.logger.info('Stopping service...')
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.running = False

    def SvcDoRun(self):
        """Main service run method"""
        try:
            self.logger.info('Starting service...')
            servicemanager.LogMsg(
                servicemanager.EVENTLOG_INFORMATION_TYPE,
                servicemanager.PYS_SERVICE_STARTED,
                (self._svc_name_, '')
            )

            # Get the path to manage.py
            base_dir = os.path.dirname(os.path.abspath(__file__))
            manage_py = os.path.join(base_dir, 'manage.py')

            while self.running:
                try:
                    # Run the management command
                    self.logger.info('Running notification check...')
                    result = subprocess.run(
                        [sys.executable, manage_py, 'check_notification_schedule'],
                        capture_output=True,
                        text=True
                    )
                    
                    if result.returncode == 0:
                        self.logger.info('Notification check completed successfully')
                        if result.stdout:
                            self.logger.info(f'Output: {result.stdout}')
                    else:
                        self.logger.error(f'Notification check failed: {result.stderr}')

                except Exception as e:
                    self.logger.error(f'Error running notification check: {str(e)}')

                # Wait for 1 minute before next check
                # The service can be stopped during this wait
                win32event.WaitForSingleObject(self.stop_event, 60 * 1000)  # 60 seconds

        except Exception as e:
            self.logger.error(f'Service error: {str(e)}')
            servicemanager.LogErrorMsg(f"Service error: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(NotificationService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(NotificationService) 